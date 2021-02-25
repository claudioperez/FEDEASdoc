[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Plot_DeformedStructure.m

</div>

# Plot_DeformedStructure

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**PLOT_DEFORMEDSTRUCTURE plot deformed shape of the structure**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Plot_DeformedStructure (Model,ElemData,U,Post,PlotOpt)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
PLOT_DEFORMEDSTRUCTURE plot deformed shape of the structure
  PLOT_DEFORMEDSTRUCTURE (MODEL,ELEMDATA,U,POST,PLOTOPT)
  the function plots the deformed shape of the structural model in data structure MODEL
  based on the current displacements U and the element deformations;
  the cell array ELEMDATA contains information about element properties and loading;
  POST is either the vector of the element deformations Veps, or
  a cell array with the element deformations in subfield ve of field Elem;
  PLOTOPT is a data structure for plotting options with the following fields:
    MAGF : magnification factor for deformed shape (default=10)
    EList: list of elements to include in deformed shape (default all elements)
    LnStl: line style for deformed shape (default = '-', i.e. solid line)
    LnWth: line thickness for deformed shape (default = 2)  
    LnClr: color for deformed shape (default = 'r', i.e. red)
    PlJnt: switch for plotting joint offsets (default='yes')
    PlCrd: switch for plotting element chord (default='no')
    PlRel: switch for plotting element releases (defaul='yes')
    HngSF: scale factor for size of release symbol (default = 1)
    HOfSF: scale factor for offset of flexural hinge symbol from element end (default = 1)  
    PlBnd: switch for displaying boundary symbols (default='yes')
    BsClr: color for boundary nodes and symbols (default=[0.6 0 0.6])
    NodSF: scale factor for size of boundary symbol (default = 1)
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

-   [Get_HngPos4DefoElem](Get_HngPos4DefoElem.html "function [AxHngCoor,FlHngCoor] = Get_HngPos4DefoElem (XYiod,XYjod,xyd,HngOpt)"){.code}
    GET_HNGPOS4DEFOELEM determine axial and flexural hinge position for
    deformed element
-   [Get_ModelScale](Get_ModelScale.html "function [ModSc,maxL,minL] = Get_ModelScale (Model,Ratio)"){.code}
    GET_MODELSCALE determines maximum and minimum element length in
    Model
-   [Plot_BounCond](Plot_BounCond.html "function Plot_BounCond (XYZ,BOUN,BsClr,BsSz)"){.code}
    PLOT_BOUNCOND plots symbols for boundary conditions of structural
    model
-   [Plot_Model](Plot_Model.html "function Plot_Model (Model,U,MPlOpt)"){.code}
    PLOT_MODEL plots the original or deformed geometry of the structural
    model

This function is called by:

-   [Animate_EventSequence](Animate_EventSequence.html "function Animate_EventSequence (Model,ElemData,Ufh,Qh,PlotOpt)"){.code}
    ANIMATE_EVENTSEQUENCE generate plot sequence with location of
    plastic hinges for each event
-   [Animate_ResponsewHngHist](Animate_ResponsewHngHist.html "function Animate_ResponsewHngHist (Model,ElemData,Post,PlotOpt)"){.code}
    ANIMATE_RESPONSEwHNGHIST interactive or recorded response and
    plastic hinge history

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
