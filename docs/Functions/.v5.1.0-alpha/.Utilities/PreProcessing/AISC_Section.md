[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> AISC_Section.m

</div>

# AISC_Section

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**AISC_SECTION extracts section properties from AISC W-,M-,S-,HP- and
HSS-section database**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function SecProp = AISC_Section (sect)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
AISC_SECTION extracts section properties from AISC W-,M-,S-,HP- and HSS-section database
  SECPROP = AISC_SECTION (SECT)
  the function extracts the following properties from the W-,M-,S-,HP- and HSS-section database
  for the section with AISC Manual Label in character array SECT:
  W, A, d, bf, tw, tf, Ix, Zx, Sx, rx, Iy, Zy, Sy, ry, J, Cw
  THE UNITS FOR THESE PROPERTIES ARE IN, IN2, IN3 and IN4
  The structure SECPROP contains the properties in fields with the same name
  Example: SecData = AISC_Section ('W14x193');
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
