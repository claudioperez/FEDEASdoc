[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Solution_Library](FEDEASLab.html) \>
TransientInitialize.m

</div>

# TransientInitialize

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**TRANSIENTINITIALIZE initialize State variables for transient response
analysis**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function State = TransientInitialize (Model,ElemData,Loading,State)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
TRANSIENTINITIALIZE initialize State variables for transient response analysis
  STATE = TRANSIENTINITIALIZE(MODEL,ELEMDATA,LOADING,STATE)
  the function initializes variables in STATE relevant for transient response analysis and
  returns an updated data structure STATE;
  MODEL is a data structure with information about the structural model, ELEMDATA is
  a cell array with element properties, and LOADING is a data structure with information
  about applied force, imposed displacement, and imposed acceleration patterns
  with corresponding load histories;
  specifically the function adds the following fields to STATE needed for transient analysis
  STATE
       lamda   = row vector of current load factors
       Pi      = initial force vector (for load sequences)
       Time    = pseudo-or real time counter
       Ugddot  = support acceleration vector
       C       = damping matrix
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
