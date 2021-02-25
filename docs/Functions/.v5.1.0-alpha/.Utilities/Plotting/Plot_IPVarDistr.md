[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Plot_IPVarDistr.m

</div>

# Plot_IPVarDistr

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**PLOT_IPVARDISTR plots distribution of integration point variables of
elements with sections**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Plot_IPVarDistr
(Model,ElemData,Post,Component,ElemList,UserScale)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
PLOT_IPVARDISTR plots distribution of integration point variables of elements with sections
  PLOT_IPVARDISTR (MODEL,ELEMDATA,POST,COMPONENT,ELEMLIST,SCALE)
  the function plots the distribution of integration point variables of elements with sections
  identified by character variable COMPONENT in the current window; plotting is limited
  to elements in ELEMLIST; the model information is available in data structure MODEL
  and the element properties in cell array ELEMDATA; post-processing information is supplied
  in data structure POST; COMPONENT is a character variable with e for section deformation
  and s for section force (Example: s(2) represents the second component of the section
  force vector, i.e. the bending moment Mz in 2d Bernoulli sections);
  the optional row vector ELEMLIST contains the numbers of elements to include for plotting,
  e.g. [1:4 7 9] selects elements 1 through 4, 7 and 9;
  the optional scalar argument USERSCALE is a magnification factor for the diagram (default=1)
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

-   [Get_ModelScale](Get_ModelScale.html "function [ModSc,maxL,minL] = Get_ModelScale (Model,Ratio)"){.code}
    GET_MODELSCALE determines maximum and minimum element length in
    Model

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
