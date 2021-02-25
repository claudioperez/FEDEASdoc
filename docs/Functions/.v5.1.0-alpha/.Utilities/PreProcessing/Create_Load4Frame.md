[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> Create_Load4Frame.m

</div>

# Create_Load4Frame

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**CREATE_LOAD4FRAME generation of nodal force vector for regular frame**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Pe = Create_Load4Frame (Frame,Pdis,index)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
CREATE_LOAD4FRAME generation of nodal force vector for regular frame    
 PE = CREATE_LOAD4FRAME (FRAME,PDIS,INDEX)
  the function generates the nodal force vector Pe from information
  about the load distribution in vector PDIS;
  if PDIS is a column vector, the function assigns its distribution to
  the column lines in INDEX (default = all columns)
  if PDIS is a row vector, the function assigns its distribution to
  the floors in INDEX (default = all floors)
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
