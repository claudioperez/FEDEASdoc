[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> Create_MultRectShape.m

</div>

# Create_MultRectShape

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**CREATE_MULTRECTSHAPE generate geometry outline and assign material
properties for shape of rectangular patches**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Shape = Create_MultRectShape (SType,Data)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
CREATE_MULTRECTSHAPE generate geometry outline and assign material properties for shape of rectangular patches 
  SHAPE = CREATE_MULTRECTSHAPE (STYPE,DATA)
  the function creates the data structure SHAPE with geometry outline information
  for the shape of rectangular patches in character variable STYPE
  using the geometry data in data structure DATA with the following fields:

        [SType\Data]  |   d    b    tw   tf   bo   Loc  |
        --------------+---------------------------------+----------------------
         'Rect'        |  x    x    -    -    -    -    |  rectangle
         'Box'        |   x    x    x    x    -    -    |  box
         'BoxwOvh'    |   x    x    x    x    x    x    |  box with overhangs
         'C-Shp'      |   x    x    x    x    -    x    |  C-Shape
         'I-Shp'      |   x    x    x    x    -    -    |  I-Shape
         'T-Shp'      |   x    x    x    x    -    x    |  T-Shape
         'L-Shp'      |   x    x    x    x    -    x    |  L-Shape
         'S-Shp'      |   x    x    x    x    -    -    |  S-Shape

     d   = total depth
     bf  = flange   width (except for BoxwOvh)
     tf  = flange   thickness (default=0)
     tw  = web      thickness (default=0)
     bo  = overhang width     (default=0)
     Loc = top or bottom flange / left or right web (1 or 2) location,
         = upper left(1), lower left(2), lower right(3), upper right(4) for flange of L-shape

     Optional data:
     bf  = flange width (set automatically, unless specified equal to b
           to request single patch for flange
     dw  = web depth    (set automatically, unless specified equal to d
           to request single patch for web
     without bf and dw specification separate patches are used for flange-web intersections

  Coordinate system:
                          y ^                             y ^
                            |                               | 
                       .----+----.               .----------+----------.
                       |    |    |               |       tf |          |
                       '--. | .--'               |   .------|------.   |
                          | | |                  |   |      |      |   | 
                  z <-----+ + |     d      z <-------+----- +      |   |  d 
                          |tw |                  |tw |             |   |
                       .--'   '--.               |   '-------------'   |
                   tf  |         |               |         tf          | 
                       '---------'               '---------------------'
                           bf                              bf 

  The function assigns the properties in the field MATDATA of the material type MATNAME
  to parts of the shape, as follows:
  MATNAME{1}, MATDATA{1} are assigned to the core  or flanges depending on shape
  MATNAME{2}, MATDATA{2} are assigned to the cover or webs    depending on shape (default=same as 1)
  MATNAME{3}, MATDATA{3} are assigned to the intersections of flange and web     (default=same as 1)
  The function returns the outline in cell array OUTLINE of data structure SHAPE;
  OUTLINE has at most 3 cells, each consisting of a 4 x N array where N is the number of
  rectangular patches that describe the outline of the corresponding part of the shape;
  OUTLINE{1} = rectangular patches for one or more flanges depending on shape
  OUTLINE{2} = rectangular patches for one or more webs    depending on shape;
  OUTLINE{3} = rectangular patches for flange and web intersections (if requested);
  each rectangular patch is described with a 4x1 vector of corner coordinates [y1;z1,y2;z2]
  where 1 refers to the upper left and 2 to the lower right corner of the rectangular patch;
  these coordinates are measured relative to the geometric centroid of the shape;
  the date structure shape also contains the area of the shape in field A,
  and the distances of its geometric centroid from the mid-depth D and mid-width B in
  fields CY and CZ, respectively.
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

-   [Create_BoxOutline](Create_BoxOutline.html "function [Outline,A,sy,sz] = Create_BoxOutline (Data)"){.code}
    CREATE_BOXOUTLINE generate geometry outline for box section
-   [Create_BoxwOvhOutline](Create_BoxwOvhOutline.html "function [Outline,A,sy,sz] = Create_BoxwOvhOutline (Data)"){.code}
    CREATE_BOXwOVHOUTLINE generate geometry outline for box section
-   [Create_CSecOutline](Create_CSecOutline.html "function [Outline,A,sy,sz] = Create_CSecOutline (Data)"){.code}
    CREATE_CSECOUTLINE generate geometry outline for C-section
-   [Create_ISecOutline](Create_ISecOutline.html "function [Outline,A,sy,sz] = Create_ISecOutline (Data)"){.code}
    CREATE_ISECOUTLINE generate geometry outline for I-section
-   [Create_LSecOutline](Create_LSecOutline.html "function [Outline,A,sy,sz] = Create_LSecOutline (Data)"){.code}
    CREATE_LSECOUTLINE generate geometry outline for L-section
-   [Create_RectOutline](Create_RectOutline.html "function [Outline,A,sy,sz] = Create_RectOutline (Data)"){.code}
    CREATE_RECTOUTLINE generate geometry outline for rectangular section
-   [Create_RectwCovOutline](Create_RectwCovOutline.html "function [Outline,A,sy,sz] = Create_RectwCovOutline (Data)"){.code}
    CREATE_RECTwCOVOUTLINE generate geometry outline for rectangular
    section with cover
-   [Create_SSecOutline](Create_SSecOutline.html "function [Outline,A,sy,sz] = Create_SSecOutline (Data)"){.code}
    CREATE_SSECOUTLINE generate geometry outline for C-section
-   [Create_TSecOutline](Create_TSecOutline.html "function [Outline,A,sy,sz] = Create_TSecOutline (Data)"){.code}
    CREATE_TSECOUTLINE generate geometry outline for T-section

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
