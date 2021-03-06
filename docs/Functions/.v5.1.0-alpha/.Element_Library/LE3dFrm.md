[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Element_Library](FEDEASLab.html) \>
LE3dFrm.m

</div>

# LE3dFrm

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**LE3dFRM 3d linear frame element under linear or nonlinear geometry**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function ElemResp = LE3dFrm (action,el_no,xyz,ElemData,ElemState)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
LE3dFRM 3d linear frame element under linear or nonlinear geometry   
  ELEMRESP = LE3dFRM (ACTION,EL_NO,XYZ,ELEMDATA,ELEMSTATE)
  response of 3d linear frame element;
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
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ELEMDATA is a data structure with element property information; it has the fields
         Geom    = character variable for geometric transformation of node variables
                   (linear, PDelta or corotational) (default=linear)
         A       = cross sectional area
         Iy      = moment of inertia about y-axis
         Iz      = moment of inertia about z-axis
         J       = polar moment of inertia
         yornt   = local y-axis orientation in global reference system (column vector)
         E       = modulus of elasticity
         G       = shear modulus
         rho     = mass density
         w       = uniform element load ( w(1) = longitudinal, w(2),w(3) = transverse in y and z, resp.)
         e0      = initial deformations ( e(1) = axial strain, e(2),e(3) = curvature about y and z, resp.)
         jntoff  = rigid joint offsets in global X, Y, Z at element ends; column 1 for node i, column 2 for node j
         Release = axial, torsional and end flexural releases in column vector (0=cont,1=hinge) (default=[0;0;0;0;0;0])
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
  ELEMMASS is a data structure with element mass information in fields
         ml    = lumped mass vector
         mc    = consistent mass matrix
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ELEMPOST is a data structure with response information for post-processing in fields
         v     = element deformations
         q     = element basic forces
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [Check3dFrmAxes](Check3dFrmAxes.html "function y = Check3dFrmAxes (el,y,xyz)"){.code}
    CHECK3dFRMAXES check that y-axis is not co-linear with element chord
-   [ExtrReshu](ExtrReshu.html "function [u,Du,DDu] = ExtrReshu (State,ndf,nen)"){.code}
    EXTRRESHU extracts displacements and increments from State and
    reshapes into array
-   [GeomTran_3dFrm](GeomTran_3dFrm.html "function [ag,bg,ab,v,Dv,DDv] = GeomTran_3dFrm (option,xyz,GeomData,u,Du,DDu)"){.code}
    GEOMTRAN_3dFRM kinematic matrices and deformations for a 2-node 3d
    frame element
-   [kg_3dFrm](kg_3dFrm.html "function kg = kg_3dFrm (option,xyz,GeomData,u,q,ElLoad)"){.code}
    KG_3dFRM geometric stiffness matrix for 2-node 3d frame element
    different options

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
