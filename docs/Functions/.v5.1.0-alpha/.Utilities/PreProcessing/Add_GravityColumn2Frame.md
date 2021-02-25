[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> Add_GravityColumn2Frame.m

</div>

# Add_GravityColumn2Frame

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**ADD_GRAVITYCOLUMN2FRAME generate gravity column and connectors to
frame**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Frame = Add_GravityColumn2Frame (Frame)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
ADD_GRAVITYCOLUMN2FRAME generate gravity column and connectors to frame
  FRAME = ADD_GRAVITYCOLUMN2FRAME (FRAME)
  the function adds coordinate and connectivity information for a gravity column located
  next to the moment resisting frame described in data structure FRAME and returns this
  information in the updated data structure FRAME;
  the functions adds one gravity column and one rigid connector per story;
  the element index of the corresponding elements is returned in the field GColIndx of
  FRAME with the first NST elements corresponding to the gravity column and the next NST
  elements to the rigid connectors, where NST is the number of stories in FRAME
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
