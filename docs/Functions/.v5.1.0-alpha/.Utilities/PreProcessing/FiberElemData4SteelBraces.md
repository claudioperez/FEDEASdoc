[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> FiberElemData4SteelBraces.m

</div>

# FiberElemData4SteelBraces

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**FIBERELEMDATA4STEELBRACES generate fiber element properties for steel
braces**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function BraceElemData = FiberElemData4SteelBraces
(Frame,Data,DBase,LUnit)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
FIBERELEMDATA4STEELBRACES generate fiber element properties for steel braces
  BRACEELEMDATA = FIBERELEMDATA4STEELBRACES (FRAME,DATA,DBASE,LUNIT)
  the function assigns the properties for inelastic frame elements with fiber
  sections from brace information in FRAME by extracting the section properties
  with the help of function DBASE from the corresponding steel section database;
  DATA carries information about the material properties;
  the optional argument LUNIT specifies the length unit for the section property data
  BRACEELEMDATA is a cell array with the same organization as FRAME.BINDX;
  currently supported options for DBASE are:
    'AISC_ROUNDHSS_SECTION' for round HSS shapes
    'AISC_RECTHSS_SECTION'  for rectangular HSS shapes
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
