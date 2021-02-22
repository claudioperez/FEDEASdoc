[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Utilities](FEDEASLab.html) \>
Create_LoadHistory.m

</div>

# Create_LoadHistory

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**CREATE_LOADHIST generate time and value pairs of a displacement cycle
with normal force**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function LoadHist = Create_LoadHistory (RevVal,LHCase,T_Rev)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
CREATE_LOADHIST generate time and value pairs of a displacement cycle with normal force    
  LOADHIST = CREATE_LOADHIST (REVVAL,LHCASE,T_REV)
  the function creates load history time and value pairs in fields Time and Value of the
  structure LOADHIST, respectively; the row vector REVVAL contains the load reversal values
  and the variable T_REV the period of reversals;
  the character variable LHCASE supports two cases:
  'A' stands for the case that the Nth reversal occurs at N*T_REV,
  'B' stands for the case that the reversal times are adjusted so that the rate of change
  for the load value is constant between reversals
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
