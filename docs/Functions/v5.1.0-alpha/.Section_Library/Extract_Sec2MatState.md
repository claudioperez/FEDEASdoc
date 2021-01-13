[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Section_Library](FEDEASLab.html) \>
Extract_Sec2MatState.m

</div>

# Extract_Sec2MatState

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**EXTRACT_SEC2MATSTATE extract material state from section state**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function MatState = Extract_Sec2MatState (m,as,SecState)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
EXTRACT_SEC2MATSTATE extract material state from section state
  MATSTATE = EXTRACT_SEC2MATSTATE (M,AS,SECSTATE)
  function extracts from data structure SECSTATE the necessary information
  for material point M, and returns it in data structure MATSTATE;
  it needs compatibility array AS to determine material strains from section deformations
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [HomoCircSecw1dMat](HomoCircSecw1dMat.html "function SecResp = HomoCircSecw1dMat (action,SecNo,ndm,SecData,SecState)"){.code}
    HOMOCIRCSECw1dMAT response of homogeneous circular section with
    uniaxial material
-   [HomoRectSecw1dMat](HomoRectSecw1dMat.html "function SecResp = HomoRectSecw1dMat (action,SecNo,ndm,SecData,SecState)"){.code}
    HOMORECTSECw1dMAT response of homogeneous rectangular section with
    uniaxial material
-   [HomoWFSecw1dMat](HomoWFSecw1dMat.html "function SecResp = HomoWFSecw1dMat (action,SecNo,ndm,SecData,SecState)"){.code}
    HOMOWFSECw1dMAT response of homogeneous wide flange (WF) section
    with uniaxial material
-   [MultRectSecw1dMat](MultRectSecw1dMat.html "function SecResp = MultRectSecw1dMat (action,SecNo,ndm,SecData,SecState)"){.code}
    MULTRECTSECw1dMAT response for section of rectangular patches and
    bars with uniaxial material
-   [ReCircSecw1dMat](ReCircSecw1dMat.html "function SecResp = ReCircSecw1dMat (action,SecNo,ndm,SecData,SecState)"){.code}
    RECIRCSECw1dMAT response of reinforced circular section with
    uniaxial materials
-   [ReRectSecw1dMat](ReRectSecw1dMat.html "function SecResp = ReRectSecw1dMat (action,SecNo,ndm,SecData,SecState)"){.code}
    RERECTSECw1dMAT response of reinforced rectangular section with
    uniaxial materials

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
