[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Plot_BounCond.m

</div>

# Plot_BounCond

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**PLOT_BOUNCOND plots symbols for boundary conditions of structural
model**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Plot_BounCond (XYZ,BOUN,BsClr,BsSz)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
PLOT_BOUNCOND plots symbols for boundary conditions of structural model
  PLOT_BOUNCOND (XYZ,BOUN,BSSZ)
  the function plots symbols for the boundary conditions of the structural
  model for the node coordinates in the array XYZ (undeformed or deformed
  configuration and the boundary conditions in the array BOUN;
  BSSZ gives the size of the node and boundary symbol
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

-   [Plot_DeformedStructure](Plot_DeformedStructure.html "function Plot_DeformedStructure (Model,ElemData,U,Post,PlotOpt)"){.code}
    PLOT_DEFORMEDSTRUCTURE plot deformed shape of the structure
-   [Plot_Model](Plot_Model.html "function Plot_Model (Model,U,MPlOpt)"){.code}
    PLOT_MODEL plots the original or deformed geometry of the structural
    model

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
