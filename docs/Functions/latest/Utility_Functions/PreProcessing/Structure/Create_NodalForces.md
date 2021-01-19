[]{#_top}

<div>

[Home](../FEDEASLab.html) &gt; [General](FEDEASLab.html) &gt;
Create\_NodalForces.m

</div>

Create\_NodalForces
===================

[]{#_name}PURPOSE [![\^](../up.png)](#_top)
-------------------------------------------

<div class="box">

**CREATE\_NODALFORCES set up reference vector of applied forces**

</div>

[]{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)
------------------------------------------------

<div class="box">

**function Pref = Create\_NodalForces (Model,Pe)**

</div>

[]{#_description}DESCRIPTION [![\^](../up.png)](#_top)
------------------------------------------------------

<div class="fragment">

``` {.comment}
CREATE_NODALFORCES set up reference vector of applied forces
  PREF = CREATE_NODALFORCES (MODEL,PE)
  the function sets up the vector of applied forces PREF at the free dofs of the model;
  model information is supplied in data structure MODEL and the applied forces in array PE;
  in array PE rows correspond to node numbers and columns to dofs
  Example: PE(3,:) = [10 0 50] means applied forces at node 3 in X,Y and Z direction
```

</div>

[]{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)
----------------------------------------------------------------

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
