---
title: "H_index"
id: "H_index"
description: "H_INDEX cell array of indices into structure arrays for continuous element deformations"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href="#">Utility_Functions</a> &gt; <a href=".autoindex.md">General</a> &gt; 
<!-- H_index.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../.autoindex.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Utility_Functions\General&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `H_index`



## <a name="_name"></a>Purpose


H_INDEX cell array of indices into structure arrays for continuous element deformations

<!-- <div class="box"><strong>H_INDEX cell array of indices into structure arrays for continuous element deformations</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function iced = H_index (Model,ElemData)` 

## Description


<pre class="comment">H_INDEX cell array of indices into structure arrays for continuous element deformations
  ICED = H_INDEX (MODEL,ELEMDATA)
  the function sets up the cell array ICED of indices for continuous element deformations
  based on release information for elements of the structural model in data structure MODEL;
  the location of element releases is specified in field RELEASE of cell array ELEMDATA
  ELEMDATA{2}.RELEASE = [0;1;0] :   a flexural release is present at end i of element 2
  ELEMDATA{3}.RELEASE = [1;0;1] : an axial and a flexural release at end j of element 3
  the function supports only truss and 2d frame elements at present</pre>
<!-- <div class="fragment"><pre class="comment">H_INDEX cell array of indices into structure arrays for continuous element deformations
  ICED = H_INDEX (MODEL,ELEMDATA)
  the function sets up the cell array ICED of indices for continuous element deformations
  based on release information for elements of the structural model in data structure MODEL;
  the location of element releases is specified in field RELEASE of cell array ELEMDATA
  ELEMDATA{2}.RELEASE = [0;1;0] :   a flexural release is present at end i of element 2
  ELEMDATA{3}.RELEASE = [1;0;1] : an axial and a flexural release at end j of element 3
  the function supports only truss and 2d frame elements at present</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>

This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="../../../latest/Solution_Scripts/S_DisplMethod.md" class="code" title="">S_DisplMethod</a>	% S_DISPLMETHOD script for displacement method of structural analysis</li><li><a href="../../../latest/Solution_Scripts/S_ForceMethod.md" class="code" title="">S_ForceMethod</a>	% S_FORCEMETHOD script for force method of structural analysis</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->