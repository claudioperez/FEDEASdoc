---
title: "TransientIterate"
id: "TransientIterate"
description: "TRANSIENTITERATE equilibrium iterations until convergence under transient conditions"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href=".autoindex.md">Dynamic</a> &gt; 
<!-- TransientIterate.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../.autoindex.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Analysis_Functions\Dynamic&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `TransientIterate`



## <a name="_name"></a>Purpose


TRANSIENTITERATE equilibrium iterations until convergence under transient conditions

<!-- <div class="box"><strong>TRANSIENTITERATE equilibrium iterations until convergence under transient conditions</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [State,SolStrat] = TransientIterate (Model,ElemData,Loading,State,SolStrat)` 

## Description


<pre class="comment">TRANSIENTITERATE equilibrium iterations until convergence under transient conditions
  [STATE,SOLSTRAT] = TRANSIENTITERATE (MODEL,ELEMDATA,LOADING,STATE,SOLSTRAT)
  the function performs equilibrium iterations until convergence under the applied loading
  and determines the corresponding displacement increments under transient conditions;
  information about the state of the structure is updated in STATE and
  information about parameters of solution strategy are updated in SOLSTRAT;
  MODEL is a data structure with information about the structural model, ELEMDATA is
  a cell array with element properties, and LOADING is a data structure with information
  about applied force and imposed displacement patterns and corresponding load histories</pre>
<!-- <div class="fragment"><pre class="comment">TRANSIENTITERATE equilibrium iterations until convergence under transient conditions
  [STATE,SOLSTRAT] = TRANSIENTITERATE (MODEL,ELEMDATA,LOADING,STATE,SOLSTRAT)
  the function performs equilibrium iterations until convergence under the applied loading
  and determines the corresponding displacement increments under transient conditions;
  information about the state of the structure is updated in STATE and
  information about parameters of solution strategy are updated in SOLSTRAT;
  MODEL is a data structure with information about the structural model, ELEMDATA is
  a cell array with element properties, and LOADING is a data structure with information
  about applied force and imposed displacement patterns and corresponding load histories</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="/Functions/OneTransientIteration" class="code" title="function [State,SolStrat] = OneTransientIteration (Model,ElemData,Loading,State,SolStrat)">OneTransientIteration</a>	ONETRANSIENTITERATION single equilibrium iteration under transient conditions</li></ul>

This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="../../../latest/Solution_Scripts/S_Transient_MultiStep.md" class="code" title="">S_Transient_MultiStep</a>	% S_TRANSIENT_MULTISTEP script for multi-step transient analysis under given load history(ies)</li><li><a href="../../../latest/Solution_Scripts/S_Transient_MultiStepwSD.md" class="code" title="">S_Transient_MultiStepwSD</a>	% S_TRANSIENT_MULTISTEPwSD script for multi-step transient analysis under given load history(ies)</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->