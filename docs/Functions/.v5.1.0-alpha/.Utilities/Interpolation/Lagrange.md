[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Interpolation](FEDEASLab.html) \> Lagrange.m

</div>

# Lagrange

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**LAGRANGE Lagrange interpolation polynomials in interval -1\<xi\<1**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function lp = Lagrange (degree,deriv,xi)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
LAGRANGE Lagrange interpolation polynomials in interval -1<xi<1
  LP = LAGRANGE(DEGREE,DERIV,XI)
  the function determines the values of Lagrange interpolation polynomials of degree DEGREE
  and derivative order DERIV at integration points in vector XI;
  the values are returned in array LP with rows representing the different Lagrange
  polynomials of degree DEGREE and columns representing the values at points XI
  NOTE: XI need to be supplied in the interval -1<xi<1
  EXAMPLE: Lagrange(2,1,xi) returns the first derivative of quadratic Lagrange polynomials at xi

  To go from the interval [-1;+1] to the interval [0;L]:
     Jac = 0.5*L;    xP = Jac.*(1.+xi);
     lp  = lp./(Jac^deriv);
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

-   [LagrangeN](LagrangeN.html "function lp = LagrangeN (nn,deriv,xi)"){.code}
    LAGRANGEN Lagrange interpolation polynomials in interval -1

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
