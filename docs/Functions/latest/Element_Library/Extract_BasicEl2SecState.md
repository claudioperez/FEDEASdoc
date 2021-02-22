---
title: "Extract_BasicEl2SecState"
id: "Extract_BasicEl2SecState"
description: "EXTRACT_BASICEL2SECSTATE extract section state from basic element state"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">Element_Library</a> &gt; 
<!-- Extract_BasicEl2SecState.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Element_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Extract_BasicEl2SecState`



## <a name="_name"></a>Purpose


EXTRACT_BASICEL2SECSTATE extract section state from basic element state

<!-- <div class="box"><strong>EXTRACT_BASICEL2SECSTATE extract section state from basic element state</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function SecState = Extract_BasicEl2SecState (sec,ae,ElState)` 

## Description


<pre class="comment">EXTRACT_BASICEL2SECSTATE extract section state from basic element state
  SECSTATE = EXTRACT_BASICEL2SECSTATE (SEC,AE,ELSTATE)
  function extracts from data structure ELSTATE the necessary information
  for section SEC, and returns it in data structure SECSTATE;
  it needs compatibility array AE to determine section from element deformations</pre>
<!-- <div class="fragment"><pre class="comment">EXTRACT_BASICEL2SECSTATE extract section state from basic element state
  SECSTATE = EXTRACT_BASICEL2SECSTATE (SEC,AE,ELSTATE)
  function extracts from data structure ELSTATE the necessary information
  for section SEC, and returns it in data structure SECSTATE;
  it needs compatibility array AE to determine section from element deformations</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="Dinel2dFrm_EBwDF.md" class="code" title="function ElemResp = Dinel2dFrm_EBwDF (action,el_no,xyz,ElemData,ElemState)">Dinel2dFrm_EBwDF</a>	DINEL2dFRM_EBwDF 2d-frame element with distributed inelasticity (displacement formulation)</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->