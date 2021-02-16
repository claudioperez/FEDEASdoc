---
title: "Extract_Str2ElState"
id: "Extract_Str2ElState"
description: "EXTRACT_STR2ELSTATE extract element state from structure state"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">General_Functions</a> &gt; 
<!-- Extract_Str2ElState.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\General_Functions&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Extract_Str2ElState`



## <a name="_name"></a>Purpose


EXTRACT_STR2ELSTATE extract element state from structure state

<!-- <div class="box"><strong>EXTRACT_STR2ELSTATE extract element state from structure state</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function ElemState = Extract_Str2ElState (el,id,State)` 

## Description


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




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->