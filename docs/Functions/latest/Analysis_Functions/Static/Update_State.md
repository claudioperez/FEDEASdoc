---
title: "Update_State"
id: "Update_State"
description: "UPDATE_STATE final state determination under static conditions, reset increments and history"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href=".autoindex.md">Static</a> &gt; 
<!-- Update_State.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../.autoindex.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Analysis_Functions\Static&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `Update_State`



## <a name="_name"></a>Purpose


UPDATE_STATE final state determination under static conditions, reset increments and history

<!-- <div class="box"><strong>UPDATE_STATE final state determination under static conditions, reset increments and history</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function State = Update_State (Model,ElemData,State)` 

## Description


<pre class="comment">UPDATE_STATE final state determination under static conditions, reset increments and history
  STATE = UPDATE_STATE (MODEL,ELEMDATA,STATE)
  the function performs a final state determination for the current state of the structure
  as described by the displacement vector and its increments as well as by the history
  variables in STATE; it then updates the structure resisting forces and history variables
  in STATE and then sets the displacement increments in STATE to zero</pre>
<!-- <div class="fragment"><pre class="comment">UPDATE_STATE final state determination under static conditions, reset increments and history
  STATE = UPDATE_STATE (MODEL,ELEMDATA,STATE)
  the function performs a final state determination for the current state of the structure
  as described by the displacement vector and its increments as well as by the history
  variables in STATE; it then updates the structure resisting forces and history variables
  in STATE and then sets the displacement increments in STATE to zero</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="/Functions/../../../latest/General_Functions/Structure" class="code" title="function Resp = Structure (action,Model,ElemData,State,ElemList)">Structure</a>	STRUCTURE performs requested action on group of elements</li></ul>

This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="../../../latest/Solution_Scripts/S_InitialStep.md" class="code" title="">S_InitialStep</a>	% S_INITIALSTEP script for initial step of incremental analysis</li><li><a href="../../../latest/Solution_Scripts/S_MultiStep.md" class="code" title="">S_MultiStep</a>	% S_MULTISTEP script for multi-step incremental analysis after load factor initialization</li><li><a href="../../../latest/Solution_Scripts/S_MultiStep_wLoadHist.md" class="code" title="">S_MultiStep_wLoadHist</a>	% S_MULTISTEP_wLOADHIST script for multi-step incremental analysis under given load history(ies)</li><li><a href="../../../latest/Solution_Scripts/S_MultiStep_wLoadHistwSD.md" class="code" title="">S_MultiStep_wLoadHistwSD</a>	% S_MULTISTEP_wLOADHISTwSD script for multi-step incremental analysis under given load history(ies)</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->