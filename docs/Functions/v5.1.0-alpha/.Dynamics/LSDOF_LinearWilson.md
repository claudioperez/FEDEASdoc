[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Dynamics](FEDEASLab.html) \>
LSDOF_LinearWilson.m

</div>

# LSDOF_LinearWilson

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**LSDOF_LINEARWILSON transient response of linear SDOF system by exact
integration of piecewise linear excitation**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[u,udot,uddot\] = LSDOF_LinearWilson
(Deltat,omega,p,zeta,u0,udot0)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
LSDOF_LINEARWILSON transient response of linear SDOF system by exact integration of piecewise linear excitation
  [U,UDOT,UDDOT] = LSDOF_LINEARWILSON (DELTAT,OMEGA,P,ZETA,U0,UDOT0)
  function determines the transient response history of linear SDOF system(s) with eigenfrequency(ies)
  in row vector OMEGA, to acceleration history (force/mass) in vector P,
  for damping ratio(s) in row vector ZETA (default=0),
  and initial conditions in row vectors U0 (displacement) and UDOT0 (velocity) (default values=0);
  the time step of integration is DELTAT;
  the function integrates exactly the equations of motion for piecewise linear interpolation of excitation;
  the function returns the displacement history(ies) in array U, the velocity history(ies)
  in array UDOT and the acceleration history(ies) in array UDDOT arranged columnwise (column no=frequency no);
  Reference: A.K.Chopra, Dynamics of Structures, 2nd edition, pp. 167-171
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [ElasticResponseSpectrum](ElasticResponseSpectrum.html "function [D,Psv,Psa] = ElasticResponseSpectrum (Acceleration,T,zeta)"){.code}
    ELASTICRESPONSESPECTRUM determines the elastic response spectrum for
    given acceleration history
-   [ModalAnalysis](ModalAnalysis.html "function [omega,Ueig,Y_t,Ydot_t,Yddot_t] = ModalAnalysis (option,Kf,M,Loading,Deltat,zeta,nmod)"){.code}
    MODALANALYSIS determines modal response history for given transient
    loading

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
