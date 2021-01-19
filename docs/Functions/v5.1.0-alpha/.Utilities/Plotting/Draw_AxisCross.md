[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Draw_AxisCross.m

</div>

# Draw_AxisCross

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**DRAW_AXISCROSS draw cross through the axes origin of the x-y data**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Draw_AxisCross (Xlim,Ylim,PlotOpt)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
DRAW_AXISCROSS draw cross through the axes origin of the x-y data
  DRAW_AXISCROSS (XLIM,YLIM,PLOTOPT)
  the function draws a cross through the axes origin of the x-y data
  with a gray, solid line style and 1.5 pt line width;
  these properties can be controlled by specifying the fields LnStl, LnWth and Color
  of the optional argument PLOTOPT;
  XLIM and YLIM are 1x2 numerical arrays for the specification of the axes endpoints
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

-   [Plot_DispPath](Plot_DispPath.html "function AxHndl = Plot_DispPath (DspHst,PlotOpt)"){.code}
    PLOT_DISPPATH plots biaxial displacement path in current window
-   [Plot_LoadHistory](Plot_LoadHistory.html "function AxHndl = Plot_LoadHistory(DspHst,FrcHst,PlotOpt)"){.code}
    PLOT_LOADHISTORY plots uniaxial or biaxial displacement and axial
    force history in current window
-   [Plot_SectionGeometry](Plot_SectionGeometry.html "function Plot_SectionGeometry (SecData,PlotOpt)"){.code}
    PLOT_SECTIONGEOMETRY plots cross section geometry in current window
-   [Plot_StoryDistr](Plot_StoryDistr.html "function AxHndl = Plot_StoryDistr (Xp,PlotOpt)"){.code}
    PLOT_STORYDISTR plots all columns of array XP against the row index
-   [Plot_XYData](Plot_XYData.html "function AxHndl = Plot_XYData (Xp,Yp,PlotOpt)"){.code}
    PLOT_XYDATA plots one or more pairs of X and Y array columns

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
