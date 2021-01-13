[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Basic](FEDEASLab.html) \> Ks_matrix.m

</div>

# Ks_matrix

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**KS_MATRIX block diagonal matrix of basic element stiffness matrices
for structural model**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function Ks = Ks_matrix (Model,ElemData)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
KS_MATRIX block diagonal matrix of basic element stiffness matrices for structural model
  KS = KS_MATRIX (MODEL,ELEMDATA)
  the function sets up the block diagonal matrix of basic element stiffness matrices KS
  for the structural model specified in data structure MODEL with element property
  information in cell array ELEMDATA
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [ElmLenOr](ElmLenOr.html "function [L,dcx] = ElmLenOr (xyz)"){.code}
    ELMLENOR element length and x-axis orientation (direction cosines)
-   [Localize](Localize.html "function [xyz,id] = Localize (Model,el)"){.code}
    LOCALIZE returns the node coordinates and id array of element

This function is called by:

-   [S_DisplMethod](S_DisplMethod.html){.code} % script for displacement
    method of structural analysis

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
