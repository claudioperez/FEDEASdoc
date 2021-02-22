---
title: "Extract_Sec2MatState"
id: "Extract_Sec2MatState"
description: "EXTRACT_SEC2MATSTATE extract material state from section state"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">Section_Library</a> &gt; 
<!-- Extract_Sec2MatState.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Section_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Extract_Sec2MatState`



## <a name="_name"></a>Purpose


EXTRACT_SEC2MATSTATE extract material state from section state

<!-- <div class="box"><strong>EXTRACT_SEC2MATSTATE extract material state from section state</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function MatState = Extract_Sec2MatState (m,as,SecState)` 

## Description


<pre class="comment">EXTRACT_SEC2MATSTATE extract material state from section state
  MATSTATE = EXTRACT_SEC2MATSTATE (M,AS,SECSTATE)
  function extracts from data structure SECSTATE the necessary information
  for material point M, and returns it in data structure MATSTATE;
  it needs compatibility array AS to determine material strains from section deformations</pre>
<!-- <div class="fragment"><pre class="comment">EXTRACT_SEC2MATSTATE extract material state from section state
  MATSTATE = EXTRACT_SEC2MATSTATE (M,AS,SECSTATE)
  function extracts from data structure SECSTATE the necessary information
  for material point M, and returns it in data structure MATSTATE;
  it needs compatibility array AS to determine material strains from section deformations</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="HomoCircSecw1dMat.md" class="code" title="function SecResp = HomoCircSecw1dMat (action,SecNo,ndm,SecData,SecState)">HomoCircSecw1dMat</a>	HOMOCIRCSECw1dMAT response of homogeneous circular section with uniaxial material</li><li><a href="HomoRectSecw1dMat.md" class="code" title="function SecResp = HomoRectSecw1dMat (action,SecNo,ndm,SecData,SecState)">HomoRectSecw1dMat</a>	HOMORECTSECw1dMAT response of homogeneous rectangular section with uniaxial material</li><li><a href="HomoWFSecw1dMat.md" class="code" title="function SecResp = HomoWFSecw1dMat (action,SecNo,ndm,SecData,SecState)">HomoWFSecw1dMat</a>	HOMOWFSECw1dMAT response of homogeneous wide flange (WF) section with uniaxial material</li><li><a href="MultRectSecw1dMat.md" class="code" title="function SecResp = MultRectSecw1dMat (action,SecNo,ndm,SecData,SecState)">MultRectSecw1dMat</a>	MULTRECTSECw1dMAT response for section of rectangular patches and bars with uniaxial material</li><li><a href="ReCircSecw1dMat.md" class="code" title="function SecResp = ReCircSecw1dMat (action,SecNo,ndm,SecData,SecState)">ReCircSecw1dMat</a>	RECIRCSECw1dMAT response of reinforced circular section with uniaxial materials</li><li><a href="ReRectSecw1dMat.md" class="code" title="function SecResp = ReRectSecw1dMat (action,SecNo,ndm,SecData,SecState)">ReRectSecw1dMat</a>	RERECTSECw1dMAT response of reinforced rectangular section with uniaxial materials</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->