
<!-- <a name="_top"></a>
<div><a href="../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="_index.md">Element_Library</a> &gt; Extract_El2MatState.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../_index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Element_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Extract_El2MatState`
<!-- <h1>Extract_El2MatState
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

EXTRACT_EL2MATSTATE extract material state from element state

<!-- <div class="box"><strong>EXTRACT_EL2MATSTATE extract material state from element state</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function MatState = Extract_El2MatState (mat,aeps,ElState,rd)` 
## <a name="_description"></a>Description

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




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->