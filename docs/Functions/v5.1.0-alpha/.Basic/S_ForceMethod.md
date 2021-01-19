[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Basic](FEDEASLab.html) \> S_ForceMethod.m

</div>

# S_ForceMethod

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**% script for force method of structural analysis**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**This is a script file.**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
% script for force method of structural analysis
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [B_matrix](B_matrix.html "function B = B_matrix (Model)"){.code}
    B_MATRIX static matrix of structural model with 2d/3d truss and 2d
    frame elements
-   [BbariBbarx_matrix](BbariBbarx_matrix.html "function [Bbari,Bbarx,ind_x] = BbariBbarx_matrix (Bf,ind_r)"){.code}
    BBARIBBARX_MATRIX force influence matrices of primary structure from
    static matrix Bf
-   [Fs_matrix](Fs_matrix.html "function Fs = Fs_matrix (Model,ElemData,Roption)"){.code}
    FS_MATRIX block diagonal matrix of element flexibity matrices for
    structural model
-   [V0_vector](V0_vector.html "function V0 = V0_vector (Model,ElemData,Roption)"){.code}
    V0_VECTOR initial element deformation vector for the structural
    model

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
