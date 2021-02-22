---
title: "Extract_El2MatState"
id: "Extract_El2MatState"
description: "EXTRACT_EL2MATSTATE extract material state from element state"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">Element_Library</a> &gt; 
<!-- Extract_El2MatState.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Element_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Extract_El2MatState`



## <a name="_name"></a>Purpose


EXTRACT_EL2MATSTATE extract material state from element state

<!-- <div class="box"><strong>EXTRACT_EL2MATSTATE extract material state from element state</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function MatState = Extract_El2MatState (mat,aeps,ElState,rd)` 

## Description


<pre class="comment">EXTRACT_EL2MATSTATE extract material state from element state
  MATSTATE = EXTRACT_EL2MATSTATE (MAT,AEPS,ELSTATE,RD)
  function extracts from data structure ELSTATE the necessary information
  for the element material, and returns it in data structure MATSTATE;
  it needs compatibility array AEPS to determine material strains from element displacements
  RD identifies the displacement DOFs to extract (default = all)</pre>
<!-- <div class="fragment"><pre class="comment">EXTRACT_EL2MATSTATE extract material state from element state
  MATSTATE = EXTRACT_EL2MATSTATE (MAT,AEPS,ELSTATE,RD)
  function extracts from data structure ELSTATE the necessary information
  for the element material, and returns it in data structure MATSTATE;
  it needs compatibility array AEPS to determine material strains from element displacements
  RD identifies the displacement DOFs to extract (default = all)</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="MaterialWrapper.md" class="code" title="function ElemResp = MaterialWrapper (action,el_no,xyz,ElemData,ElemState)">MaterialWrapper</a>	MATERIALWRAPPER wrapper element that passes on arguments to the material state determination</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->