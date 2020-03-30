[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [General](FEDEASLab.html) \>
Create\_PwForces.m

</div>

Create\_PwForces
================

PURPOSE [![\^](../up.png)](#_top)
-------------------------------------------

::: {.box}
**CREATE\_PWFORCES set up equivalent nodal forces due to uniform element
loading w**
:::

SYNOPSIS [![\^](../up.png)](#_top)
------------------------------------------------

::: {.box}
**function Pw = Create\_PwForces (Model,ElemData)**
:::

DESCRIPTION [![\^](../up.png)](#_top)
------------------------------------------------------

::: {.fragment}
``` {.comment}
CREATE_PWFORCES set up equivalent nodal forces due to uniform element loading w
  PW = CREATE_PWFORCES (MODEL,ELEMDATA)
  the function sets up the vector of equivalent nodal forces PW due to uniform element loading w;
  model information is supplied in data structure MODEL,
  and the magnitude of w is supplied for each element in field W of ELEMDATA
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
