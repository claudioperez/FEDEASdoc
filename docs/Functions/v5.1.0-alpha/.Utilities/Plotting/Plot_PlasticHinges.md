[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Plot_PlasticHinges.m

</div>

# Plot_PlasticHinges

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**PLOT_PLASTICHINGES display plastic hinge locations in current window**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Plot_PlasticHinges (Model,ElemData,U,Post,PlotOpt)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
PLOT_PLASTICHINGES display plastic hinge locations in current window
  PLOT_PLASTICHINGES (MODEL,ELEMDATA,U,POST,PLOTOPT)
  the function displays in the current window the plastic hinge locations
  for the elements of the structural model in data structure MODEL (only 2d models for now).
  There are two options for supplying the plastic capacities and basic force values:
      (a) ELEMDATA is a vector of plastic capacities and 
  or, (b) ELEMDATA is a cell array with the plastic capacities in fields Np for the axial,
          and Mp for the flexural capacity.
  In the presence of the global dof displacements U the plastic hinges are displayed
  in the deformed configuration otherwise in the undeformed.
  There are three options for POST:
      (a) POST is the vector of basic forces Q corresponding to case (a) of ELEMDATA 
      (b) POST is the vector of plastic deformation increments DVPL in which case
          ELEMDATA is either empty or a character variable with the N-M interaction option NMOPT;
          NMOPT can be one of three options: 'None' (default), 'Dmnd' or 'AISC';
      (c) POST is a cell array with post-processing information in the fields of POST.ELEM{el}.
  PLOTOPT is an optional data structure controlling the display;
  in its absense the function displays the plastic hinges with default properties;
  PLOTOPT has the following fields:
    EList: list of elements for which plastic hinges are displayed (default all elements)
    HngSF: scale factor for size of plastic hinge symbol                  (default = 1)
    HOfSF: factor for offset of the plastic hinge symbol from element end (default = 1)  
    FHClr: color for flexural hinges                                      (default='r')
    CHClr: color for column hinges with N-M interaction               (default = [1 0.6 0])
    AHClr: color for axial hinges in truss elements                   (default = [1 0.6 0])
    tol:   relative tolerance for plastic capacity check;
           absolute tolerance for plastic rotation check              (default=1e-6)
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

-   [Get_ModelScale](Get_ModelScale.html "function [ModSc,maxL,minL] = Get_ModelScale (Model,Ratio)"){.code}
    GET_MODELSCALE determines maximum and minimum element length in
    Model
-   [Plot_Hinge4Elem](Plot_Hinge4Elem.html "function Plot_Hinge4Elem (nq,HngId,AxHngCoor,FlHngCoor,Colors)"){.code}
    PLOT_HINGE4ELEM plot releases or plastic hinges for truss or frame
    element

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
