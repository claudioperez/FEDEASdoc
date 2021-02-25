[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
kg_Truss.m

</div>

# kg_Truss

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**KG_TRUSS geometric stiffness matrix for 2d/3d 2-node truss element for
different options**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function kg = kg_Truss (option,xyz,u,q)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
KG_TRUSS geometric stiffness matrix for 2d/3d 2-node truss element for different options
  KG = KG_TRUSS (OPTION,XYZ,U,Q)
  the function determines the geometric stiffness matrix KG of a 2-node 2d/3d truss element
  with end coordinates in array XYZ (node i corresponds to first column and node j to second);
  the geometric stiffness matrix depends on the node displacement values in array U (ndmx2)
  in the global reference system and on the basic force vector Q;
  OPTION is a character variable with one of three values:
  'linear','PDelta' and 'corotational' for linear, P-Delta and corotational geometry, resp.
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [InelTruss](InelTruss.html "function ElemResp = InelTruss (action,el_no,xyz,ElemData,ElemState)"){.code}
    INELTRUSS 2d/3d inelastic truss element under linear or nonlinear
    geometry
-   [LETruss](LETruss.html "function ElemResp = LETruss (action,el_no,xyz,ElemData,ElemState)"){.code}
    LETRUSS 2d/3d linear truss element under linear or nonlinear
    geometry

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
