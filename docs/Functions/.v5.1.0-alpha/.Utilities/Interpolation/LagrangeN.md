[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Interpolation](FEDEASLab.html) \> LagrangeN.m

</div>

# LagrangeN

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**LAGRANGEN Lagrange interpolation polynomials in interval -1\<xi\<1**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function lp = LagrangeN (nn,deriv,xi)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
LAGRANGEN Lagrange interpolation polynomials in interval -1<xi<1
  LP = LAGRANGEN(NN,DERIV,XI)
  the function determines the values of Lagrange interpolation polynomials of degree
  DEGREE = NN - 1, where NN is number of equally spaced nodes used to
  compute the polynomilas. The functions provides the derivative of order DERIV
  at integration points in the vector XI;
  the values are returned in array LP with NN rows representing the different Lagrange
  polynomials and columns representing the values at points XI;
  The polynomial associated to the end nodes of the interval are located in
  the first 2 rows of lp and the other locations are reserved for the polynomial
  associated to internal nodes;

  NOTE: XI need to be supplied in the interval -1<xi<1
  EXAMPLE: LagrangeN(3,1,xi) returns the first derivative of quadratic Lagrange polynomials at xi

  To go from the interval [-1;+1] to the interval [0;L]:
     Jac = 0.5*L;    xP = Jac.*(1.+xi);
     lp  = lp./(Jac^deriv);
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

-   [Lagrange](Lagrange.html "function lp = Lagrange (degree,deriv,xi)"){.code}
    LAGRANGE Lagrange interpolation polynomials in interval -1

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
