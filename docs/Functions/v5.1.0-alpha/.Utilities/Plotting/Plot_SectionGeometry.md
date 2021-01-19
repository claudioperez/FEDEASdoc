[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Plot_SectionGeometry.m

</div>

# Plot_SectionGeometry

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**PLOT_SECTIONGEOMETRY plots cross section geometry in current window**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Plot_SectionGeometry (SecData,PlotOpt)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
PLOT_SECTIONGEOMETRY plots cross section geometry in current window
  PLOT_SECTIONGEOMETRY(SECDATA,PLOTOPT)
  the function plots the geometry of the cross section in SECDATA in the current window
  PLOTOPT is a structure with the following fields:
  PLOTOPT.IPDsp : true or false for displaying the location of integration points
         .FibDsp: true or false for displaying the fiber (section discretization) outline
         .BarDsp: true or false for displaying the reinforcing bars, if present
         .AxsDsp: true or false for displaying the section reference axes
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

-   [Draw_Arrow](Draw_Arrow.html "function varargout = Draw_Arrow (Astr,Aend,Aln,PlotOpt)"){.code}
    DRAW_ARROW draws 2d or 3d arrow
-   [Draw_AxisCross](Draw_AxisCross.html "function Draw_AxisCross (Xlim,Ylim,PlotOpt)"){.code}
    DRAW_AXISCROSS draw cross through the axes origin of the x-y data
-   [FontProp4PlotSection](FontProp4PlotSection.html "function [Font,lt,ls] = FontProp4PlotSection()"){.code}
    =========================================================================================
-   [LineProp4PlotSection](LineProp4PlotSection.html "function [Line] = LineProp4PlotSection()"){.code}
    =========================================================================================
-   [Plot_Mesh4Circ](Plot_Mesh4Circ.html "function Plot_Mesh4Circ (SecData)"){.code}
    PLOT_MESH4CIRC plots mesh for a circular disc or annulus in current
    window
-   [Plot_Mesh4MultRectShape](Plot_Mesh4MultRectShape.html "function Plot_Mesh4MultRectShape (SecData)"){.code}
    PLOT_MESH4MULTRECTSHAPE plot the mesh for section of several
    rectangular patches

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
