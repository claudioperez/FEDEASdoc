[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Get_HngPos4DefoElem.m

</div>

# Get_HngPos4DefoElem

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**GET_HNGPOS4DEFOELEM determine axial and flexural hinge position for
deformed element**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function \[AxHngCoor,FlHngCoor\] = Get_HngPos4DefoElem
(XYiod,XYjod,xyd,HngOpt)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
GET_HNGPOS4DEFOELEM determine axial and flexural hinge position for deformed element
  [AXHNGCOOR,FLHNGCOOR] = GET_HNGPOS4DEFOELEM(XYIOD,XYJOD,XYD,HNGOPT)
  the function determines the axial hinge coordinates AXHNGCOOR and the
  flexural hinge coordinates FLHNGCOOR for a deformed truss or frame element
  from the end node coordinates XYIOD and XYJOD of the deformed configuration
  and the local deformed coordinates XYD of the deformed shape;
  the data structure HNGOPT has the fields HngSz for the hinge size and
  HngOf for the offset of the hinge location from the element end
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

-   [Plot_DeformedStructure](Plot_DeformedStructure.html "function Plot_DeformedStructure (Model,ElemData,U,Post,PlotOpt)"){.code}
    PLOT_DEFORMEDSTRUCTURE plot deformed shape of the structure

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
