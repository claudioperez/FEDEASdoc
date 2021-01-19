[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
Dinel2dFrm_EBwFF.m

</div>

# Dinel2dFrm_EBwFF

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**DINEL2dFRM_EBwFF 2d-frame element with distributed inelasticity (force
formulation)**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function ElemResp = Dinel2dFrm_EBwFF
(action,el_no,xyz,ElemData,ElemState)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
DINEL2dFRM_EBwFF 2d-frame element with distributed inelasticity (force formulation)
  ELEMRESP = DINEL2dFRM_EBwFF (ACTION,EL_NO,XYZ,ELEMDATA,ELEMSTATE)
  function determines the response of 2d frame element with distributed inelasticity for any
           type of section and material under linear and nonlinear geometry;
           iterative or non-iterative force formulation with small deformations
           reference: Spacone/Filippou/Taucer IJSDEE, Vol.25, No.7, July 1996, pp. 711-725
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
           'defo': report function handle for deformed shape
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The data structure ELEMRESP stands for the following data object(s) for each ACTION:
  ELEMRESP = ARSZ        for action = 'size' 
  ELEMRESP = ELEMDATA    for action = 'chec'
  ELEMRESP = ELEMSTATE   for action = 'init'
  ELEMRESP = ELEMSTATE   for action = 'stif'
  ELEMRESP = ELEMSTATE   for action = 'forc'
  ELEMRESP = ELEMMASS    for action = 'mass'
  ELEMRESP = ELEMPOST    for action = 'post'
  ELEMRESP = FunHandle   for action = 'defo'
  ELEMRESP is empty      for unsupported keywords
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ARSZ   is an Boolean array of size NDF x NEN,
         where NDF = number of DOFs/node, NEN = number of nodes,
         with unit values corresponding to the active element DOFs
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ELEMDATA is a data structure with element property information in fields
        Geom    = character variable for geometric transformation of node variables
                  (linear, PDelta or corotational) (default=linear)
        w       = uniform element load ( w(1) = longitudinal, w(2) = transverse )
        MR      = moment release code (0=cont,1=hinge) (default=[0;0])
        jntoff  = rigid joint offsets in global X and Y at element ends;
                  column 1 for node i, column 2 for node j
        nIP     = number of integration points
        IntTyp  = function name for element integration
        Tol     = relative tolerance for convergence of state determination (10^-16)
        MaxIter = maximum number of iterations for state convergence (15)
        SubDivNo= number of element deformation subdivisions (5)
        SecName = function name for section s-e response
        SecData{i} = section property data at integration point i (see function with SecName)
        LdIdx   = load history no for element loading in x-direction
        LdIdy   = load history no for element loading in y-direction
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
         v     = element deformations
         q     = element basic forces
         Sec{i}= section response information at integration point i (see function with SecName)
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [ElementLoading](ElementLoading.html "function wC = ElementLoading (w0,lamda,LdId)"){.code}
    ELEMENTLOADING determines current distributed element load value
-   [ExtrReshu](ExtrReshu.html "function [u,Du,DDu] = ExtrReshu (State,ndf,nen)"){.code}
    EXTRRESHU extracts displacements and increments from State and
    reshapes into array
-   [GeomTran_2dFrm](GeomTran_2dFrm.html "function [ag,bg,ab,v,Dv,DDv] = GeomTran_2dFrm (option,xyz,GeomData,u,Du,DDu)"){.code}
    GEOMTRAN_2dFRM kinematic matrices and deformations for a 2-node 2d
    frame element
-   [kg_2dFrm](kg_2dFrm.html "function kg = kg_2dFrm (option,xyz,u,q)"){.code}
    KG_2dFRM geometric stiffness matrix for 2-node 2d frame element for
    different options

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
