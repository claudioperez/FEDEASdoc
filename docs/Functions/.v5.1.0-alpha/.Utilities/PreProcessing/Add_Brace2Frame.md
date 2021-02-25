[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> Add_Brace2Frame.m

</div>

# Add_Brace2Frame

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**ADD_BRACE2FRAME adds brace elements to a bay of a frame**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Frame = Add_Brace2Frame
(Frame,BayNo,BrType,EccR,StrRng,nsBr)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
ADD_BRACE2FRAME adds brace elements to a bay of a frame
  FRAME = ADD_BRACE2FRAME (FRAME,BAYNO,BRTYPE,ECCR,STRRNG,NSBR)
  the function adds braces to the bay BAYNO of the frame in data structure
  FRAME over the stories in the contiguous range STRRNG (default is all stories);
  the braces are subdivided into NSBR elements with middle eccentricity ECCR,
  where ECCR is specified as a percentage of the brace length (default = 0)
  BRTYPE is a character variable with the following options:
   'RDbr': rising diagonal brace
   'FDbr': falling diagonal brace
   'IVbr': inverted V-brace
   'RVbr': regular  V-brace
   'AVbr': alternating V- and inverted V-braces (also known as X-brace)
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
