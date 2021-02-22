[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> Add_Bars2Section.m

</div>

# Add_Bars2Section

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**ADD_BARS2SECTION add bar group geometry and material data to section
data**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function SecData = Add_Bars2Section
(SecData,BarAyz,MatName,MatData,CrdOr)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
ADD_BARS2SECTION add bar group geometry and material data to section data
  the function adds information about the group of reinforcing bars with area and
  y- and z-coordinates in array BARAYZ to the section description in data structure SECDATA;
  MATNAME specifies the material type of the bar group with properties in data structure MATDATA;
  the optional argument CRDOR permits placement of the shape centroid
  at a specific location relative to the reference point of the section;
  CRDOR has the fields yc and zc for the centroid coordinates of the bar group in the
  y- and z-direction of the section coordinate system
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
