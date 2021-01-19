[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Solution_Library](FEDEASLab.html) \>
Initialize.m

</div>

# Initialize

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**INITIALIZE initialize analysis variables in STATE and load control
parameters in SOLSTRAT**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[State,SolStrat\] = Initialize
(Model,ElemData,Loading,State,SolStrat)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
INITIALIZE initialize analysis variables in STATE and load control parameters in SOLSTRAT
  [STATE,SOLSTRAT] = INITIALIZE(MODEL,ELEMDATA,LOADING,STATE,SOLSTRAT)
  the function initializes analysis variables in STATE and load control parameters
  in SOLSTRAT (only if IncrStrat.LFCtrl = 'yes';
  the function returns updated data structures STATE and SOLSTRAT:
  MODEL is a data structure with information about the structural model, ELEMDATA is
  a cell array with element properties, and LOADING is a data structure with information
  about applied force and imposed displacement patterns and corresponding load histories;
  specifically the function adds the following fields to STATE
  STATE
       lamda   = row vector of current load factors
       Pi      = initial force vector (for load sequences)
       Time    = pseudo-or real time counter
  the function also adds the field HIST to SOLSTRAT with subfields Sp0 and sgnK0 for
  adjusting the load factor under load incrementation, if IncrStrat.LFCtrl='yes'
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [LoadFactorControl](LoadFactorControl.html "function SolStrat = LoadFactorControl (action,SolStrat,detKf,Pref,Ut,DUr)"){.code}
    LOADFACTORCONTROL determine load factor increment under load control
    strategy

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
