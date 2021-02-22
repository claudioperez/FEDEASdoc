[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> Create_IPMesh4WFShape.m

</div>

# Create_IPMesh4WFShape

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**CREATE_IPMESH4WFSHAPE coordinates, weights and material IDs for wide
flange section**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function \[yfib,zfib,wfib,MatID\] = Create_IPMesh4WFShape (SecData)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
CREATE_IPMESH4WFSHAPE coordinates, weights and material IDs for wide flange section
  [YFIB,ZFIB,WFIB,MATID] = CREATE_IPMESH4WFSHAPE (SECDATA)
  the function generates the coordinates YFIB and ZFIB, the integration weights WFIB, and
  the material ID MATID for the fiber discretization of the wide flange section in SECDATA;
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

-   [Create_RectPatch](Create_RectPatch.html "function yz = Create_RectPatch (ty,tz,sy,sz)"){.code}
    CREATE_RECTPATCH generate corner coordinates of rectangular patch
    for given reference point
-   [Rectangle2Fiber](Rectangle2Fiber.html "function [yfib,zfib,wfib] = Rectangle2Fiber (patcoor,IntTyp,nyfib,nzfib)"){.code}
    RECTANGLE2FIBER integration points and weights for 2d-integration of
    a rectangle

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
