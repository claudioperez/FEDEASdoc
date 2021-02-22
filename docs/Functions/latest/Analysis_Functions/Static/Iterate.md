---
title: "Iterate"
id: "Iterate"
description: "ITERATE equilibrium iterations until convergence under static conditions"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href=".autoindex.md">Static</a> &gt; 
<!-- Iterate.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../.autoindex.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Analysis_Functions\Static&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `Iterate`



## <a name="_name"></a>Purpose


ITERATE equilibrium iterations until convergence under static conditions

<!-- <div class="box"><strong>ITERATE equilibrium iterations until convergence under static conditions</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [State,SolStrat] = Iterate (Model,ElemData,Loading,State,SolStrat)` 

## Description


<pre class="comment">ITERATE equilibrium iterations until convergence under static conditions
  [STATE,SOLSTRAT] = ITERATE(MODEL,ELEMDATA,LOADING,STATE,SOLSTRAT)
  the function performs equilibrium iterations until convergence under the applied loading
  and determines the corresponding displacement increments under static conditions;
  information about the state of the structure is updated in STATE and
  information about parameters of solution strategy are updated in SOLSTRAT;
  MODEL is a data structure with information about the structural model, ELEMDATA is
  a cell array with element properties, and LOADING is a data structure with information
  about applied force and imposed displacement patterns and corresponding load histories</pre>
<!-- <div class="fragment"><pre class="comment">ITERATE equilibrium iterations until convergence under static conditions
  [STATE,SOLSTRAT] = ITERATE(MODEL,ELEMDATA,LOADING,STATE,SOLSTRAT)
  the function performs equilibrium iterations until convergence under the applied loading
  and determines the corresponding displacement increments under static conditions;
  information about the state of the structure is updated in STATE and
  information about parameters of solution strategy are updated in SOLSTRAT;
  MODEL is a data structure with information about the structural model, ELEMDATA is
  a cell array with element properties, and LOADING is a data structure with information
  about applied force and imposed displacement patterns and corresponding load histories</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="/Functions/OneIteration" class="code" title="function [State,SolStrat] = OneIteration (Model,ElemData,Loading,State,SolStrat)">OneIteration</a>	ONEITERATION single equilibrium iteration under static conditions</li></ul>

This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="../../../latest/Solution_Scripts/S_InitialStep.md" class="code" title="">S_InitialStep</a>	% S_INITIALSTEP script for initial step of incremental analysis</li><li><a href="../../../latest/Solution_Scripts/S_MultiStep.md" class="code" title="">S_MultiStep</a>	% S_MULTISTEP script for multi-step incremental analysis after load factor initialization</li><li><a href="../../../latest/Solution_Scripts/S_MultiStep_wLoadHist.md" class="code" title="">S_MultiStep_wLoadHist</a>	% S_MULTISTEP_wLOADHIST script for multi-step incremental analysis under given load history(ies)</li><li><a href="../../../latest/Solution_Scripts/S_MultiStep_wLoadHistwSD.md" class="code" title="">S_MultiStep_wLoadHistwSD</a>	% S_MULTISTEP_wLOADHISTwSD script for multi-step incremental analysis under given load history(ies)</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->