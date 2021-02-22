[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Utilities](FEDEASLab.html) \>
Print_PDFile.m

</div>

# Print_PDFile

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**PRINT_PDFILE sends the current figure to file**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function Print_PDFile (FName,FigOpt,PrOpt)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
PRINT_PDFILE sends the current figure to file 
  PRINT_PDFILE(FNAME,FIGOPT,PROPT)
  the function generates the FNAME.EXT file from the current figure; if FNAME is missing,
  it is replaced by 'PFile'; the optional arguments FIGOPT and PROPT are data structures
  with the following fields for controlling the display and the output:
  FIGOPT.Pos  : position of figure relative to display (1x4 numeric array) 
        .Ornt : figure orientation ('landscape' or 'portrait')
  PROPT.Format: file format (default=-dpdf for PDF file)
       .Reso  : print resolution
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
