[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
TranJnt.m

</div>

# TranJnt

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**TRANJNT sets up transformation matrix for finite size joints**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function aj = TranJnt (jntoff)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
TRANJNT sets up transformation matrix for finite size joints
  AJ = TRANJNT (JNTOFF)
  the function sets up the transformation matrix AJ for finite size joints of 2d and 3d frame elements;
  the rigid joint offsets at the element ends are specified in array JNTOFF
  with the first column corresponding to node i and the second column to node j
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
-   [GeomTran_2dFrm](GeomTran_2dFrm.html "function [ag,bg,ab,v,Dv,DDv] = GeomTran_2dFrm (option,xyz,GeomData,u,Du,DDu)"){.code}
    GEOMTRAN_2dFRM kinematic matrices and deformations for a 2-node 2d
    frame element
-   [GeomTran_3dFrm](GeomTran_3dFrm.html "function [ag,bg,ab,v,Dv,DDv] = GeomTran_3dFrm (option,xyz,GeomData,u,Du,DDu)"){.code}
    GEOMTRAN_3dFRM kinematic matrices and deformations for a 2-node 3d
    frame element

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
