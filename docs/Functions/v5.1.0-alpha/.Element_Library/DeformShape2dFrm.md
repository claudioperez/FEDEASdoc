[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
DeformShape2dFrm.m

</div>

# DeformShape2dFrm

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**DEFORMSHAPE2dFRM deformed shape of linear elastic, uniform, prismatic
2d frame element**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[XYd,xyd\] = DeformShape2dFrm (xyz,ElemData,u,v,MAGF,nsub)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
DEFORMSHAPE2dFRM deformed shape of linear elastic, uniform, prismatic 2d frame element
  [XYd,xyd] = DEFORMSHAPE2DFRM (ELEMDATA,XYZ,U,V,MAGF,NSUB);
  The function returns the global coordinates of the magnified deformed shape
  of a 2d frame element under large end displacements in array XYd,
  and the local coordinates of the magnified deformed shape in array xyd.
  Input arguments are the end node coordinates in array XYZ, the element
  properties in cell array ELEMDATA, and the end displacements in vector U.
  Optional arguments are the end deformations V for elements with releases
  or plastic hinges (these can be supplied in a data structure with fields VE or V),
  the magnification factor MAGF (default=10), and the number
  of intermediate points NSUB (default=100) for the deformed shape.
  The function uses the exact homogeneous and particular solution of
  the differential equation for a linear elastic homogeneous frame element
  under uniformly distributed transverse load and uniform curvature.
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [DefGeom_2dFrm](DefGeom_2dFrm.html "function [L,T] = DefGeom_2dFrm (xyz)"){.code}
    DEFGEOM_2dFRM determines current length and corotational diad of
    2-node, 2d frame element
-   [Large2du2v_Frm](Large2du2v_Frm.html "function v = Large2du2v_Frm (xyz,u)"){.code}
    LARGE2DU2V_FRM determine 2d frame element deformations from end
    displacements
-   [TranJnt](TranJnt.html "function aj = TranJnt (jntoff)"){.code}
    TRANJNT sets up transformation matrix for finite size joints

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
