[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
kg_2dFrm.m

</div>

# kg_2dFrm

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**KG_2dFRM geometric stiffness matrix for 2-node 2d frame element for
different options**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function kg = kg_2dFrm (option,xyz,u,q)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
KG_2dFRM geometric stiffness matrix for 2-node 2d frame element for different options
  KG = KG_2dFRM (OPTION,XYZ,U,Q)
  the function determines the geometric stiffness matrix KG of a 2-node 2d frame element
  with end coordinates in array XYZ (node i corresponds to first column and node j to second);
  the geometric stiffness matrix depends on the node displacement values in array U (ndfx2)
  in the global reference system and on the basic force vector Q;
  OPTION is a character variable with one of three values:
  'linear','PDelta' and 'corotational' for linear, P-Delta and corotational geometry, resp.
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

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
