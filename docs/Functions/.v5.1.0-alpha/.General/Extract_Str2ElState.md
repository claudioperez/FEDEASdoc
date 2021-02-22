[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [General](FEDEASLab.html) \>
Extract_Str2ElState.m

</div>

# Extract_Str2ElState

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**EXTRACT_STR2ELSTATE extract element state from structure state**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function ElemState = Extract_Str2ElState (el,id,State)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
EXTRACT_STR2ELSTATE extract element state from structure state
  ELEMSTATE = EXTRACT_STR2ELSTATE(EL,ID,STATE)
  the function extracts from the data structure STATE the necessary state information
  for element EL, with id-array ID, and returns it in data structure ELEMSTATE;
  when STATE is numeric, it is assumed to represent the global dof displacement vector
  and the function extracts only the element dof displacements in ELEMSTATE.U
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [Structure](Structure.html "function Resp = Structure (action,Model,ElemData,State,ElemList)"){.code}
    STRUCTURE performs requested action on group of elements

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
