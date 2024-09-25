---
title: createBubble.H
draft: true
tags:
---

## Center of the Bubble

```cpp
scalar totalBubbleVolume = 0.0;
vector weightedPosition(vector::zero);

forAll(alpha1, cellI)
{
    if (alpha1[cellI] > 0.5) // Assuming alpha1 represents the bubble phase
    {
        totalBubbleVolume += mesh.V()[cellI];
        weightedPosition += mesh.V()[cellI] * mesh.C()[cellI];
    }
}

reduce(totalBubbleVolume, sumOp<scalar>());
reduce(weightedPosition, sumOp<vector>());

if (totalBubbleVolume > SMALL) // prevents div. by 0 error. SMALL in OpenFOAM is defined as 1e-15. ()
{
    Cb = weightedPosition / totalBubbleVolume;
}
Info<< "Updated bubble center: " << Cb << endl;
```

## Write Cb as a Field (to visualize it in paraview)

```cpp
volScalarField CbField
(
    IOobject
    (
        "CbField",
        runTime.timeName(),
        mesh,
        IOobject::READ_IF_PRESENT,
        IOobject::AUTO_WRITE
    ),
    mesh,
    dimensionedScalar("zero", dimless, 0.0)
);


{
    // Reset CbField to zero
    CbField = dimensionedScalar("zero", dimless, 0.0);

    // Find the cell containing Cb
    label cellId = mesh.findCell(Cb);

    if (cellId >= 0)
    {
        // Set the value to 1 in the cell containing Cb
        CbField[cellId] = 1.0;
    }

    // Correct boundary conditions
    CbField.correctBoundaryConditions();

    Info<< "Cb field updated. Center at cell: " << cellId << endl;
}

```

## Domain Center

```cpp
scalar totalVolume = gSum(mesh.V());

// Weighted sum of cell centers
vector volumeWeightedSum = vector::zero;
forAll(mesh.C(), cellI)
{
    volumeWeightedSum += mesh.C()[cellI] * mesh.V()[cellI];
}
reduce(volumeWeightedSum, sumOp<vector>());

vector domainCenter = volumeWeightedSum / totalVolume;

Info << "Domain center: " << domainCenter << endl;

```

## Bubble Velocity 

```cpp
vector Cbf(0, 0, 0);  // Target/initial bubble center position
vector Cb0 = Cb;  // Previous time step bubble center position
vector UF(0, 0, 0);  // Initial bubble velocity
vector XF = Cb;  // Initial bubble position
// at the moment the target and the initial are the same

// Hardcoded parameters
scalar lambdaFf = 1.0;
scalar lambdaF0 = 1.0;

// Calculate change in velocity (bubble displacement / time)
vector dUF = lambdaFf * (Cb - Cbf) / runTime.deltaT().value()
           + lambdaF0 * (Cb - Cb0) / runTime.deltaT().value();
```
Here, 
1. **Long-term tracking**
    - Ensures that the bubble tends towards its initial position over time.
    - If the bubble has moved far from its initial position, this term will be larger, creating a stronger "restoring" velocity.
2. **Short-term adjustment** (second term):
    - This term accounts for recent changes in the bubble's position.
    - It allows the model to respond to rapid changes or perturbations in the bubble's motion.

```cpp
dimensionedVector dimUF("UF", dimVelocity, UF);
dimensionedVector dimDUF("dUF", dimVelocity, dUF);
dimensionedVector dimXF("XF", dimLength, XF);
```
This ensures that the variables are stored along with their dimensions. 

## Updating Bubble Position (Verlet Algorithm)

```cpp
dimXF += (dimUF + 0.5 * dimDUF) * runTime.deltaT();
XF = dimXF.value();  // Convert back to vector
```

Given:
- Initial velocity: $v_i = \text{dimUF}$
- Velocity change: $\Delta v = \text{dimDUF}$
- Final velocity: $v_f = v_i + \Delta v = \text{dimUF} + \text{dimDUF}$

We assume constant acceleration over the time step. In this case, the average velocity $\bar{v}$ is the arithmetic mean of the initial and final velocities:

$$
\bar{v} = \frac{v_i + v_f}{2}
$$

Substituting the expressions for $v_i$ and $v_f$:

$$
\bar{v} = \dfrac{\text{dimUF} + (\text{dimUF} + \text{dimDUF})}{2} = \text{dimUF} + 0.5 \cdot \text{dimDUF}
$$


