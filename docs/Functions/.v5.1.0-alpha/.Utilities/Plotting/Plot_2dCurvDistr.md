[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Plot_2dCurvDistr.m

</div>

# Plot_2dCurvDistr

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**PLOT_2dCURVDISTR plot curvature distribution of 2d linear elastic
frame elements**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Plot_2dCurvDistr (Model,ElemData,Post,ElemList,UserScale)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
PLOT_2dCURVDISTR plot curvature distribution of 2d linear elastic frame elements    
  PLOT_2dCURVDISTR (MODEL,ELEMDATA,POST,ELEMLIST,USERSCALE)
  the function plots in the current window the curvature distribution for 2d linear elastic
  frame elements in ELEMLIST for the structural model in data structure MODEL;
  the cell array ELEMDATA carries information about element properties and loading;
  POST is either the vector of basic forces Q, or
  a cell array with post-processing information for the basic element forces in POST.ELEM{el}.Q;
  the optional row vector ELEMLIST contains the numbers of elements to include for plotting,
  e.g. [1:4 7 9] selects elements 1 through 4, 7 and 9;
  the optional scalar argument USERSCALE is a magnification factor for the diagram (default=1)
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

-   [Get_ModelScale](Get_ModelScale.html "function [ModSc,maxL,minL] = Get_ModelScale (Model,Ratio)"){.code}
    GET_MODELSCALE determines maximum and minimum element length in
    Model

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
