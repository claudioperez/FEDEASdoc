[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
Large3du2v_Frm.m

</div>

# Large3du2v_Frm

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**LARGE3DU2V_FRM determine 3d frame element deformations from end
displacements**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[v,vthetaI,vthetaJ\] = Large3du2v_Frm (xyz,GeomData,u)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
LARGE3DU2V_FRM determine 3d frame element deformations from end displacements
  [V,VTHETAI,VTHETAJ] = LARGE3DU2V_FRM(XYZ,GEOMDATA,U)
  the function determines the deformations V and
  the relative pseudo-rotation vectors VTHETAI and VTHETAJ at nodes I and J
  of a 2-node, 3d frame element with end node coordinates XYZ
  under large end node displacements U; the data structure GEOMDATA carries
  information about the joint offsets for the element
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [DefGeom_3dFrm](DefGeom_3dFrm.html "function [L,T] = DefGeom_3dFrm (xyz,GeomData,u)"){.code}
    DEFGEOM_3dFRM determines current length and corotational triad of
    2-node, 3d frame element

This function is called by:

-   [GeomTran_3dFrm](GeomTran_3dFrm.html "function [ag,bg,ab,v,Dv,DDv] = GeomTran_3dFrm (option,xyz,GeomData,u,Du,DDu)"){.code}
    GEOMTRAN_3dFRM kinematic matrices and deformations for a 2-node 3d
    frame element

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
