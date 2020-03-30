[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [General](FEDEASLab.html) \>
Create\_NodalMass.m

</div>

Create\_NodalMass
=================

PURPOSE [![\^](../up.png)](#_top)
-------------------------------------------

::: {.box}
**CREATE\_NODALMASS free dof lumped mass vector for structural model**
:::

SYNOPSIS [![\^](../up.png)](#_top)
------------------------------------------------

::: {.box}
**function Ml = Create\_NodalMass (Model,Me)**
:::

DESCRIPTION [![\^](../up.png)](#_top)
------------------------------------------------------

::: {.fragment}
``` {.comment}
CREATE_NODALMASS free dof lumped mass vector for structural model
  ML = CREATE_NODALMASS (MODEL,ME)
  the function sets up the free dof lumped mass vector ML for the structural model
  specified in data structure MODEL from the specified nodal lumped mass values in array ME
  in which rows correspond to node numbers and columns to dof direction
  Example: ME(5,:) = [20 20 0]; lumped mass value in X and Y at node 5; no rotary inertia
```
:::

CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)
----------------------------------------------------------------

This function calls:

This function is called by:

-   [Add\_Mass2Model](Add_Mass2Model.html "function Model = Add_Mass2Model (Model,Me,ElemData,option)"){.code}
    ADD\_MASS2MODEL sets up lumped or consistent mass in Model.M

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
