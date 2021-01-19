[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> Create_MPMesh4Circ.m

</div>

# Create_MPMesh4Circ

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**CREATE_MPMESH4CIRC generate the mesh for a circular disc or annulus**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function \[R1,R2,thfib,dth\] = Create_MPMesh4Circ
(Ri,Ro,nrfib,nthfib,MeshOpt)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
CREATE_MPMESH4CIRC generate the mesh for a circular disc or annulus
  [R1,R2,THFIB,DTH] = CREATE_MPMESH4CIRC (RI,RO,NRFIB,NTHFIB,MESHOPT)
  the function generates the mesh for a circular disc or annulus with inner radius RI and
  outer radius RO; there are NRFIB radial and NTHFIB circumferential subdivisions;
  the function returns the radial subdivision in vectors R1 and R2 and the circumferential
  subdivisions for each ring in the cellarray THFIB;
  DTH is a vector with the circumfererential angle increment for each ring;
  the discretization is controlled by the optional data structure MESHOPT with the following fields:
  MESHOPT.BASIC = true (for NRFIB x NTHFIB mesh) or false (for NRFIB x variable NTHFIB mesh)
         .CP    = true (with IP at center)       or false (without IP at center)
         .UW    = true (for uniform IP weight)   or false (for variable IP weight)
         .ThInc = increment in number of circumferential fibers/quadrant
         .Phi   = angle of first integration point in circumferential direction relative to y-axis
                  if Phi='var' each ring is offset by half the angle between successive IPs
         .Nthst = initial number of circumferential fibers/quadrant (default = 4*Ri/Ro)
  Default values for MESHOPT fields:
         BASIC = true, CP = false, UW = false, ThInc = 1, Phi = 0
  the function returns
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

-   [MP2dInt4Circ](MP2dInt4Circ.html "function [yfib,zfib,wfib] = MP2dInt4Circ (R,nrfib,nthfib,MeshOpt)"){.code}
    MP2dINT4CIRC integration points and weights for 2d-midpoint rule of
    circular disc or annulus

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
