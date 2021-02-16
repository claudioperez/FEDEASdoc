[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Basic](FEDEASLab.html) \> ElmLenOr.m

</div>

# ElmLenOr

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**ELMLENOR element length and x-axis orientation (direction cosines)**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[L,dcx\] = ElmLenOr (xyz)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
ELMLENOR element length and x-axis orientation (direction cosines)
  [L,DCX] = ELMLENOR (XYZ);
  the function determines the length L and x-axis orientation of an element
  with end node coordinates XYZ (column 1 for node i, column 2 for node j);
  the direction cosines for the element x-axis are reported in vector DCX
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
