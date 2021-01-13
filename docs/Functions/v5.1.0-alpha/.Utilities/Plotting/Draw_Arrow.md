[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Draw_Arrow.m

</div>

# Draw_Arrow

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**DRAW_ARROW draws 2d or 3d arrow**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function varargout = Draw_Arrow (Astr,Aend,Aln,PlotOpt)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
DRAW_ARROW draws 2d or 3d arrow
  AEND = DRAW_ARROW (ASTR,AEND,ALN,PLOTOPT)
  the function draws an arrow with starting point ASTR and end point AEND, if ALN is empty;
  if ALN is specified, then it represents the arrow length
  with AEND interpreted as the arrow direction; in this case the function returns
  the end point coordinates of the arrow in vector AEND
  PLOTOPT is a data structure for controlling the arrow display with the following fields:
         TipSF: scale factor for controlling the size of the arrow tip (default = 1);
         ArWth: line width of arrow shaft (default = 1);
         ArClr: color of arrow shaft and tip (default = 'k');
         AbsSF: true or false to indicate absolute or relative to arrow length scaling
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

-   [Label_Model](Label_Model.html "function Label_Model (Model,LblOpt)"){.code}
    LABEL_MODEL displays element and node numbers and global axes in the
    current window
-   [Plot_DispPath](Plot_DispPath.html "function AxHndl = Plot_DispPath (DspHst,PlotOpt)"){.code}
    PLOT_DISPPATH plots biaxial displacement path in current window
-   [Plot_ElemLoading](Plot_ElemLoading.html "function Plot_ElemLoading (Model,ElemData,PlotOpt)"){.code}
    PLOT_ELEMLOADING display element loading in current window
-   [Plot_NodalForces](Plot_NodalForces.html "function Plot_NodalForces (Model,Loading,PlotOpt)"){.code}
    PLOT_NODALFORCES display nodal forces in current window
-   [Plot_SectionGeometry](Plot_SectionGeometry.html "function Plot_SectionGeometry (SecData,PlotOpt)"){.code}
    PLOT_SECTIONGEOMETRY plots cross section geometry in current window

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
