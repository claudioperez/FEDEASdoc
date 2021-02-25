[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Utilities](FEDEASLab.html) \>
Create_DispCyclewN.m

</div>

# Create_DispCyclewN

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**CREATE_DISPCYCLEwN generate time and value pairs of a displacement
cycle with normal force**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[DspHst,FrcHst\] = Create_DispCyclewN (DspPat,Options)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
CREATE_DISPCYCLEwN generate time and value pairs of a displacement cycle with normal force    
  [DSPHST,FRCHST] = CREATE_DISPCYCLEwN (DSPPAT,OPTIONS)
  the function generates the time and value pairs for the displacement path in DSPPAT
  under constant or variable normal force N; the function returns the displacement history
  in the data structure array DSPHST with fields Time and Value
  and the axial force history in the data structure FRCHST with fields Time and Value;
  the displacement history consists of unit or zero values at reversals,
  while the force history consists of unit values for constant axial force +- the variable
  axial force ratio NRat relative to the constant axial force specified in Options;
  the structure array DSPHST has one entry for uniaxial and 2 entries for biaxial
  displacement patterns; FRCHST has only one entry;
  DSPPAT is a character variable identifying the displacement path:
  cases 1-4 correspond to constant axial force N and cases 5-8 to variable axial force
  A1(A5)  : uniaxial displacement history in 1-direction
  A2(A6)  : uniaxial displacement history in 2-direction
  A3(A7)  : counter-clock wise clover leaf pattern
  A4(A8)  : diagonal displacement history (scaling to be specified in reference values)
  AN1(AN5): diamond  displacement pattern
  AN2(AN6): circular displacement pattern
  OPTIONS is an optional data structure with the following fields:
        .TrmpN = time interval for ramping up         the application of the axial force N
        .TrmpU = time interval for ramping up or down the application of first U
        .Nsub  = time subdivision for description of circular path
        .NRat  = ratio for axial force variation relative to constant value
        .HCyc  = true or false; if true the function returns a half    cycle instead of full
        .QCyc  = true or false; if true the function returns a quarter cycle instead of full
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [Create_MultDispCycleswN](Create_MultDispCycleswN.html "function [DspHst,FrcHst] = Create_MultDispCycleswN (DspPat,Ucyc,Ncyc,TmStr,Options)"){.code}
    CREATE_MULTDISPCYCLESwN sequence of full, half or quarter
    displacement cycles with axial force

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
