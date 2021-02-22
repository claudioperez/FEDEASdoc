---
title: "S_ForceMethod"
id: "S_ForceMethod"
description: "% S_FORCEMETHOD script for force method of structural analysis"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">Solution_Scripts</a> &gt; 
<!-- S_ForceMethod.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Solution_Scripts&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `S_ForceMethod`



## <a name="_name"></a>Purpose


% S_FORCEMETHOD script for force method of structural analysis

<!-- <div class="box"><strong>% S_FORCEMETHOD script for force method of structural analysis</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`This is a script file.` 

## Description


<pre class="comment">% S_FORCEMETHOD script for force method of structural analysis
  the script contains the steps for the force method of structural analysis:
  (1) set up the equilibrium matrix Bf
  (2) set up the force influence matrices for the primary structure Bbari and Bbarx
  (3) set up the collection of element flexibility matrices Fs
  (4) set up the compatibility conditions and solve for the redundant basic forces Qx
  (5) determine the basic element forces Q=Qp+Bbarx*Qx
  (6) determine the element deformations Ve=Fs*Q+V0
  (7) determine the free DOF displacements Uf=Bbari'*Ve</pre>
<!-- <div class="fragment"><pre class="comment">% S_FORCEMETHOD script for force method of structural analysis
  the script contains the steps for the force method of structural analysis:
  (1) set up the equilibrium matrix Bf
  (2) set up the force influence matrices for the primary structure Bbari and Bbarx
  (3) set up the collection of element flexibility matrices Fs
  (4) set up the compatibility conditions and solve for the redundant basic forces Qx
  (5) determine the basic element forces Q=Qp+Bbarx*Qx
  (6) determine the element deformations Ve=Fs*Q+V0
  (7) determine the free DOF displacements Uf=Bbari'*Ve</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="/Functions/../../latest/General_Functions/B_matrix" class="code" title="function B = B_matrix (Model)">B_matrix</a>	B_MATRIX equilibrium matrix of structural model with 2d/3d truss and 2d frame elements</li><li><a href="/Functions/../../latest/General_Functions/BbariBbarx_matrix" class="code" title="function [Bbari,Bbarx,ind_x] = BbariBbarx_matrix (Bf,ind_r,ind_rng)">BbariBbarx_matrix</a>	BBARIBBARX_MATRIX force influence matrices of primary structure from equilibrium matrix Bf</li><li><a href="/Functions/../../latest/General_Functions/Create_PwForces" class="code" title="function Pw = Create_PwForces (Model,ElemData)">Create_PwForces</a>	CREATE_PWFORCES set up equivalent nodal forces due to uniform element loading w</li><li><a href="/Functions/../../latest/General_Functions/Fs_matrix" class="code" title="function Fs = Fs_matrix (Model,ElemData,Roption)">Fs_matrix</a>	FS_MATRIX block diagonal matrix of element flexibity matrices for structural model</li><li><a href="/Functions/../../latest/General_Functions/V0_vector" class="code" title="function V0 = V0_vector (Model,ElemData,Roption)">V0_vector</a>	V0_VECTOR initial element deformation vector for the structural model</li><li><a href="/Functions/../../latest/Utility_Functions/General/H_index" class="code" title="function iced = H_index (Model,ElemData)">H_index</a>	H_INDEX cell array of indices into structure arrays for continuous element deformations</li></ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->