
<!-- <a name="_top"></a>
<div><a href="../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="_index.md">Element_Library</a> &gt; TranJnt.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../_index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Element_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `TranJnt`
<!-- <h1>TranJnt
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

TRANJNT sets up transformation matrix for finite size joints

<!-- <div class="box"><strong>TRANJNT sets up transformation matrix for finite size joints</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function aj = TranJnt (JntOff)` 
## <a name="_description"></a>Description

<pre class="comment">TRANJNT sets up transformation matrix for finite size joints
  AJ = TRANJNT (JNTOFF)
  the function sets up the transformation matrix AJ for finite size joints of 2d and 3d frame elements;
  the rigid joint offsets at the element ends are specified in array JNTOFF
  with the first column corresponding to node i and the second column to node j</pre>
<!-- <div class="fragment"><pre class="comment">TRANJNT sets up transformation matrix for finite size joints
  AJ = TRANJNT (JNTOFF)
  the function sets up the transformation matrix AJ for finite size joints of 2d and 3d frame elements;
  the rigid joint offsets at the element ends are specified in array JNTOFF
  with the first column corresponding to node i and the second column to node j</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="GeomTran_2dFrm.md" class="code" title="function [ag,bg,ab,v,Dv,DDv] = GeomTran_2dFrm (option,xyz,GeomData,u,Du,DDu)">GeomTran_2dFrm</a>	GEOMTRAN_2dFRM kinematic matrices and deformations for a 2-node 2d frame element</li><li><a href="GeomTran_3dFrm.md" class="code" title="function [ag,bg,ab,v,Dv,DDv] = GeomTran_3dFrm (option,xyz,GeomData,u,Du,DDu)">GeomTran_3dFrm</a>	GEOMTRAN_3dFRM kinematic matrices and deformations for a 2-node 3d frame element</li><li><a href="../../latest/General_Functions/Aj_matrix.md" class="code" title="function Aj = Aj_matrix (Model)">Aj_matrix</a>	AJ_MATRIX kinematic matrix of structural model with 2d/3d truss and 2d frame elements</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->