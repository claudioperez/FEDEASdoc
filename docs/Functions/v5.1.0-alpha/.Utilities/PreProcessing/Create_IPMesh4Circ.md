[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> Create_IPMesh4Circ.m

</div>

# Create_IPMesh4Circ

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**CREATE_IPMESH4CIRC integration point coordinates, weights and material
IDs for circular disc or annulus**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function \[yfib,zfib,wfib,MatID\] = Create_IPMesh4Circ (SecData)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
CREATE_IPMESH4CIRC integration point coordinates, weights and material IDs for circular disc or annulus
  [YFIB,ZFIB,WFIB,MATID] = CREATE_IPMESH4CIRC (SECDATA)
  function generates the coordinates YFIB and ZFIB, the weights WFIB, and the material ID MATID
  for the fiber discretization of the circular disc or annulus in SECDATA;
  the circular disc or annulus can have a different outer and inner cover,
  as may be required for sections with reinforcing bars;
  NDM=2 generates a discretization in the y-axis only and NDM=3 in both y- and z-axis
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

-   [MP1dInt4Circ](MP1dInt4Circ.html "function [yfib,wfib] = MP1dInt4Circ (R,nrfib)"){.code}
    MP1dINT4CIRC integration points and weights for 1d-midpoint rule of
    circular disc or annulus
-   [MP2dInt4Circ](MP2dInt4Circ.html "function [yfib,zfib,wfib] = MP2dInt4Circ (R,nrfib,nthfib,MeshOpt)"){.code}
    MP2dINT4CIRC integration points and weights for 2d-midpoint rule of
    circular disc or annulus

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
