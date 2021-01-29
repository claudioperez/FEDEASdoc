
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href="_index.md">Dynamic</a> &gt; TransientStateDetermination.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Analysis_Functions\Dynamic&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `TransientStateDetermination`
<!-- <h1>TransientStateDetermination
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

TRANSIENTSTATEDETERMINATION structure state determination under transient conditions

<!-- <div class="box"><strong>TRANSIENTSTATEDETERMINATION structure state determination under transient conditions</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function State = TransientStateDetermination (StifUpdt,Model,ElemData,State,Int_Constants)` 
## <a name="_description"></a>Description

<pre class="comment">TRANSIENTSTATEDETERMINATION structure state determination under transient conditions
  STATE = TRANSIENTSTATEDETERMINATION (STIFUPDT,MODEL,ELEMDATA,STATE)
  the function updates the structure resisting force vector in STATE for the current
  state of the structure as described by the displacement vector and its increments as
  as well as by the history variables in STATE; the effective resisting force and tangent
  stiffness matrix depend on integration constants in cell array INT_CONSTANTS
  depending on the value of character variable STIFUPDT the function also updates
  the tangent stiffness matrix in STATE
  MODEL is a data structure with information about the structural model,
  ELEMDATA is a cell array with element properties</pre>
<!-- <div class="fragment"><pre class="comment">TRANSIENTSTATEDETERMINATION structure state determination under transient conditions
  STATE = TRANSIENTSTATEDETERMINATION (STIFUPDT,MODEL,ELEMDATA,STATE)
  the function updates the structure resisting force vector in STATE for the current
  state of the structure as described by the displacement vector and its increments as
  as well as by the history variables in STATE; the effective resisting force and tangent
  stiffness matrix depend on integration constants in cell array INT_CONSTANTS
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
<li><a href="OneTransientIteration.md" class="code" title="function [State,SolStrat] = OneTransientIteration (Model,ElemData,Loading,State,SolStrat)">OneTransientIteration</a>	ONETRANSIENTITERATION single equilibrium iteration under transient conditions</li><li><a href="TransientIncrement.md" class="code" title="function [State,SolStrat] = TransientIncrement(Model,ElemData,Loading,State,SolStrat)">TransientIncrement</a>	TRANSIENTINCREMENT load incrementation and state advance under transient conditions</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->