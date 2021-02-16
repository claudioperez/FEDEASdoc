---
title: "kg_2dFrm"
id: "kg_2dFrm"
description: "KG_2dFRM geometric stiffness matrix for 2-node 2d frame element for different options"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">Element_Library</a> &gt; 
<!-- kg_2dFrm.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Element_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `kg_2dFrm`



## <a name="_name"></a>Purpose


KG_2dFRM geometric stiffness matrix for 2-node 2d frame element for different options

<!-- <div class="box"><strong>KG_2dFRM geometric stiffness matrix for 2-node 2d frame element for different options</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function kg = kg_2dFrm (option,xyz,u,q)` 

## Description


<pre class="comment">KG_2dFRM geometric stiffness matrix for 2-node 2d frame element for different options
  KG = KG_2dFRM (OPTION,XYZ,U,Q)
  the function determines the geometric stiffness matrix KG of a 2-node 2d frame element
  with end coordinates in array XYZ (node i corresponds to first column and node j to second);
  the geometric stiffness matrix depends on the node displacement values in array U (ndfx2)
  in the global reference system and on the basic force vector Q;
  OPTION is a character variable with one of three values:
  'linear','PDelta' and 'corotational' for linear, P-Delta and corotational geometry, resp.</pre>
<!-- <div class="fragment"><pre class="comment">KG_2dFRM geometric stiffness matrix for 2-node 2d frame element for different options
  KG = KG_2dFRM (OPTION,XYZ,U,Q)
  the function determines the geometric stiffness matrix KG of a 2-node 2d frame element
  with end coordinates in array XYZ (node i corresponds to first column and node j to second);
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
<li><a href="Dinel2dFrm_EBwDF.md" class="code" title="function ElemResp = Dinel2dFrm_EBwDF (action,el_no,xyz,ElemData,ElemState)">Dinel2dFrm_EBwDF</a>	DINEL2dFRM_EBwDF 2d-frame element with distributed inelasticity (displacement formulation)</li><li><a href="Dinel2dFrm_EBwFF.md" class="code" title="function ElemResp = Dinel2dFrm_EBwFF (action,el_no,xyz,ElemData,ElemState)">Dinel2dFrm_EBwFF</a>	DINEL2dFRM_EBwFF 2d-frame element with distributed inelasticity (force formulation)</li><li><a href="Inel2dFrm.md" class="code" title="function ElemResp = Inel2dFrm (action,el_no,xyz,ElemData,ElemState)">Inel2dFrm</a>	INEL2dFRM inelastic 2d frame element with different basic element types</li><li><a href="LE2dFrm.md" class="code" title="function ElemResp = LE2dFrm (action,el_no,xyz,ElemData,ElemState)">LE2dFrm</a>	LE2dFRM 2d LE frame element under linear or nonlinear geometry</li><li><a href="LE2dFrm_wPdelta.md" class="code" title="function ElemResp = LE2dFrm_wPdelta (action,el_no,xyz,ElemData,ElemState)">LE2dFrm_wPdelta</a>	LE2dFRM 2d linear elastic frame element with P-delta effect under linear or nonlinear geometry</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->