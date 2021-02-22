[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Utilities](FEDEASLab.html) \> D_index.m

</div>

# D_index

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**D_INDEX cell array of indices into structure arrays for non-zero
element deformations**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function ied = D_index (Model)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
D_INDEX cell array of indices into structure arrays for non-zero element deformations
  IED = IDEF_INDEX (MODEL)
  the function sets up the cell array IED of indices for non-zero element deformations
  of the structural model in data structure MODEL;
  the list of inextensible elements is provided in field INEXTELIST of MODEL,
  and the list of inflexible elements in field INFLEXELIST of MODEL
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
