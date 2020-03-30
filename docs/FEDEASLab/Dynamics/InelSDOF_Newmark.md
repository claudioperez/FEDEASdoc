[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Dynamics](FEDEASLab.html) \>
InelSDOF\_Newmark.m

</div>

InelSDOF\_Newmark
=================

PURPOSE [![\^](../up.png)](#_top)
-------------------------------------------

::: {.box}
**INELSDOF\_NEWMARK inelastic response of SDOF system to acceleration
history with Newmark\'s method**
:::

SYNOPSIS [![\^](../up.png)](#_top)
------------------------------------------------

::: {.box}
**function \[u,udot,uddot,pr\] = InelSDOF\_Newmark
(Deltat,omega,p,InelSDFData,zeta,u0,udot0)**
:::

DESCRIPTION [![\^](../up.png)](#_top)
------------------------------------------------------

::: {.fragment}
``` {.comment}
INELSDOF_NEWMARK inelastic response of SDOF system to acceleration history with Newmark's method
  [U,UDOT,UDDOT,PR] = INELSDOF_NEWMARK (DELT,OMEGA,P,INELSDFDATA,ZETA,U0,UDOT0)
  the function determines the transient response history of an inelastic SDOF system
  to the acceleration history (force/mass) in vector P
  with Newmark's constant average acceleration method (1959)
  with time step of integration DELTAT;
  row vector OMEGA contains the eigenfrequency(ies) of the SDOF system,
  and row vector ZETA the optional damping ratio(s) (default = 0);
  the optional initial conditions are specified in row vectors U0 for the displacement
  and UDOT0 for the velocity (default values for both = 0);
  INELSDFDATA carries the force-deformation properties for the inelastic SDOF system:
  MatName = function name for 1d relation (default = InelLPwLH1dMat)
  uy      = yield displacement         (default = 1)
  eta     = post-yield stiffness ratio (default = 0)
  the function returns the displacement history(ies) in array U,
  the velocity history(ies) in array UDOT,
  the acceleration history(ies) in array UDDOT,
  and the resisting force history(ies) in array PR (also in the form force/mass!);
  these arrays are arranged columnwise (column no=frequency no)
```
:::

CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)
----------------------------------------------------------------

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
