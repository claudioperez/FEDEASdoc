[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Solution_Library](FEDEASLab.html) \>
StateDetermination.m

</div>

# StateDetermination

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**STATEDETERMINATION structure state determination under static
conditions**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function State = StateDetermination (StifUpdt,Model,ElemData,State)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
STATEDETERMINATION structure state determination under static conditions
  STATE = STATEDETERMINATION (STIFUPDT,MODEL,ELEMDATA,STATE)
  the function updates the structure resisting force vector in STATE for the current
  state of the structure as described by the displacement vector and its increments as
  as well as by the history variables in STATE;
  depending on the value of character variable STIFUPDT the function also updates
  the tangent stiffness matrix in STATE
  MODEL is a data structure with information about the structural model,
  ELEMDATA is a cell array with element properties
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [Increment](Increment.html "function [State,SolStrat] = Increment(Model,ElemData,Loading,State,SolStrat)"){.code}
    INCREMENT load incrementation and state advance under static
    conditions
-   [OneIteration](OneIteration.html "function [State,SolStrat] = OneIteration (Model,ElemData,Loading,State,SolStrat)"){.code}
    ONEITERATION single equilibrium iteration under static conditions

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
