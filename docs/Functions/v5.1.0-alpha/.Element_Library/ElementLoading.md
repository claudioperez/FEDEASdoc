[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
ElementLoading.m

</div>

# ElementLoading

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**ELEMENTLOADING determines current distributed element load value**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function wC = ElementLoading (w0,lamda,LdId)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
ELEMENTLOADING determines current distributed element load value
  WC = ELEMENTLOADING (w0,LAMDA,LDID);
  function determines the current distributed element load values as the product of the
  user specified reference values in vector W0 and the current load factor(s) in row vector
  LAMDA; the load history ID for distributed element loads is specified in row vector LDID
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
-   [Inel2dFrm_wOneComp](Inel2dFrm_wOneComp.html "function ElemResp = Inel2dFrm_wOneComp (action,el_no,xyz,ElemData,ElemState)"){.code}
    INEL2dFRM_wONECOMP one component 2d frame element with rigid-linear
    hardening end hinges

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
