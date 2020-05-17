Nonlinear Static Analysis {#sec:nsa}
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

![Figure 1: Pushover curve for simple inelastic frame
model.](docs/img/p3/lambda-roof-1.pdf){#fig:lr1}

The pushover curves for two cases are presented in fig. 1, which
consider two different concentrated plasticity elements. The zoomed
field indicates that the curves are essentially identical.

2
-

![](docs/img/p3//lambda-roof-2.pdf)

The pushover curves for all prescribed transient analysis cases are
presented above. The legend indicates the element name, along with the
length of time required by the analysis to conclude.
