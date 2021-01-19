[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
kg_3dFrm.m

</div>

# kg_3dFrm

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**KG_3dFRM geometric stiffness matrix for 2-node 3d frame element
different options**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function kg = kg_3dFrm (option,xyz,GeomData,u,q,ElLoad)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
KG_3dFRM geometric stiffness matrix for 2-node 3d frame element different options
  KG = KG_3dFRM (OPTION,XYZ,GEOMDATA,U,Q,ELLOAD)
  the function determines the geometric stiffness matrix KG of a 2-node element with end
  coordinates in array XYZ (node i corresponds to first column and node j to second);
  the geometric stiffness matrix depends on the node displacement values in array U (ndfx2)
  in the global reference system and on the basic force vector Q;
  OPTION is a character variable with one of three values:
  'linear','PDelta' and 'corotational' for linear, P-Delta and corotational geometry, resp.
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [LE3dFrm](LE3dFrm.html "function ElemResp = LE3dFrm (action,el_no,xyz,ElemData,ElemState)"){.code}
    LE3dFRM 3d linear frame element under linear or nonlinear geometry

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
