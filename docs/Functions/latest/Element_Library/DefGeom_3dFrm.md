
<!-- <a name="_top"></a>
<div><a href="../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="_index.md">Element_Library</a> &gt; DefGeom_3dFrm.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../_index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Element_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `DefGeom_3dFrm`
<!-- <h1>DefGeom_3dFrm
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

DEFGEOM_3dFRM determines current length and corotational triad of 2-node, 3d frame element

<!-- <div class="box"><strong>DEFGEOM_3dFRM determines current length and corotational triad of 2-node, 3d frame element</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [L,T] = DefGeom_3dFrm (xyz,GeomData,u)` 
## <a name="_description"></a>Description

<pre class="comment">DEFGEOM_3dFRM determines current length and corotational triad of 2-node, 3d frame element
  [L,T] = DEFGEOM_3dFRM (XYZ,GEOMDATA,U);
  the function determines the length L and corotational triad T
  of a 2-node, 3d frame element in the current configuration
  from the end node coordinates XYZ (column 1 for node i, column 2 for node j)
  and the end displacement vector U (optional);
  the corotational triad is given in matrix T whose columns correspond to axes x,y,z resp.</pre>
<!-- <div class="fragment"><pre class="comment">DEFGEOM_3dFRM determines current length and corotational triad of 2-node, 3d frame element
  [L,T] = DEFGEOM_3dFRM (XYZ,GEOMDATA,U);
  the function determines the length L and corotational triad T
  of a 2-node, 3d frame element in the current configuration
  from the end node coordinates XYZ (column 1 for node i, column 2 for node j)
  and the end displacement vector U (optional);
  the corotational triad is given in matrix T whose columns correspond to axes x,y,z resp.</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="GeomTran_3dFrm.md" class="code" title="function [ag,bg,ab,v,Dv,DDv] = GeomTran_3dFrm (option,xyz,GeomData,u,Du,DDu)">GeomTran_3dFrm</a>	GEOMTRAN_3dFRM kinematic matrices and deformations for a 2-node 3d frame element</li><li><a href="Large3du2v_Frm.md" class="code" title="function [v,vthetaI,vthetaJ] = Large3du2v_Frm (xyz,GeomData,u)">Large3du2v_Frm</a>	LARGE3DU2V_FRM determine 3d frame element deformations from end displacements</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->