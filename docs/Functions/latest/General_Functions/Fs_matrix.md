---
title: "Fs_matrix"
id: "Fs_matrix"
description: "FS_MATRIX block diagonal matrix of element flexibity matrices for structural model"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">General_Functions</a> &gt; 
<!-- Fs_matrix.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\General_Functions&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Fs_matrix`



## <a name="_name"></a>Purpose


FS_MATRIX block diagonal matrix of element flexibity matrices for structural model

<!-- <div class="box"><strong>FS_MATRIX block diagonal matrix of element flexibity matrices for structural model</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function Fs = Fs_matrix (Model,ElemData,Roption)` 

## Description


<pre class="comment">FS_MATRIX block diagonal matrix of element flexibity matrices for structural model
  FS = FS_MATRIX (MODEL,ELEMDATA,ROPTION)
  the function sets up the block diagonal matrix of element flexibility matrices FS
  for the structural model specified in data structure MODEL with element property
  information in cell array ELEMDATA;
  if ROPTION=0 the element release information is not accounted for in setting up Fs (default=1)</pre>
<!-- <div class="fragment"><pre class="comment">FS_MATRIX block diagonal matrix of element flexibity matrices for structural model
  FS = FS_MATRIX (MODEL,ELEMDATA,ROPTION)
  the function sets up the block diagonal matrix of element flexibility matrices FS
  for the structural model specified in data structure MODEL with element property
  information in cell array ELEMDATA;
  if ROPTION=0 the element release information is not accounted for in setting up Fs (default=1)</pre></div> -->

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