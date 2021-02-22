---
title: "S_MultiStep_wLoadHist"
id: "S_MultiStep_wLoadHist"
description: "% S_MULTISTEP_wLOADHIST script for multi-step incremental analysis under given load history(ies)"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">Solution_Scripts</a> &gt; 
<!-- S_MultiStep_wLoadHist.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Solution_Scripts&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `S_MultiStep_wLoadHist`



## <a name="_name"></a>Purpose


% S_MULTISTEP_wLOADHIST script for multi-step incremental analysis under given load history(ies)

<!-- <div class="box"><strong>% S_MULTISTEP_wLOADHIST script for multi-step incremental analysis under given load history(ies)</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`This is a script file.` 

## Description


<pre class="comment">% S_MULTISTEP_wLOADHIST script for multi-step incremental analysis under given load history(ies)
                        with load factor initialization  
  the script sets up the necessary variables for the load factor evolution for the
  static analysis under one or more more load patterns with given load histories;
  it initializes the state of the structural model, only if the variable State does not exist;
  it is, therefore, useful both for the application of load patterns with load histories
  from the unstressed state or for the continuation of incremental analysis
  after a change of the load patterns or the load histories;
  it initializes the counter pc only if it does not exist in the workspace and saves
  post-processing information of the initial response state;
  it performs several load steps of static analysis with the parameters in SolStrat
  until the pseudo-time parameter Time in State exceeds the specified maximum time Tmax</pre>
<!-- <div class="fragment"><pre class="comment">% S_MULTISTEP_wLOADHIST script for multi-step incremental analysis under given load history(ies)
                        with load factor initialization  
  the script sets up the necessary variables for the load factor evolution for the
  static analysis under one or more more load patterns with given load histories;
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
<li><a href="/Functions/../../latest/Analysis_Functions/Static/Increment" class="code" title="function [State,SolStrat] = Increment(Model,ElemData,Loading,State,SolStrat)">Increment</a>	INCREMENT load incrementation and state advance under static conditions</li><li><a href="/Functions/../../latest/Analysis_Functions/Static/Initialize" class="code" title="function [State,SolStrat] = Initialize (Model,ElemData,Loading,State,SolStrat)">Initialize</a>	INITIALIZE initialize analysis variables in STATE and load control parameters in SOLSTRAT</li><li><a href="/Functions/../../latest/Analysis_Functions/Static/Initialize_State" class="code" title="function State = Initialize_State (Model,ElemData)">Initialize_State</a>	INITIALIZE_STATE initialize state variables of structural model and create STATE</li><li><a href="/Functions/../../latest/Analysis_Functions/Static/Iterate" class="code" title="function [State,SolStrat] = Iterate (Model,ElemData,Loading,State,SolStrat)">Iterate</a>	ITERATE equilibrium iterations until convergence under static conditions</li><li><a href="/Functions/../../latest/Analysis_Functions/Static/Update_State" class="code" title="function State = Update_State (Model,ElemData,State)">Update_State</a>	UPDATE_STATE final state determination under static conditions, reset increments and history</li><li><a href="/Functions/../../latest/General_Functions/Structure" class="code" title="function Resp = Structure (action,Model,ElemData,State,ElemList)">Structure</a>	STRUCTURE performs requested action on group of elements</li></ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="S_MomCurvAnalysis.md" class="code" title="">S_MomCurvAnalysis</a>	% S_MOMCURVANALYSIS script for moment-curvature analysis under constant axial force</li><li><a href="S_NMAnalysiswSepLoadHist.md" class="code" title="">S_NMAnalysiswSepLoadHist</a>	% S_NMANALYSISwSEPLOADHIST script for application N and M with separate load histories</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->