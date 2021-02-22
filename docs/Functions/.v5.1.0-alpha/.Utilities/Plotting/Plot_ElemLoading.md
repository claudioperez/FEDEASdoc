[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Plot_ElemLoading.m

</div>

# Plot_ElemLoading

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**PLOT_ELEMLOADING display element loading in current window**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Plot_ElemLoading (Model,ElemData,PlotOpt)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
PLOT_ELEMLOADING display element loading in current window
  PLOT_ELEMLOADING (MODEL,ELEMDATA,PLOTOPT)
  the function displays in the current window the distributed element loading
  and the initial deformations in ELEMDATA for the structural model in data structure MODEL;
  PLOTOPT is an optional data structure controlling the display;
  in its absense the function plots the model with default values;
  PLOTOPT has the following fields:
    FrcSF: scale factor for shaft of nodal force arrow (default = 1)
    TipSF: scale factor for nodal force arrow tip
    ArWth: width of nodal force arrow shaft (default=3)
    ArClr: color for nodal force arrow shaft and tip (default='r')
    FntSF: scale factor for font size of force label
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

-   [Draw_Arrow](Draw_Arrow.html "function varargout = Draw_Arrow (Astr,Aend,Aln,PlotOpt)"){.code}
    DRAW_ARROW draws 2d or 3d arrow
-   [Get_ModelScale](Get_ModelScale.html "function [ModSc,maxL,minL] = Get_ModelScale (Model,Ratio)"){.code}
    GET_MODELSCALE determines maximum and minimum element length in
    Model

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
