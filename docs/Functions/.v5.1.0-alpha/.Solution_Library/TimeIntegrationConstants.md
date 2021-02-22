[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Solution_Library](FEDEASLab.html) \>
TimeIntegrationConstants.m

</div>

# TimeIntegrationConstants

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**TIMEINTEGRATIONCONSTANTS constants of time integration strategy**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function Int_Constants = TimeIntegrationConstants (TimeStrat,option)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
TIMEINTEGRATIONCONSTANTS constants of time integration strategy
  INT_CONSTANTS = TIMEINTEGRATIONCONSTANTS (TIMESTRAT)
  the function determines the constants of the time integration strategy speficied in field
  Type of data structure TIMESTRAT and returns them in vector INT_CONSTRANTS
  the data structure TIMESTRAT contains information about the integration strategy in fiels
      DELTAT = time step (scalar)
      TYPE   = name of integration method (character variable)
      PARAM  = parameters of integration method (vector)
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
-   [Update_TransientState](Update_TransientState.html "function State = Update_TransientState (Model,ElemData,State,SolStrat)"){.code}
    UPDATE_TRANSIENTSTATE final state determination under transient
    conditions, reset increments and history

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
