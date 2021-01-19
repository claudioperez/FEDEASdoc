[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
GeomTran_2dFrm.m

</div>

# GeomTran_2dFrm

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**GEOMTRAN_2dFRM kinematic matrices and deformations for a 2-node 2d
frame element**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[ag,bg,ab,v,Dv,DDv\] = GeomTran_2dFrm
(option,xyz,GeomData,u,Du,DDu)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
GEOMTRAN_2dFRM kinematic matrices and deformations for a 2-node 2d frame element
  [AG,BG,AB,V,DV,DDV] = GEOMTRAN_2dFRM (OPTION,XYZ,GEOMDATA,U,DU,DDU)
  the function determines the kinematic matrix AG from the global to the basic reference system,
  the static matrix BG from the basic to the global reference system, 
  and the kinematic matrix AB from the global to the local reference system
  as well as the element deformation vector V and its increments DV and DDV
  from the node displacement array U and its increments DU and DDU
  for a 2-node 2d frame element with end node coordinates XYZ;
  OPTION is a character variable with one of three values:
  'linear','PDelta' and 'corotational' for linear, P-Delta and corotational geometry, resp.
  GEOMDATA is a data structure with information about rigid joint offsets in field JNTOFF,
  (first column for node i, second column for node j)
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [Large2du2v_Frm](Large2du2v_Frm.html "function v = Large2du2v_Frm (xyz,u)"){.code}
    LARGE2DU2V_FRM determine 2d frame element deformations from end
    displacements
-   [TranJnt](TranJnt.html "function aj = TranJnt (jntoff)"){.code}
    TRANJNT sets up transformation matrix for finite size joints

This function is called by:

-   [Dinel2dFrm_EBwDF](Dinel2dFrm_EBwDF.html "function ElemResp = Dinel2dFrm_EBwDF (action,el_no,xyz,ElemData,ElemState)"){.code}
    DINEL2dFRM_EBwDF 2d-frame element with distributed inelasticity
    (displacement formulation)
-   [Dinel2dFrm_EBwFF](Dinel2dFrm_EBwFF.html "function ElemResp = Dinel2dFrm_EBwFF (action,el_no,xyz,ElemData,ElemState)"){.code}
    DINEL2dFRM_EBwFF 2d-frame element with distributed inelasticity
    (force formulation)
-   [Inel2dFrm_wLHNMYS](Inel2dFrm_wLHNMYS.html "function ElemResp = Inel2dFrm_wLHNMYS (action,el_no,xyz,ElemData,ElemState)"){.code}
    INEL2dFRM_wLHNMYS 2d linear elastic frame element with linear
    plastic hardening axial-flexure hinges
-   [Inel2dFrm_wLPPM](Inel2dFrm_wLPPM.html "function ElemResp = Inel2dFrm_wLPPM (action,el_no,xyz,ElemData,ElemState)"){.code}
    INEL2dFRM_wLPPM 2d frame linear elastic element perfectly plastic
    flexural response
-   [Inel2dFrm_wOneComp](Inel2dFrm_wOneComp.html "function ElemResp = Inel2dFrm_wOneComp (action,el_no,xyz,ElemData,ElemState)"){.code}
    INEL2dFRM_wONECOMP one component 2d frame element with rigid-linear
    hardening end hinges
-   [Inel2dFrm_wTwoComp](Inel2dFrm_wTwoComp.html "function ElemResp = Inel2dFrm_wTwoComp (action,el_no,xyz,ElemData,ElemState)"){.code}
    INEL2dFRM_wTWOCOMP two component 2d frame element (linear +
    linear-perfectly plastic)
-   [LE2dFrm](LE2dFrm.html "function ElemResp = LE2dFrm (action,el_no,xyz,ElemData,ElemState)"){.code}
    LE2dFRM 2d LE frame element under linear or nonlinear geometry
-   [LE2dFrm_wPdelta](LE2dFrm_wPdelta.html "function ElemResp = LE2dFrm_wPdelta (action,el_no,xyz,ElemData,ElemState)"){.code}
    LE2dFRM 2d linear elastic frame element with P-delta effect under
    linear or nonlinear geometry

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
