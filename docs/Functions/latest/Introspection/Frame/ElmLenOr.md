
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Introspection</a> &gt; <a href="_index.md">Frame</a> &gt; ElmLenOr.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Introspection\Frame&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `ElmLenOr`
<!-- <h1>ElmLenOr
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

ELMLENOR element length and x-axis orientation (direction cosines)

<!-- <div class="box"><strong>ELMLENOR element length and x-axis orientation (direction cosines)</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [L,dcx] = ElmLenOr (xyz)` 
## <a name="_description"></a>Description

<pre class="comment">ELMLENOR element length and x-axis orientation (direction cosines)
  [L,DCX] = ELMLENOR (XYZ);
  the function determines the length L and x-axis orientation of an element
  with end node coordinates XYZ (column 1 for node i, column 2 for node j);
  the direction cosines for the element x-axis are reported in vector DCX</pre>
<!-- <div class="fragment"><pre class="comment">ELMLENOR element length and x-axis orientation (direction cosines)
  [L,DCX] = ELMLENOR (XYZ);
  the function determines the length L and x-axis orientation of an element
  with end node coordinates XYZ (column 1 for node i, column 2 for node j);
  the direction cosines for the element x-axis are reported in vector DCX</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="../../../latest/Introspection/Structure/A_matrix.md" class="code" title="function A = A_matrix (Model)">A_matrix</a>	A_MATRIX kinematic matrix of structural model with 2d/3d truss and 2d frame elements</li><li><a href="../../../latest/Introspection/Structure/B_matrix.md" class="code" title="function B = B_matrix (Model)">B_matrix</a>	B_MATRIX equilibrium matrix of structural model with 2d/3d truss and 2d frame elements</li><li><a href="../../../latest/Introspection/Structure/Fs_matrix.md" class="code" title="function Fs = Fs_matrix (Model,ElemData,Roption)">Fs_matrix</a>	FS_MATRIX block diagonal matrix of element flexibity matrices for structural model</li><li><a href="../../../latest/Introspection/Structure/Ks_matrix.md" class="code" title="function Ks = Ks_matrix (Model,ElemData)">Ks_matrix</a>	KS_MATRIX block diagonal matrix of basic element stiffness matrices for structural model</li><li><a href="../../../latest/Introspection/Structure/Q0_vector.md" class="code" title="function Q0 = Q0_vector (Model,ElemData)">Q0_vector</a>	Q0_VECTOR initial (fixed-end) force vector for structural model</li><li><a href="../../../latest/Introspection/Structure/V0_vector.md" class="code" title="function V0 = V0_vector (Model,ElemData,Roption)">V0_vector</a>	V0_VECTOR initial element deformation vector for the structural model</li><li><a href="../../../latest/Modeling_Library/Frame/InelTruss.md" class="code" title="function ElemResp = InelTruss (action,el_no,xyz,ElemData,ElemState)">InelTruss</a>	INELTRUSS 2d/3d inelastic truss element under linear or nonlinear geometry</li><li><a href="../../../latest/Modeling_Library/Frame/LE2dFrm.md" class="code" title="function ElemResp = LE2dFrm (action,el_no,xyz,ElemData,ElemState)">LE2dFrm</a>	LE2dFRM 2d LE frame element under linear or nonlinear geometry</li><li><a href="../../../latest/Utilities/Plotting/Draw_Arrow.md" class="code" title="function varargout = Draw_Arrow (Astr,Aend,Aln,PlotOpt)">Draw_Arrow</a>	DRAW_ARROW draws 2d or 3d arrow</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Sun 20-Dec-2020 19:28:50 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->