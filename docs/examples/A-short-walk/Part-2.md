Inelasticity in Frame Members
=============================

``` {.matlab}
Output = Hw12P2A( Elem,     Hkr ,          )
Output = Hw12P2B( EIntType, Hkr, SIntTyp,nfl,nwl,nIP)
```

Concentrated plasticity
-----------------------

![Figure 1: Response of two concentrated plasticity elements. The time
taken to complete each analysis is shown in the
legend](docs/img/p2/force-displ-1.png){#fig:cpcol}

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

![Response of the `Dinel2dFrm` element for various integration
schemes.](docs/img/p2/axial-moment-full.png)
