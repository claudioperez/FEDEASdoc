[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Interpolation](FEDEASLab.html) \> HermiteN.m

</div>

# HermiteN

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**HERMITEN Hermite interpolation polynomials in interval -1\<xi\<1**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function hp = HermiteN(nn,deriv,xi)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
HERMITEN Hermite interpolation polynomials in interval -1<xi<1
  HP = HERMITEN (NN,DERIV,XI)
  the function determines the values of Hermite interpolation polynomials of degree
  DEGREE = 2*NN - 1, where NN is number of equally spaced nodes used to
  compute the polynomilas. At each node, both the value of the required
  polynomial and its derivative are considered for its evaluation.
  The functions provides the derivative of order DERIV at integration points in the vector XI;
  The values are returned in array LP with 2*NN rows representing the
  different Hermite polynomials (2 per each node) and columns representing the
  values at points XI;
  The polynomial associated to the end nodes of the interval are located in
  the first 4 rows of lp and the other locations are reserved for the polynomial
  associated to internal nodes;

  NOTE: XI need to be supplied in the interval -1<xi<1
  EXAMPLE: HermiteN(3,2,xi) returns the second derivative of quintic Hermite polynomials at xi

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
