[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Solution_Library](FEDEASLab.html) \>
Event2Event_NLAnalysis.m

</div>

# Event2Event_NLAnalysis

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**event-to-event incremental analysis of elasto-plastic structure with
linear or P-DELTA geometry**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[lamdah,Qh,Ufh,Vph,Iph\] = Event2Event_NLAnalysis
(opt,Model,ElemData,Loading,ConvPar)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
  event-to-event incremental analysis of elasto-plastic structure with linear or P-DELTA geometry
  [LAMDAH,QH,UFH,VPH,IPH] = EVENT2EVENT_NLANALYSIS (OPT,MODEL,ELEMDATA,LOADING)
  the function determines the load factor history LAMDAH of a structural model for an
  event-to-event analysis under loading information in data structure LOADING;
  the latter should have two fields, Pref for the load pattern to be factored, and
  Pcf for the load pattern to remain constant;
  each row of the load factor history vector corresponds to a different event;
  OPT is a character variable with values of LG for linear, or NG for nonlinear geometry 
  the data structure MODEL contains information about the structural model, and
  element property information is provided in cell array ELEMDATA
  the function returns the load factor history for each event in row vector LAMDAH,
  the basic force history in array QH, the free global dof displacement history in array UFH,
  the plastic element deformation history in array VPH, and the history of the index
  of plastic hinge locations in array IPH; in the array UFH the row number corresponds
  to the degree of freedom number, while in the arrays QH, VPH, and IPH the row number
  corresponds to the basic force number; in the history arrays QH, UFH, VPH,and IPH
  the column number corresponds to the event number
  -----------------------------------------------------------------------------------------
  developed by Chin-Long Lee using mixed-formulation and consistent Newton-Raphson    01/08
  -----------------------------------------------------------------------------------------
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
