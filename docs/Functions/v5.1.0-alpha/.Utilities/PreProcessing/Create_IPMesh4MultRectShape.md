[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> Create_IPMesh4MultRectShape.m

</div>

# Create_IPMesh4MultRectShape

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**CREATE_IPMESH4MULTRECTSHAPE fiber discretization for section of
several rectangular patches**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Shape = Create_IPMesh4MultRectShape (Shape,MeshData)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
CREATE_IPMESH4MULTRECTSHAPE fiber discretization for section of several rectangular patches
  the function generates the integration point locations and weights
  for a section of several rectangular patches described in the data structure SHAPE;
  the data structure MESHDATA supplies details for the fiber discretization in the fields:
  MESHDATA.ny  = number of IPs in the y-direction (for rectangular sections)
          .nz  = number of IPs in the z-direction (for rectangular sections)
          .ncl = number of IPs in the longitudinal cover direction (for rectangular sections)
          .nct = number of IPs in the transverse   cover direction (for rectangular sections)
          .nfl = number of IPs along  the flange width
          .nft = number of IPs across the flange thickness
          .nwl = number of IPs along  the web depth
          .nwt = number of IPs across the web thickness
          .niy = number of IPs in the y-direction for flange-web intersection
          .niz = number of IPs in the z-direction for flange-web intersection
          .IntTyp = quadrature rule
          .ndm = 2 (discretization in y), 3 (discretization in y and z)
  the data structure SHAPE supplies the section shape and the outline in the fields
  SHAPE.SType    = character variable for section shape with the following options:
                   'Rect', 'RectwCov', 'I-Shp', 'T-Shp', 'L-Shp', 'C-Shp', 'S-Shp',
                   'Box' , 'BoxwOvh' , 'Circ-Shp'
  SHAPE.Outline  =  cell array with the coordinates of each rectangular patch group:
                   {1} for flange(s), {2} for web(s), {3} for flange-web intersection
  on return SHAPE is enriched with the following fields
  SHAPE.FibAyz   = (nfib x 3) numerical array with y- and z-coordinates and weights of IPs
  SHAPE.FMatID   =  nfib x 1 with the material number for each IP
  SHAPE.MeshData = IP mesh information for SType with relevant scalar fields 
                   ny nz, ncl, nct, nfl, nft, nwl, nwt, niy, niz
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

-   [Rectangle2Fiber](Rectangle2Fiber.html "function [yfib,zfib,wfib] = Rectangle2Fiber (patcoor,IntTyp,nyfib,nzfib)"){.code}
    RECTANGLE2FIBER integration points and weights for 2d-integration of
    a rectangle

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
