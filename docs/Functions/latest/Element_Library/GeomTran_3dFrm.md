
<!-- <a name="_top"></a>
<div><a href="../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="_index.md">Element_Library</a> &gt; GeomTran_3dFrm.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../_index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Element_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `GeomTran_3dFrm`
<!-- <h1>GeomTran_3dFrm
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

GEOMTRAN_3dFRM kinematic matrices and deformations for a 2-node 3d frame element

<!-- <div class="box"><strong>GEOMTRAN_3dFRM kinematic matrices and deformations for a 2-node 3d frame element</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [ag,bg,ab,v,Dv,DDv] = GeomTran_3dFrm (option,xyz,GeomData,u,Du,DDu)` 
## <a name="_description"></a>Description

<pre class="comment">GEOMTRAN_3dFRM kinematic matrices and deformations for a 2-node 3d frame element
  [AG,BG,AB,V,DV,DDV] = GEOMTRAN_3dFRM (OPTION,XYZ,GEOMDATA,U,DU,DDU)
  the function determines the kinematic matrix AG from the global to the basic reference system,
  the static matrix BG from the basic to the global reference system, 
  and the kinematic matrix AB from the global to the local reference system
  as well as the element deformation vector V and its increments DV and DDV
  from the node displacement array U and its increments DU and DDU
  for a 2-node 3d frame element with end node coordinates XYZ;
  OPTION is a character variable with one of three values:
  'linear','PDelta' and 'corotational' for linear, P-Delta and corotational geometry, resp.
  GEOMDATA is a data structure with information about rigid joint offsets in field JNTOFF
  (first column for node i, second column for node j),
  and orientation (direction cosines) of the local y-axis in vector YORNT</pre>
<!-- <div class="fragment"><pre class="comment">GEOMTRAN_3dFRM kinematic matrices and deformations for a 2-node 3d frame element
  [AG,BG,AB,V,DV,DDV] = GEOMTRAN_3dFRM (OPTION,XYZ,GEOMDATA,U,DU,DDU)
  the function determines the kinematic matrix AG from the global to the basic reference system,
  the static matrix BG from the basic to the global reference system, 
  and the kinematic matrix AB from the global to the local reference system
  as well as the element deformation vector V and its increments DV and DDV
  from the node displacement array U and its increments DU and DDU
  for a 2-node 3d frame element with end node coordinates XYZ;
  OPTION is a character variable with one of three values:
  'linear','PDelta' and 'corotational' for linear, P-Delta and corotational geometry, resp.
  GEOMDATA is a data structure with information about rigid joint offsets in field JNTOFF
  (first column for node i, second column for node j),
  and orientation (direction cosines) of the local y-axis in vector YORNT</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="DefGeom_3dFrm" class="code" title="function [L,T] = DefGeom_3dFrm (xyz,GeomData,u)">DefGeom_3dFrm</a>	DEFGEOM_3dFRM determines current length and corotational triad of 2-node, 3d frame element</li><li><a href="Large3du2v_Frm" class="code" title="function [v,vthetaI,vthetaJ] = Large3du2v_Frm (xyz,GeomData,u)">Large3du2v_Frm</a>	LARGE3DU2V_FRM determine 3d frame element deformations from end displacements</li><li><a href="TranJnt" class="code" title="function aj = TranJnt (JntOff)">TranJnt</a>	TRANJNT sets up transformation matrix for finite size joints</li></ul>
This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="LE3dFrm.md" class="code" title="function ElemResp = LE3dFrm (action,el_no,xyz,ElemData,ElemState)">LE3dFrm</a>	LE3dFRM 3d linear frame element under linear or nonlinear geometry</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->