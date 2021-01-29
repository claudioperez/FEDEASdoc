
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href="_index.md">Dynamic</a> &gt; Update_TransientState.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Analysis_Functions\Dynamic&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `Update_TransientState`
<!-- <h1>Update_TransientState
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

UPDATE_TRANSIENTSTATE final state determination under transient conditions, reset increments and history

<!-- <div class="box"><strong>UPDATE_TRANSIENTSTATE final state determination under transient conditions, reset increments and history</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function State = Update_TransientState (Model,ElemData,State,SolStrat)` 
## <a name="_description"></a>Description

<pre class="comment">UPDATE_TRANSIENTSTATE final state determination under transient conditions, reset increments and history
  STATE = UPDATE_TRANSIENTSTATE (MODEL,ELEMDATA,STATE,SOLSTRAT)
  the function performs a final state determination for the current state of the structure
  as described by the displacement vector and its increments as well as by the history
  variables in STATE; it then updates the structure resisting forces, and history variables
  as well as the nodal velocities and accelerations in STATE and then
  sets the displacement increments in STATE to zero
  data structure SOLSTRAT carries information about the time integration scheme in field TimeStrat</pre>
<!-- <div class="fragment"><pre class="comment">UPDATE_TRANSIENTSTATE final state determination under transient conditions, reset increments and history
  STATE = UPDATE_TRANSIENTSTATE (MODEL,ELEMDATA,STATE,SOLSTRAT)
  the function performs a final state determination for the current state of the structure
  as described by the displacement vector and its increments as well as by the history
  variables in STATE; it then updates the structure resisting forces, and history variables
  as well as the nodal velocities and accelerations in STATE and then
  sets the displacement increments in STATE to zero
  data structure SOLSTRAT carries information about the time integration scheme in field TimeStrat</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="TimeIntegrationConstants" class="code" title="function Int_Constants = TimeIntegrationConstants (TimeStrat,option)">TimeIntegrationConstants</a>	TIMEINTEGRATIONCONSTANTS constants of time integration strategy</li><li><a href="../../../latest/General_Functions/Structure" class="code" title="function Resp = Structure (action,Model,ElemData,State,ElemList)">Structure</a>	STRUCTURE performs requested action on group of elements</li></ul>
This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="../../../latest/Solution_Scripts/S_Transient_MultiStep.md" class="code" title="">S_Transient_MultiStep</a>	% S_TRANSIENT_MULTISTEP script for multi-step transient analysis under given load history(ies)</li><li><a href="../../../latest/Solution_Scripts/S_Transient_MultiStepwSD.md" class="code" title="">S_Transient_MultiStepwSD</a>	% S_TRANSIENT_MULTISTEPwSD script for multi-step transient analysis under given load history(ies)</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->