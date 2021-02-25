[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Interpolation](FEDEASLab.html) \> Hermite.m

</div>

# Hermite

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**HERMITE Hermite interpolation polynomials in interval -1\<xi\<1**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function hp = Hermite (degree,deriv,xi)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
HERMITE Hermite interpolation polynomials in interval -1<xi<1
  HP = HERMITE (DEGREE,DERIV,XI)
  the function determines the values of Hermite interpolation polynomials of degree DEGREE
  and derivative order DERIV at integration points in vector XI;
  the values are returned in array HP with rows representing the different Hermite
  polynomials of degree DEGREE and columns representing the values at points XI
  NOTE: XI need to be supplied in the interval -1<xi<1
  EXAMPLE: Hermite(3,2,xi) returns the second derivative of cubic Hermite polynomials at xi

  If degree is even, one node of the equispaced grid used to evaluate the
  polynomials considers only the value of ordinate, without the
  derivative. This node is always the last node of the grid, considering
  that the end nodes are located in the first two positions.

  To go from the interval [-1;+1] to the interval [0;L]:
     Jac = 0.5*L;    xP = Jac.*(1.+xi);
     hp(1:2:size(hp,1),:) = hp(1:2:size(hp,1),:)./(Jac^deriv);
     hp(2:2:size(hp,1),:) = hp(2:2:size(hp,1),:)./(Jac^(deriv-1));
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
