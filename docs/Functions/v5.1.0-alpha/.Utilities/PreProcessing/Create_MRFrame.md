[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PreProcessing](FEDEASLab.html) \> Create_MRFrame.m

</div>

# Create_MRFrame

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**CREATE_FRAME generation of nodes and elements for regular N-story,
M-bay MR frame**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Frame = Create_MRFrame (Lbv,Hsv,nsub)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
CREATE_FRAME generation of nodes and elements for regular N-story, M-bay MR frame    
 FRAME = CREATE_MRFRAME (LBV,HSV,NSUB)
  function generates the node coordinates XYZ and element connectivity CON
  for a regular N-story, M-bay frame with bay spans in row vector LBV and
  story heights in row vector HSV; the optional row vector NSUB specifies
  the number of subelements for each frame girder 
  the function returns the generated information in data structure FRAME
  with fields XYZ (node coordinates), CON (element connectivity),
  CINDX (column index by story), GINDX (girder index by floor),
  NBY (no of bays), NST (no of stories), NC (no of columns), NG (no of girders)
  NN (no of nodes), NE (no of elements)
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
