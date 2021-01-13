[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Solution_Library](FEDEASLab.html) \>
Create_PlastLimSurface.m

</div>

# Create_PlastLimSurface

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**CREATE_PLASTLIMSURFACE set up pologonal plastic limit surface for
truss and 2d frame elements**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function LimitSurf = Create_PlastLimSurface (ElemName,ElemData)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
CREATE_PLASTLIMSURFACE set up pologonal plastic limit surface for truss and 2d frame elements
  LIMITSURF = CREATE_PLASTLIMSURFACE(ELEMNAME,ELEMDATA)
  the function sets up the polygonal plastic limit surface for the element
  type ELEMNAME (only truss and 2d frame elements supported);
  the polygonal plastic surface depends on the plastic axial capacity NP
  and flexural capacity MP in ELEMDATA;
  LIMITSURF is an array with the plastic capacity values at the polygon corners;
  the field NMOPT of ELEMDATA determines the type of plastic surface;
  the current options are:
    'None' : no interaction between axial and flexural capacity
    'Dmnd' : diamond shaped polygon for plastic limit surface
    'AISC' : 8-sided polygon according to AISC specifications
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
