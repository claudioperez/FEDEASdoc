[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Animate_ResponsewHngHist.m

</div>

# Animate_ResponsewHngHist

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**ANIMATE_RESPONSEwHNGHIST interactive or recorded response and plastic
hinge history**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Animate_ResponsewHngHist (Model,ElemData,Post,PlotOpt)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
ANIMATE_RESPONSEwHNGHIST interactive or recorded response and plastic hinge history
  ANIMATE_RESPONSEwHNGHIST (MODEL,ELEMDATA,POST,PLOTOPT)
  the function generates the response and plastic hinge history of the model
  either interactively or in a recorded video file;
  the data structure MODEL contains information about the structural model, and
  element property information is provided in cell array ELEMDATA;
  the data structure POST contains the structure response history
  PLOTOPT is a data structure for controlling the response and plastic
  hinge display with the following fields:
    MAGF:  magnification factor for deformed shape (default=10)
    NodSF: scale factor for size of node symbol (default=1)
    HngSF: scale factor for size of plastic hinge symbol (default=1)
    HOfSF: factor for offset of plastic hinge symbol from element end (default=1)  
    Inter: switch for interactive animation (yes) or video generation (no=default)
    MovieFN:   video file name (default=Movie)
    PauseDur:  pause duration for screen animation in sec (default=0)
    FrameRate: frames per second for video recording (default=30)
    LnClr: line color for deformed shape (default='r' for red)
    PlJnt: switch for plotting joint offsets (default='yes')
    Nskip: number   of response states to skip (default=1, i.e. no skipping)
    Nstrt: first response state to plot (default=2, i.e. first after zero state)
    Npend: last  response state to plot (default=end of Post)
    ShowT: switch for showing time step number on screen (default=no)
    PlCrd: display element chords with deformed shape (default='no')
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

-   [Plot_DeformedStructure](Plot_DeformedStructure.html "function Plot_DeformedStructure (Model,ElemData,U,Post,PlotOpt)"){.code}
    PLOT_DEFORMEDSTRUCTURE plot deformed shape of the structure
-   [Plot_Model](Plot_Model.html "function Plot_Model (Model,U,MPlOpt)"){.code}
    PLOT_MODEL plots the original or deformed geometry of the structural
    model
-   [Plot_OpenPlasticHinges](Plot_OpenPlasticHinges.html "function Plot_OpenPlasticHinges (Model,ElemData,Post,PlotOpt)"){.code}
    PLOT_OPENPLASTICHINGES display plastic hinge locations in original
    or deformed configuration
-   [Plot_PlasticHinges](Plot_PlasticHinges.html "function Plot_PlasticHinges (Model,ElemData,U,Post,PlotOpt)"){.code}
    PLOT_PLASTICHINGES display plastic hinge locations in current window

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
