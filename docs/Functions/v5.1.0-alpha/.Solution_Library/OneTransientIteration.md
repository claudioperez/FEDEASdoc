[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Solution_Library](FEDEASLab.html) \>
OneTransientIteration.m

</div>

# OneTransientIteration

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**ONETRANSIENTITERATION single equilibrium iteration under transient
conditions**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[State,SolStrat\] = OneTransientIteration
(Model,ElemData,Loading,State,SolStrat)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
 ONETRANSIENTITERATION single equilibrium iteration under transient conditions
  [STATE,SOLSTRAT] = ONETRANSIENTITERATION (MODEL,ELEMDATA,LOADING,STATE,SOLSTRAT)
  the function performs a single equilibrium iteration under the applied loading
  and determines the corresponding displacement increments under transient conditions;
  information about the state of the structure is updated in STATE and
  information about parameters of solution strategy are updated in SOLSTRAT;
  MODEL is a data structure with information about the structural model, ELEMDATA is
  a cell array with element properties, and LOADING is a data structure with information
  about applied force and imposed displacement patterns and corresponding load histories
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [TimeIntegrationConstants](TimeIntegrationConstants.html "function Int_Constants = TimeIntegrationConstants (TimeStrat,option)"){.code}
    TIMEINTEGRATIONCONSTANTS constants of time integration strategy
-   [TransientStateDetermination](TransientStateDetermination.html "function State = TransientStateDetermination (StifUpdt,Model,ElemData,State,Int_Constants)"){.code}
    TRANSIENTSTATEDETERMINATION structure state determination under
    transient conditions

This function is called by:

-   [TransientIterate](TransientIterate.html "function [State,SolStrat] = TransientIterate (Model,ElemData,Loading,State,SolStrat)"){.code}
    TRANSIENTITERATE equilibrium iterations until convergence under
    transient conditions

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
