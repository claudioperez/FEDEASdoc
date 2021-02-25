[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Plot_LoadHistory.m

</div>

# Plot_LoadHistory

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**PLOT_LOADHISTORY plots uniaxial or biaxial displacement and axial
force history in current window**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function AxHndl = Plot_LoadHistory(DspHst,FrcHst,PlotOpt)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
PLOT_LOADHISTORY plots uniaxial or biaxial displacement and axial force history in current window
  AXHNDL = PLOT_LOADHISTORY(DSPHST,FRCHST,PLOTOPT)
  the function plots the uniaxial or biaxial displacement history in the data structure DSPHST
  and the axial force history in the data structure FRCHST in the current window and
  returns the axis handle in AXHNDL;
  DSPHST has one entry for uniaxial and 2 entries for biaxial displacement patterns and
  has the fields Time and Value; FRCHST also has the fields Time and Value;
  the optional argument PLOTOPT is a structure with the following fields:
  PLOTOPT.LnWth : line width for 2 or 3 plots (default=3)
         .LnStl : line style sequence for 2 or 3 plots (default='s-','o-','h-')
         .Color : color      sequence for 2 or 3 plots (default='k','b','r') 
         .MarSz : marker size for 2 or 3 plots (default=3)
         .MFClr : marker face color sequence for 2 or 3 plots (default='k','b','r')
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

-   [Draw_AxisCross](Draw_AxisCross.html "function Draw_AxisCross (Xlim,Ylim,PlotOpt)"){.code}
    DRAW_AXISCROSS draw cross through the axes origin of the x-y data

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
