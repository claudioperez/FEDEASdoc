[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Dynamics](FEDEASLab.html) \>
LSDOF_Newmark.m

</div>

# LSDOF_Newmark

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**LSDOF_NEWMARK determines the response of linear SDOF system to
acceleration history with Newmark\'s method**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[u,udot,uddot\] = LSDOF_Newmark
(Deltat,omega,p,zeta,u0,udot0)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
LSDOF_NEWMARK determines the response of linear SDOF system to acceleration history with Newmark's method
  [U,UDOT,UDDOT] = LSDOF_NEWMARK (DELTAT,OMEGA,P,ZETA,U0,UDOT0)
  function determines the transient response history of linear SDOF system(s) with eigenfrequency(ies)
  in row vector OMEGA, to acceleration history (force/mass) in vector P,
  for damping ratio(s) in row vector ZETA (default=0),
  and initial conditions in row vectors U0 (displacement) and UDOT0 (velocity) (default values=0);
  the time step of integration is DELTAT;
  N.M. Newmark's method from 1959 is used for the numerical integration of the equations of motion;
  the function returns the displacement history(ies) in array U, the velocity history(ies)
  in array UDOT and the acceleration history(ies) in array UDDOT arranged columnwise (column no=frequency no);
  Reference: A.K.Chopra, Dynamics of Structures, 2nd edition, pp. 174-180
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
