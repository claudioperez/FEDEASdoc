[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Solution_Library](FEDEASLab.html) \>
Initialize_SolStrat.m

</div>

# Initialize_SolStrat

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**INITIALIZE_SOLSTRAT default values for most solution strategy
parameters**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function SolStrat = Initialize_SolStrat**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
INITIALIZE_SOLSTRAT default values for most solution strategy parameters
  SOLSTRAT = INITIALIZE_SOLSTRAT
  the function assigns default values to most solution strategy parameters and creates
  the data structure SOLSTRAT with corresponding information;
  SOLSTRAT contains three substructures: INCRSTRAT, ITERSTRAT and TIMESTRAT;
  these data structures contain the following fields
  INCRSTRAT
           Dlam0    = initial load factor increment(s) (row vector)
           Deltat   = pseudo-time increment (scalar)
           StifUpdt = stiffness update (character variable)
           LFCtrl   = load control (character variable)
           LCType   = load control type
           gamma    = exponent of current stiffness parameter method of load control
  ITERSTRAT
           StifUpdt = stiffness update (character variable)
           Type     = 'NR', 'ModNR', 'Krylov', 'LnSrch'
           LFCtrl   = load control (character variable)
           LCType   = load control type
           LCParam  = load control parameters
           maxiter  = maximum number of iterations for equilibrium (scalar)
           tol      = tolerance for satifaction of equilibrium equations (scalar)
  TIMESTRAT
           Delta    = time step of transient analysis (scalar)
           Type     = type of numerical integration (character variable)
           Param    = parameters of numerical time integration scheme (row vector)
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
