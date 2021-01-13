[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
DefGeom_3dFrm.m

</div>

# DefGeom_3dFrm

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**DEFGEOM_3dFRM determines current length and corotational triad of
2-node, 3d frame element**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[L,T\] = DefGeom_3dFrm (xyz,GeomData,u)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
DEFGEOM_3dFRM determines current length and corotational triad of 2-node, 3d frame element
  [L,T] = DEFGEOM_3dFRM (XYZ,GEOMDATA,U);
  the function determines the length L and corotational triad T
  of a 2-node, 3d frame element in the current configuration
  from the end node coordinates XYZ (column 1 for node i, column 2 for node j)
  and the end displacement vector U (optional);
  the corotational triad is given in matrix T whose columns correspond to axes x,y,z resp.
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [GeomTran_3dFrm](GeomTran_3dFrm.html "function [ag,bg,ab,v,Dv,DDv] = GeomTran_3dFrm (option,xyz,GeomData,u,Du,DDu)"){.code}
    GEOMTRAN_3dFRM kinematic matrices and deformations for a 2-node 3d
    frame element
-   [Large3du2v_Frm](Large3du2v_Frm.html "function [v,vthetaI,vthetaJ] = Large3du2v_Frm (xyz,GeomData,u)"){.code}
    LARGE3DU2V_FRM determine 3d frame element deformations from end
    displacements

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
