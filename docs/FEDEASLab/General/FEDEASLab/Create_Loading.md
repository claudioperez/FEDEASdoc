[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [General](FEDEASLab.html) \>
Create\_Loading.m

</div>

Create\_Loading
===============

PURPOSE [![\^](../up.png)](#_top)
-------------------------------------------

::: {.box}
**CREATE\_LOADING create data structure Loading with reference vector(s)
for applied forces and imposed displacements**
:::

SYNOPSIS [![\^](../up.png)](#_top)
------------------------------------------------

::: {.box}
**function Loading = Create\_Loading (Model,Pe,Ue)**
:::

DESCRIPTION [![\^](../up.png)](#_top)
------------------------------------------------------

::: {.fragment}
``` {.comment}
CREATE_LOADING create data structure Loading with reference vector(s) for applied forces and imposed displacements
  LOADING = CREATE_LOADING (MODEL,PE,UE)
  the function sets up the data structure LOADING with the array of applied force patterns
  at the free dofs of the model in field Pref and the array of imposed displacement patterns
  at the restrained dofs of the model in field Uref; model information is specified
  in data structure MODEL and the applied forces and imposed displacements are
  specified in arrays PE and UE, respectively;
  in arrays PE and UE rows correspond to node numbers and columns to dof direction
  Example: PE(3,:,1) = [10 0 50]; applied forces at node 3 in X,Y and Z direction for force pattern 1
           UE(5,2,3) = 0.02;      imposed displacement in Y-direction at node 5 for displacement pattern 3
```
:::

CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)
----------------------------------------------------------------

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
