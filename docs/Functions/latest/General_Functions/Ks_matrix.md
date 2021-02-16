
<!-- <a name="_top"></a>
<div><a href="../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="_index.md">General_Functions</a> &gt; Ks_matrix.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../_index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\General_Functions&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Ks_matrix`
<!-- <h1>Ks_matrix
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

KS_MATRIX block diagonal matrix of basic element stiffness matrices for structural model

<!-- <div class="box"><strong>KS_MATRIX block diagonal matrix of basic element stiffness matrices for structural model</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function Ks = Ks_matrix (Model,ElemData)` 
## <a name="_description"></a>Description

<pre class="comment">KS_MATRIX block diagonal matrix of basic element stiffness matrices for structural model
  KS = KS_MATRIX (MODEL,ELEMDATA)
  the function sets up the block diagonal matrix of basic element stiffness matrices KS
  for the structural model specified in data structure MODEL with element property
  information in cell array ELEMDATA</pre>
<!-- <div class="fragment"><pre class="comment">KS_MATRIX block diagonal matrix of basic element stiffness matrices for structural model
  KS = KS_MATRIX (MODEL,ELEMDATA)
  the function sets up the block diagonal matrix of basic element stiffness matrices KS
  for the structural model specified in data structure MODEL with element property
  information in cell array ELEMDATA</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="Localize" class="code" title="function [xyz,id] = Localize (Model,el)">Localize</a>	LOCALIZE returns the node coordinates and id array of element</li></ul>
This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="../../latest/Solution_Scripts/S_DisplMethod.md" class="code" title="">S_DisplMethod</a>	% S_DISPLMETHOD script for displacement method of structural analysis</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->