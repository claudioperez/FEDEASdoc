
<!-- <a name="_top"></a>
<div><a href="../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="_index.md">Element_Library</a> &gt; Extract_El2SecState.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../_index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Element_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Extract_El2SecState`
<!-- <h1>Extract_El2SecState
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

EXTRACT_EL2SECSTATE extract section state from element state

<!-- <div class="box"><strong>EXTRACT_EL2SECSTATE extract section state from element state</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function SecState = Extract_El2SecState (sec,ae,ElemState)` 
## <a name="_description"></a>Description

<pre class="comment">EXTRACT_EL2SECSTATE extract section state from element state
  SECSTATE = EXTRACT_EL2SECSTATE (SEC,AE,ELSTATE)
  function extracts from data structure ELSTATE the necessary information
  for section SEC, and returns it in data structure SECSTATE;
  it needs compatibility array AE to determine section from element deformations</pre>
<!-- <div class="fragment"><pre class="comment">EXTRACT_EL2SECSTATE extract section state from element state
  SECSTATE = EXTRACT_EL2SECSTATE (SEC,AE,ELSTATE)
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
<li><a href="SectionWrapper.md" class="code" title="function ElemResp = SectionWrapper (action,el_no,xyz,ElemData,ElemState)">SectionWrapper</a>	SECTIONWRAPPER wrapper element that passes on arguments to the section state determination</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->