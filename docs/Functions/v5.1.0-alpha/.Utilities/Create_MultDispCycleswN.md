[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Utilities](FEDEASLab.html) \>
Create_MultDispCycleswN.m

</div>

# Create_MultDispCycleswN

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**CREATE_MULTDISPCYCLESwN sequence of full, half or quarter displacement
cycles with axial force**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[DspHst,FrcHst\] = Create_MultDispCycleswN
(DspPat,Ucyc,Ncyc,TmStr,Options)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
CREATE_MULTDISPCYCLESwN sequence of full, half or quarter displacement cycles with axial force 
  [DSPHST,FRCHST] = CREATE_MULTDISPCYCLESwN (DSPPAT,UCYC,NCYC,TMSTR,OPTIONS)
  the function generates a sequence of full, half or quarter displacement cycles
  after factoring each with the corresponding factor in array UCYC;
  the axial force factor of the correponding cycle is specified in the optional array NCYC;
  UCYC is an ND x NCYC array and NCYC is a 1 x NCYC row vector, where ND is the number
  of imposed displacements (1=uniaxial, 2=biaxial) and NCYC is the number of cycles;
  if NCYC is not specified, it is assumed equal to ONES(1,NCYC);
  the function returns the displacement history in the data structure array DSPHST
  with the fields Time and Value and the axial force history in the data structure FRCHST
  with the fields Time and Value; the data structure array DSPHST has one entry for uniaxial and 2 entries for biaxial
  and 2 entries for biaxial displacement patterns; FRCHST has only one entry.
  DSPPAT is a character variable if the displacement pattern is the same for all cycles and
  a character cell array, if the displacement pattern varies from cycle to cycle;
  the character variable identifies the path of the displacement pattern with numbers
  1-4 corresponding to a constant axial force N and numbers 5-8 to a variable axial force
  A1(A5)  : uniaxial displacement history in 1-direction
  A2(A6)  : uniaxial displacement history in 2-direction
  A3(A7)  : counter-clock wise clover leaf pattern
  A4(A8)  : diagonal displacement history
  AN1(AN5): diamond  displacement pattern
  AN2(AN6): circular displacement pattern
  the optional argument TMSTR is a logical variable (true or false) to indicate whether the
  the pseudo-time needs stretching/shortening to maintain equal displacement increment
  for each displacement reversal (default = false)
  OPTIONS(NCYC) is an optional structure array with the following fields:
        .TrmpN = time interval for ramping up         the application of the axial force N
        .TrmpU = time interval for ramping up or down the application of the first displacement
        .Nsub  = time subdivision for description of the circular path
        .NRat  = ratio of axial force variation relative to constant value
        .HCyc  = true or false; true for half    cycle instead of full displacement cycle
        .QCyc  = true or false; true for quarter cycle instead of full displacement cycle
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [Create_DispCyclewN](Create_DispCyclewN.html "function [DspHst,FrcHst] = Create_DispCyclewN (DspPat,Options)"){.code}
    CREATE_DISPCYCLEwN generate time and value pairs of a displacement
    cycle with normal force

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
