[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Animate_EventSequence.m

</div>

# Animate_EventSequence

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**ANIMATE_EVENTSEQUENCE generate plot sequence with location of plastic
hinges for each event**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Animate_EventSequence (Model,ElemData,Ufh,Qh,PlotOpt)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
ANIMATE_EVENTSEQUENCE generate plot sequence with location of plastic hinges for each event 
  ANIMATE_EVENTSEQUENCE (MODEL,ELEMDATA,UFH,QH,PLOTOPT)
  the function generates a plot sequence of the deformed structural model with the plastic hinge
  locations at each event, thus animating the plastic hinge formation sequence;
  the free global dof displacement history is provided in array UFH, with one column for each event,
  and the corresponding basic force history in array QH, with one column for each event;
  the data structure MODEL contains information about the structural model, while
  ELEMDATA contains element property information; there are two options for supplying
  the plastic capacities of the structural elements in ELEMDATA:
  (a) as fields Np for axial and Mp for flexural of the cell array ELEMDATA 
  (a) as a column vector
  PLOTOPT is a data structure for controlling the plastic hinge display
  with the following fields:
    HngSF: scale factor for size of plastic hinge symbol (default = 1)
    HOfSF: factor for offset of the plastic hinge symbol from element end (default = 1)  
    LnClr: line color for deformed shape (default='r' for red)
    CdClr: line color for element chord (default='k' for black)
    PlJnt: switch for plotting joint offsets (default='yes')
    PlCrd: display element chords with deformed shape (default='no')
    NodSF: factor for relative size of node symbol (default=1)  
    tol:   relative tolerance for plastic capacity check;
           absolute tolerance for plastic rotation check
    Inter: switch for interactive animation (yes, default) or video generation (no)
  MovieFN: video file name (default=Movie)
  PauseDur: pause duration for screen animation in sec (default=0)
  FrameRate: frames per second for video recording (default=30)
  Nsub :  number of interpolated intermediate plots between events for movie
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

-   [Plot_DeformedStructure](Plot_DeformedStructure.html "function Plot_DeformedStructure (Model,ElemData,U,Post,PlotOpt)"){.code}
    PLOT_DEFORMEDSTRUCTURE plot deformed shape of the structure
-   [Plot_Model](Plot_Model.html "function Plot_Model (Model,U,MPlOpt)"){.code}
    PLOT_MODEL plots the original or deformed geometry of the structural
    model
-   [Plot_PlasticHinges](Plot_PlasticHinges.html "function Plot_PlasticHinges (Model,ElemData,U,Post,PlotOpt)"){.code}
    PLOT_PLASTICHINGES display plastic hinge locations in current window

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
