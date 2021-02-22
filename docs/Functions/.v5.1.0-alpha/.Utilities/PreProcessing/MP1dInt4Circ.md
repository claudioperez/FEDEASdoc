[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> MP1dInt4Circ.m

</div>

# MP1dInt4Circ

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**MP1dINT4CIRC integration points and weights for 1d-midpoint rule of
circular disc or annulus**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function \[yfib,wfib\] = MP1dInt4Circ (R,nrfib)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
MP1dINT4CIRC integration points and weights for 1d-midpoint rule of circular disc or annulus
  [YFIB,WFIB] = MP1dINT4CIRC (R,NRFIB)
  the function determines the locations YFIB and the integration weights WFIB for the 1d
  integration of a circular disc or annulus by the midpoint rule with 2*NRFIB integration points
  in the radial direction, where YFIB and WFIB are (2xNRFIB) x 1 column vectors;
  R = [Ro Ri] is the outer/inner radius of the annulus (for circular disc R = Ro);

  Section coordinate system:
                                   ^ y
                                   |
                                 . + .
                               /   |   \
                              /    |    \
                         z <- |----+     | 
                              \         /
                               \       /
                                 . _ .
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

-   [Create_IPMesh4Circ](Create_IPMesh4Circ.html "function [yfib,zfib,wfib,MatID] = Create_IPMesh4Circ (SecData)"){.code}
    CREATE_IPMESH4CIRC integration point coordinates, weights and
    material IDs for circular disc or annulus

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
