[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Dynamics](FEDEASLab.html) \>
ModalAnalysis.m

</div>

ModalAnalysis
=============

PURPOSE [![\^](../up.png)](#_top)
-------------------------------------------

::: {.box}
**MODALANALYSIS determines modal response history for given transient
loading**
:::

SYNOPSIS [![\^](../up.png)](#_top)
------------------------------------------------

::: {.box}
**function \[omega,Ueig,Y\_t,Ydot\_t,Yddot\_t\] = ModalAnalysis
(option,Kf,M,Loading,Deltat,zeta,nmod)**
:::

DESCRIPTION [![\^](../up.png)](#_top)
------------------------------------------------------

::: {.fragment}
``` {.comment}
MODALANALYSIS determines modal response history for given transient loading
  [OMEGA,UEIG,Y_T,YDOT_T,YDDOT_T] = MODALANALYSIS (OPTION,KF,M,LOADING,DELTAT,ZETA,NMOD)
  the function determines the response history of a multi-dof structural model
  with stiffness matrix at free dofs KF and consistent mass matrix or lumped mass vector M
  under given transient loading in data structure LOADING
  for the lowest NMOD (default=all) eigenmodes or NMOD Ritz vectors
  with damping ratios in row vector ZETA (default=0);
  the time step of integration is DELTAT;
        OPTION = 'eig'  uses nmod eigenvectors,
  while OPTION = 'Ritz' uses nmod Ritz vectors in the modal analysis; 
  the function returns NMOD eigenfrequencies of the structural model in row vector OMEGA,
  the eigenmode or Ritz vector shapes in array UEIG arranged columnwise (column no=mode no),
  and the response history of each eigenmode or Ritz vector
  in array Y_T arranged columnwise (column no=mode no),
  the velocity history of each eigenmode or Ritz vector in array YDOT_t, and
  the acceleration history of each eigenmode or Ritz vector in array YDDOT_t
  the data structure LOADING has the following fields
  LOADING.Uddref = vector of reference acceleration values at model dofs
          Pref   = vector of reference load         values at model dofs
          U0     = vector of initial displacement   values at model dofs
          Udot0  = vector of initial velocity       values at model dofs
          FrcHst = force time history in field Value
          AccHst = acceleration time history in field Value
```
:::

CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)
----------------------------------------------------------------

This function calls:

-   [EigenMode](EigenMode.html "function [omega,Ueig] = EigenMode (Kf,M,nmod)"){.code}
    EIGENMODE determines eigenfrequencies and eigenmodes of structural
    model
-   [LSDOF\_LinearWilson](LSDOF_LinearWilson.html "function [u,udot,uddot] = LSDOF_LinearWilson (Deltat,omega,p,zeta,u0,udot0)"){.code}
    LSDOF\_LINEARWILSON transient response of linear SDOF system by
    exact integration of piecewise linear excitation
-   [ModeDecomposition](ModeDecomposition.html "function [Mmod,Ymod,Vmod] = ModeDecomposition (M,Ueig,V)"){.code}
    MODEDECOMPOSITION determines eigenmode participation factors of
    given vector V

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
