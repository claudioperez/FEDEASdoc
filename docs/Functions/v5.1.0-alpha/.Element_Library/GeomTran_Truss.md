[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
GeomTran_Truss.m

</div>

# GeomTran_Truss

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**GEOMTRAN_TRUSS kinematic matrices and deformations for a 2-node truss
element**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function \[ag,bg,v,Dv,DDv\] = GeomTran_Truss (option,xyz,u,Du,DDu)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
GEOMTRAN_TRUSS kinematic matrices and deformations for a 2-node truss element
  [AG,BG,V,DV,DDV] = GEOMTRAN_TRUSS (NDF,XYZ,GEOMDATA,U,DU,DDU)
  the function determines the kinematic matrix AG from the global to the basic reference system,
  and the static matrix BG from the basic to the global reference system 
  as well as the element deformation vector V and its increments DV and DDV
  from the end displacement vector U and its increments DU and DDU
  for a 2-node truss element with end node coordinates XYZ and NDF dofs/node;
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
