[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Solution_Library](FEDEASLab.html) \>
OneIteration.m

</div>

# OneIteration

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**ONEITERATION single equilibrium iteration under static conditions**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[State,SolStrat\] = OneIteration
(Model,ElemData,Loading,State,SolStrat)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
 ONEITERATION single equilibrium iteration under static conditions
  [STATE,SOLSTRAT] = ONEITERATION (MODEL,ELEMDATA,LOADING,STATE,SOLSTRAT)
  the function performs a single equilibrium iteration under the applied loading
  and determines the corresponding displacement increments under static conditions;
  information about the state of the structure is updated in STATE and
  information about the parameters of the solution strategy is updated in SOLSTRAT;
  MODEL is a data structure with information about the structural model, ELEMDATA is
  a cell array with element properties, and LOADING is a data structure with information
  about applied force and imposed displacement patterns with corresponding load histories
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [LoadFactorControl](LoadFactorControl.html "function SolStrat = LoadFactorControl (action,SolStrat,detKf,Pref,Ut,DUr)"){.code}
    LOADFACTORCONTROL determine load factor increment under load control
    strategy
-   [StateDetermination](StateDetermination.html "function State = StateDetermination (StifUpdt,Model,ElemData,State)"){.code}
    STATEDETERMINATION structure state determination under static
    conditions

This function is called by:

-   [Iterate](Iterate.html "function [State,SolStrat] = Iterate (Model,ElemData,Loading,State,SolStrat)"){.code}
    ITERATE equilibrium iterations until convergence under static
    conditions

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
