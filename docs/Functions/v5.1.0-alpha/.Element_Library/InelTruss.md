[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
InelTruss.m

</div>

# InelTruss

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**INELTRUSS 2d/3d inelastic truss element under linear or nonlinear
geometry**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function ElemResp = InelTruss (action,el_no,xyz,ElemData,ElemState)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
INELTRUSS 2d/3d inelastic truss element under linear or nonlinear geometry   
  ELEMRESP = INELTRUSS (ACTION,EL_NO,XYZ,ELEMDATA,ELEMSTATE)
  response of 2d/3d inelastic truss element;
  the element accounts for linear and nonlinear geometry for the nodal dof transformations; 
  depending on the value of the character variable ACTION the function returns information
  in data structure ELEMRESP for the element with number EL_NO, end node coordinates XYZ,
  and material and loading properties in the data structure ELEMDATA.
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  When the character variable ACTION has one of the following values,
  the function performs the listed operations and returns the results in ELEMRESP:
  ACTION = 'size': report size of element arrays
           'chec': check element property data for omissions and assign default values
           'init': initialize element history variables
           'forc': report element resisting forces
           'stif': report element stiffness matrix and resisting forces
           'mass': report lumped mass vector and consistent mass matrix
           'post': report post-processing information
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The data structure ELEMRESP stands for the following data object(s) for each ACTION:
  ELEMRESP = ARSZ        for action = 'size' 
  ELEMRESP = ELEMDATA    for action = 'chec'
  ELEMRESP = ELEMSTATE   for action = 'init'
  ELEMRESP = ELEMSTATE   for action = 'stif'
  ELEMRESP = ELEMSTATE   for action = 'forc'
  ELEMRESP = ELEMMASS    for action = 'mass'
  ELEMRESP = ELEMPOST    for action = 'post'
  ELEMRESP is empty      for unsupported keywords
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ARSZ   is an Boolean array of size NDF x NEN,
         where NDF = number of DOFs/node, NEN = number of nodes,
         with unit values corresponding to the active element DOFs
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ELDATA is a data structure with element property information in fields
         Geom    = character variable for geometric transformation of node variables
                   (linear, PDelta or corotational) (default=linear)
         A       = cross sectional area
         MatName = function for material stress-strain response
         MatData = material property data
         s0      = initial force (default = 0)
         e0      = initial deformation (default = 0)
         jntoff  = rigid joint offsets in global X and Y at element ends; column 1 for node i, column 2 for node j
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ELEMSTATE is a data structure with the current element state; it has the fields
         u     = vector of total element displacements in global reference
         Du    = vector of element displacement increments from last convergence
         DDu   = vector of element displacement increments from last iteration
         ke    = element stiffness matrix in global reference; updated under ACTION = 'stif'
         p     = element resisting force vector in global reference; updated under ACTION = 'stif' or 'forc'
         Past  = element history variables at last converged state
         Pres  = current element history variables
         lamda = row vector of current load factor(s)
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ELEMPOST is a data structure with element response information for post-processing in fields
         v     = element deformations
         q     = element basic forces
         Mat   = material response information for post-processing (see material function with MatName)
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [ExtrReshu](ExtrReshu.html "function [u,Du,DDu] = ExtrReshu (State,ndf,nen)"){.code}
    EXTRRESHU extracts displacements and increments from State and
    reshapes into array
-   [GeomTran_Truss](GeomTran_Truss.html "function [ag,bg,v,Dv,DDv] = GeomTran_Truss (option,xyz,u,Du,DDu)"){.code}
    GEOMTRAN_TRUSS kinematic matrices and deformations for a 2-node
    truss element
-   [kg_Truss](kg_Truss.html "function kg = kg_Truss (option,xyz,u,q)"){.code}
    KG_TRUSS geometric stiffness matrix for 2d/3d 2-node truss element
    for different options

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
