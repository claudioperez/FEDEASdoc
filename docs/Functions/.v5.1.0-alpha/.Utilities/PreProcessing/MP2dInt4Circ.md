[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> MP2dInt4Circ.m

</div>

# MP2dInt4Circ

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**MP2dINT4CIRC integration points and weights for 2d-midpoint rule of
circular disc or annulus**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function \[yfib,zfib,wfib\] = MP2dInt4Circ (R,nrfib,nthfib,MeshOpt)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
MP2dINT4CIRC integration points and weights for 2d-midpoint rule of circular disc or annulus
  [YFIB,ZFIB,WFIB] = MP2dINT4CIRC (R,NRFIB,NTHFIB,MESHOPT)
  the function determines the locations in vectors YFIB and ZFIB and the integration weights in vector WFIB
  for midpoint integration of a circular disc or annulus with number of integration points NRFIB
  in the radial direction and either a fixed number NTHFIB or a variable number
  of integration points (IPs) in the circumferential direction where
  YFIB, ZFIB and WFIB are (NFTOT x 1) column vectors, with NFTOT the total number of fibers;
  R = [Ro Ri] is the outer/inner radius of the annulus (for circular disc R = Ro);
  the discretization is controlled by the optional data structure MESHOPT with the following fields:
  MESHOPT.BASIC = true (for NRFIB x NTHFIB mesh) or false (for NRFIB x variable NTHFIB mesh)
         .CP    = true (with IP at center)       or false (without IP at center)
         .UW    = true (for uniform IP weight)   or false (for variable IP weight)
         .ThInc = increment in number of circumferential fibers/quadrant
         .IPCg  = true (IP at exact centroid)    or false (IP at average ring radius)
         .Phi   = angle of first integration point in circumferential direction relative to y-axis
                  if Phi='var' each ring is offset by half the angle between successive IPs
         .Nthst = initial number of circumferential fibers/quadrant (default = 4*Ri/Ro)
         .Rdrat = limit ratio of Ri/Ro; for Ri/Ro larger than the limit the function uses the
                  specified NTHFIB number in the circumferential direction, otherwise it uses
                  the mesh discretization specified in MESHOPT
  Default values for MESHOPT fields:
         BASIC = true, CP = false, UW = false, ThInc = 1, IPCg = true, Phi = 0, Rdrat = 0.75

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

-   [Create_MPMesh4Circ](Create_MPMesh4Circ.html "function [R1,R2,thfib,dth] = Create_MPMesh4Circ (Ri,Ro,nrfib,nthfib,MeshOpt)"){.code}
    CREATE_MPMESH4CIRC generate the mesh for a circular disc or annulus

This function is called by:

-   [Create_IPMesh4Circ](Create_IPMesh4Circ.html "function [yfib,zfib,wfib,MatID] = Create_IPMesh4Circ (SecData)"){.code}
    CREATE_IPMESH4CIRC integration point coordinates, weights and
    material IDs for circular disc or annulus

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
