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

![](docs/img/p1/moment-curvature-5.png){#fig:mc5}

### 6

![Cyclic response.](docs/img/p1/moment-curvature-6.png)

![](docs/img/p1/n-m-all.png)

![](docs/img/p1/strain-curvature.png)

Part B: Rectangular Section
---------------------------

This problem was used to study some possible applications of automatic
differentiation to inelastic section analysis. Using a differentiable
programming framework, a return-mapping algorithm was implemented which
accounts for linear or nonlinear isotropic hardening, and basic
kinematic hardening. This algorithm is called to evaluate cross
sectional forces for a given strain distribution, and this procedure is
differentiated with forward-mode automatic differentiation to yield the
tangent stiffness of the cross section.

![Plastic limit surface for various integration rules.](docs/img/p1/B-1-1-40.png)

plastic surface

### Experiment I: O-A-B-O

![Stress and strain distributions over the loading history of experiment I.](docs/img/p1/B-3-stress-strain-1-4.png)

![](docs/img/p1/limit-quad-4.png){width="60%," height="60%"}

![Section response to load history O-A-B-O](docs/img/p1/stress-hist-3d-4-4.png){width="60%," height="60%"}

![Strain and stiffness history for load path O-A-B-O](docs/img/p1/strain-stiffness-1-4.png){#fig:ssh-oabo}

![Final state of cross section after experiment I.](docs/img/p1/final-state-1-4.png)

### Experiment II: O-A-B-C-O

![Loadpath O-A-B-C-O](docs/img/p1/limit-quad4-4.png){width="60%,"
height="60%"}

![Section response to load history O-A-B-C-O](docs/img/p1/stress-hist-3d-4-4-4.png){width=60%,height="60%"}

![Strain and stiffness history for load path O-A-B-O](docs/img/p1/strain-stiffness-1-4.png)

![Strain and stiffness history for load path O-A-B-C-O](docs/img/p1/strain-stiffness-2-4.png){#fig:ssh-oabco}



Inelasticity in Frame Members
=============================

``` {.matlab}
Output = Hw12P2A( Elem,     Hkr ,          )
Output = Hw12P2B( EIntType, Hkr, SIntTyp,nfl,nwl,nIP)
```

Concentrated plasticity
-----------------------

![Figure 1: Response of two concentrated plasticity elements. The time taken to complete each analysis is shown in the legend](docs/img/p2/force-displ-1.png){#fig:cpcol}

The cyclic response of two concentrated plasticity elements is compared
in fig. 1. Under the conditions of this analysis, the `LHNMYS` element
appears to very closely approximate the true plastic limit capacity of
the cross section, shown in red in fig. 1 (a). However, it should be
noted that the "exact" surface which is depicted here is only
representative of a single cross section slice, and not neccessarily the
full column. The lack of any axial-moment interaction in the `OneComp`
element is very evident in from plots.

The additional computational time required by the `LHNMYS` element
appears to be considerable, but it remains to be seen how this time
demand will scale to larger models.

Distributed inelasticity
------------------------

![`\label{fig:col-2}`{=tex}](docs/img/p2/force-displ-2.png)

![Response of the `Dinel2dFrm` element for various integration schemes.](docs/img/p2/axial-moment-full.png)

![](docs/img/p2/force-displ-2.png)

Nonlinear Static Analysis
=========================

A nonlinear static analysis of an 8-story framed structure is performed
useing a function with the following handle:

``` {.matlab}
Output = Hw12P3(Geom, Column, Dlam0, nostep, Hkr)
```

In this function, `Geom` specifies the frame element geometric stiffness
(`linear`, `PDelta` or `corotational`). The argument `Column` is used to
specify the finite element formulation used in the vertical elements of
the model. For the purpose of this study, and that of
sec. **¿sec:4-nta?** `\ref{sec:4-nta}`{=tex} ,all girders are modeled
using the `Inel2dFrm_wOneComp` formulation.

Inelastic without interaction
-----------------------------

![Figure 1: Pushover curve for simple inelastic frame model.](docs/img/p3/lambda-roof-1.png){#fig:lr1}

The pushover curves for two cases are presented in fig. 1, which
consider two different concentrated plasticity elements. The zoomed
field indicates that the curves are essentially identical.

2
-

![](docs/img/p3/lambda-roof-2.png)

The pushover curves for all prescribed transient analysis cases are
presented above. The legend indicates the element name, along with the
length of time required by the analysis to conclude.

Nonlinear Transient Analysis
============================

``` {.matlab}
[output,Model] = Hw12P4(Geom, Column, Factor)
```

Inelastic without interaction
-----------------------------

![Axial force-moment history at base columns.`\label{fig:c1-1}`{=tex}](docs/img/p4/c1-1.png)

2
-

![Axial force-moment history at base columns - Second Analysis.`\label{fig:c1-2}`{=tex}](docs/img/p4/c1-2.png)

3
-

![Axial force-moment history at base columns - Third Analysis.`\label{fig:c1-3}`{=tex}](docs/img/p4/c1-3.png)

4
-

Other
-----

![Ground motion with superposed husid plot](docs/img/p4//ground-motion.png)
