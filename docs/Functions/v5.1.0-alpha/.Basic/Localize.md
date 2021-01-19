[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Basic](FEDEASLab.html) \> Localize.m

</div>

# Localize

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**LOCALIZE returns the node coordinates and id array of element**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[xyz,id\] = Localize (Model,el)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
LOCALIZE returns the node coordinates and id array of element
  [XYZ,ID] = LOCALIZE (MODEL,EL)
  the function returns the node coordinates XYZ and the id array ID
  of the element with number EL for the structural model specified in data structure MODEL
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [A_matrix](A_matrix.html "function A = A_matrix (Model)"){.code}
    A_MATRIX kinematic matrix of structural model with 2d/3d truss and
    2d frame elements
-   [B_matrix](B_matrix.html "function B = B_matrix (Model)"){.code}
    B_MATRIX static matrix of structural model with 2d/3d truss and 2d
    frame elements
-   [Fs_matrix](Fs_matrix.html "function Fs = Fs_matrix (Model,ElemData,Roption)"){.code}
    FS_MATRIX block diagonal matrix of element flexibity matrices for
    structural model
-   [Ks_matrix](Ks_matrix.html "function Ks = Ks_matrix (Model,ElemData)"){.code}
    KS_MATRIX block diagonal matrix of basic element stiffness matrices
    for structural model
-   [Q0_vector](Q0_vector.html "function Q0 = Q0_vector (Model,ElemData)"){.code}
    Q0_VECTOR initial (fixed-end) force vector for structural model
-   [V0_vector](V0_vector.html "function V0 = V0_vector (Model,ElemData,Roption)"){.code}
    V0_VECTOR initial element deformation vector for the structural
    model

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
