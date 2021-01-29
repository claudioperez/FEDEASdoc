
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href="_index.md">Dynamic</a> &gt; OneTransientIteration.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Analysis_Functions\Dynamic&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `OneTransientIteration`
<!-- <h1>OneTransientIteration
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

ONETRANSIENTITERATION single equilibrium iteration under transient conditions

<!-- <div class="box"><strong>ONETRANSIENTITERATION single equilibrium iteration under transient conditions</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [State,SolStrat] = OneTransientIteration (Model,ElemData,Loading,State,SolStrat)` 
## <a name="_description"></a>Description

<pre class="comment"> ONETRANSIENTITERATION single equilibrium iteration under transient conditions
  [STATE,SOLSTRAT] = ONETRANSIENTITERATION (MODEL,ELEMDATA,LOADING,STATE,SOLSTRAT)
  the function performs a single equilibrium iteration under the applied loading
  and determines the corresponding displacement increments under transient conditions;
  information about the state of the structure is updated in STATE and
  information about parameters of solution strategy are updated in SOLSTRAT;
  MODEL is a data structure with information about the structural model, ELEMDATA is
  a cell array with element properties, and LOADING is a data structure with information
  about applied force and imposed displacement patterns and corresponding load histories</pre>
<!-- <div class="fragment"><pre class="comment"> ONETRANSIENTITERATION single equilibrium iteration under transient conditions
  [STATE,SOLSTRAT] = ONETRANSIENTITERATION (MODEL,ELEMDATA,LOADING,STATE,SOLSTRAT)
  the function performs a single equilibrium iteration under the applied loading
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
<li><a href="TimeIntegrationConstants" class="code" title="function Int_Constants = TimeIntegrationConstants (TimeStrat,option)">TimeIntegrationConstants</a>	TIMEINTEGRATIONCONSTANTS constants of time integration strategy</li><li><a href="TransientStateDetermination" class="code" title="function State = TransientStateDetermination (StifUpdt,Model,ElemData,State,Int_Constants)">TransientStateDetermination</a>	TRANSIENTSTATEDETERMINATION structure state determination under transient conditions</li></ul>
This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="TransientIterate.md" class="code" title="function [State,SolStrat] = TransientIterate (Model,ElemData,Loading,State,SolStrat)">TransientIterate</a>	TRANSIENTITERATE equilibrium iterations until convergence under transient conditions</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->