[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Quadrature](FEDEASLab.html) \> Gauss.m

</div>

# Gauss

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**GAUSS locations and weights of Gauss-Legendre integration scheme**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function \[xIP,wIP\] = Gauss (nIP)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
GAUSS locations and weights of Gauss-Legendre integration scheme    
 [XIP,WIP] = GAUSS (NIP)
  the function determines the locations in the interval -1<x<1 and the weights
  of the Gauss-Legendre integration scheme for NIP integration points;
  the locations are reported in vector XIP and the weights in vector WIP;
  the first vector term corresponds to x=-1;
  the function supports NIP values of  1,2,3,4,5,..20, 32 and 64
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
