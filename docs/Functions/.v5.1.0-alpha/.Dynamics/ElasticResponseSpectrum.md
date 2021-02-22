[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Dynamics](FEDEASLab.html) \>
ElasticResponseSpectrum.m

</div>

# ElasticResponseSpectrum

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**ELASTICRESPONSESPECTRUM determines the elastic response spectrum for
given acceleration history**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[D,Psv,Psa\] = ElasticResponseSpectrum
(Acceleration,T,zeta)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
ELASTICRESPONSESPECTRUM determines the elastic response spectrum for given acceleration history
  [D,PSV,PSA] = ELASTICRESPONSESPECTRUM (ACCELERATION,T,ZETA)
  the function determines the elastic response spectrum for a given acceleration history in
  data structure ACCELERATION with fields Deltat (time step size) and Value (acceleration value);
  the periods for the spectrum are specified in row vector T ( default= [0.001 0.1:0.1:5] );
  the row vector ZETA contains the damping ratio(s) ( default=0 );
  the response spectrum values for the periods in row vector T are returned
  in arrays D for displacement, PSV for pseudo-velocity, and PSA for pseudo-acceleration
  with the row number corresponding to the period and the column number to the damping ratio
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [LSDOF_LinearWilson](LSDOF_LinearWilson.html "function [u,udot,uddot] = LSDOF_LinearWilson (Deltat,omega,p,zeta,u0,udot0)"){.code}
    LSDOF_LINEARWILSON transient response of linear SDOF system by exact
    integration of piecewise linear excitation

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
