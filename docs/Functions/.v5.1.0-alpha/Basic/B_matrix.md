[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Basic](FEDEASLab.html) \> B_matrix.m

</div>

# B_matrix

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**B_MATRIX static matrix of structural model with 2d/3d truss and 2d
frame elements**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function B = B_matrix (Model)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
B_MATRIX static matrix of structural model with 2d/3d truss and 2d frame elements
  B = B_MATRIX (MODEL)
  the function forms the static matrix B for all degrees of freedom and
  all basic forces of the structural model specified in data structure MODEL;
  the function is currently limited to 2d/3d truss and 2d frame elements
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [ElmLenOr](ElmLenOr.html "function [L,dcx] = ElmLenOr (xyz)"){.code}
    ELMLENOR element length and x-axis orientation (direction cosines)
-   [Localize](Localize.html "function [xyz,id] = Localize (Model,el)"){.code}
    LOCALIZE returns the node coordinates and id array of element

This function is called by:

-   [PlasticAnalysis_wLBT](PlasticAnalysis_wLBT.html "function [lamdac,Qc] = PlasticAnalysis_wLBT (Bf,Qpl,Pref,Pcf,Options)"){.code}
    PLASTICANALYSIS_wLBT collapse load factor and basic element forces
    by lower bound theorem of plastic analysis
-   [S_ForceMethod](S_ForceMethod.html){.code} % script for force method
    of structural analysis

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
