---
title: "Add_Mass2Model"
id: "Add_Mass2Model"
description: "ADD_MASS2MODEL sets up lumped or consistent mass in Model.M"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">General_Functions</a> &gt; 
<!-- Add_Mass2Model.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\General_Functions&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Add_Mass2Model`



## <a name="_name"></a>Purpose


ADD_MASS2MODEL sets up lumped or consistent mass in Model.M

<!-- <div class="box"><strong>ADD_MASS2MODEL sets up lumped or consistent mass in Model.M</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function Model = Add_Mass2Model (Model,Me,ElemData,option)` 

## Description


<pre class="comment">ADD_MASS2MODEL sets up lumped or consistent mass in Model.M
  MODEL = ADD_MASS2MODEL (MODEL,ME,ELEMDATA,OPTION)
  the function adds the field M to the data structure Model, which carries information
  about the structural model; M is either a nfx1 column vector for the lumped mass
  or, a nfxnf array for the consistent mass of the model, where nf is the number of free DOFs;
  this depends on the presence ELEMDATA in the argument list and on the
  character variable OPTION; the following cases are possible:
  (1) without ELEMDATA the function takes the nodal lumped mass values in
      array ME where row=node no and column=dof no and assigns them to the
      column vector M with the row corresponding to the DOF number;
          Example: ME(5,:) = [20 20 0]; lumped mass value in X and Y at node 5; no rotary inertia
  (2) if ELEMDATA is present in the argument list the function calculates
      the lumped and consistent mass contribution of each element in the structural model
      that supports this feature; it adds the element lumped mass to
      the nodal lumped mass and returns the lumped mass in column vector M
  (3) if ELEMDATA is present and OPTION='CONSISTENT' the function returns
      the consistent mass matrix M after adding the nodal lumped mass on its diagonal
  if the Model was generated with Create_Model and supports sparse DOF indexing
  then M is a sparse column vector or matrix; if the Model was generated with
  Create_SimpleModel then the column vector or matrix are full</pre>
<!-- <div class="fragment"><pre class="comment">ADD_MASS2MODEL sets up lumped or consistent mass in Model.M
  MODEL = ADD_MASS2MODEL (MODEL,ME,ELEMDATA,OPTION)
  the function adds the field M to the data structure Model, which carries information
  about the structural model; M is either a nfx1 column vector for the lumped mass
  or, a nfxnf array for the consistent mass of the model, where nf is the number of free DOFs;
  this depends on the presence ELEMDATA in the argument list and on the
  character variable OPTION; the following cases are possible:
  (1) without ELEMDATA the function takes the nodal lumped mass values in
      array ME where row=node no and column=dof no and assigns them to the
      column vector M with the row corresponding to the DOF number;
          Example: ME(5,:) = [20 20 0]; lumped mass value in X and Y at node 5; no rotary inertia
  (2) if ELEMDATA is present in the argument list the function calculates
      the lumped and consistent mass contribution of each element in the structural model
      that supports this feature; it adds the element lumped mass to
      the nodal lumped mass and returns the lumped mass in column vector M
  (3) if ELEMDATA is present and OPTION='CONSISTENT' the function returns
      the consistent mass matrix M after adding the nodal lumped mass on its diagonal
  if the Model was generated with Create_Model and supports sparse DOF indexing
  then M is a sparse column vector or matrix; if the Model was generated with
  Create_SimpleModel then the column vector or matrix are full</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="/Functions/Create_NodalMass" class="code" title="function Ml = Create_NodalMass (Model,Me)">Create_NodalMass</a>	CREATE_NODALMASS free dof lumped mass vector for structural model</li><li><a href="/Functions/Structure" class="code" title="function Resp = Structure (action,Model,ElemData,State,ElemList)">Structure</a>	STRUCTURE performs requested action on group of elements</li></ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->