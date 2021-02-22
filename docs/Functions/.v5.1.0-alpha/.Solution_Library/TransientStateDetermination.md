[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Solution_Library](FEDEASLab.html) \>
TransientStateDetermination.m

</div>

# TransientStateDetermination

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**TRANSIENTSTATEDETERMINATION structure state determination under
transient conditions**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function State = TransientStateDetermination
(StifUpdt,Model,ElemData,State,Int_Constants)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
TRANSIENTSTATEDETERMINATION structure state determination under transient conditions
  STATE = TRANSIENTSTATEDETERMINATION (STIFUPDT,MODEL,ELEMDATA,STATE)
  the function updates the structure resisting force vector in STATE for the current
  state of the structure as described by the displacement vector and its increments as
  as well as by the history variables in STATE; the effective resisting force and tangent
  stiffness matrix depend on integration constants in cell array INT_CONSTANTS
  depending on the value of character variable STIFUPDT the function also updates
  the tangent stiffness matrix in STATE
  MODEL is a data structure with information about the structural model,
  ELEMDATA is a cell array with element properties
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [OneTransientIteration](OneTransientIteration.html "function [State,SolStrat] = OneTransientIteration (Model,ElemData,Loading,State,SolStrat)"){.code}
    ONETRANSIENTITERATION single equilibrium iteration under transient
    conditions
-   [TransientIncrement](TransientIncrement.html "function [State,SolStrat] = TransientIncrement(Model,ElemData,Loading,State,SolStrat)"){.code}
    TRANSIENTINCREMENT load incrementation and state advance under
    transient conditions

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
