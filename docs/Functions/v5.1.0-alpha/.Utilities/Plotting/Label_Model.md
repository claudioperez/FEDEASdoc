[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Label_Model.m

</div>

# Label_Model

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**LABEL_MODEL displays element and node numbers and global axes in the
current window**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Label_Model (Model,LblOpt)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
LABEL_MODEL displays element and node numbers and global axes in the current window   
  LABEL_MODEL (MODEL,LBLOPT)
  the function displays in the current window labels for nodes and elements,
  and the global coordinate axes;
  LBLOPT is an optional data structure controlling the display;
  in its absense the function plots all items with default values;
  LBLOPT has the following fields (all optional)
    Item : character variable with values 'node','elem', 'axes' (default='all')
    FntSF: font magnification factor (default = 1)
    AxsSF: axis arrow length magnification factor (default = 1)
    LOfSF: node and element label offset magnification factor (default = 1)
    NList: list of nodes    to label (default all nodes    in the model)
    EList: list of elements to label (default all elements in the model)
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

-   [Draw_Arrow](Draw_Arrow.html "function varargout = Draw_Arrow (Astr,Aend,Aln,PlotOpt)"){.code}
    DRAW_ARROW draws 2d or 3d arrow
-   [Get_ModelScale](Get_ModelScale.html "function [ModSc,maxL,minL] = Get_ModelScale (Model,Ratio)"){.code}
    GET_MODELSCALE determines maximum and minimum element length in
    Model

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
