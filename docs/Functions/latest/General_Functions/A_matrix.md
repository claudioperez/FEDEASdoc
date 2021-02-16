
<!-- <a name="_top"></a>
<div><a href="../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="_index.md">General_Functions</a> &gt; A_matrix.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../_index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\General_Functions&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `A_matrix`
<!-- <h1>A_matrix
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

A_MATRIX kinematic matrix of structural model with 2d/3d truss and 2d frame elements

<!-- <div class="box"><strong>A_MATRIX kinematic matrix of structural model with 2d/3d truss and 2d frame elements</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function A = A_matrix (Model)` 
## <a name="_description"></a>Description

<pre class="comment">A_MATRIX kinematic matrix of structural model with 2d/3d truss and 2d frame elements
  A = A_MATRIX (MODEL)
  the function forms the kinematic matrix A for all degrees of freedom (DOFs) and
  all element deformations of the structural model specified in data structure MODEL; 
  this version is limited to 2d/3d truss and 2d frame elements</pre>
<!-- <div class="fragment"><pre class="comment">A_MATRIX kinematic matrix of structural model with 2d/3d truss and 2d frame elements
  A = A_MATRIX (MODEL)
  the function forms the kinematic matrix A for all degrees of freedom (DOFs) and
  all element deformations of the structural model specified in data structure MODEL; 
  this version is limited to 2d/3d truss and 2d frame elements</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="Localize" class="code" title="function [xyz,id] = Localize (Model,el)">Localize</a>	LOCALIZE returns the node coordinates and id array of element</li></ul>
This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="../../latest/Analysis_Functions/Static/Event2Event_NLAnalysis.md" class="code" title="function [lamdah,Qh,Ufh,Vph,Iph] = Event2Event_NLAnalysis (opt,Model,ElemData,Loading,ConvPar)">Event2Event_NLAnalysis</a>	EVENT2EVENT_NLANALYSIS event-to-event incremental analysis with linear or P-DELTA geometry</li><li><a href="../../latest/Analysis_Functions/Static/PlasticAnalysis.md" class="code" title="function [lamdac,Qc,DUf,DVpl] = PlasticAnalysis (Model,ElemData,Loading,LPOpt)">PlasticAnalysis</a>	PLASTICANALYSIS collapse load factor, basic forces, and collapse mechanism by plastic analysis</li><li><a href="../../latest/Solution_Scripts/S_DisplMethod.md" class="code" title="">S_DisplMethod</a>	% S_DISPLMETHOD script for displacement method of structural analysis</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->