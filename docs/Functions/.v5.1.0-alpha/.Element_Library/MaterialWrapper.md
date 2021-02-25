[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
MaterialWrapper.m

</div>

# MaterialWrapper

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**MATERIALWRAPPER wrapper element that passes on arguments to the
material state determination**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function ElemResp = MaterialWrapper
(action,el_no,xyz,ElemData,ElemState)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
MATERIALWRAPPER wrapper element that passes on arguments to the material state determination
  ELEMRESP = MATERIALWRAPPER (ACTION,EL_NO,XYZ,ELEMDATA,ELEMSTATE)
  the function determines the response of the material MATNAME in ELEMDATA
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  the character variable ACTION should have one of the following values
  ACTION = 'size' function reports size of element arrays in variable ARSZ
           'chec' function checks element property data for omissions
                  and returns default values in ELEMDATA
           'init' function returns element history variables in ELEMSTATE
           'forc' function returns element resisting forces in ELEMSTATE
           'stif' function returns element stiffness matrix and resisting forces in ELEMSTATE
           'post' function returns data structure ELEMPOST with post-processing information
  depending on value of character variable ACTION the function returns information
  in data structure ELEMRESP for the element with number EL_NO and end node coordinates XYZ;
  the data structure ELEMDATA supplies the element property data.
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  data structure ELEMRESP stands for the following data object depending on value of ACTION 
  ELEMRESP = ARSZ       for action = 'size' 
  ELEMRESP = ELEMDATA   for action = 'chec'
  ELEMRESP = ELEMSTATE  for action = 'init'
  ELEMRESP = ELEMSTATE  for action = 'stif'
  ELEMRESP = ELEMSTATE  for action = 'forc'
  ELEMRESP = ELEMPOST   for action = 'post'
  ELEMRESP is empty     for unsupported keywords
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ARSZ   is an Boolean array of size NDF x NEN,
         where NDF = number of DOFs/node, NEN = number of nodes,
         with unit values corresponding to the active element DOFs
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
         v     = eps = material strains 
         q     = sig = material stresses
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [Extract_El2MatState](Extract_El2MatState.html "function MatState = Extract_El2MatState (mat,aeps,ElState,rd)"){.code}
    EXTRACT_EL2MATSTATE extract material state from element state

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
