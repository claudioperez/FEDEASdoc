[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Solution_Library](FEDEASLab.html) \>
Condense_MV.m

</div>

# Condense_MV

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**CONDENSE_MV condense matrix Kf and vector Pf to a reduced set idr of
degrees of freedom**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[Kfc,Pfc\] = Condense_MV (Kf,idr,Pf)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
CONDENSE_MV condense matrix Kf and vector Pf to a reduced set idr of degrees of freedom
  [KFC,PFC] = CONDENSE_MV (KF,IDR,PF)
  function condenses free dof stiffness matrix KF and applied force vector PF
  to a reduced set of dofs as specified in list or row vector IDR;
  the condensed stiffness matrix is KFC and the initial force vector is PFC
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
