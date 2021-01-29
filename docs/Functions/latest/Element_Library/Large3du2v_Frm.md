
<!-- <a name="_top"></a>
<div><a href="../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="_index.md">Element_Library</a> &gt; Large3du2v_Frm.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../_index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Element_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Large3du2v_Frm`
<!-- <h1>Large3du2v_Frm
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

LARGE3DU2V_FRM determine 3d frame element deformations from end displacements

<!-- <div class="box"><strong>LARGE3DU2V_FRM determine 3d frame element deformations from end displacements</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [v,vthetaI,vthetaJ] = Large3du2v_Frm (xyz,GeomData,u)` 
## <a name="_description"></a>Description

<pre class="comment">LARGE3DU2V_FRM determine 3d frame element deformations from end displacements
  [V,VTHETAI,VTHETAJ] = LARGE3DU2V_FRM(XYZ,GEOMDATA,U)
  the function determines the deformations V and
  the relative pseudo-rotation vectors VTHETAI and VTHETAJ at nodes I and J
  of a 2-node, 3d frame element with end node coordinates XYZ
  under large end node displacements U; the data structure GEOMDATA carries
  information about the joint offsets for the element</pre>
<!-- <div class="fragment"><pre class="comment">LARGE3DU2V_FRM determine 3d frame element deformations from end displacements
  [V,VTHETAI,VTHETAJ] = LARGE3DU2V_FRM(XYZ,GEOMDATA,U)
  the function determines the deformations V and
  the relative pseudo-rotation vectors VTHETAI and VTHETAJ at nodes I and J
  of a 2-node, 3d frame element with end node coordinates XYZ
  under large end node displacements U; the data structure GEOMDATA carries
  information about the joint offsets for the element</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="DefGeom_3dFrm" class="code" title="function [L,T] = DefGeom_3dFrm (xyz,GeomData,u)">DefGeom_3dFrm</a>	DEFGEOM_3dFRM determines current length and corotational triad of 2-node, 3d frame element</li></ul>
This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="GeomTran_3dFrm.md" class="code" title="function [ag,bg,ab,v,Dv,DDv] = GeomTran_3dFrm (option,xyz,GeomData,u,Du,DDu)">GeomTran_3dFrm</a>	GEOMTRAN_3dFRM kinematic matrices and deformations for a 2-node 3d frame element</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->