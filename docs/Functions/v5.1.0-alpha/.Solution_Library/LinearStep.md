[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Solution_Library](FEDEASLab.html) \>
LinearStep.m

</div>

# LinearStep

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**LINEARSTEP sets up and solves the structure equilibrium equations for
single load step**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function State = LinearStep (Model,ElemData,Loading)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
LINEARSTEP sets up and solves the structure equilibrium equations for single load step
  STATE = LINEARSTEP (MODEL,ELEMDATA,LOADING)
  function sets up and solves the structure equilibrium equations for single load step
  by direct assembly of element stiffness matrices; the structural response is contained
  in data structure STATE with fields U for the global dof displacement vector, Pr for the
  resisting force vector and Kf for the stiffness matrix at the free dofs of the structure;
  information about the structural model is supplied in data structure MODEL,
  the element properties are supplied in cell array ELEMDATA and loading information is
  given in data structure LOADING with fields Pref and Uref for a single applied force and
  a single imposed displacement vector, respectively
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [Initialize_State](Initialize_State.html "function State = Initialize_State (Model,ElemData)"){.code}
    INITIALIZE_STATE initialize state variables of structural model and
    create STATE

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
