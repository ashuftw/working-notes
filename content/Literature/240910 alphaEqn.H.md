---
title: alphaEqn.H
draft: true
tags:
---
## 1. Scheme Selection and Off-Centering

```cpp
word alphaScheme("div(phi,alpha)");
word alpharScheme("div(phirb,alpha)");

tmp<fv::ddtScheme<scalar>> ddtAlpha
(
    fv::ddtScheme<scalar>::New
    (
        mesh,
        mesh.ddtScheme("ddt(alpha)")
    )
);
```

This section selects the numerical schemes for the convection terms and time derivative. It also sets up off-centering for the Crank-Nicolson scheme if used.

## 2. Interface Compression

```cpp
surfaceScalarField phic(mixture.cAlpha()*mag(phi/mesh.magSf()));

if (icAlpha > 0)
{
    phic *= (1.0 - icAlpha);
    phic += (mixture.cAlpha()*icAlpha)*fvc::interpolate(mag(U));
}
```

This part calculates the interface compression term `phic`, which helps maintain a sharp interface between phases.

## 3. MULES (Multidimensional Universal Limiter with Explicit Solution) Correction

```cpp
if (MULESCorr)
{
    fvScalarMatrix alpha1Eqn
    (
        // ... equation setup ...
    );

    alpha1Eqn.solve();

    // ... MULES correction ...
}
```

This section applies the MULES algorithm to ensure boundedness of the volume fraction.

## 4. Main Solution Loop

```cpp
for (int aCorr=0; aCorr<nAlphaCorr; aCorr++)
{
    // ... calculate fluxes ...

    // ... solve alpha equation ...

    // ... update alpha2 and mixture properties ...
}
```

This loop iteratively solves the volume fraction equation, applying corrections and updating related properties.

## 5. Final Updates

```cpp
if
(
    word(mesh.ddtScheme("ddt(rho,U)"))
 == fv::EulerDdtScheme<vector>::typeName
)
{
    rhoPhi = alphaPhi*(rho1 - rho2) + phiCN*rho2;
}
else
{
    // ... calculate end-of-time-step fluxes ...
}
```

This section finalizes the solution by updating mass fluxes based on the solved volume fraction.

The `alphaEqn.H` file is crucial for accurately tracking the interface between phases in multiphase simulations, ensuring mass conservation and maintaining a sharp interface.