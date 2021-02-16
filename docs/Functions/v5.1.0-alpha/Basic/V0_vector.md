[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Basic](FEDEASLab.html) \> V0_vector.m

</div>

# V0_vector

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**V0_VECTOR initial element deformation vector for the structural
model**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function V0 = V0_vector (Model,ElemData,Roption)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
V0_VECTOR initial element deformation vector for the structural model
  V0 = V0_VECTOR (MODEL,ELEMDATA,ROPTION)
  the function sets up the initial element deformation vector V0 for the structural model
  specified in data structure MODEL with element property information in cell array ELEMDATA
  if ROPTION=0, element release information is not accounted for in setting up V0 (default=1)
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
