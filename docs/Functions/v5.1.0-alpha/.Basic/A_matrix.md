[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Basic](FEDEASLab.html) \> A_matrix.m

</div>

# A_matrix

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**A_MATRIX kinematic matrix of structural model with 2d/3d truss and 2d
frame elements**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function A = A_matrix (Model)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
A_MATRIX kinematic matrix of structural model with 2d/3d truss and 2d frame elements
  A = A_MATRIX (MODEL)
  the function forms the kinematic matrix A for all degrees of freedom and
  all element deformations of the structural model specified in data structure MODEL; 
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

-   [PlasticAnalysis_wUBT](PlasticAnalysis_wUBT.html "function [lamdac,DUf,DVhp] = PlasticAnalysis_wUBT (Af,Qpl,Pref,Pfc,Options)"){.code}
    PLASTICANALYSIS_wUBT collapse load factor and deformation increments
    by upper bound theorem of plastic analysis
-   [S_DisplMethod](S_DisplMethod.html){.code} % script for displacement
    method of structural analysis

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
