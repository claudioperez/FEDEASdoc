[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
DefGeom_2dFrm.m

</div>

# DefGeom_2dFrm

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**DEFGEOM_2dFRM determines current length and corotational diad of
2-node, 2d frame element**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[L,T\] = DefGeom_2dFrm (xyz)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
DEFGEOM_2dFRM determines current length and corotational diad of 2-node, 2d frame element
  [L,T] = DEFGEOM_2dFRM (XYZ);
  the function determines the length L and the corotational diad T
  of a 2d frame element in the current configuration
  from the end node coordinates XYZ (column 1 for node i, column 2 for node j);
  the corotational diad is given in matrix T whose columns correspond to axes x and y, resp.
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [DeformShape2dFrm](DeformShape2dFrm.html "function [XYd,xyd] = DeformShape2dFrm (xyz,ElemData,u,v,MAGF,nsub)"){.code}
    DEFORMSHAPE2dFRM deformed shape of linear elastic, uniform,
    prismatic 2d frame element
-   [DeformShape2dFrm_wCurvIntp](DeformShape2dFrm_wCurvIntp.html "function [XYd,xyd] = DeformShape2dFrm_wCurvIntp (xyz,ElemData,u,EPost,MAGF,nsub)"){.code}
    DEFORMSHAPE2dFRM_wCURVINTP deformed shape of 2d frame element from
    curvatures
-   [DeformShape2dFrm_wDispIntp](DeformShape2dFrm_wDispIntp.html "function [XYd,xyd] = DeformShape2dFrm_wDispIntp (xyz,ElemData,u,v,MAGF,nsub)"){.code}
    DEFORMSHAPE2dFRM_wDISPINTP deformed shape of 2d frame element with
    cubic polynomials

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
