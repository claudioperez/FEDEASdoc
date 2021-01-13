[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [General](FEDEASLab.html) \> Create_Model.m

</div>

# Create_Model

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**CREATE_MODEL creates data structure Model from node coordinates,
connectivity and boundary conditions**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function Model = Create_Model (XYZ,CON,BOUN,ElemName)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
CREATE_MODEL creates data structure Model from node coordinates, connectivity and boundary conditions
  MODEL = CREATE_MODEL (XYZ,CON,BOUN,ELEMNAME)
  function creates data structure MODEL with model information from the array of
  node coordinates XYZ (rows correspond to node numbers and columns to dofs),
  the cell array of element connectivity CON (rows correspond to element numbers),
  the array of boundary conditions BOUN (rows correspond to node numbers and columns to dofs),
  and the cell array of element names ELEMNAME (rows correspond to element numbers)
  Example: XYZ  (3,:)  = [10 15 22]; coordinates of node 3
           BOUN (3,:)  = [ 1  0  1]; boundary condition code for node 3 (0=free and 1=fixed)
           CON {4}     = [ 6 7];     element 4 connects nodes 6 and 7
           ELEMNAME{4} = 'LinTruss'; element 4 is a linear elastic truss

  data structure MODEL has the following fields
  MODEL.ndm      = dimension of structural model
        nn       = number of nodes in structural model
        ne       = number of elements
        nf       = number of free degrees of freedom
        nt       = total number of degrees of freedom
        XYZ      = node coordinates, nodes are stored columnwise
        BOUN     = boundary conditions, nodes are stored columnwise
        CON      = node connectivity array
        DOF      = array with degree of freedom numbering, nodes are stored columnwise
        ndf(el)  = no of dofs/node for element el
        nen(el)  = no of nodes     for element el
        ElemName = cell array of element names
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
