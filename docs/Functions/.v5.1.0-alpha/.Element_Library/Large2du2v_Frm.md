[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
Large2du2v_Frm.m

</div>

# Large2du2v_Frm

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**LARGE2DU2V_FRM determine 2d frame element deformations from end
displacements**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function v = Large2du2v_Frm (xyz,u)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
LARGE2DU2V_FRM determine 2d frame element deformations from end displacements
  V = LARGE2DU2V_FRM (XYZ,U)
  the function determines the deformations V of a 2-node, 2d frame element
  with end node coordinates XYZ under large end node displacements U
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [DeformShape2dFrm](DeformShape2dFrm.html "function [XYd,xyd] = DeformShape2dFrm (xyz,ElemData,u,v,MAGF,nsub)"){.code}
    DEFORMSHAPE2dFRM deformed shape of linear elastic, uniform,
    prismatic 2d frame element
-   [DeformShape2dFrm_wDispIntp](DeformShape2dFrm_wDispIntp.html "function [XYd,xyd] = DeformShape2dFrm_wDispIntp (xyz,ElemData,u,v,MAGF,nsub)"){.code}
    DEFORMSHAPE2dFRM_wDISPINTP deformed shape of 2d frame element with
    cubic polynomials
-   [GeomTran_2dFrm](GeomTran_2dFrm.html "function [ag,bg,ab,v,Dv,DDv] = GeomTran_2dFrm (option,xyz,GeomData,u,Du,DDu)"){.code}
    GEOMTRAN_2dFRM kinematic matrices and deformations for a 2-node 2d
    frame element

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
