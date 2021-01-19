[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Solution_Library](FEDEASLab.html) \>
PlasticAnalysis.m

</div>

# PlasticAnalysis

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**determine collapse load factor, element forces, and collapse mechanism
by plastic analysis**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[lamdac,Qc,DUf,DVpl\] = PlasticAnalysis
(Model,ElemData,Loading,LPOpt)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
  determine collapse load factor, element forces, and collapse mechanism by plastic analysis
  [LAMDAC,QC,DUF,DVPL] = PLASTICANALYSIS (MODEL,ELEMDATA,LOADING,LPOPT)
  the function determines the collapse load factor LAMDAC of a structural model under loading
  information in data structure LOADING; the latter should have two fields, PREF for the
  load pattern to be factored and Pcf for the load pattern to remain constant;
  the data structure MODEL contains information about the structural model, and
  element property information is provided in cell array ELEMDATA
  the function also returns the basic forces at incipient collapse in vector QC, the
  displacement increments of the collapse mechanism in vector DUF, and the plastic
  deformation increments of the collapse mechanism in vector DVPL
  LPOPT is an optional data structure for selecting options of
  the linear programming algorithm; these options are discussed in the
  Matlab manual pages for the linprog function
  the function uses 'dual-simplex' and 'LargeScale' by default; 
  the tolerance variable tol refers to OptimalityTolerance of the dual-simplex
  algorithm with default value 1e-7
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
