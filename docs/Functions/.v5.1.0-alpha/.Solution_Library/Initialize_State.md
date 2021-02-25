[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Solution_Library](FEDEASLab.html) \>
Initialize_State.m

</div>

# Initialize_State

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**INITIALIZE_STATE initialize state variables of structural model and
create STATE**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function State = Initialize_State (Model,ElemData)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
INITIALIZE_STATE initialize state variables of structural model and create STATE    
  INITIALIZE_STATE (MODEL,ELEMDATA)
  function initializes the displacement, velocity and acceleration vectors
  for the structural model with information in data structure MODEL;
  the cell array ELEMDATA supplies the element property data for element history initialization;
  the function returns data structure STATE with the following fields
  STATE.U       = global dof total displacement vector
        DU      = global dof displacement increments from last convergence
        DDU     = global dof displacement increments from last iteration
        Udot    = global dof velocity vector
        Udotdot = global dof acceleration vector
        Past    = data structure of last    element history variables in cell array Elem
        Pres    = data structure of current element history variables in cell array Elem
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [LinearStep](LinearStep.html "function State = LinearStep (Model,ElemData,Loading)"){.code}
    LINEARSTEP sets up and solves the structure equilibrium equations
    for single load step

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
