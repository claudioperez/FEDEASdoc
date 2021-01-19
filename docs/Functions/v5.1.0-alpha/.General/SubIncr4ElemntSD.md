[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [General](FEDEASLab.html) \>
SubIncr4ElemntSD.m

</div>

# SubIncr4ElemntSD

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**SUBINCR4ELMNTSD element displacement increment subdivision for state
determination**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function ElemState = SubIncr4ElemntSD
(el,ElemName,xyz,ElemData,ElemState)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
SUBINCR4ELMNTSD element displacement increment subdivision for state determination
ELEMSTATE = SUBINCR4ELMNTSD (EL,ELEMNAME,XYZ,ELEMDATA,ELEMSTATE)
  function calls the state determination function for all elements in the structural model
  with the option of subdividing the displacement increment in case of non-convergence;
  the latter case is represented by the logical variable CONVFLAG in ELEMSTATE;
  to activate the option of element displacement increment subdivision, the variable
  SUBDIVNO must be set in the element property data structure ELEMDATA
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [Structure](Structure.html "function Resp = Structure (action,Model,ElemData,State,ElemList)"){.code}
    STRUCTURE performs requested action on group of elements

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
