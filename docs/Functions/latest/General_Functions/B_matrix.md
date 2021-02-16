---
title: "B_matrix"
id: "B_matrix"
description: "B_MATRIX equilibrium matrix of structural model with 2d/3d truss and 2d frame elements"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">General_Functions</a> &gt; 
<!-- B_matrix.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\General_Functions&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `B_matrix`



## <a name="_name"></a>Purpose


B_MATRIX equilibrium matrix of structural model with 2d/3d truss and 2d frame elements

<!-- <div class="box"><strong>B_MATRIX equilibrium matrix of structural model with 2d/3d truss and 2d frame elements</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function B = B_matrix (Model)` 

## Description


<pre class="comment">B_MATRIX equilibrium matrix of structural model with 2d/3d truss and 2d frame elements
  B = B_MATRIX (MODEL)
  the function forms the equilibrium matrix B for all degrees of freedom (DOFs) and
  all basic forces of the structural model specified in data structure MODEL;
  this version is limited to 2d/3d truss and 2d frame elements</pre>
<!-- <div class="fragment"><pre class="comment">B_MATRIX equilibrium matrix of structural model with 2d/3d truss and 2d frame elements
  B = B_MATRIX (MODEL)
  the function forms the equilibrium matrix B for all degrees of freedom (DOFs) and
  all basic forces of the structural model specified in data structure MODEL;
  this version is limited to 2d/3d truss and 2d frame elements</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="/Functions/Localize" class="code" title="function [xyz,id] = Localize (Model,el)">Localize</a>	LOCALIZE returns the node coordinates and id array of element</li></ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="../../latest/Solution_Scripts/S_ForceMethod.md" class="code" title="">S_ForceMethod</a>	% S_FORCEMETHOD script for force method of structural analysis</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->