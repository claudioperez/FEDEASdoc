[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Basic](FEDEASLab.html) \>
PlasticAnalysis_wUBT.m

</div>

# PlasticAnalysis_wUBT

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**PLASTICANALYSIS_wUBT collapse load factor and deformation increments
by upper bound theorem of plastic analysis**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[lamdac,DUf,DVhp\] = PlasticAnalysis_wUBT
(Af,Qpl,Pref,Pfc,Options)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
PLASTICANALYSIS_wUBT collapse load factor and deformation increments by upper bound theorem of plastic analysis
  [LAMDAC,DUF,DVHP] = PLASTICANALYSIS_wUBT (AF,QPL,PREF,PFC)
  the function uses the upper bound theorem of plastic analysis
  to determine the collapse load factor LAMDAC, and the displacement and plastic deformation
  increments of the collapse mechanism DUF and DVHP, respectively,
  of a structural model under reference load vector PREF and force vector PFC at free dofs;
  the reference force vector PREF represents the load pattern to be factored, while
  the force vector PFC represents the load pattern that remains unfactored;
  for the sign of PFU note that the equilibrium equations are: lambda Pref + Pfc = Bf Q;
  there are two options for supplying the kinematic matrix Af:
  (a) as data structure Model with information about the structural model, that is used
      to set up the kinematic matrix Af of the structure automatically, or
  (b) as nq by nf matrix where nq = total number of deformations and nf = no of free dofs;
  there are two options for supplying the plastic capacities QPL:
  (a) as cell array ELEMDATA with plastic capacities in fields Np for axial and Mp for flexural
  (a) as one column vector for the case that positive and negative capacities are the same,
       or, as two column array with positive plastic capacities in the first column
       and negative plastic capacities in the second (in absolute value) (signs matching Q!)
  NOTE: mixing of options (a) and (b) is not supported!
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [A_matrix](A_matrix.html "function A = A_matrix (Model)"){.code}
    A_MATRIX kinematic matrix of structural model with 2d/3d truss and
    2d frame elements

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
