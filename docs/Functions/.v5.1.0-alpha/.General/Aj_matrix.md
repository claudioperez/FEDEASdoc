[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [General](FEDEASLab.html) \> Aj_matrix.m

</div>

# Aj_matrix

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**AJ_MATRIX kinematic matrix of structural model with 2d/3d truss and 2d
frame elements**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function Aj = Aj_matrix (Model)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
AJ_MATRIX kinematic matrix of structural model with 2d/3d truss and 2d frame elements
  AJ = AJ_MATRIX (MODEL)
  the function forms the kinematic matrix AJ for all degrees of freedom and
  all element deformations of the structural model specified in data structure MODEL; 
  the kinematic matrix AJ includes the effect of joint offsets for the elements;
  the function is currently limited to 2d/3d truss and 2d frame elements
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
