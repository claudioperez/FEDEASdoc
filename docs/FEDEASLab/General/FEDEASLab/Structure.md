[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [General](FEDEASLab.html) \> Structure.m

</div>

Structure
=========

PURPOSE [![\^](../up.png)](#_top)
-------------------------------------------

::: {.box}
**STRUCTURE performs requested action on group of elements**
:::

SYNOPSIS [![\^](../up.png)](#_top)
------------------------------------------------

::: {.box}
**function Resp = Structure (action,Model,ElemData,State,ElemList)**
:::

DESCRIPTION [![\^](../up.png)](#_top)
------------------------------------------------------

::: {.fragment}
``` {.comment}
STRUCTURE performs requested action on group of elements
  RESP = STRUCTURE (ACTION,MODEL,ELEMDATA,STATE,ELEMLIST)
  response of some or all elements in the structural model, as requested in ELEMLIST (default=all);
  depending on the value of the character variable ACTION, the function returns information
  in data structure RESP for the structural model with properties in MODEL;
  the cell array ELEMDATA contains the element properties;
  the optional data structure STATE  contains current response state variables for the model.
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  When the character variable ACTION has one of the following values, the function
  performs the listed operations and returns the results in RESP:
  ACTION  = 'chec' check element property data for omissions and assign default values
            'init' initialize element history variables
            'forc' report structure resisting forces
            'stif' report structure stiffness matrix and resisting forces
            'mass' report lumped mass vector and consistent mass matrix
            'post' report post-processing information
            'stre' nodal stress recovery with element least squares
            'nstr' nodal stress recovery with direct nodal stress calculations
            'spre' nodal stress recovery with superconvergent global patch (ZZ-method) (not implemented)
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The data structure RESP stands for the following data object(s) for each ACTION:
  RESP = ELEMDATA for action = 'chec'
  RESP = STATE    for action = 'init'
  RESP = STATE    for action = 'stif'
  RESP = STATE    for action = 'forc'
  RESP = MASS     for action = 'mass'
  RESP = POST     for action = 'post'
  RESP = NDSTR    for action = 'stre','nstr','spre'
  RESP is empty   for unsupported keywords
  additional keywords can be added in the function ADD_ACTION
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  STATE is a data structure with information about the current response state of the model in fields
       lamda   = row vector of current load factor(s)
       U       = global dof total displacement vector
       DU      = global dof displacement increments from last convergencey
       DDU     = global dof displacement increments from last iteration
       Udot    = global dof velocity vector
       Udotdot = global dof acceleration vector
       Kf      = structure stiffness matrix at free dofs; returned along with U under action = 'stif'
       Kfd     = structure stiffness matrix coupling free and restrained dofs
       Pr      = structure resisting force vector; returned along with U under action = 'stif' or 'forc'
       Past    = data structure of         element history variables at last convergence in cell array Elem
       Pres    = data structure of current element history variables                     in cell array Elem
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   MASS is a data structure with mass information in fields:
       Ml      = lumped mass vector of free dofs of structural model
       Mc      = consistent mass matrix of free dofs of structural model
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   POST is a data structure with structure and element response information
        for post-processing in fields:
       lamda    = row vector of current load factor(s)
       Elem{el} = cell array with post-processing information for each element
       U        = global dof displacement vector
       Udot     = global dof velocity     vector (for transient analysis)
       Uddot    = global dof acceleration vector (for transient analysis)
       Pr       = structure resisting force vector
       Time     = time 
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   NDSTR is a data structure with nodal stress information in fields:
       SigNd   = nodal stresses for plane and membrane finite elements
       MomNd   = nodal moments  for plate and shell    finite elements
       ShrNd   = nodal shears   for plate and shell    finite elements with shear deformations
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   ELEMLIST    = list of elements to which action applies (default=all elements in model)
```
:::

CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)
----------------------------------------------------------------

This function calls:

-   [Extract\_Str2ElState](Extract_Str2ElState.html "function ElemState = Extract_Str2ElState (el,id,State)"){.code}
    EXTRACT\_STR2ELSTATE extract element state from structure state
-   [SubIncr4ElemntSD](SubIncr4ElemntSD.html "function ElemState = SubIncr4ElemntSD (el,ElemName,xyz,ElemData,ElemState)"){.code}
    SUBINCR4ELMNTSD element displacement increment subdivision for state
    determination

This function is called by:

-   [Add\_Mass2Model](Add_Mass2Model.html "function Model = Add_Mass2Model (Model,Me,ElemData,option)"){.code}
    ADD\_MASS2MODEL sets up lumped or consistent mass in Model.M

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
