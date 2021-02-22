---
title: "S_DisplMethod"
id: "S_DisplMethod"
description: "% S_DISPLMETHOD script for displacement method of structural analysis"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">Solution_Scripts</a> &gt; 
<!-- S_DisplMethod.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Solution_Scripts&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `S_DisplMethod`



## <a name="_name"></a>Purpose


% S_DISPLMETHOD script for displacement method of structural analysis

<!-- <div class="box"><strong>% S_DISPLMETHOD script for displacement method of structural analysis</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`This is a script file.` 

## Description


<pre class="comment">% S_DISPLMETHOD script for displacement method of structural analysis
  the script contains the steps for the classical displacement method of structural analysis:
  (1) set up the kinematic matrix Af
  (2) set up the collection of element stiffness matrices Ks
  (3) set up the structure stiffness matrix Kf = Af'*Ks*Af
  (4) set up the equivalent nodal forces Pwf due to element loading
  (5) set up the initial element forces Q0
  (6) set up the initial nodal forces P0 = Af'Q0 + Pwf
  (7) solve for the free global DOF displacements Uf from Pf-P0 = Kf*Uf
  (8) determine the element deformations V=Af*Uf
  (9) determine the basic element forces Q=Ks*V+Q0</pre>
<!-- <div class="fragment"><pre class="comment">% S_DISPLMETHOD script for displacement method of structural analysis
  the script contains the steps for the classical displacement method of structural analysis:
  (1) set up the kinematic matrix Af
  (2) set up the collection of element stiffness matrices Ks
  (3) set up the structure stiffness matrix Kf = Af'*Ks*Af
  (4) set up the equivalent nodal forces Pwf due to element loading
  (5) set up the initial element forces Q0
  (6) set up the initial nodal forces P0 = Af'Q0 + Pwf
  (7) solve for the free global DOF displacements Uf from Pf-P0 = Kf*Uf
  (8) determine the element deformations V=Af*Uf
  (9) determine the basic element forces Q=Ks*V+Q0</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="/Functions/../../latest/General_Functions/A_matrix" class="code" title="function A = A_matrix (Model)">A_matrix</a>	A_MATRIX kinematic matrix of structural model with 2d/3d truss and 2d frame elements</li><li><a href="/Functions/../../latest/General_Functions/Create_PwForces" class="code" title="function Pw = Create_PwForces (Model,ElemData)">Create_PwForces</a>	CREATE_PWFORCES set up equivalent nodal forces due to uniform element loading w</li><li><a href="/Functions/../../latest/General_Functions/Ks_matrix" class="code" title="function Ks = Ks_matrix (Model,ElemData)">Ks_matrix</a>	KS_MATRIX block diagonal matrix of basic element stiffness matrices for structural model</li><li><a href="/Functions/../../latest/General_Functions/Q0_vector" class="code" title="function Q0 = Q0_vector (Model,ElemData)">Q0_vector</a>	Q0_VECTOR initial (fixed-end) force vector for structural model</li><li><a href="/Functions/../../latest/Utility_Functions/General/H_index" class="code" title="function iced = H_index (Model,ElemData)">H_index</a>	H_INDEX cell array of indices into structure arrays for continuous element deformations</li></ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->