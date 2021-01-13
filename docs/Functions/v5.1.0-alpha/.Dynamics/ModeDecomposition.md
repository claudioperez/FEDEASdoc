[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Dynamics](FEDEASLab.html) \>
ModeDecomposition.m

</div>

# ModeDecomposition

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**MODEDECOMPOSITION determines eigenmode participation factors of given
vector V**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[Mmod,Ymod,Vmod\] = ModeDecomposition (M,Ueig,V)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
MODEDECOMPOSITION determines eigenmode participation factors of given vector V
  [MMOD,YMOD,VMOD] = MODEDECOMPOSITION (M,UEIG,V)
  the function determines the mode participation factors of vector V
  for a structural model with free dof consistent mass matrix or lumped mass vector M
  for the modes in array UEIG arranged columnwise (column no=mode no);
  the function returns the modal mass terms in row vector MMOD,
  the mode participation factors in row vector YMOD and the
  inertial force decomposition vectors in array VMOD arranged columwise
  the size of the consistent mass matrix or the length of lumped mass vector M,
  the length of vector V and the number of rows of arrays UEIG
  and VMOD is equal to the number of free dofs of the structural model;
  the length of row vectors MMOD and YMOD is equal
  to the number of non-zero mass terms in the lumped mass vector M or
  the number of free dofs of the structural model for the case of consistent mass matrix M
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
