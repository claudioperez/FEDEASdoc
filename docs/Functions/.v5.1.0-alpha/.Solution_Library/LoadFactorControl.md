[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Solution_Library](FEDEASLab.html) \>
LoadFactorControl.m

</div>

# LoadFactorControl

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**LOADFACTORCONTROL determine load factor increment under load control
strategy**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function SolStrat = LoadFactorControl
(action,SolStrat,detKf,Pref,Ut,DUr)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
 LOADFACTORCONTROL determine load factor increment under load control strategy
  SOLSTRAT = LOADFACTORCONTROL(ACTION,SOLSTRAT,KL,KU,PREF,UT,DUR)
  the function determines the load factor increment in field DLAM of data structure SOLSTRAT
  under the specified load control strategy in field LCTYPE of SOLSTRAT;
  ACTION is a character variable that distinguishes various load control stages, i.e.
  initialization, incrementation and iteration; accordingly, the choices are
  ACTION = 'init': initialization of load control parameters in field HIST of SOLSTRAT
  ACTION = 'incr': determination of DLAM during load incrementation; parameter update in HIST
  ACTION = 'iter': determination of DLAM during equilibrium iteration (the following load
                   control methods are currently supported: 'MinDispNorm' and 'KeyDOF'
  KL and KU are the lower and upper diagonal LU components of the tangent stiffness matrix,
  PREF is the reference force vector and UT the corresponding displacement vector under PREF,
  DUR is the vector of displacement increments under the current unbalance force vector
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [Increment](Increment.html "function [State,SolStrat] = Increment(Model,ElemData,Loading,State,SolStrat)"){.code}
    INCREMENT load incrementation and state advance under static
    conditions
-   [Initialize](Initialize.html "function [State,SolStrat] = Initialize (Model,ElemData,Loading,State,SolStrat)"){.code}
    INITIALIZE initialize analysis variables in STATE and load control
    parameters in SOLSTRAT
-   [OneIteration](OneIteration.html "function [State,SolStrat] = OneIteration (Model,ElemData,Loading,State,SolStrat)"){.code}
    ONEITERATION single equilibrium iteration under static conditions

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
