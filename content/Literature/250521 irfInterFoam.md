---
title: irfInterFoam
draft: true
tags: 
date: 2025-05-21
---
### Eötvös Number (Eo) [^1]
The ratio of buoyancy forces to surface tension forces:

$$\text{Eo} = \frac{g \cdot \Delta\rho \cdot d^2}{\sigma}$$

Where ,
- $\Delta\rho = \rho_{\text{droplet}} - \rho_{\text{medium}}$
- $g\rightarrow$ Gravitational acceleration
- $d\rightarrow$ Droplet diameter
- $\sigma\rightarrow$ Surface Tension

### Morton Number (M)
The ratio of viscous forces to surface tension forces:

$$\text{M} = \frac{g \cdot \mu_{\text{medium}}^4}{\rho_{\text{medium}} \cdot \sigma^3}$$

### Reynolds Number (Re)
The ratio of inertial forces to viscous forces:

$$\text{Re} = \frac{\rho_{\text{medium}} \cdot u \cdot d}{\mu_{\text{medium}}}$$

Where $u$ is the terminal velocity of the droplet.

## Derivation of Physical Properties

Given Eo, M, and Re, we can solve for the physical properties:

### Surface Tension
From the Eötvös number:

$$\sigma = \frac{g \cdot \Delta\rho \cdot d^2}{\text{Eo}} = \frac{g \cdot \rho_{\text{medium}} \cdot (\text{densityRatio} - 1) \cdot d^2}{\text{Eo}}$$
Where, $\text{densityRatio} = \rho_\text{droplet}/\rho_\text{medium}$

### Medium Viscosity
From the Morton number:

$$\mu_{\text{medium}} = \left(\frac{\text{M} \cdot \rho_{\text{medium}} \cdot \sigma^3}{g}\right)^{1/4}$$

And the kinematic viscosity:

$$\nu_{\text{medium}} = \frac{\mu_{\text{medium}}}{\rho_{\text{medium}}}$$

### Terminal Velocity
From the Reynolds number:

$$u = \frac{\text{Re} \cdot \mu_{\text{medium}}}{\rho_{\text{medium}} \cdot d}$$

### Droplet Properties
Droplet density based on the density ratio:

$$\rho_{\text{droplet}} = \text{densityRatio} \cdot \rho_{\text{medium}}$$

Droplet viscosity based on viscosity ratio:

$$\mu_{\text{droplet}} = \text{viscosityRatio} \cdot \mu_{\text{medium}}$$

And the kinematic viscosity:

$$\nu_{\text{droplet}} = \frac{\mu_{\text{droplet}}}{\rho_{\text{droplet}}}$$

## Terminal Velocity from Analytical Solution

An alternative formula for terminal velocity based on balancing drag and buoyancy forces:

$$u_t = \frac{2 \cdot R^2 \cdot g \cdot (\rho_{\text{droplet}} - \rho_{\text{medium}}) \cdot (\mu_{\text{droplet}} + \mu_{\text{medium}})}{3 \cdot \mu_{\text{medium}} \cdot (2\mu_{\text{medium}} + 3\mu_{\text{droplet}})}$$

Where $R$ is the droplet radius.

[^1]: https://en.wikipedia.org/wiki/E%C3%B6tv%C3%B6s_number