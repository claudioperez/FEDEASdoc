[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> Create_FrameSections.m

</div>

# Create_FrameSections

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**CREATE_FRAMESECTIONS assign section information to column and girder
elements**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Frame = Create_FrameSections (Frame,ColSect,GrdSect)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
CREATE_FRAMESECTIONS assign section information to column and girder elements
  the function assigns the steel shape information in COLSECT and GRDSECT
  to the COLSECT and GRDSECT fields of data structure FRAME, respectively;
  the function duplicates a single entry per story or floor
  as many times as the number of elements of the corresponding story or floor
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
