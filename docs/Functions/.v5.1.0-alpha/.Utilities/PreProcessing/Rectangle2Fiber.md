[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> Rectangle2Fiber.m

</div>

# Rectangle2Fiber

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**RECTANGLE2FIBER integration points and weights for 2d-integration of a
rectangle**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function \[yfib,zfib,wfib\] = Rectangle2Fiber
(patcoor,IntTyp,nyfib,nzfib)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
RECTANGLE2FIBER integration points and weights for 2d-integration of a rectangle
  [YFIB,ZFIB,WFIB] = RECTANGLE2FIBER (PATCOOR,INTTYP,NYFIB,NZFIB)
  the function determines the locations in vectors YFIB and ZFIB and the integration weights
  in vector WFIB for the 2d integration of a rectangle with the integration scheme
  in character array INTTYP and the number of integration points in the y-direction in NYFIB
  and in the z-direction in NZFIB, respectively;
  the geometry of the rectangle is supplied by specifying the
  coordinates of opposite corners in array PATCOOR [ y1 z1 (top left); y2 z2 (bottom right)]
  (NOTE: right handed local coordinate system x-y-z!)
  INTTYP can be either 'Midpoint', 'Gauss', Lobatto' or 'Trap'
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

-   [Create_IPMesh4MultRectShape](Create_IPMesh4MultRectShape.html "function Shape = Create_IPMesh4MultRectShape (Shape,MeshData)"){.code}
    CREATE_IPMESH4MULTRECTSHAPE fiber discretization for section of
    several rectangular patches
-   [Create_IPMesh4Rect](Create_IPMesh4Rect.html "function [yfib,zfib,wfib,MatID] = Create_IPMesh4Rect (SecData)"){.code}
    CREATE_IPMESH4RECT coordinates, weights and material IDs for
    rectangular section with cover
-   [Create_IPMesh4WFShape](Create_IPMesh4WFShape.html "function [yfib,zfib,wfib,MatID] = Create_IPMesh4WFShape (SecData)"){.code}
    CREATE_IPMESH4WFSHAPE coordinates, weights and material IDs for wide
    flange section

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
