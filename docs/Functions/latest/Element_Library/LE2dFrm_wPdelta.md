---
title: "LE2dFrm_wPdelta"
id: "LE2dFrm_wPdelta"
description: "LE2dFRM 2d linear elastic frame element with P-delta effect under linear or nonlinear geometry"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">Element_Library</a> &gt; 
<!-- LE2dFrm_wPdelta.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Element_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `LE2dFrm_wPdelta`



## <a name="_name"></a>Purpose


LE2dFRM 2d linear elastic frame element with P-delta effect under linear or nonlinear geometry

<!-- <div class="box"><strong>LE2dFRM 2d linear elastic frame element with P-delta effect under linear or nonlinear geometry</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function ElemResp = LE2dFrm_wPdelta (action,el_no,xyz,ElemData,ElemState)` 

## Description


<pre class="comment">LE2dFRM 2d linear elastic frame element with P-delta effect under linear or nonlinear geometry   
  ELEMRESP = LE2dFRM_wPDELTA (ACTION,EL_NO,XYZ,ELEMDATA,ELEMSTATE)
  response of 2d linear elastic frame element with P-delta effects;
  the element accounts for linear and nonlinear geometry for the nodal dof transformations; 
  depending on the value of the character variable ACTION the function returns information
  in data structure ELEMRESP for the element with number EL_NO, end node coordinates XYZ,
  and material and loading properties in the data structure ELEMDATA.
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  When the character variable ACTION has one of the following values,
  the function performs the listed operations and returns the results in ELEMRESP:
  ACTION = 'size': report size of element arrays
           'chec': check element property data for omissions and assign default values
           'defo': report function handle for deformed shape

           'init': initialize element history variables
           'forc': report element resisting forces
           'stif': report element stiffness matrix and resisting forces
           'mass': report lumped mass vector and consistent mass matrix
           'post': report post-processing information
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The data structure ELEMRESP stands for the following data object(s) for each ACTION:
  ELEMRESP = ARSZ        for action = 'size' 
  ELEMRESP = ELEMDATA    for action = 'chec'
  ELEMRESP = FunHandle   for action = 'defo'

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
  ELEMDATA is a data structure with element property information in fields
         Geom   = character variable for geometric transformation of node variables
                  (linear, PDelta or corotational) (default=linear)
         A      = cross sectional area
         E      = modulus of elasticity
         I      = moment of inertia
         rho    = mass density
         JntOff = rigid joint offsets in global X and Y at element ends; column 1 for node i, column 2 for node j
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
  ELEMPOST is a data structure with element response information for post-processing in fields
         v     = element deformations
         q     = element basic forces</pre>
<!-- <div class="fragment"><pre class="comment">LE2dFRM 2d linear elastic frame element with P-delta effect under linear or nonlinear geometry   
  ELEMRESP = LE2dFRM_wPDELTA (ACTION,EL_NO,XYZ,ELEMDATA,ELEMSTATE)
  response of 2d linear elastic frame element with P-delta effects;
  the element accounts for linear and nonlinear geometry for the nodal dof transformations; 
  depending on the value of the character variable ACTION the function returns information
  in data structure ELEMRESP for the element with number EL_NO, end node coordinates XYZ,
  and material and loading properties in the data structure ELEMDATA.
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  When the character variable ACTION has one of the following values,
  the function performs the listed operations and returns the results in ELEMRESP:
  ACTION = 'size': report size of element arrays
           'chec': check element property data for omissions and assign default values
           'defo': report function handle for deformed shape

           'init': initialize element history variables
           'forc': report element resisting forces
           'stif': report element stiffness matrix and resisting forces
           'mass': report lumped mass vector and consistent mass matrix
           'post': report post-processing information
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The data structure ELEMRESP stands for the following data object(s) for each ACTION:
  ELEMRESP = ARSZ        for action = 'size' 
  ELEMRESP = ELEMDATA    for action = 'chec'
  ELEMRESP = FunHandle   for action = 'defo'

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
  ELEMDATA is a data structure with element property information in fields
         Geom   = character variable for geometric transformation of node variables
                  (linear, PDelta or corotational) (default=linear)
         A      = cross sectional area
         E      = modulus of elasticity
         I      = moment of inertia
         rho    = mass density
         JntOff = rigid joint offsets in global X and Y at element ends; column 1 for node i, column 2 for node j
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
  ELEMPOST is a data structure with element response information for post-processing in fields
         v     = element deformations
         q     = element basic forces</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="/Functions/ExtrReshu" class="code" title="function [u,Du,DDu] = ExtrReshu (State,ndf,nen)">ExtrReshu</a>	EXTRRESHU extracts displacements and increments from State and reshapes into array</li><li><a href="/Functions/GeomTran_2dFrm" class="code" title="function [ag,bg,ab,v,Dv,DDv] = GeomTran_2dFrm (option,xyz,GeomData,u,Du,DDu)">GeomTran_2dFrm</a>	GEOMTRAN_2dFRM kinematic matrices and deformations for a 2-node 2d frame element</li><li><a href="/Functions/kg_2dFrm" class="code" title="function kg = kg_2dFrm (option,xyz,u,q)">kg_2dFrm</a>	KG_2dFRM geometric stiffness matrix for 2-node 2d frame element for different options</li></ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->