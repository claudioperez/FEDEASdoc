---
title: "OneIteration"
id: "OneIteration"
description: "ONEITERATION single equilibrium iteration under static conditions"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href=".autoindex.md">Static</a> &gt; 
<!-- OneIteration.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../.autoindex.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Analysis_Functions\Static&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `OneIteration`



## <a name="_name"></a>Purpose


ONEITERATION single equilibrium iteration under static conditions

<!-- <div class="box"><strong>ONEITERATION single equilibrium iteration under static conditions</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [State,SolStrat] = OneIteration (Model,ElemData,Loading,State,SolStrat)` 

## Description


<pre class="comment"> ONEITERATION single equilibrium iteration under static conditions
  [STATE,SOLSTRAT] = ONEITERATION (MODEL,ELEMDATA,LOADING,STATE,SOLSTRAT)
  the function performs a single equilibrium iteration under the applied loading
  and determines the corresponding displacement increments under static conditions;
  information about the state of the structure is updated in STATE and
  information about the parameters of the solution strategy is updated in SOLSTRAT;
  MODEL is a data structure with information about the structural model, ELEMDATA is
  a cell array with element properties, and LOADING is a data structure with information
  about applied force and imposed displacement patterns with corresponding load histories</pre>
<!-- <div class="fragment"><pre class="comment"> ONEITERATION single equilibrium iteration under static conditions
  [STATE,SOLSTRAT] = ONEITERATION (MODEL,ELEMDATA,LOADING,STATE,SOLSTRAT)
  the function performs a single equilibrium iteration under the applied loading
  and determines the corresponding displacement increments under static conditions;
  information about the state of the structure is updated in STATE and
  information about the parameters of the solution strategy is updated in SOLSTRAT;
  MODEL is a data structure with information about the structural model, ELEMDATA is
  a cell array with element properties, and LOADING is a data structure with information
  about applied force and imposed displacement patterns with corresponding load histories</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="/Functions/LoadFactorControl" class="code" title="function SolStrat = LoadFactorControl (action,SolStrat,detKf,Pref,Ut,DUr)">LoadFactorControl</a>	LOADFACTORCONTROL determine load factor increment under load control strategy</li><li><a href="/Functions/StateDetermination" class="code" title="function State = StateDetermination (StifUpdt,Model,ElemData,State)">StateDetermination</a>	STATEDETERMINATION structure state determination under static conditions</li></ul>

This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="Iterate.md" class="code" title="function [State,SolStrat] = Iterate (Model,ElemData,Loading,State,SolStrat)">Iterate</a>	ITERATE equilibrium iterations until convergence under static conditions</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->