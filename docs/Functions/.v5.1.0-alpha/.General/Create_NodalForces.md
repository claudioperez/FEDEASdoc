[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [General](FEDEASLab.html) \>
Create_NodalForces.m

</div>

# Create_NodalForces

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**CREATE_NODALFORCES set up reference vector of applied forces**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function Pref = Create_NodalForces (Model,Pe)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
CREATE_NODALFORCES set up reference vector of applied forces
  PREF = CREATE_NODALFORCES (MODEL,PE)
  the function sets up the vector of applied forces PREF at the free dofs of the model;
  model information is supplied in data structure MODEL and the applied forces in array PE;
  in array PE rows correspond to node numbers and columns to dofs
  Example: PE(3,:) = [10 0 50] means applied forces at node 3 in X,Y and Z direction
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
