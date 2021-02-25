[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Basic](FEDEASLab.html) \>
BbariBbarx_matrix.m

</div>

# BbariBbarx_matrix

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**BBARIBBARX_MATRIX force influence matrices of primary structure from
static matrix Bf**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[Bbari,Bbarx,ind_x\] = BbariBbarx_matrix (Bf,ind_r)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
BBARIBBARX_MATRIX force influence matrices of primary structure from static matrix Bf
  [BBARI,BBARX,IND_X] = BBARIBBARX_MATRIX (BF,IND_R)
  the function determines the force influence matrices BBARI and BBARX
  of the primary structure from static matrix BF;
  the optional argument IND_R specifies the index for the selected redundant basic forces;
  BBARI is the force influence matrix for the applied forces at the free dofs,
  and BBARX is the force influence matrix for the redundant basic forces;
  IND_X is the redundant force index vector into the basic forces of the structure
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [S_ForceMethod](S_ForceMethod.html){.code} % script for force method
    of structural analysis

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
