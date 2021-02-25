[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \> GPYS.m

</div>

# GPYS

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**GPYS function value, gradient and Hessian of polynomial yield
surface**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[f,g,h\] = GPYS (GPYSC,xyz,ScVec)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
GPYS function value, gradient and Hessian of polynomial yield surface    
  [F,G,H] = GPYS (GPYSC,XYZ,SCVEC)
  the function determines the value F(X,Y,Z), the gradient G(X,Y,Z), and
  the Hessian matrix (2nd derivative) H(X,Y,Z) of F at a point XYZ
  for a general polynomial yield surface with coefficients GPYSC
  SCVEC is a scale vector for the variables X, Y, and Z
   G = the gradient (normal)   of the yield surface = [dF/dX; dF/dY; dF/dZ]
   H = the Hessian (2nd deriv) of the yield surface = dG/dXYZ
     = [d2(F)/d(X)^2    d2(F)/d(X)d(Y) d2(F)/d(X)d(Z);
        d2(F)/d(Y)d(X)  d2(F)/d(Y)^2   d2(F)/d(Y)d(Z);
        d2(F)/d(Z)d(X)  d2(F)/d(Z)d(Y) d2(F)/d(Z)^2]

  The coefficients of the polynomial yield surface are specified as follows
  general 3d case
           GPYSC = [d1 a1 b1 c1; d2 a2 b2 c2; d3 a3 b3 c3; ...]
          for  F = Sum_i (di*(X^ai)*(Y^bi)*(Z^ci))
  general 2d case
           GPYSC = [c1 a1 b1; c2 a2 b2; c3 a3 b3; ...]
       for     F = Sum_i (ci*(X^ai)*(Y^bi))
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [Inel2dFrm_wLHNMYS](Inel2dFrm_wLHNMYS.html "function ElemResp = Inel2dFrm_wLHNMYS (action,el_no,xyz,ElemData,ElemState)"){.code}
    INEL2dFRM_wLHNMYS 2d linear elastic frame element with linear
    plastic hardening axial-flexure hinges

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
