[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
DeformShape2dFrm_wCurvIntp.m

</div>

# DeformShape2dFrm_wCurvIntp

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**DEFORMSHAPE2dFRM_wCURVINTP deformed shape of 2d frame element from
curvatures**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[XYd,xyd\] = DeformShape2dFrm_wCurvIntp
(xyz,ElemData,u,EPost,MAGF,nsub)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
DEFORMSHAPE2dFRM_wCURVINTP deformed shape of 2d frame element from curvatures
  [XYd,xyd] = DEFORMSHAPE2dFRM_wCURVINTP (XYZ,ELEMDATA,U,EPOST,MAGF,NSUB)
  The function returns the global coordinates of the magnified deformed shape
  of a 2d frame element under large end displacements in array XYd,
  and the local coordinates of the magnified deformed shape in array xyd.
  Input arguments are the end node coordinates in array XYZ, the element
  properties in cell array ELEMDATA, the end displacements in vector U,
  and the data structure EPOST with information about the curvatures KAPPA
  along the element axis in field Sec{iP}.e(2).
  Optional arguments are the magnification factor MAGF (default=10)
  and the number of intermediate points NSUB (default=100) for the deformed shape.
  The function uses double integration of the interpolation polynomial
  of the curvatures at the integration points.
  (reference: Neuenhofer/Filippou, ASCE, JSE, June 1998, pp. 704-711)
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [DefGeom_2dFrm](DefGeom_2dFrm.html "function [L,T] = DefGeom_2dFrm (xyz)"){.code}
    DEFGEOM_2dFRM determines current length and corotational diad of
    2-node, 2d frame element
-   [TranJnt](TranJnt.html "function aj = TranJnt (jntoff)"){.code}
    TRANJNT sets up transformation matrix for finite size joints

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
