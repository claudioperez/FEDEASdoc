[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> FiberElemData4SteelFrame.m

</div>

# FiberElemData4SteelFrame

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**FIBERELEMDATA4STEELFRAME generate fiber element properties for steel
moment resisting frame (SMRF)**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function \[ColElemData,GrdElemData\] = FiberElemData4SteelFrame
(Frame,Data,DBase,LUnit,Member)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
FIBERELEMDATA4STEELFRAME generate fiber element properties for steel moment resisting frame (SMRF)
  [COLELEMDATA,GRDELEMDATA] = FIBERELEMDATA4STEELFRAME (FRAME,DATA,DBASE,LUNIT,MEMBER)
  the function assigns the properties for inelastic frame elements with fiber
  sections from column and girder section information in FRAME
 by extracting the section properties with the help of function DBASE from
  the corresponding steel section database; DATA carries information about
  the material properties; the optional argument LUNIT specifies the length
  unit for the section property data and the optional character argument MEMBER
  limits the section property retrieval to the girders or columns with
  'girders' or 'columns', respectively
  COLELEMDATA and GRDELEMDATA are cell arrays with the same organization
  as FRAME.CINDX and FRAME.GINDX, respectively;
  currently supported options for DBASE are:
    'AISC_WSECTION'  for wide flange shapes
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
