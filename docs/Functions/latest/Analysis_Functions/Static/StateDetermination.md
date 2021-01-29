
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href="_index.md">Static</a> &gt; StateDetermination.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Analysis_Functions\Static&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `StateDetermination`
<!-- <h1>StateDetermination
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

STATEDETERMINATION structure state determination under static conditions

<!-- <div class="box"><strong>STATEDETERMINATION structure state determination under static conditions</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function State = StateDetermination (StifUpdt,Model,ElemData,State)` 
## <a name="_description"></a>Description

<pre class="comment">STATEDETERMINATION structure state determination under static conditions
  STATE = STATEDETERMINATION (STIFUPDT,MODEL,ELEMDATA,STATE)
  the function updates the structure resisting force vector in STATE for the current
  state of the structure as described by the displacement vector and its increments as
  as well as by the history variables in STATE;
  depending on the value of character variable STIFUPDT the function also updates
  the tangent stiffness matrix in STATE
  MODEL is a data structure with information about the structural model,
  ELEMDATA is a cell array with element properties</pre>
<!-- <div class="fragment"><pre class="comment">STATEDETERMINATION structure state determination under static conditions
  STATE = STATEDETERMINATION (STIFUPDT,MODEL,ELEMDATA,STATE)
  the function updates the structure resisting force vector in STATE for the current
  state of the structure as described by the displacement vector and its increments as
  as well as by the history variables in STATE;
  depending on the value of character variable STIFUPDT the function also updates
  the tangent stiffness matrix in STATE
  MODEL is a data structure with information about the structural model,
  ELEMDATA is a cell array with element properties</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="../../../latest/General_Functions/Structure" class="code" title="function Resp = Structure (action,Model,ElemData,State,ElemList)">Structure</a>	STRUCTURE performs requested action on group of elements</li></ul>
This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="Increment.md" class="code" title="function [State,SolStrat] = Increment(Model,ElemData,Loading,State,SolStrat)">Increment</a>	INCREMENT load incrementation and state advance under static conditions</li><li><a href="OneIteration.md" class="code" title="function [State,SolStrat] = OneIteration (Model,ElemData,Loading,State,SolStrat)">OneIteration</a>	ONEITERATION single equilibrium iteration under static conditions</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->