[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Plot_DispPath.m

</div>

# Plot_DispPath

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**PLOT_DISPPATH plots biaxial displacement path in current window**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function AxHndl = Plot_DispPath (DspHst,PlotOpt)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
PLOT_DISPPATH plots biaxial displacement path in current window
  AXHNDL = PLOT_DISPPATH (DSPHST,PLOTOPT)
  the function plots the biaxial displacement history in the structure array DSPHST
  in the current window and returns the axis handle in AXHNDL;
  the arrow on the displacement path corresponds to increasing pseudo-time;
  DSPHST has two entries with fields Time and Value;
  the optional argument PLOTOPT is a structure with the following fields:
  PLOTOPT.LnWth : line width for 2 or 3 plots (default=3)
         .LnStl : line style sequence for 2 or 3 plots (default='s-','o-','h-')
         .Color : color      sequence for 2 or 3 plots (default='k','b','r') 
         .MrkSz : marker size for 2 or 3 plots (default=5)
         .MFClr : marker face color sequence for 2 or 3 plots (default='k','b','r')
         .TipSF : scale factor for controlling the size of the arrow tip (default = 1);
         .ArWth : line width of arrow shaft (default = 1);
         .ArClr : color of arrow shaft and tip (default = 'k');
         .AbsSF : true or false to indicate absolute or relative to arrow length scaling
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

-   [Draw_Arrow](Draw_Arrow.html "function varargout = Draw_Arrow (Astr,Aend,Aln,PlotOpt)"){.code}
    DRAW_ARROW draws 2d or 3d arrow
-   [Draw_AxisCross](Draw_AxisCross.html "function Draw_AxisCross (Xlim,Ylim,PlotOpt)"){.code}
    DRAW_AXISCROSS draw cross through the axes origin of the x-y data

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
