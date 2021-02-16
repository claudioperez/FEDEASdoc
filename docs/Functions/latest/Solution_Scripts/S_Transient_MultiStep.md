
<!-- <a name="_top"></a>
<div><a href="../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="_index.md">Solution_Scripts</a> &gt; S_Transient_MultiStep.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../_index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Solution_Scripts&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `S_Transient_MultiStep`
<!-- <h1>S_Transient_MultiStep
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

% S_TRANSIENT_MULTISTEP script for multi-step transient analysis under given load history(ies)

<!-- <div class="box"><strong>% S_TRANSIENT_MULTISTEP script for multi-step transient analysis under given load history(ies)</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`This is a script file.` 
## <a name="_description"></a>Description

<pre class="comment">% S_TRANSIENT_MULTISTEP script for multi-step transient analysis under given load history(ies)                         
  the script sets up the necessary variables for the load factor evolution for the
  transient analysis under one or more more load patterns with given load histories;
  it initializes the state of the structural model, only if the variable State does not exist;
  it is, therefore, useful both for the application of load patterns with load histories
  from the unstressed state or for the continuation of incremental analysis
  after a change of the load patterns or the load histories;
  it initializes the counter pc only if it does not exist in the workspace and saves
  post-processing information of the initial response state;
  it performs several load steps of static analysis with the parameters in SolStrat
  until the pseudo-time parameter Time in State exceeds the specified maximum time Tmax</pre>
<!-- <div class="fragment"><pre class="comment">% S_TRANSIENT_MULTISTEP script for multi-step transient analysis under given load history(ies)                         
  the script sets up the necessary variables for the load factor evolution for the
  transient analysis under one or more more load patterns with given load histories;
  it initializes the state of the structural model, only if the variable State does not exist;
  it is, therefore, useful both for the application of load patterns with load histories
  from the unstressed state or for the continuation of incremental analysis
  after a change of the load patterns or the load histories;
  it initializes the counter pc only if it does not exist in the workspace and saves
  post-processing information of the initial response state;
  it performs several load steps of static analysis with the parameters in SolStrat
  until the pseudo-time parameter Time in State exceeds the specified maximum time Tmax</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="../../latest/Analysis_Functions/Dynamic/TransientIncrement" class="code" title="function [State,SolStrat] = TransientIncrement(Model,ElemData,Loading,State,SolStrat)">TransientIncrement</a>	TRANSIENTINCREMENT load incrementation and state advance under transient conditions</li><li><a href="../../latest/Analysis_Functions/Dynamic/TransientInitialize" class="code" title="function State = TransientInitialize (Model,ElemData,Loading,State)">TransientInitialize</a>	TRANSIENTINITIALIZE initialize State variables for transient response analysis</li><li><a href="../../latest/Analysis_Functions/Dynamic/TransientIterate" class="code" title="function [State,SolStrat] = TransientIterate (Model,ElemData,Loading,State,SolStrat)">TransientIterate</a>	TRANSIENTITERATE equilibrium iterations until convergence under transient conditions</li><li><a href="../../latest/Analysis_Functions/Dynamic/Update_TransientState" class="code" title="function State = Update_TransientState (Model,ElemData,State,SolStrat)">Update_TransientState</a>	UPDATE_TRANSIENTSTATE final state determination under transient conditions, reset increments and history</li><li><a href="../../latest/Analysis_Functions/Static/Initialize_State" class="code" title="function State = Initialize_State (Model,ElemData)">Initialize_State</a>	INITIALIZE_STATE initialize state variables of structural model and create STATE</li><li><a href="../../latest/General_Functions/Structure" class="code" title="function Resp = Structure (action,Model,ElemData,State,ElemList)">Structure</a>	STRUCTURE performs requested action on group of elements</li></ul>
This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->