---
title: "GeomTran_2dFrm"
id: "GeomTran_2dFrm"
description: "GEOMTRAN_2dFRM kinematic matrices and deformations for a 2-node 2d frame element"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">Element_Library</a> &gt; 
<!-- GeomTran_2dFrm.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Element_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `GeomTran_2dFrm`



## <a name="_name"></a>Purpose


GEOMTRAN_2dFRM kinematic matrices and deformations for a 2-node 2d frame element

<!-- <div class="box"><strong>GEOMTRAN_2dFRM kinematic matrices and deformations for a 2-node 2d frame element</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [ag,bg,ab,v,Dv,DDv] = GeomTran_2dFrm (option,xyz,GeomData,u,Du,DDu)` 

## Description


<pre class="comment">GEOMTRAN_2dFRM kinematic matrices and deformations for a 2-node 2d frame element
  [AG,BG,AB,V,DV,DDV] = GEOMTRAN_2dFRM (OPTION,XYZ,GEOMDATA,U,DU,DDU)
  the function determines the kinematic matrix AG from the global to the basic reference system,
  the static matrix BG from the basic to the global reference system, 
  and the kinematic matrix AB from the global to the local reference system
  as well as the element deformation vector V and its increments DV and DDV
  from the node displacement array U and its increments DU and DDU
  for a 2-node 2d frame element with end node coordinates XYZ;
  OPTION is a character variable with one of three values:
  'linear','PDelta' and 'corotational' for linear, P-Delta and corotational geometry, resp.
  GEOMDATA is a data structure with information about rigid joint offsets in field JNTOFF,
  (first column for node i, second column for node j)</pre>
<!-- <div class="fragment"><pre class="comment">GEOMTRAN_2dFRM kinematic matrices and deformations for a 2-node 2d frame element
  [AG,BG,AB,V,DV,DDV] = GEOMTRAN_2dFRM (OPTION,XYZ,GEOMDATA,U,DU,DDU)
  the function determines the kinematic matrix AG from the global to the basic reference system,
  the static matrix BG from the basic to the global reference system, 
  and the kinematic matrix AB from the global to the local reference system
  as well as the element deformation vector V and its increments DV and DDV
  from the node displacement array U and its increments DU and DDU
  for a 2-node 2d frame element with end node coordinates XYZ;
  OPTION is a character variable with one of three values:
  'linear','PDelta' and 'corotational' for linear, P-Delta and corotational geometry, resp.
  GEOMDATA is a data structure with information about rigid joint offsets in field JNTOFF,
  (first column for node i, second column for node j)</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="/Functions/Large2du2v_Frm" class="code" title="function v = Large2du2v_Frm (xyz,u)">Large2du2v_Frm</a>	LARGE2DU2V_FRM determine 2d frame element deformations from end displacements</li><li><a href="/Functions/TranJnt" class="code" title="function aj = TranJnt (JntOff)">TranJnt</a>	TRANJNT sets up transformation matrix for finite size joints</li></ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="Dinel2dFrm_EBwDF.md" class="code" title="function ElemResp = Dinel2dFrm_EBwDF (action,el_no,xyz,ElemData,ElemState)">Dinel2dFrm_EBwDF</a>	DINEL2dFRM_EBwDF 2d-frame element with distributed inelasticity (displacement formulation)</li><li><a href="Dinel2dFrm_EBwFF.md" class="code" title="function ElemResp = Dinel2dFrm_EBwFF (action,el_no,xyz,ElemData,ElemState)">Dinel2dFrm_EBwFF</a>	DINEL2dFRM_EBwFF 2d-frame element with distributed inelasticity (force formulation)</li><li><a href="Inel2dFrm.md" class="code" title="function ElemResp = Inel2dFrm (action,el_no,xyz,ElemData,ElemState)">Inel2dFrm</a>	INEL2dFRM inelastic 2d frame element with different basic element types</li><li><a href="LE2dFrm.md" class="code" title="function ElemResp = LE2dFrm (action,el_no,xyz,ElemData,ElemState)">LE2dFrm</a>	LE2dFRM 2d LE frame element under linear or nonlinear geometry</li><li><a href="LE2dFrm_wPdelta.md" class="code" title="function ElemResp = LE2dFrm_wPdelta (action,el_no,xyz,ElemData,ElemState)">LE2dFrm_wPdelta</a>	LE2dFRM 2d linear elastic frame element with P-delta effect under linear or nonlinear geometry</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->