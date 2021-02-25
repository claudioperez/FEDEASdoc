[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Solution_Library](FEDEASLab.html) \>
Increment.m

</div>

# Increment

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**INCREMENT load incrementation and state advance under static
conditions**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[State,SolStrat\] =
Increment(Model,ElemData,Loading,State,SolStrat)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
INCREMENT load incrementation and state advance under static conditions
  [STATE,SOLSTRAT] = INCREMENT(MODEL,ELEMDATA,LOADING,STATE,SOLSTRAT)
  the function increments the applied loading and determines the corresponding displacement
  increments under static conditions;
  information about the state of the structure is updated in STATE and
  information about parameters of solution strategy are updated in SOLSTRAT;
  MODEL is a data structure with information about the structural model, ELEMDATA is
  a cell array with element properties, and LOADING is a data structure with information
  about applied force and imposed displacement patterns and corresponding load histories
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [LoadFactorControl](LoadFactorControl.html "function SolStrat = LoadFactorControl (action,SolStrat,detKf,Pref,Ut,DUr)"){.code}
    LOADFACTORCONTROL determine load factor increment under load control
    strategy
-   [LoadFactorIncrement](LoadFactorIncrement.html "function Dlam = LoadFactorIncrement (History,Time,Deltat)"){.code}
    LOADFACTORINCREMENT load factor increment(s) for given load
    histories
-   [StateDetermination](StateDetermination.html "function State = StateDetermination (StifUpdt,Model,ElemData,State)"){.code}
    STATEDETERMINATION structure state determination under static
    conditions

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
