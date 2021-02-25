[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Solution_Library](FEDEASLab.html) \>
Update_TransientState.m

</div>

# Update_TransientState

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**UPDATE_TRANSIENTSTATE final state determination under transient
conditions, reset increments and history**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function State = Update_TransientState
(Model,ElemData,State,SolStrat)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
UPDATE_TRANSIENTSTATE final state determination under transient conditions, reset increments and history
  STATE = UPDATE_TRANSIENTSTATE (MODEL,ELEMDATA,STATE,SOLSTRAT)
  the function performs a final state determination for the current state of the structure
  as described by the displacement vector and its increments as well as by the history
  variables in STATE; it then updates the structure resisting forces, and history variables
  as well as the nodal velocities and accelerations in STATE and then
  sets the displacement increments in STATE to zero
  data structure SOLSTRAT carries information about the time integration scheme in field TimeStrat
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [TimeIntegrationConstants](TimeIntegrationConstants.html "function Int_Constants = TimeIntegrationConstants (TimeStrat,option)"){.code}
    TIMEINTEGRATIONCONSTANTS constants of time integration strategy

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
