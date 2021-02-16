---
title: "Initialize"
id: "Initialize"
description: "INITIALIZE initialize analysis variables in STATE and load control parameters in SOLSTRAT"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href=".autoindex.md">Static</a> &gt; 
<!-- Initialize.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../.autoindex.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Analysis_Functions\Static&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `Initialize`



## <a name="_name"></a>Purpose


INITIALIZE initialize analysis variables in STATE and load control parameters in SOLSTRAT

<!-- <div class="box"><strong>INITIALIZE initialize analysis variables in STATE and load control parameters in SOLSTRAT</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [State,SolStrat] = Initialize (Model,ElemData,Loading,State,SolStrat)` 

## Description


<pre class="comment">INITIALIZE initialize analysis variables in STATE and load control parameters in SOLSTRAT
  [STATE,SOLSTRAT] = INITIALIZE(MODEL,ELEMDATA,LOADING,STATE,SOLSTRAT)
  the function initializes analysis variables in STATE and load control parameters
  in SOLSTRAT (only if IncrStrat.LFCtrl = 'yes');
  the function returns updated data structures STATE and SOLSTRAT:
  MODEL is a data structure with information about the structural model, ELEMDATA is
  a cell array with element properties, and LOADING is a data structure with information
  about applied force and imposed displacement patterns and corresponding load histories;
  specifically the function adds the following fields to STATE
  STATE
       lamda = row vector of current load factors
       Pi    = initial force vector (for load sequences)
       Time  = pseudo-or real time counter
  the function also adds the field HIST to SOLSTRAT with subfields Sp0 and sgnK0 for
  adjusting the load factor under load incrementation, if IncrStrat.LFCtrl='yes'</pre>
<!-- <div class="fragment"><pre class="comment">INITIALIZE initialize analysis variables in STATE and load control parameters in SOLSTRAT
  [STATE,SOLSTRAT] = INITIALIZE(MODEL,ELEMDATA,LOADING,STATE,SOLSTRAT)
  the function initializes analysis variables in STATE and load control parameters
  in SOLSTRAT (only if IncrStrat.LFCtrl = 'yes');
  the function returns updated data structures STATE and SOLSTRAT:
  MODEL is a data structure with information about the structural model, ELEMDATA is
  a cell array with element properties, and LOADING is a data structure with information
  about applied force and imposed displacement patterns and corresponding load histories;
  specifically the function adds the following fields to STATE
  STATE
       lamda = row vector of current load factors
       Pi    = initial force vector (for load sequences)
       Time  = pseudo-or real time counter
  the function also adds the field HIST to SOLSTRAT with subfields Sp0 and sgnK0 for
  adjusting the load factor under load incrementation, if IncrStrat.LFCtrl='yes'</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="/Functions/LoadFactorControl" class="code" title="function SolStrat = LoadFactorControl (action,SolStrat,detKf,Pref,Ut,DUr)">LoadFactorControl</a>	LOADFACTORCONTROL determine load factor increment under load control strategy</li><li><a href="/Functions/../../../latest/General_Functions/Structure" class="code" title="function Resp = Structure (action,Model,ElemData,State,ElemList)">Structure</a>	STRUCTURE performs requested action on group of elements</li></ul>

This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="../../../latest/Solution_Scripts/S_InitialStep.md" class="code" title="">S_InitialStep</a>	% S_INITIALSTEP script for initial step of incremental analysis</li><li><a href="../../../latest/Solution_Scripts/S_MultiStep.md" class="code" title="">S_MultiStep</a>	% S_MULTISTEP script for multi-step incremental analysis after load factor initialization</li><li><a href="../../../latest/Solution_Scripts/S_MultiStep_wLoadHist.md" class="code" title="">S_MultiStep_wLoadHist</a>	% S_MULTISTEP_wLOADHIST script for multi-step incremental analysis under given load history(ies)</li><li><a href="../../../latest/Solution_Scripts/S_MultiStep_wLoadHistwSD.md" class="code" title="">S_MultiStep_wLoadHistwSD</a>	% S_MULTISTEP_wLOADHISTwSD script for multi-step incremental analysis under given load history(ies)</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->