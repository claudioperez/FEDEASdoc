[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
Extract_BasicEl2SecState.m

</div>

# Extract_BasicEl2SecState

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**EXTRACT_BASICEL2SECSTATE extract section state from basic element
state**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function SecState = Extract_BasicEl2SecState (sec,ae,ElState)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
EXTRACT_BASICEL2SECSTATE extract section state from basic element state
  SECSTATE = EXTRACT_BASICEL2SECSTATE (SEC,AE,ELSTATE)
  function extracts from data structure ELSTATE the necessary information
  for section SEC, and returns it in data structure SECSTATE;
  it needs compatibility array AE to determine section from element deformations
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [Dinel2dFrm_EBwDF](Dinel2dFrm_EBwDF.html "function ElemResp = Dinel2dFrm_EBwDF (action,el_no,xyz,ElemData,ElemState)"){.code}
    DINEL2dFRM_EBwDF 2d-frame element with distributed inelasticity
    (displacement formulation)

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
