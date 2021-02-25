[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[PostProcessing](FEDEASLab.html) \> Q2Post.m

</div>

# Q2Post

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**Q2POST converts the vector of basic forces Q to cell array
Post.Elem{}**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function Post = Q2Post (Model,Q)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
Q2POST converts the vector of basic forces Q to cell array Post.Elem{}
  POST = Q2POST(MODEL,Q)
  the function converts the basic force values in vector Q to
  the data structure POST consisting of the field Elem{el}
  for each el of the structural model in data structure MODEL
  which, in turn, contains the field Elem{el}.q with the basic forces
  of the particular element; the function uses information
  about missing basic forces in Q based on the field Model.Qmis;
  any missing basic forces are set to zero in Elem{el}.q
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
