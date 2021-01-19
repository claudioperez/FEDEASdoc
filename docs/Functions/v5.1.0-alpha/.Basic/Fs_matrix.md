[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Basic](FEDEASLab.html) \> Fs_matrix.m

</div>

# Fs_matrix

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**FS_MATRIX block diagonal matrix of element flexibity matrices for
structural model**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function Fs = Fs_matrix (Model,ElemData,Roption)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
FS_MATRIX block diagonal matrix of element flexibity matrices for structural model
  FS = FS_MATRIX (MODEL,ELEMDATA,ROPTION)
  the function sets up the block diagonal matrix of element flexibility matrices FS
  for the structural model specified in data structure MODEL with element property
  information in cell array ELEMDATA;
  if ROPTION=0, element release information is not accounted for in setting up Fs (default=1)
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [ElmLenOr](ElmLenOr.html "function [L,dcx] = ElmLenOr (xyz)"){.code}
    ELMLENOR element length and x-axis orientation (direction cosines)
-   [Localize](Localize.html "function [xyz,id] = Localize (Model,el)"){.code}
    LOCALIZE returns the node coordinates and id array of element

This function is called by:

-   [S_ForceMethod](S_ForceMethod.html){.code} % script for force method
    of structural analysis

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
