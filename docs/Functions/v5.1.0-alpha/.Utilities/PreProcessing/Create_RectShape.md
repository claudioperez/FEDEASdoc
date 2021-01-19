[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> Create_RectShape.m

</div>

# Create_RectShape

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**CREATE_RECTSHAPE generate geometry outline and assign material
properties for rectangle**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Shape = Create_RectShape (ndm,SType,Data)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
CREATE_RECTSHAPE generate geometry outline and assign material properties for rectangle 
  SHAPE = CREATE_RECTSHAPE (NDM,STYPE,DATA)
  the function creates the data structure SHAPE with geometry outline information
  for the shape of the rectangular patches making up the rectangular section of the type
  in character variable STYPE; NDM=2 combines the side cover patches into a single patch;
  the function uses the geometry data in data structure DATA with the following fields:

        [SType\Data]  |   d    b   cv   tw   tf   bo   Loc  |
        --------------+-------------------------------------+----------------------
         'Rect'       |   x    x   -    -    -    -    -    |  rectangle
         'RectwCov'   |   x    x   x    -    -    -    -    |  rectangle with cover

         d   = depth
         b   = width
         cv  = cover    thickness

  Coordinate system:
                        y ^                        
                          |                          
                      .---+---.                
                      |   |   |                
                      |   |   |                 
                z <---+---+   |  d             
                      |       |            
                      |       |                
                      '-------'                 
                          b                  
                                               
  The function assigns the properties in the field MATDATA of the material type MATNAME
  to parts of the shape, as follows:
  MATNAME{1}, MATDATA{1} are assigned to the core
  MATNAME{2}, MATDATA{2} are assigned to the cover, if present (default=same as 1)
  The function returns the outline in cell array OUTLINE of data structure SHAPE;
  OUTLINE has at most 2 cells:
  OUTLINE{1} contains a 4x1 array for the rectangular patch of the core;
  OUTLINE{2} contains a 4 x N array, where N=4 as the number of rectangular patches
  describing the cover outline;
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

-   [Create_RectPatch](Create_RectPatch.html "function yz = Create_RectPatch (ty,tz,sy,sz)"){.code}
    CREATE_RECTPATCH generate corner coordinates of rectangular patch
    for given reference point

This function is called by:

-   [Create_IPMesh4Rect](Create_IPMesh4Rect.html "function [yfib,zfib,wfib,MatID] = Create_IPMesh4Rect (SecData)"){.code}
    CREATE_IPMESH4RECT coordinates, weights and material IDs for
    rectangular section with cover

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
