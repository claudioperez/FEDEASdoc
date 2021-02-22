[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Utilities](FEDEASLab.html) \> H_index.m

</div>

# H_index

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**H_INDEX cell array of indices into structure arrays for continuous
element deformations**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function iced = H_index (Model,ElemData)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
H_INDEX cell array of indices into structure arrays for continuous element deformations
  ICED = H_INDEX (MODEL,ELEMDATA)
  the function sets up the cell array ICED of indices for continuous element deformations
  based on release information for elements of the structural model in data structure MODEL;
  the location of element releases is specified in field RELEASE of cell array ELEMDATA
  ELEMDATA{3}.RELEASE = [0;1;0] :   a flexural release is present at end i of element 3
  ELEMDATA{2}.RELEASE = [1;0;1] : an axial and a flexural release at end j of element 2
  the function supports only truss and 2d frame elements at present
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
