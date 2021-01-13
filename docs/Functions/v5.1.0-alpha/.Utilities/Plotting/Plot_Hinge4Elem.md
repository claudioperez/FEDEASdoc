[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Plot_Hinge4Elem.m

</div>

# Plot_Hinge4Elem

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**PLOT_HINGE4ELEM plot releases or plastic hinges for truss or frame
element**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Plot_Hinge4Elem (nq,HngId,AxHngCoor,FlHngCoor,Colors)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
PLOT_HINGE4ELEM plot releases or plastic hinges for truss or frame element
  PLOT_HINGE4ELEM (NQ,HNGID,AXHNGCOOR,FLHNGCOOR,PLOTOPT)
  the function plots the releases or plastic hinges for a truss or frame element
  NQ is the number of basic forces
  HNGID is the index vector for the location of releases/plastic hinges
  AXHNGCOOR are the coordinates for the axial hinge location
  FLHNGCOOR are the coordinates for the flexural hinge location
  COLORS is a data structure with the release/plastic hinge colors in fields
        .AHCrl color for axial release or plastic hinge
        .FHCrl color for flexural release or plastic hinge without N-M interaction
        .CHCrl color for flexural release or plastic hinge with    N-M interaction
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

-   [Plot_PlasticHinges](Plot_PlasticHinges.html "function Plot_PlasticHinges (Model,ElemData,U,Post,PlotOpt)"){.code}
    PLOT_PLASTICHINGES display plastic hinge locations in current window

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
