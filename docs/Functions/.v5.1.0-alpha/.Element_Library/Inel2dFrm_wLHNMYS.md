[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
Inel2dFrm_wLHNMYS.m

</div>

# Inel2dFrm_wLHNMYS

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**INEL2dFRM_wLHNMYS 2d linear elastic frame element with linear plastic
hardening axial-flexure hinges**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function ElemResp = Inel2dFrm_wLHNMYS
(action,el_no,xyz,ElemData,ElemState)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
INEL2dFRM_wLHNMYS 2d linear elastic frame element with linear plastic hardening axial-flexure hinges
  ELEMRESP = INEL2dFRM_wLHNMYS (ACTION,EL_NO,XYZ,ELEMDATA,ELEMSTATE)
  response of 2d linear elastic frame element with linear plastic hardening axial-flexure hinges
  with General Closest Point Project (GCPP) Iteration for the N-M yield surface;
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
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ELEMDATA is a data structure with element property information in fields
         Geom    = character variable for geometric transformation of node variables
                   (linear, PDelta or corotational) (default=linear)
         rho     = mass density
         A       = cross sectional area
         I       = moment of inertia
         E       = modulus of elasticity
         Np      = plastic axial capacity of element
         Mp      = plastic moment capacity of element
         GPYSC   = polynomial exponents for plastic surface (see help for function GPYS)
         Hir     = isotropic hardening ratio for flexural end i and j ([0;0])
         Hkr     = kinematic hardening ratio for axial, flexural end i and end j ([0;0;0])
         w       = uniform element load ( w(1) = longitudinal, w(2) = transverse )
         jntoff  = rigid joint offsets in global X and Y at element ends;
                   column 1 for node i, column 2 for node j
         LdIdx   = load history no for element loading in x-direction
         LdIdy   = load history no for element loading in y-direction
         Wtol    = incremental work tolerance for state convergence (10^-16)
         MaxIter = maximum number of iterations for state convergence (15)
         SubDivNo= number of element deformation subdivisions (5)
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
         vp    = plastic deformations
         q     = element basic forces
         w     = current value of distributed element load
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [ElementLoading](ElementLoading.html "function wC = ElementLoading (w0,lamda,LdId)"){.code}
    ELEMENTLOADING determines current distributed element load value
-   [ExtrReshu](ExtrReshu.html "function [u,Du,DDu] = ExtrReshu (State,ndf,nen)"){.code}
    EXTRRESHU extracts displacements and increments from State and
    reshapes into array
-   [GPYS](GPYS.html "function [f,g,h] = GPYS (GPYSC,xyz,ScVec)"){.code}
    GPYS function value, gradient and Hessian of polynomial yield
    surface
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
