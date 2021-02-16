
<!-- <a name="_top"></a>
<div><a href="../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="_index.md">General_Functions</a> &gt; Create_Loading.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../_index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\General_Functions&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Create_Loading`
<!-- <h1>Create_Loading
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

CREATE_LOADING create data structure Loading with reference vector(s) for applied forces and imposed displacements

<!-- <div class="box"><strong>CREATE_LOADING create data structure Loading with reference vector(s) for applied forces and imposed displacements</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function Loading = Create_Loading (Model,Pe,Ue)` 
## <a name="_description"></a>Description

<pre class="comment">CREATE_LOADING create data structure Loading with reference vector(s) for applied forces and imposed displacements
  LOADING = CREATE_LOADING (MODEL,PE,UE)
  the function sets up the data structure LOADING with the array of applied force patterns
  at the free dofs of the model in field Pref and the array of imposed displacement patterns
  at the restrained dofs of the model in field Uref; model information is specified
  in data structure MODEL and the applied forces and imposed displacements are
  specified in arrays PE and UE, respectively;
  in arrays PE and UE rows correspond to node numbers and columns to dof direction
  Example: PE(3,:,1) = [10 0 50]; applied forces at node 3 in X,Y and Z direction for force pattern 1
           UE(5,2,3) = 0.02;      imposed displacement in Y-direction at node 5 for displacement pattern 3</pre>
<!-- <div class="fragment"><pre class="comment">CREATE_LOADING create data structure Loading with reference vector(s) for applied forces and imposed displacements
  LOADING = CREATE_LOADING (MODEL,PE,UE)
  the function sets up the data structure LOADING with the array of applied force patterns
  at the free dofs of the model in field Pref and the array of imposed displacement patterns
  at the restrained dofs of the model in field Uref; model information is specified
  in data structure MODEL and the applied forces and imposed displacements are
  specified in arrays PE and UE, respectively;
  in arrays PE and UE rows correspond to node numbers and columns to dof direction
  Example: PE(3,:,1) = [10 0 50]; applied forces at node 3 in X,Y and Z direction for force pattern 1
           UE(5,2,3) = 0.02;      imposed displacement in Y-direction at node 5 for displacement pattern 3</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="../../latest/Solution_Scripts/S_MomCurvAnalysis.md" class="code" title="">S_MomCurvAnalysis</a>	% S_MOMCURVANALYSIS script for moment-curvature analysis under constant axial force</li><li><a href="../../latest/Solution_Scripts/S_NMAnalysis.md" class="code" title="">S_NMAnalysis</a>	% S_NMANALYSIS script for incremental application of N-M pair on section</li><li><a href="../../latest/Solution_Scripts/S_NMAnalysiswSepLoadHist.md" class="code" title="">S_NMAnalysiswSepLoadHist</a>	% S_NMANALYSISwSEPLOADHIST script for application N and M with separate load histories</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->