
<!-- <a name="_top"></a>
<div><a href="../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="_index.md">Element_Library</a> &gt; GeomTran_Truss.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../_index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Element_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `GeomTran_Truss`
<!-- <h1>GeomTran_Truss
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

GEOMTRAN_TRUSS kinematic matrices and deformations for a 2-node truss element

<!-- <div class="box"><strong>GEOMTRAN_TRUSS kinematic matrices and deformations for a 2-node truss element</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [ag,bg,v,Dv,DDv] = GeomTran_Truss (option,xyz,u,Du,DDu)` 
## <a name="_description"></a>Description

<pre class="comment">GEOMTRAN_TRUSS kinematic matrices and deformations for a 2-node truss element
  [AG,BG,V,DV,DDV] = GEOMTRAN_TRUSS (NDF,XYZ,GEOMDATA,U,DU,DDU)
  the function determines the kinematic matrix AG from the global to the basic reference system,
  and the static matrix BG from the basic to the global reference system 
  as well as the element deformation vector V and its increments DV and DDV
  from the end displacement vector U and its increments DU and DDU
  for a 2-node truss element with end node coordinates XYZ and NDF dofs/node;
  OPTION is a character variable with one of three values:
  'linear','PDelta' and 'corotational' for linear, P-Delta and corotational geometry, resp.</pre>
<!-- <div class="fragment"><pre class="comment">GEOMTRAN_TRUSS kinematic matrices and deformations for a 2-node truss element
  [AG,BG,V,DV,DDV] = GEOMTRAN_TRUSS (NDF,XYZ,GEOMDATA,U,DU,DDU)
  the function determines the kinematic matrix AG from the global to the basic reference system,
  and the static matrix BG from the basic to the global reference system 
  as well as the element deformation vector V and its increments DV and DDV
  from the end displacement vector U and its increments DU and DDU
  for a 2-node truss element with end node coordinates XYZ and NDF dofs/node;
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




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->