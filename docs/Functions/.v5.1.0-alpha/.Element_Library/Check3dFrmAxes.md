[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
Check3dFrmAxes.m

</div>

# Check3dFrmAxes

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**CHECK3dFRMAXES check that y-axis is not co-linear with element chord**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function y = Check3dFrmAxes (el,y,xyz)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
CHECK3dFRMAXES check that y-axis is not co-linear with element chord
  Y = CHECK3dFRMAXES(EL,Y,XYZ)
  the function checks that the specified Y-axis for the element EL 
  with end node coordinates XYZ is not colinear with the element chord;
  if colinearity is detected, the function returns a unit vector in the global
  Y- or Z-axis and issues a warning message with information about the change;
  if not, the function returns the normalized vector Y
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [LE3dFrm](LE3dFrm.html "function ElemResp = LE3dFrm (action,el_no,xyz,ElemData,ElemState)"){.code}
    LE3dFRM 3d linear frame element under linear or nonlinear geometry

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
