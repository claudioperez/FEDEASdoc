
<!-- <a name="_top"></a>
<div><a href="../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="_index.md">General_Functions</a> &gt; Extract_Str2ElState.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../_index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\General_Functions&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Extract_Str2ElState`
<!-- <h1>Extract_Str2ElState
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

EXTRACT_STR2ELSTATE extract element state from structure state

<!-- <div class="box"><strong>EXTRACT_STR2ELSTATE extract element state from structure state</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function ElemState = Extract_Str2ElState (el,id,State)` 
## <a name="_description"></a>Description

<pre class="comment">EXTRACT_STR2ELSTATE extract element state from structure state
  ELEMSTATE = EXTRACT_STR2ELSTATE(EL,ID,STATE)
  the function extracts from the data structure STATE the necessary state information
  for element EL, with id-array ID, and returns it in data structure ELEMSTATE;
  when STATE is numeric, it is assumed to represent the global dof displacement vector
  and the function extracts only the element dof displacements in ELEMSTATE.U</pre>
<!-- <div class="fragment"><pre class="comment">EXTRACT_STR2ELSTATE extract element state from structure state
  ELEMSTATE = EXTRACT_STR2ELSTATE(EL,ID,STATE)
  the function extracts from the data structure STATE the necessary state information
  for element EL, with id-array ID, and returns it in data structure ELEMSTATE;
  when STATE is numeric, it is assumed to represent the global dof displacement vector
  and the function extracts only the element dof displacements in ELEMSTATE.U</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="Structure.md" class="code" title="function Resp = Structure (action,Model,ElemData,State,ElemList)">Structure</a>	STRUCTURE performs requested action on group of elements</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->