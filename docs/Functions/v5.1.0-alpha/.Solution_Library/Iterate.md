[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Solution_Library](FEDEASLab.html) \>
Iterate.m

</div>

# Iterate

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**ITERATE equilibrium iterations until convergence under static
conditions**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[State,SolStrat\] = Iterate
(Model,ElemData,Loading,State,SolStrat)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
ITERATE equilibrium iterations until convergence under static conditions
  [STATE,SOLSTRAT] = ITERATE(MODEL,ELEMDATA,LOADING,STATE,SOLSTRAT)
  the function performs equilibrium iterations until convergence under the applied loading
  and determines the corresponding displacement increments under static conditions;
  information about the state of the structure is updated in STATE and
  information about parameters of solution strategy are updated in SOLSTRAT;
  MODEL is a data structure with information about the structural model, ELEMDATA is
  a cell array with element properties, and LOADING is a data structure with information
  about applied force and imposed displacement patterns and corresponding load histories
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [OneIteration](OneIteration.html "function [State,SolStrat] = OneIteration (Model,ElemData,Loading,State,SolStrat)"){.code}
    ONEITERATION single equilibrium iteration under static conditions

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
