[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
ExtrReshu.m

</div>

# ExtrReshu

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**EXTRRESHU extracts displacements and increments from State and
reshapes into array**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[u,Du,DDu\] = ExtrReshu (State,ndf,nen)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
EXTRRESHU extracts displacements and increments from State and reshapes into array
 [U,DU,DDU] = EXTRRESHU (STATE,NDF,NEN)
  the function extracts the displacements and their increments from State
  and reshapes these into an NDF x NEN array,
  where NDF is no of dofs/node and NEN number of end nodes for element
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
-   [InelTruss](InelTruss.html "function ElemResp = InelTruss (action,el_no,xyz,ElemData,ElemState)"){.code}
    INELTRUSS 2d/3d inelastic truss element under linear or nonlinear
    geometry
-   [LE2dFrm](LE2dFrm.html "function ElemResp = LE2dFrm (action,el_no,xyz,ElemData,ElemState)"){.code}
    LE2dFRM 2d LE frame element under linear or nonlinear geometry
-   [LE2dFrm_wPdelta](LE2dFrm_wPdelta.html "function ElemResp = LE2dFrm_wPdelta (action,el_no,xyz,ElemData,ElemState)"){.code}
    LE2dFRM 2d linear elastic frame element with P-delta effect under
    linear or nonlinear geometry
-   [LE3dFrm](LE3dFrm.html "function ElemResp = LE3dFrm (action,el_no,xyz,ElemData,ElemState)"){.code}
    LE3dFRM 3d linear frame element under linear or nonlinear geometry
-   [LETruss](LETruss.html "function ElemResp = LETruss (action,el_no,xyz,ElemData,ElemState)"){.code}
    LETRUSS 2d/3d linear truss element under linear or nonlinear
    geometry

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
