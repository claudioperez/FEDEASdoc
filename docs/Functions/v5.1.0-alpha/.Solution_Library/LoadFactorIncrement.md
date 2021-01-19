[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Solution_Library](FEDEASLab.html) \>
LoadFactorIncrement.m

</div>

# LoadFactorIncrement

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**LOADFACTORINCREMENT load factor increment(s) for given load
histories**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function Dlam = LoadFactorIncrement (History,Time,Deltat)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
LOADFACTORINCREMENT load factor increment(s) for given load histories
  DLAM = LOADFACTORINCREMENT(HISTORY,TIME,DELTAT)
  the function determines the load factor increment(s) in vector DLAM for the number of
  time histories in data structure HISTORY with fields TIME and VALUE; linear interpolation
  with current time TIME and time step DELTAT gives the load factor increment(s)
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [Increment](Increment.html "function [State,SolStrat] = Increment(Model,ElemData,Loading,State,SolStrat)"){.code}
    INCREMENT load incrementation and state advance under static
    conditions
-   [TransientIncrement](TransientIncrement.html "function [State,SolStrat] = TransientIncrement(Model,ElemData,Loading,State,SolStrat)"){.code}
    TRANSIENTINCREMENT load incrementation and state advance under
    transient conditions

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
