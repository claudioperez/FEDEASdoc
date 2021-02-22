[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> Add_Shape2Section.m

</div>

# Add_Shape2Section

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**ADD_SHAPE2SECTION add section shape geometry and material data to
section data**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function SecData = Add_Shape2Section (SecData,Shape,CrdOr)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
ADD_SHAPE2SECTION add section shape geometry and material data to section data
  the function adds information about the section shape in data structure SHAPE
  to the section description in data structure SECDATA;
  the optional argument CRDOR permits placement of the shape centroid
  at a specific location relative to the reference point of the section;
  CRDOR has the fields yc and zc for the centroid coordinates of the bar group in the
  y- and z-direction of the section coordinate system
  SHAPE has the following fields:
       .STYpe    = type of section shape
       .ShLoc    = shear center location
       .Outline  = y-z coordinates for shape outline description
       .MeshData = IP mesh information for SType with relevant scalar fields 
                   ny nz, ncl, nct, nfl, nft, nwl, nwt, niy, niz
       .FibAyz   = y-z coordinates and weights for fiber mesh discretization
       .FMatName = material type of shape
       .FMatData = material properties
       .FMatID   = material ID
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
