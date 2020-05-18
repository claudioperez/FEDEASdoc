Inelasticity in Frame Sections
==============================

In this section, the response of a nonlinear cross section is analyzed,
which is assumed to represent a thin slice of a frame member, for which
fiber strains can be considered constant.

Part A: T-Section
-----------------

``` {.matlab}
Output = Hw12P1A(nft, nwl, SIntTyp, Hk, yc, N_Np, Tmax, LoadOpt)
```

### Solution stability under perfect plasticity

![Figure 1: Moment-curvature response with minimal
hardening.`\label{mc1}`{=tex}](docs/img/p1/moment-curvature-1.png){#fig:mc1}

fig. 1 presents the moment-curvature response for the first two cases,
which utilize perfectly-pastic and effectively plastic ($H_k = 10^{-9}$)
materials, respectively. Additionally, this figure tracks the movement
of the neutral axis location throughout the moment curvature analysis
for runs `\ref{run:P1-0}`{=tex} and `\ref{run:P1-1}`{=tex}. At each load
step, this location is calculated according to the following relation:

$$y_{NA} = \dfrac{\epsilon_{ref, i}}{\kappa_i} - y_{ref}$$

Where $\epsilon_{ref, i}$ is the axial strain measured at the current
reference axis location, $y_{ref}$.

### Effects of axial force

![](docs/img/p1/moment-curvature-2.pdf)

### Cyclic loading

### 4

![](docs/img/p1/moment-curvature-4.png){#fig:mc4}

### 5

![](docs/img/p1/moment-curvature-5.pdf){#fig:mc5}

### 6

![Cyclic response.](docs/img/p1/moment-curvature-6.png)

![](docs/img/p1/n-m-all.pdf)
