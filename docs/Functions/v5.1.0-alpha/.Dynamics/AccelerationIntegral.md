[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Dynamics](FEDEASLab.html) \>
AccelerationIntegral.m

</div>

# AccelerationIntegral

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**ACCELERATIONINTEGRAL determines displacement and velocity history for
given acceleration history**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[u,udot\] = AccelerationIntegral
(uddot,Deltat,nstep,u0,udot0)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
ACCELERATIONINTEGRAL determines displacement and velocity history for given acceleration history 
  [U,UDOT] = ACCELERATIONINTEGRAL (UDDOT,DELTAT,NSTEP,U0,UDOT0)
  function integrates the acceleration history(ies) in array UDDOT to obtain
  the displacement history(ies) in array U and velocity history(ies) in array UDOT;
  the time step of the acceleration record is DELTAT
  and the total number of steps is NSTEP (default=no of acceleration values) 
  the initial displacement is supplied in row vector U0 and the initial velocity in row vector UDOT0 (default=0);
  histories are arranged columnwise in arrays UDDOT, U and UDOT (column no=history no);
  the displacement and velocity histories are corrected for zero end values
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
