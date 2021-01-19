[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Plot_Model.m

</div>

# Plot_Model

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**PLOT_MODEL plots the original or deformed geometry of the structural
model**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Plot_Model (Model,U,MPlOpt)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
PLOT_MODEL plots the original or deformed geometry of the structural model
  PLOT_MODEL (MODEL,U,MPLOPT)
  the function plots in the current window the original or deformed geometry
  of the structural model in the data structure MODEL depending
  on the presence of the global displacement vector U in the argument list;
  MPLOPT is an optional data structure controlling the display;
  in its absense the function plots the model with default values;
  MPLOPT has the following fields:
    MAGF : magnification factor for deformed wireframe (default=10)
    NodSF: scale factor for size of node symbol (default=1)
    LnStl: line style (default = '-' for undeformed, '-.' for deformed configuration)
    LnWth: line width (default = 2)
    LnClr: wireframe and node color (default = 'b' for undeformed,
                                               'k' for deformed configuration)
    PlNod: switch for displaying node symbols (default ='no')
    PlBnd: switch for displaying boundary symbols (default='no')
    BsClr: color for boundary nodes and symbols (default=[0.6 0 0.6])
    PlJnt: switch for plotting joint offsets  (default='yes')
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

-   [Draw_Cube](Draw_Cube.html "function Draw_Cube (XYZc,Size,Color)"){.code}
    DRAW_CUBE draws cube in current window
-   [Get_ModelScale](Get_ModelScale.html "function [ModSc,maxL,minL] = Get_ModelScale (Model,Ratio)"){.code}
    GET_MODELSCALE determines maximum and minimum element length in
    Model
-   [Plot_BounCond](Plot_BounCond.html "function Plot_BounCond (XYZ,BOUN,BsClr,BsSz)"){.code}
    PLOT_BOUNCOND plots symbols for boundary conditions of structural
    model

This function is called by:

-   [Animate_EventSequence](Animate_EventSequence.html "function Animate_EventSequence (Model,ElemData,Ufh,Qh,PlotOpt)"){.code}
    ANIMATE_EVENTSEQUENCE generate plot sequence with location of
    plastic hinges for each event
-   [Animate_ResponsewHngHist](Animate_ResponsewHngHist.html "function Animate_ResponsewHngHist (Model,ElemData,Post,PlotOpt)"){.code}
    ANIMATE_RESPONSEwHNGHIST interactive or recorded response and
    plastic hinge history
-   [Plot_DeformedStructure](Plot_DeformedStructure.html "function Plot_DeformedStructure (Model,ElemData,U,Post,PlotOpt)"){.code}
    PLOT_DEFORMEDSTRUCTURE plot deformed shape of the structure

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
