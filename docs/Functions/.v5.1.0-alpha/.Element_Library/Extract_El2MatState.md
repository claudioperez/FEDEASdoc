[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
Extract_El2MatState.m

</div>

# Extract_El2MatState

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**EXTRACT_EL2MATSTATE extract material state from element state**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function MatState = Extract_El2MatState (mat,aeps,ElState,rd)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
EXTRACT_EL2MATSTATE extract material state from element state
  MATSTATE = EXTRACT_EL2MATSTATE (MAT,AEPS,ELSTATE,RD)
  function extracts from data structure ELSTATE the necessary information
  for the element material, and returns it in data structure MATSTATE;
  it needs compatibility array AEPS to determine material strains from element displacements
  RD identifies the displacement DOFs to extract (default = all)
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [MaterialWrapper](MaterialWrapper.html "function ElemResp = MaterialWrapper (action,el_no,xyz,ElemData,ElemState)"){.code}
    MATERIALWRAPPER wrapper element that passes on arguments to the
    material state determination

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
