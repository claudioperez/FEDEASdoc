[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PostProcessing](FEDEASLab.html) \> Complete_QV.m

</div>

# Complete_QV

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**COMPLETE_QV complete basic force QIN and element deformation vector VE
with values at releases**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function \[Q,Ve\] = Complete_QV (Model,ElemData,Qin)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
COMPLETE_QV complete basic force QIN and element deformation vector VE with values at releases 
  [Q,VE] = COMPLETE_QV (MODEL,ELEMDATA,QIN)
  the function completes the basic force and element deformation vectors, Q and VE, resp.
  with the values at releases for the elements of the structural model in data structure MODEL;
  the location of element releases is specified in field RELEASE of cell array ELEMDATA;
  QIN is the vector of basic forces without the zero values at releases
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
