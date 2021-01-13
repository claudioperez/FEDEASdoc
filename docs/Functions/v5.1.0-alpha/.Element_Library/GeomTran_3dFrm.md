[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
GeomTran_3dFrm.m

</div>

# GeomTran_3dFrm

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**GEOMTRAN_3dFRM kinematic matrices and deformations for a 2-node 3d
frame element**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[ag,bg,ab,v,Dv,DDv\] = GeomTran_3dFrm
(option,xyz,GeomData,u,Du,DDu)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
GEOMTRAN_3dFRM kinematic matrices and deformations for a 2-node 3d frame element
  [AG,BG,AB,V,DV,DDV] = GEOMTRAN_3dFRM (OPTION,XYZ,GEOMDATA,U,DU,DDU)
  the function determines the kinematic matrix AG from the global to the basic reference system,
  the static matrix BG from the basic to the global reference system, 
  and the kinematic matrix AB from the global to the local reference system
  as well as the element deformation vector V and its increments DV and DDV
  from the node displacement array U and its increments DU and DDU
  for a 2-node 3d frame element with end node coordinates XYZ;
  OPTION is a character variable with one of three values:
  'linear','PDelta' and 'corotational' for linear, P-Delta and corotational geometry, resp.
  GEOMDATA is a data structure with information about rigid joint offsets in field JNTOFF
  (first column for node i, second column for node j),
  and orientation (direction cosines) of the local y-axis in vector YORNT
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [DefGeom_3dFrm](DefGeom_3dFrm.html "function [L,T] = DefGeom_3dFrm (xyz,GeomData,u)"){.code}
    DEFGEOM_3dFRM determines current length and corotational triad of
    2-node, 3d frame element
-   [Large3du2v_Frm](Large3du2v_Frm.html "function [v,vthetaI,vthetaJ] = Large3du2v_Frm (xyz,GeomData,u)"){.code}
    LARGE3DU2V_FRM determine 3d frame element deformations from end
    displacements
-   [TranJnt](TranJnt.html "function aj = TranJnt (jntoff)"){.code}
    TRANJNT sets up transformation matrix for finite size joints

This function is called by:

-   [LE3dFrm](LE3dFrm.html "function ElemResp = LE3dFrm (action,el_no,xyz,ElemData,ElemState)"){.code}
    LE3dFRM 3d linear frame element under linear or nonlinear geometry

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
