[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [General](FEDEASLab.html) \>
Add_Mass2Model.m

</div>

# Add_Mass2Model

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**ADD_MASS2MODEL sets up lumped or consistent mass in Model.M**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function Model = Add_Mass2Model (Model,Me,ElemData,option)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
ADD_MASS2MODEL sets up lumped or consistent mass in Model.M
  MODEL = ADD_MASS2MODEL (MODEL,ME,ELEMDATA,OPTION)
  the function adds the field M to the data structure Model, which carries information
  about the structural model; M is either a nfx1 column vector for the lumped mass
  or, a nfxnf array for the consistent mass of the model, where nf is the number of free DOFs;
  this depends on the presence ELEMDATA in the argument list and on the
  character variable OPTION; the following cases are possible:
  (1) without ELEMDATA the function takes the nodal lumped mass values in
      array ME where row=node no and column=dof no and assigns them to the
      column vector M with the row corresponding to the DOF number;
          Example: ME(5,:) = [20 20 0]; lumped mass value in X and Y at node 5; no rotary inertia
  (2) if ELEMDATA is present in the argument list the function calculates
      the lumped and consistent mass contribution of each element in the structural model
      that supports this feature; it adds the element lumped mass to
      the nodal lumped mass and returns the lumped mass in column vector M
  (3) if ELEMDATA is present and OPTION='CONSISTENT' the function returns
      the consistent mass matrix M after adding the nodal lumped mass on its diagonal
  if the Model was generated with Create_Model and supports sparse DOF indexing
  then M is a sparse column vector or matrix; if the Model was generated with
  Create_SimpleModel then the column vector or matrix are full
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [Create_NodalMass](Create_NodalMass.html "function Ml = Create_NodalMass (Model,Me)"){.code}
    CREATE_NODALMASS free dof lumped mass vector for structural model
-   [Structure](Structure.html "function Resp = Structure (action,Model,ElemData,State,ElemList)"){.code}
    STRUCTURE performs requested action on group of elements

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
