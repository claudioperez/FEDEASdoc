---
title: "ElementLoading"
id: "ElementLoading"
description: "ELEMENTLOADING determines current distributed element load value"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">Element_Library</a> &gt; 
<!-- ElementLoading.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Element_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `ElementLoading`



## <a name="_name"></a>Purpose


ELEMENTLOADING determines current distributed element load value

<!-- <div class="box"><strong>ELEMENTLOADING determines current distributed element load value</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function wC = ElementLoading (w0,lamda,LdId)` 

## Description


<pre class="comment">ELEMENTLOADING determines current distributed element load value
  WC = ELEMENTLOADING (w0,LAMDA,LDID);
  function determines the current distributed element load values as the product of the
  user specified reference values in vector W0 and the current load factor(s) in row vector
  LAMDA; the load history ID for distributed element loads is specified in row vector LDID</pre>
<!-- <div class="fragment"><pre class="comment">ELEMENTLOADING determines current distributed element load value
  WC = ELEMENTLOADING (w0,LAMDA,LDID);
  function determines the current distributed element load values as the product of the
  user specified reference values in vector W0 and the current load factor(s) in row vector
  LAMDA; the load history ID for distributed element loads is specified in row vector LDID</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="BInel2dFrm_wEPLHM.md" class="code" title="function BElemResp = BInel2dFrm_wEPLHM (action,L,BElemData,BElemState)">BInel2dFrm_wEPLHM</a>	BINELP2dFRM_WEPLHM 2d elasto-plastic, linear hardening basic frame element with hinge offsets</li><li><a href="BInel2dFrm_wEPLHNMYS.md" class="code" title="function BElemResp = BInel2dFrm_wEPLHNMYS (action,L,BElemData,BElemState)">BInel2dFrm_wEPLHNMYS</a>	BINELP2dFRM_WEPLHNMYS 2d elasto-plastic, linear hardening basic frame element</li><li><a href="Dinel2dFrm_EBwDF.md" class="code" title="function ElemResp = Dinel2dFrm_EBwDF (action,el_no,xyz,ElemData,ElemState)">Dinel2dFrm_EBwDF</a>	DINEL2dFRM_EBwDF 2d-frame element with distributed inelasticity (displacement formulation)</li><li><a href="Dinel2dFrm_EBwFF.md" class="code" title="function ElemResp = Dinel2dFrm_EBwFF (action,el_no,xyz,ElemData,ElemState)">Dinel2dFrm_EBwFF</a>	DINEL2dFRM_EBwFF 2d-frame element with distributed inelasticity (force formulation)</li><li><a href="Inel2dFrm.md" class="code" title="function ElemResp = Inel2dFrm (action,el_no,xyz,ElemData,ElemState)">Inel2dFrm</a>	INEL2dFRM inelastic 2d frame element with different basic element types</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->