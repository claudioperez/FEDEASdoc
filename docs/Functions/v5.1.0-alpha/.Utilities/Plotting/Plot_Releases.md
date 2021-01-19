[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Plot_Releases.m

</div>

# Plot_Releases

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**PLOT_RELEASES display element releases in current window**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Plot_Releases (Model,ElemData,U,PlotOpt)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
PLOT_RELEASES display element releases in current window
  PLOT_RELEASES (MODEL,ELEMDATA,U,PLOTOPT)
  the function displays in the current window internal force releases
  for the elements of the structural model in data structure MODEL;
  flexural releases are inserted for truss elements; for frame elements
  releases are inserted according to entries in the field Release of ELEMDATA
  the releases are displayed in the undeformed or deformed configuration (chords only)
  depending on the presence of the input argument U; 
  PLOTOPT is an optional data structure controlling the display;
  in its absense the function plots the model with default values;
  PLOTOPT has the following fields:
    MAGF : magnification factor for deformed configuration   (default=10)
    HngSF: scale factor for size of hinge symbol             (default = 1)
    HOfSF: factor for hinge symbol offset from element end   (default = 1)
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
