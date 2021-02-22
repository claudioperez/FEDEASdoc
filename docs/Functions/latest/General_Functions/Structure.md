---
title: "Structure"
id: "Structure"
description: "STRUCTURE performs requested action on group of elements"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">General_Functions</a> &gt; 
<!-- Structure.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\General_Functions&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Structure`



## <a name="_name"></a>Purpose


STRUCTURE performs requested action on group of elements

<!-- <div class="box"><strong>STRUCTURE performs requested action on group of elements</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function Resp = Structure (action,Model,ElemData,State,ElemList)` 

## Description


<pre class="comment">STRUCTURE performs requested action on group of elements
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
   ELEMLIST    = list of elements to which action applies (default=all elements in model)</pre>
<!-- <div class="fragment"><pre class="comment">STRUCTURE performs requested action on group of elements
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
   ELEMLIST    = list of elements to which action applies (default=all elements in model)</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="/Functions/Extract_Str2ElState" class="code" title="function ElemState = Extract_Str2ElState (el,id,State)">Extract_Str2ElState</a>	EXTRACT_STR2ELSTATE extract element state from structure state</li><li><a href="/Functions/Localize" class="code" title="function [xyz,id] = Localize (Model,el)">Localize</a>	LOCALIZE returns the node coordinates and id array of element</li><li><a href="/Functions/SubIncr4ElemntSD" class="code" title="function ElemState = SubIncr4ElemntSD (el,ElemName,xyz,ElemData,ElemState)">SubIncr4ElemntSD</a>	SUBINCR4ELMNTSD element displacement increment subdivision for state determination</li></ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="../../latest/Analysis_Functions/Dynamic/TransientStateDetermination.md" class="code" title="function State = TransientStateDetermination (StifUpdt,Model,ElemData,State,Int_Constants)">TransientStateDetermination</a>	TRANSIENTSTATEDETERMINATION structure state determination under transient conditions</li><li><a href="../../latest/Analysis_Functions/Dynamic/Update_TransientState.md" class="code" title="function State = Update_TransientState (Model,ElemData,State,SolStrat)">Update_TransientState</a>	UPDATE_TRANSIENTSTATE final state determination under transient conditions, reset increments and history</li><li><a href="../../latest/Analysis_Functions/Static/Initialize.md" class="code" title="function [State,SolStrat] = Initialize (Model,ElemData,Loading,State,SolStrat)">Initialize</a>	INITIALIZE initialize analysis variables in STATE and load control parameters in SOLSTRAT</li><li><a href="../../latest/Analysis_Functions/Static/Initialize_State.md" class="code" title="function State = Initialize_State (Model,ElemData)">Initialize_State</a>	INITIALIZE_STATE initialize state variables of structural model and create STATE</li><li><a href="../../latest/Analysis_Functions/Static/LinearStep.md" class="code" title="function State = LinearStep (Model,ElemData,Loading)">LinearStep</a>	LINEARSTEP sets up and solves the structure equilibrium equations for single load step</li><li><a href="../../latest/Analysis_Functions/Static/StateDetermination.md" class="code" title="function State = StateDetermination (StifUpdt,Model,ElemData,State)">StateDetermination</a>	STATEDETERMINATION structure state determination under static conditions</li><li><a href="../../latest/Analysis_Functions/Static/Update_State.md" class="code" title="function State = Update_State (Model,ElemData,State)">Update_State</a>	UPDATE_STATE final state determination under static conditions, reset increments and history</li><li><a href="Add_Mass2Model.md" class="code" title="function Model = Add_Mass2Model (Model,Me,ElemData,option)">Add_Mass2Model</a>	ADD_MASS2MODEL sets up lumped or consistent mass in Model.M</li><li><a href="../../latest/Solution_Scripts/S_InitialStep.md" class="code" title="">S_InitialStep</a>	% S_INITIALSTEP script for initial step of incremental analysis</li><li><a href="../../latest/Solution_Scripts/S_MultiStep.md" class="code" title="">S_MultiStep</a>	% S_MULTISTEP script for multi-step incremental analysis after load factor initialization</li><li><a href="../../latest/Solution_Scripts/S_MultiStep_wLoadHist.md" class="code" title="">S_MultiStep_wLoadHist</a>	% S_MULTISTEP_wLOADHIST script for multi-step incremental analysis under given load history(ies)</li><li><a href="../../latest/Solution_Scripts/S_MultiStep_wLoadHistwSD.md" class="code" title="">S_MultiStep_wLoadHistwSD</a>	% S_MULTISTEP_wLOADHISTwSD script for multi-step incremental analysis under given load history(ies)</li><li><a href="../../latest/Solution_Scripts/S_Transient_MultiStep.md" class="code" title="">S_Transient_MultiStep</a>	% S_TRANSIENT_MULTISTEP script for multi-step transient analysis under given load history(ies)</li><li><a href="../../latest/Solution_Scripts/S_Transient_MultiStepwSD.md" class="code" title="">S_Transient_MultiStepwSD</a>	% S_TRANSIENT_MULTISTEPwSD script for multi-step transient analysis under given load history(ies)</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->