[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> Create_CircBarGrid.m

</div>

# Create_CircBarGrid

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**CREATE_CIRCBARGRID area and coordinates for circular grid of bars**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function FibAyz = Create_CircBarGrid (BarData)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
CREATE_CIRCBARGRID area and coordinates for circular grid of bars 
  FIBAYZ = CREATE_CIRCBARGRID (BARDATA)
  the function generates an array FIBAYZ with the coordinates and area of bars in a circular grid;
  the data structure BARDATA supplies details of the bar arrangement in fields
  AB  = area of one bar, R = [ Ro Ri ] radii of outermost and innermost layer (default Ri = Ro), 
  NBR = no of bars in radial direction (default = 1),
  NBP = no of bars in circumferential direction (default = 1);
  PHI = [PHIs PHIe] angles for the first and the last bar of each layer in radians measured 
  from the y-axis (default = [0 2*pi])

  each row of the FIBAYZ array corresponds to one bar with the y-coordinate of the bar in the first,
  the z-coordinate in the second, and the area of the bar in the third column.

  Coordinate system:
                                   ^ y
                                   |
                                 . + .
                               /   |   \
                              /    |R   \
                        z <--|-----+     |
                              \ R       /
                               \       /
                                 . _ .
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
