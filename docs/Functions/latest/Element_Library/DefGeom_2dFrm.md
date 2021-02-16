
<!-- <a name="_top"></a>
<div><a href="../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="_index.md">Element_Library</a> &gt; DefGeom_2dFrm.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../_index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Element_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `DefGeom_2dFrm`
<!-- <h1>DefGeom_2dFrm
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

DEFGEOM_2dFRM determines current length and corotational diad of 2-node, 2d frame element

<!-- <div class="box"><strong>DEFGEOM_2dFRM determines current length and corotational diad of 2-node, 2d frame element</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [L,T] = DefGeom_2dFrm (xyz)` 
## <a name="_description"></a>Description

<pre class="comment">DEFGEOM_2dFRM determines current length and corotational diad of 2-node, 2d frame element
  [L,T] = DEFGEOM_2dFRM (XYZ);
  the function determines the length L and the corotational diad T
  of a 2d frame element in the current configuration
  from the end node coordinates XYZ (column 1 for node i, column 2 for node j);
  the corotational diad is given in matrix T whose columns correspond to axes x and y, resp.</pre>
<!-- <div class="fragment"><pre class="comment">DEFGEOM_2dFRM determines current length and corotational diad of 2-node, 2d frame element
  [L,T] = DEFGEOM_2dFRM (XYZ);
  the function determines the length L and the corotational diad T
  of a 2d frame element in the current configuration
  from the end node coordinates XYZ (column 1 for node i, column 2 for node j);
  the corotational diad is given in matrix T whose columns correspond to axes x and y, resp.</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->