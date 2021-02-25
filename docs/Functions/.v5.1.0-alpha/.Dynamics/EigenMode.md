[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Dynamics](FEDEASLab.html) \> EigenMode.m

</div>

# EigenMode

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**EIGENMODE determines eigenfrequencies and eigenmodes of structural
model**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[omega,Ueig\] = EigenMode (Kf,M,nmod)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
EIGENMODE determines eigenfrequencies and eigenmodes of structural model
  [OMEGA UEIG] = EIGENMODE(KF,M,NMOD)
  function determines the lowest NMOD (default=all) eigenfrequencies in row vector OMEGA
  and corresponding eigenmodes in array UEIG for a structure with free dof stiffness matrix KF
  and free dof lumped mass vector or consistent mass matrix M;
  the eigenmodes in array UEIG are arranged columnwise (column no=mode no)
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [ModalAnalysis](ModalAnalysis.html "function [omega,Ueig,Y_t,Ydot_t,Yddot_t] = ModalAnalysis (option,Kf,M,Loading,Deltat,zeta,nmod)"){.code}
    MODALANALYSIS determines modal response history for given transient
    loading

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
