[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Basic](FEDEASLab.html) \> Q0_vector.m

</div>

# Q0_vector

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**Q0_VECTOR initial (fixed-end) force vector for structural model**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function Q0 = Q0_vector (Model,ElemData)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
Q0_VECTOR initial (fixed-end) force vector for structural model
  Q0 = Q0_VECTOR (MODEL,ELEMDATA)
  the function sets up the initial (fixed-end) force vector Q0 for the structural model
  specified in data structure MODEL with element property information in cell array ELEMDATA
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
