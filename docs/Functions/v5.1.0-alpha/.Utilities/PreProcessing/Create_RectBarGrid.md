[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> Create_RectBarGrid.m

</div>

# Create_RectBarGrid

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**CREATE_RECTBARGRID area and coordinates for rectangular grid of bars**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function FibAyz = Create_RectBarGrid (BarGeomData)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
CREATE_RECTBARGRID area and coordinates for rectangular grid of bars 
  FIBAYZ = CREATE_RECTBARGRID (BARGEOMDATA)
  the function generates an array FIBAYZ with the coordinates and area of bars in a rectangular grid;
  the data structure BARGEOMDATA supplies details of the grid geometry in fields
  AB = area of one bar, BGY,BGZ = grid dimensions and NY,NZ = no of bars in Y-Z, respectively;
  the bars are evenly spaced on the grid which is assumed to be symmetrically placed
  relative to the origin of the Y-Z coordinate system;
  if NY or NZ is equal to 1, the function generates a layer of bars normal to the Y or Z-direction 
  at a distance GDY/2 or GDZ/2 from the origin of the coordinate system, respectively;
  each row of the FIBAYZ array corresponds to one bar with the y-coordinate of the bar in the first,
  the z-coordinate in the second, and the area of the bar in the third column.

  Coordinate system:
                                   ^ y
                                   |
                               ----+----
                               |   |   |
                               |   |   |
                         z <---+---+   |  BGy
                               |       |
                               |       |
                               ---------
                                  BGz
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
