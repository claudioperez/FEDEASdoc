[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Solution_Library](FEDEASLab.html) \>
TransientIterate.m

</div>

# TransientIterate

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**TRANSIENTITERATE equilibrium iterations until convergence under
transient conditions**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[State,SolStrat\] = TransientIterate
(Model,ElemData,Loading,State,SolStrat)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
TRANSIENTITERATE equilibrium iterations until convergence under transient conditions
  [STATE,SOLSTRAT] = TRANSIENTITERATE (MODEL,ELEMDATA,LOADING,STATE,SOLSTRAT)
  the function performs equilibrium iterations until convergence under the applied loading
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

-   [OneTransientIteration](OneTransientIteration.html "function [State,SolStrat] = OneTransientIteration (Model,ElemData,Loading,State,SolStrat)"){.code}
    ONETRANSIENTITERATION single equilibrium iteration under transient
    conditions

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
