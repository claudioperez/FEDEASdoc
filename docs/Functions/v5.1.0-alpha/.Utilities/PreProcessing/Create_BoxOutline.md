[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> Create_BoxOutline.m

</div>

# Create_BoxOutline

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**CREATE_BOXOUTLINE generate geometry outline for box section**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function \[Outline,A,sy,sz\] = Create_BoxOutline (Data)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
CREATE_BOXOUTLINE generate geometry outline for box section
  [OUTLINE,A,SY,SZ] = CREATE_BOXOUTLINE (NDM,DATA)
  the function creates the data structure OUTLINE for box section
  with geometric properties in data structure DATA with the following fields:
       ndm = 2 or 3 for uniaxial or biaxial section model, respectively 
       d   = total  depth
       bf  = flange width
       tf  = flange thickness
       tw  = web    thickness
       FlgOpt = true/false, FlgOpt = true : single outline for flange
       WebOpt = true/false, WebOpt = true : single outline for web
       FlgOpt = false + WebOpt = false : create separate outline for web-flange intersection 
     
  the function returns the following information
       A  = area of the cross section
       SY = centroidal distance relative to section mid-depth
       SZ = centroidal distance relative to section mid-width

  Dimensions and coordinate system:

                               y ^
                                 | 
                      .----------+----------.
                      |       tf |          |
                      |   .------|------.   |
                      |   |      |      |   | 
                z <-------+----- +      |   |  d 
                      |tw |             |   |
                      |   '-------------'   |
                      |       tf            | 
                      '---------------------'
                                 bf
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

-   [Create_RectPatch](Create_RectPatch.html "function yz = Create_RectPatch (ty,tz,sy,sz)"){.code}
    CREATE_RECTPATCH generate corner coordinates of rectangular patch
    for given reference point

This function is called by:

-   [Create_MultRectShape](Create_MultRectShape.html "function Shape = Create_MultRectShape (SType,Data)"){.code}
    CREATE_MULTRECTSHAPE generate geometry outline and assign material
    properties for shape of rectangular patches
-   [Create_ShapewMat](Create_ShapewMat.html "function Shape = Create_ShapewMat (SType,Data)"){.code}
    CREATE_SHAPEwMAT generate geometry outline and assign material
    properties for shape STYPE

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
