
<!-- <a name="_top"></a>
<div><a href="../../index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="index.md">Introspection</a> &gt; Fs_matrix.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for latest\Introspection&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Fs_matrix`
<!-- <h1>Fs_matrix
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

FS_MATRIX block diagonal matrix of element flexibity matrices for structural model

<!-- <div class="box"><strong>FS_MATRIX block diagonal matrix of element flexibity matrices for structural model</strong></div> -->

## <a name="_synopsis"></a>Syntax

`function Fs = Fs_matrix (Model,ElemData,Roption)` 
## <a name="_description"></a>Description

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
<li><a href="ElmLenOr" class="code" title="function [L,dcx] = ElmLenOr (xyz)">ElmLenOr</a>	ELMLENOR element length and x-axis orientation (direction cosines)</li><li><a href="Localize" class="code" title="function [xyz,id] = Localize (Model,el)">Localize</a>	LOCALIZE returns the node coordinates and id array of element</li></ul>
This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Sat 19-Dec-2020 21:58:36 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->