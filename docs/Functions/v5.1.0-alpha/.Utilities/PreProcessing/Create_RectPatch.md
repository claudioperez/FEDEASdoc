[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> Create_RectPatch.m

</div>

# Create_RectPatch

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**CREATE_RECTPATCH generate corner coordinates of rectangular patch for
given reference point**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function yz = Create_RectPatch (ty,tz,sy,sz)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
CREATE_RECTPATCH generate corner coordinates of rectangular patch for given reference point
  YZ = CREATE_RECTPATCH (TY,TZ,SY,SZ)
  the function generates the corner coordinates of a rectangular patch TY x TZ, where TY is
  the dimension in Y and TZ is the dimension in Z, with respect to a reference point at a
  distance SY in Y and SZ in Z from the centroid of the patch;
  the function returns the corner coordinates in the 1x4 array YZ = [Y1 Z1 Y2 Z2] where
  1 refers to the upper left corner and 2 to the lower right corner of the rectangular patch

  Section coordinate system:
                                   ^ y
                                   |
                               ----+----
                               |   |   |
                               |   |   |
                         z <---+---+   |
                               |       |
                               |       |
                               ---------
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

-   [Create_BoxOutline](Create_BoxOutline.html "function [Outline,A,sy,sz] = Create_BoxOutline (Data)"){.code}
    CREATE_BOXOUTLINE generate geometry outline for box section
-   [Create_BoxwOvhOutline](Create_BoxwOvhOutline.html "function [Outline,A,sy,sz] = Create_BoxwOvhOutline (Data)"){.code}
    CREATE_BOXwOVHOUTLINE generate geometry outline for box section
-   [Create_CSecOutline](Create_CSecOutline.html "function [Outline,A,sy,sz] = Create_CSecOutline (Data)"){.code}
    CREATE_CSECOUTLINE generate geometry outline for C-section
-   [Create_IPMesh4WFShape](Create_IPMesh4WFShape.html "function [yfib,zfib,wfib,MatID] = Create_IPMesh4WFShape (SecData)"){.code}
    CREATE_IPMESH4WFSHAPE coordinates, weights and material IDs for wide
    flange section
-   [Create_ISecOutline](Create_ISecOutline.html "function [Outline,A,sy,sz] = Create_ISecOutline (Data)"){.code}
    CREATE_ISECOUTLINE generate geometry outline for I-section
-   [Create_LSecOutline](Create_LSecOutline.html "function [Outline,A,sy,sz] = Create_LSecOutline (Data)"){.code}
    CREATE_LSECOUTLINE generate geometry outline for L-section
-   [Create_RectShape](Create_RectShape.html "function Shape = Create_RectShape (ndm,SType,Data)"){.code}
    CREATE_RECTSHAPE generate geometry outline and assign material
    properties for rectangle
-   [Create_RectwCovOutline](Create_RectwCovOutline.html "function [Outline,A,sy,sz] = Create_RectwCovOutline (Data)"){.code}
    CREATE_RECTwCOVOUTLINE generate geometry outline for rectangular
    section with cover
-   [Create_SSecOutline](Create_SSecOutline.html "function [Outline,A,sy,sz] = Create_SSecOutline (Data)"){.code}
    CREATE_SSECOUTLINE generate geometry outline for C-section
-   [Create_TSecOutline](Create_TSecOutline.html "function [Outline,A,sy,sz] = Create_TSecOutline (Data)"){.code}
    CREATE_TSECOUTLINE generate geometry outline for T-section

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
