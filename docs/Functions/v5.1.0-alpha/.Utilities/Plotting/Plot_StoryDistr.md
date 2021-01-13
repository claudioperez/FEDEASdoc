[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Plot_StoryDistr.m

</div>

# Plot_StoryDistr

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**PLOT_STORYDISTR plots all columns of array XP against the row index**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function AxHndl = Plot_StoryDistr (Xp,PlotOpt)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
PLOT_STORYDISTR plots all columns of array XP against the row index
  AXHNDL = PLOT_STORYDISTR (XP,PLOTOPT)
  the function plots in the current window all columns of the array XP against the row index
  which is supposed to correspond to the story number and returns the axis handle in AXHNDL;
  the optional argument PLOTOPT is a structure with the following fields:
  PLOTOPT.LnWth : line width             for plot   (default = 2)
         .LnStl  : line style sequence   for plot   (default = {'-','--',':','-.',':','--'} )
         .LnClr  : color      sequence   for plot   (default = {'b','r','k','b','r','k'} ) 
         .MrkSz  : marker size           for plot   (default = 3)
         .MrkClr : marker color sequence for plot   (default = {'b','r','k','b','r','k'} )
         .MrkTyp : marker type sequence  for plot   (default = {'o','s','d','p','+','*'} )
         .NoXTk  : number of tick marks on X-axis (default = 5 including end points)
         .NoYTk  : number of tick marks on Y-axis (default = 5 including end points)
         .FntSz  : font size for plot elements    (default = 30)
         .XLbl   : character variable for X-Label (default = 'X-data')
         .YLbl   : character variable for Y-Label (default = 'X-data')
         .Legnd  : cell array of characters for plot legend (default: 1.Data, 2.Data, etc)
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
