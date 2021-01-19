[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> Create_IPMesh4Rect.m

</div>

# Create_IPMesh4Rect

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**CREATE_IPMESH4RECT coordinates, weights and material IDs for
rectangular section with cover**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function \[yfib,zfib,wfib,MatID\] = Create_IPMesh4Rect (SecData)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
CREATE_IPMESH4RECT coordinates, weights and material IDs for rectangular section with cover
  [YFIB,ZFIB,WFIB,MATID] = CREATE_IPMESH4RECT (SECDATA)
  the function generates the coordinates YFIB and ZFIB, the integration weights WFIB, and
  the material ID MATID for the fiber discretization of the rectangular section in SECDATA;
  the rectangular section can have a different top/bottom and side cover,
  as may be required for sections with reinforcing bars;
  SECDATA has two fields for assigning material IDs to core and cover fibers:
  FMatID  = row vector with material ID for corresponding core fiber  (default = row vector of 1s)
  FCovMID = row vector with material ID for corresponding cover fiber (default = row vector of 2s)
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

-   [Create_RectShape](Create_RectShape.html "function Shape = Create_RectShape (ndm,SType,Data)"){.code}
    CREATE_RECTSHAPE generate geometry outline and assign material
    properties for rectangle
-   [Rectangle2Fiber](Rectangle2Fiber.html "function [yfib,zfib,wfib] = Rectangle2Fiber (patcoor,IntTyp,nyfib,nzfib)"){.code}
    RECTANGLE2FIBER integration points and weights for 2d-integration of
    a rectangle

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
