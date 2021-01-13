
<!-- <a name="_top"></a>
<div><a href="../../index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="index.md">Introspection</a> &gt; Localize.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for latest\Introspection&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Localize`
<!-- <h1>Localize
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

LOCALIZE returns the node coordinates and id array of element

<!-- <div class="box"><strong>LOCALIZE returns the node coordinates and id array of element</strong></div> -->

## <a name="_synopsis"></a>Syntax

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
<li><a href="A_matrix.md" class="code" title="function A = A_matrix (Model)">A_matrix</a>	A_MATRIX kinematic matrix of structural model with 2d/3d truss and 2d frame elements</li><li><a href="B_matrix.md" class="code" title="function B = B_matrix (Model)">B_matrix</a>	B_MATRIX equilibrium matrix of structural model with 2d/3d truss and 2d frame elements</li><li><a href="Fs_matrix.md" class="code" title="function Fs = Fs_matrix (Model,ElemData,Roption)">Fs_matrix</a>	FS_MATRIX block diagonal matrix of element flexibity matrices for structural model</li><li><a href="Ks_matrix.md" class="code" title="function Ks = Ks_matrix (Model,ElemData)">Ks_matrix</a>	KS_MATRIX block diagonal matrix of basic element stiffness matrices for structural model</li><li><a href="Q0_vector.md" class="code" title="function Q0 = Q0_vector (Model,ElemData)">Q0_vector</a>	Q0_VECTOR initial (fixed-end) force vector for structural model</li><li><a href="V0_vector.md" class="code" title="function V0 = V0_vector (Model,ElemData,Roption)">V0_vector</a>	V0_VECTOR initial element deformation vector for the structural model</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Sat 19-Dec-2020 21:58:36 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->