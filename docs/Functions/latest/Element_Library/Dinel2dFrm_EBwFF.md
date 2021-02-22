---
title: "Dinel2dFrm_EBwFF"
id: "Dinel2dFrm_EBwFF"
description: "DINEL2dFRM_EBwFF 2d-frame element with distributed inelasticity (force formulation)"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">Element_Library</a> &gt; 
<!-- Dinel2dFrm_EBwFF.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Element_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Dinel2dFrm_EBwFF`



## <a name="_name"></a>Purpose


DINEL2dFRM_EBwFF 2d-frame element with distributed inelasticity (force formulation)

<!-- <div class="box"><strong>DINEL2dFRM_EBwFF 2d-frame element with distributed inelasticity (force formulation)</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function ElemResp = Dinel2dFrm_EBwFF (action,el_no,xyz,ElemData,ElemState)` 

## Description


<pre class="comment">DINEL2dFRM_EBwFF 2d-frame element with distributed inelasticity (force formulation)
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
        Geom    = character variable for geometric transformation of node variables
                  (linear, PDelta or corotational) (default=linear)
        w       = uniform element load ( w(1) = longitudinal, w(2) = transverse )
        MR      = moment release code (0=cont,1=hinge) (default=[0;0])
        JntOff  = rigid joint offsets in global X and Y at element ends;
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
         Sec{i}= section response information at integration point i (see function with SecName)</pre>
<!-- <div class="fragment"><pre class="comment">DINEL2dFRM_EBwFF 2d-frame element with distributed inelasticity (force formulation)
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
        Geom    = character variable for geometric transformation of node variables
                  (linear, PDelta or corotational) (default=linear)
        w       = uniform element load ( w(1) = longitudinal, w(2) = transverse )
        MR      = moment release code (0=cont,1=hinge) (default=[0;0])
        JntOff  = rigid joint offsets in global X and Y at element ends;
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
         Sec{i}= section response information at integration point i (see function with SecName)</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="/Functions/ElementLoading" class="code" title="function wC = ElementLoading (w0,lamda,LdId)">ElementLoading</a>	ELEMENTLOADING determines current distributed element load value</li><li><a href="/Functions/ExtrReshu" class="code" title="function [u,Du,DDu] = ExtrReshu (State,ndf,nen)">ExtrReshu</a>	EXTRRESHU extracts displacements and increments from State and reshapes into array</li><li><a href="/Functions/GeomTran_2dFrm" class="code" title="function [ag,bg,ab,v,Dv,DDv] = GeomTran_2dFrm (option,xyz,GeomData,u,Du,DDu)">GeomTran_2dFrm</a>	GEOMTRAN_2dFRM kinematic matrices and deformations for a 2-node 2d frame element</li><li><a href="/Functions/kg_2dFrm" class="code" title="function kg = kg_2dFrm (option,xyz,u,q)">kg_2dFrm</a>	KG_2dFRM geometric stiffness matrix for 2-node 2d frame element for different options</li></ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->