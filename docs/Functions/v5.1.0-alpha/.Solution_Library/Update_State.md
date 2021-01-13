[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Solution_Library](FEDEASLab.html) \>
Update_State.m

</div>

# Update_State

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**UPDATE_STATE final state determination under static conditions, reset
increments and history**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function State = Update_State (Model,ElemData,State)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
UPDATE_STATE final state determination under static conditions, reset increments and history
  STATE = UPDATE_STATE (MODEL,ELEMDATA,STATE)
  the function performs a final state determination for the current state of the structure
  as described by the displacement vector and its increments as well as by the history
  variables in STATE; it then updates the structure resisting forces and history variables
  in STATE and then sets the displacement increments in STATE to zero
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
