---
title: "kg_Truss"
id: "kg_Truss"
description: "KG_TRUSS geometric stiffness matrix for 2d/3d 2-node truss element for different options"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">Element_Library</a> &gt; 
<!-- kg_Truss.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Element_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `kg_Truss`



## <a name="_name"></a>Purpose


KG_TRUSS geometric stiffness matrix for 2d/3d 2-node truss element for different options

<!-- <div class="box"><strong>KG_TRUSS geometric stiffness matrix for 2d/3d 2-node truss element for different options</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function kg = kg_Truss (option,xyz,u,q)` 

## Description


<pre class="comment">KG_TRUSS geometric stiffness matrix for 2d/3d 2-node truss element for different options
  KG = KG_TRUSS (OPTION,XYZ,U,Q)
  the function determines the geometric stiffness matrix KG of a 2-node 2d/3d truss element
  with end coordinates in array XYZ (node i corresponds to first column and node j to second);
  the geometric stiffness matrix depends on the node displacement values in array U (ndmx2)
  in the global reference system and on the basic force vector Q;
  OPTION is a character variable with one of three values:
  'linear','PDelta' and 'corotational' for linear, P-Delta and corotational geometry, resp.</pre>
<!-- <div class="fragment"><pre class="comment">KG_TRUSS geometric stiffness matrix for 2d/3d 2-node truss element for different options
  KG = KG_TRUSS (OPTION,XYZ,U,Q)
  the function determines the geometric stiffness matrix KG of a 2-node 2d/3d truss element
  with end coordinates in array XYZ (node i corresponds to first column and node j to second);
  the geometric stiffness matrix depends on the node displacement values in array U (ndmx2)
  in the global reference system and on the basic force vector Q;
  OPTION is a character variable with one of three values:
  'linear','PDelta' and 'corotational' for linear, P-Delta and corotational geometry, resp.</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="InelTruss.md" class="code" title="function ElemResp = InelTruss (action,el_no,xyz,ElemData,ElemState)">InelTruss</a>	INELTRUSS 2d/3d inelastic truss element under linear or nonlinear geometry</li><li><a href="LETruss.md" class="code" title="function ElemResp = LETruss (action,el_no,xyz,ElemData,ElemState)">LETruss</a>	LETRUSS 2d/3d linear truss element under linear or nonlinear geometry</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->