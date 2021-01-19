[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Plot_OpenPlasticHinges.m

</div>

# Plot_OpenPlasticHinges

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**PLOT_OPENPLASTICHINGES display plastic hinge locations in original or
deformed configuration**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Plot_OpenPlasticHinges (Model,ElemData,Post,PlotOpt)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
PLOT_OPENPLASTICHINGES display plastic hinge locations in original or deformed configuration
  PLOT_OPENPLASTICHINGES (MODEL,ELEMDATA,POST,PLOTOPT)
  the function displays in the current window the open plastic hinge locations;
  the data structure MODEL contains information about the structural model,
  with element property information provided in cell array ELEMDATA;
  the data structure POST contains all recorded structural response variables for one step
  PLOTOPT is a data structure for controlling the plastic hinge display
  with the following fields:
    EList: list of elements for which plastic hinges are displayed (default all elements)
    HngSF: scale factor for size of plastic hinge symbol (default = 1)
    HOfSF: factor for offset of the plastic hinge symbol from element end (default = 1)  
    FHClr: color for flexural hinges
    CHClr: color for column hinges with N-M interaction
    AHClr: color for axial hinges in truss elements
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

-   [Get_ModelScale](Get_ModelScale.html "function [ModSc,maxL,minL] = Get_ModelScale (Model,Ratio)"){.code}
    GET_MODELSCALE determines maximum and minimum element length in
    Model

This function is called by:

-   [Animate_ResponsewHngHist](Animate_ResponsewHngHist.html "function Animate_ResponsewHngHist (Model,ElemData,Post,PlotOpt)"){.code}
    ANIMATE_RESPONSEwHNGHIST interactive or recorded response and
    plastic hinge history

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
