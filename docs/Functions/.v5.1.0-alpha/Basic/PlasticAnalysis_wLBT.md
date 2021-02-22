[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Basic](FEDEASLab.html) \>
PlasticAnalysis_wLBT.m

</div>

# PlasticAnalysis_wLBT

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**PLASTICANALYSIS_wLBT collapse load factor and basic element forces by
lower bound theorem of plastic analysis**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[lamdac,Qc\] = PlasticAnalysis_wLBT
(Bf,Qpl,Pref,Pcf,Options)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
PLASTICANALYSIS_wLBT collapse load factor and basic element forces by lower bound theorem of plastic analysis
  [LAMDAC,QC] = PLASTICANALYSIS_wLBT (BF,QPL,PREF,PCF,OPTIONS)
  the function uses the lower bound theorem of plastic analysis
  to determine the collapse load factor LAMDAC and the basic forces QC at collapse
  of a structural model under reference load vector PREF and force vector PCF at free dofs;
  the reference force vector PREF represents the load pattern to be factored, while
  the force vector PCF represents the load pattern that remains unfactored;
  for the sign of PCF note that the equilibrium equations are: lambda Pref + Pcf = Bf Q;
  there are two options for supplying the static matrix Bf:
  (a) as data structure Model with information about the structural model, that is used
      to set up the static matrix Bf of the structure automatically, or
  (b) as nf by nq matrix where nf = no of free dofs and nq = total number of basic forces;
  there are two options for supplying the plastic capacities QPL:
  (a) as cell array ELEMDATA with plastic capacities in fields Np for axial and Mp for flexural
  (b) as one column vector for the case that positive and negative capacities are the same,
       or, as two column array with positive plastic capacities in the first column
       and negative plastic capacities in the second (in absolute value) (signs matching Q!)
  NOTE: mixing of options (a) and (b) is not supported!
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [B_matrix](B_matrix.html "function B = B_matrix (Model)"){.code}
    B_MATRIX static matrix of structural model with 2d/3d truss and 2d
    frame elements

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
