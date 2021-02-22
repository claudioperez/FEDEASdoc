---
title: "DefGeom_2dFrm"
id: "DefGeom_2dFrm"
description: "DEFGEOM_2dFRM determines current length and corotational diad of 2-node, 2d frame element"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">Element_Library</a> &gt; 
<!-- DefGeom_2dFrm.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Element_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `DefGeom_2dFrm`



## <a name="_name"></a>Purpose


DEFGEOM_2dFRM determines current length and corotational diad of 2-node, 2d frame element

<!-- <div class="box"><strong>DEFGEOM_2dFRM determines current length and corotational diad of 2-node, 2d frame element</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [L,T] = DefGeom_2dFrm (xyz)` 

## Description


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




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->