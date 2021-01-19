[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Label_2dMoments.m

</div>

# Label_2dMoments

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**LABEL_2dMOMENTS label end moment values for 2d frame elements in
current window**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Label_2dMoments (Model,Post,ElemList,Digit,Units)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
LABEL_2dMOMENTS label end moment values for 2d frame elements in current window
  LABEL_2dMOMENTS (MODEL,POST,ELEMLIST,DIGIT,UNITS)
  the function displays in the current window the end moment values of 2d frame elements
  in ELEMLIST for the structural model in data structure MODEL;
  POST is either the vector of basic forces Q, or
  a cell array with post-processing information for the basic element forces in POST.ELEM{el}.Q;
  the optional row vector ELEMLIST contains the numbers of elements to include for labeling,
  e.g. [1:4 7 9] selects elements 1 through 4, 7 and 9;
  the optional integer DIGIT controls the number of digits after the comma (default=1)
  the optional integer UNITS scales the output values by the UNITS value
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
