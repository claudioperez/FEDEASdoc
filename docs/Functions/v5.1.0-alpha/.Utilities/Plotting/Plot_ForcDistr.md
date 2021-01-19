[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Plot_ForcDistr.m

</div>

# Plot_ForcDistr

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**PLOT_FORCDISTR plots internal force distribution for truss and frame
elements in ElemList**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Plot_ForcDistr
(Model,ElemData,Post,Component,ElemList,UserScale)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
PLOT_FORCDISTR plots internal force distribution for truss and frame elements in ElemList
  PLOT_FORCDISTR (MODEL,ELEMDATA,POST,COMPONENT,ELEMLIST,USERSCALE)
  function plots the distribution of the internal force identified by COMPONENT
  for the truss and frame elements in ELEMLIST in the current window; the model information
  is available in data structure MODEL and the element properties in cell array ELEMDATA;
  the current response of the model is supplied in data structure POST;
  COMPONENT is a character variable with one of the following values:
  N for axial force, Mx for torsional moment, My for bending moment about y-axis
  and Mz for bending moment about z-axis; ELEMLIST is optional (default is all elements)
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
