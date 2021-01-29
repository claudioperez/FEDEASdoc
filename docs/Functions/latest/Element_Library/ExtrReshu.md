
<!-- <a name="_top"></a>
<div><a href="../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="_index.md">Element_Library</a> &gt; ExtrReshu.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../_index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Element_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `ExtrReshu`
<!-- <h1>ExtrReshu
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

EXTRRESHU extracts displacements and increments from State and reshapes into array

<!-- <div class="box"><strong>EXTRRESHU extracts displacements and increments from State and reshapes into array</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [u,Du,DDu] = ExtrReshu (State,ndf,nen)` 
## <a name="_description"></a>Description

<pre class="comment">EXTRRESHU extracts displacements and increments from State and reshapes into array
 [U,DU,DDU] = EXTRRESHU (STATE,NDF,NEN)
  the function extracts the displacements and their increments from State
  and reshapes these into an NDF x NEN array,
  where NDF is no of dofs/node and NEN number of end nodes for element</pre>
<!-- <div class="fragment"><pre class="comment">EXTRRESHU extracts displacements and increments from State and reshapes into array
 [U,DU,DDU] = EXTRRESHU (STATE,NDF,NEN)
  the function extracts the displacements and their increments from State
  and reshapes these into an NDF x NEN array,
  where NDF is no of dofs/node and NEN number of end nodes for element</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="Dinel2dFrm_EBwDF.md" class="code" title="function ElemResp = Dinel2dFrm_EBwDF (action,el_no,xyz,ElemData,ElemState)">Dinel2dFrm_EBwDF</a>	DINEL2dFRM_EBwDF 2d-frame element with distributed inelasticity (displacement formulation)</li><li><a href="Dinel2dFrm_EBwFF.md" class="code" title="function ElemResp = Dinel2dFrm_EBwFF (action,el_no,xyz,ElemData,ElemState)">Dinel2dFrm_EBwFF</a>	DINEL2dFRM_EBwFF 2d-frame element with distributed inelasticity (force formulation)</li><li><a href="Inel2dFrm.md" class="code" title="function ElemResp = Inel2dFrm (action,el_no,xyz,ElemData,ElemState)">Inel2dFrm</a>	INEL2dFRM inelastic 2d frame element with different basic element types</li><li><a href="InelTruss.md" class="code" title="function ElemResp = InelTruss (action,el_no,xyz,ElemData,ElemState)">InelTruss</a>	INELTRUSS 2d/3d inelastic truss element under linear or nonlinear geometry</li><li><a href="LE2dFrm.md" class="code" title="function ElemResp = LE2dFrm (action,el_no,xyz,ElemData,ElemState)">LE2dFrm</a>	LE2dFRM 2d LE frame element under linear or nonlinear geometry</li><li><a href="LE2dFrm_wPdelta.md" class="code" title="function ElemResp = LE2dFrm_wPdelta (action,el_no,xyz,ElemData,ElemState)">LE2dFrm_wPdelta</a>	LE2dFRM 2d linear elastic frame element with P-delta effect under linear or nonlinear geometry</li><li><a href="LE3dFrm.md" class="code" title="function ElemResp = LE3dFrm (action,el_no,xyz,ElemData,ElemState)">LE3dFrm</a>	LE3dFRM 3d linear frame element under linear or nonlinear geometry</li><li><a href="LETruss.md" class="code" title="function ElemResp = LETruss (action,el_no,xyz,ElemData,ElemState)">LETruss</a>	LETRUSS 2d/3d linear truss element under linear or nonlinear geometry</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->