---
title: "kg_3dFrm"
id: "kg_3dFrm"
description: "KG_3dFRM geometric stiffness matrix for 2-node 3d frame element different options"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">Element_Library</a> &gt; 
<!-- kg_3dFrm.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Element_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `kg_3dFrm`



## <a name="_name"></a>Purpose


KG_3dFRM geometric stiffness matrix for 2-node 3d frame element different options

<!-- <div class="box"><strong>KG_3dFRM geometric stiffness matrix for 2-node 3d frame element different options</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function kg = kg_3dFrm (option,xyz,GeomData,u,q,ElLoad)` 

## Description


<pre class="comment">KG_3dFRM geometric stiffness matrix for 2-node 3d frame element different options
  KG = KG_3dFRM (OPTION,XYZ,GEOMDATA,U,Q,ELLOAD)
  the function determines the geometric stiffness matrix KG of a 2-node element with end
  coordinates in array XYZ (node i corresponds to first column and node j to second);
  the geometric stiffness matrix depends on the node displacement values in array U (ndfx2)
  in the global reference system and on the basic force vector Q;
  OPTION is a character variable with one of three values:
  'linear','PDelta' and 'corotational' for linear, P-Delta and corotational geometry, resp.</pre>
<!-- <div class="fragment"><pre class="comment">KG_3dFRM geometric stiffness matrix for 2-node 3d frame element different options
  KG = KG_3dFRM (OPTION,XYZ,GEOMDATA,U,Q,ELLOAD)
  the function determines the geometric stiffness matrix KG of a 2-node element with end
  coordinates in array XYZ (node i corresponds to first column and node j to second);
  the geometric stiffness matrix depends on the node displacement values in array U (ndfx2)
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
<li><a href="LE3dFrm.md" class="code" title="function ElemResp = LE3dFrm (action,el_no,xyz,ElemData,ElemState)">LE3dFrm</a>	LE3dFRM 3d linear frame element under linear or nonlinear geometry</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->