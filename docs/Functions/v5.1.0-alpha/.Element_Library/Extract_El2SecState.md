[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
Extract_El2SecState.m

</div>

# Extract_El2SecState

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**EXTRACT_EL2SECSTATE extract section state from element state**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function SecState = Extract_El2SecState (sec,ae,ElemState)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
EXTRACT_EL2SECSTATE extract section state from element state
  SECSTATE = EXTRACT_EL2SECSTATE (SEC,AE,ELSTATE)
  function extracts from data structure ELSTATE the necessary information
  for section SEC, and returns it in data structure SECSTATE;
  it needs compatibility array AE to determine section from element deformations
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [SectionWrapper](SectionWrapper.html "function ElemResp = SectionWrapper (action,el_no,xyz,ElemData,ElemState)"){.code}
    SECTIONWRAPPER wrapper element that passes on arguments to the
    section state determination

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
