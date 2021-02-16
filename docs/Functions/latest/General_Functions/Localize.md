
<!-- <a name="_top"></a>
<div><a href="../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="_index.md">General_Functions</a> &gt; Localize.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../_index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\General_Functions&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Localize`
<!-- <h1>Localize
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

LOCALIZE returns the node coordinates and id array of element

<!-- <div class="box"><strong>LOCALIZE returns the node coordinates and id array of element</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [xyz,id] = Localize (Model,el)` 
## <a name="_description"></a>Description

<pre class="comment">LOCALIZE returns the node coordinates and id array of element
  [XYZ,ID] = LOCALIZE (MODEL,EL)
  the function returns the node coordinates XYZ and the id array ID
  of the element with number EL for the structural model specified in data structure MODEL</pre>
<!-- <div class="fragment"><pre class="comment">LOCALIZE returns the node coordinates and id array of element
  [XYZ,ID] = LOCALIZE (MODEL,EL)
  the function returns the node coordinates XYZ and the id array ID
  of the element with number EL for the structural model specified in data structure MODEL</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="../../latest/Analysis_Functions/Static/Event2Event_NLAnalysis.md" class="code" title="function [lamdah,Qh,Ufh,Vph,Iph] = Event2Event_NLAnalysis (opt,Model,ElemData,Loading,ConvPar)">Event2Event_NLAnalysis</a>	EVENT2EVENT_NLANALYSIS event-to-event incremental analysis with linear or P-DELTA geometry</li><li><a href="../../latest/Analysis_Functions/Static/PlasticAnalysis.md" class="code" title="function [lamdac,Qc,DUf,DVpl] = PlasticAnalysis (Model,ElemData,Loading,LPOpt)">PlasticAnalysis</a>	PLASTICANALYSIS collapse load factor, basic forces, and collapse mechanism by plastic analysis</li><li><a href="A_matrix.md" class="code" title="function A = A_matrix (Model)">A_matrix</a>	A_MATRIX kinematic matrix of structural model with 2d/3d truss and 2d frame elements</li><li><a href="Aj_matrix.md" class="code" title="function Aj = Aj_matrix (Model)">Aj_matrix</a>	AJ_MATRIX kinematic matrix of structural model with 2d/3d truss and 2d frame elements</li><li><a href="B_matrix.md" class="code" title="function B = B_matrix (Model)">B_matrix</a>	B_MATRIX equilibrium matrix of structural model with 2d/3d truss and 2d frame elements</li><li><a href="Create_PwForces.md" class="code" title="function Pw = Create_PwForces (Model,ElemData)">Create_PwForces</a>	CREATE_PWFORCES set up equivalent nodal forces due to uniform element loading w</li><li><a href="Fs_matrix.md" class="code" title="function Fs = Fs_matrix (Model,ElemData,Roption)">Fs_matrix</a>	FS_MATRIX block diagonal matrix of element flexibity matrices for structural model</li><li><a href="Ks_matrix.md" class="code" title="function Ks = Ks_matrix (Model,ElemData)">Ks_matrix</a>	KS_MATRIX block diagonal matrix of basic element stiffness matrices for structural model</li><li><a href="Q0_vector.md" class="code" title="function Q0 = Q0_vector (Model,ElemData)">Q0_vector</a>	Q0_VECTOR initial (fixed-end) force vector for structural model</li><li><a href="Structure.md" class="code" title="function Resp = Structure (action,Model,ElemData,State,ElemList)">Structure</a>	STRUCTURE performs requested action on group of elements</li><li><a href="V0_vector.md" class="code" title="function V0 = V0_vector (Model,ElemData,Roption)">V0_vector</a>	V0_VECTOR initial element deformation vector for the structural model</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->