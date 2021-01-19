[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> Create_JntOffsets.m

</div>

# Create_JntOffsets

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**CREATE_JNTOFFSETS generation of joint offsets for regular plane
frame**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function JntOff = Create_JntOffsets (Frame,DBase)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
CREATE_JNTOFFSETS generation of joint offsets for regular plane frame    
  JNTOFFSETS = CREATE_JNTOFFSETS (FRAME,DBASE)
  the function generates the element joint offsets for the regular plane frame
  in data structure FRAME from the section depth of the elements
  by extracting the corresponding value with the help of function DBASE
  from the corresponding steel section database;
  JNTOFF is a cell array with NE rows equal to the number of elements in FRAME
  each cell contains the joint offsets of the corresponding element in a
  2x2 array with the first column referring to node I and the second to node J
  currently supported options for DBASE are:
    'AISC_SECTION'   for all AISC wide flange and HSS shapes
    'EURO_IPSECTION' for European IP shapes
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
