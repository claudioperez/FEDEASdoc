
<!-- <a name="_top"></a>
<div><a href="../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="index.md">Solution_Scripts</a> &gt; S_MultiStep_wLoadHist.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../index.md"><img alt="<" border="0" src="../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Solution_Scripts&nbsp;<img alt=">" border="0" src="../../../../../right.png"></a></td></tr></table>-->
# `S_MultiStep_wLoadHist`
<!-- <h1>S_MultiStep_wLoadHist
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

% S_MULTISTEP_wLOADHIST : script for multi-step incremental analysis including initialization

<!-- <div class="box"><strong>% S_MULTISTEP_wLOADHIST : script for multi-step incremental analysis including initialization</strong></div> -->

## <a name="_synopsis"></a>Syntax

`This is a script file.` 
## <a name="_description"></a>Description

<pre class="comment">% S_MULTISTEP_wLOADHIST : script for multi-step incremental analysis including initialization
                          under given load history(ies) 

  =========================================================================================
  FEDEASLab - Release 5.1, July 2020
  Matlab Finite Elements for Design, Evaluation and Analysis of Structures
  Professor Filip C. Filippou (filippou@berkeley.edu)
  Department of Civil and Environmental Engineering, UC Berkeley
  Copyright(c) 1998-2020. The Regents of the University of California. All Rights Reserved.
  =========================================================================================</pre>
<!-- <div class="fragment"><pre class="comment">% S_MULTISTEP_wLOADHIST : script for multi-step incremental analysis including initialization
                          under given load history(ies) 

  =========================================================================================
  FEDEASLab - Release 5.1, July 2020
  Matlab Finite Elements for Design, Evaluation and Analysis of Structures
  Professor Filip C. Filippou (filippou@berkeley.edu)
  Department of Civil and Environmental Engineering, UC Berkeley
  Copyright(c) 1998-2020. The Regents of the University of California. All Rights Reserved.
  =========================================================================================</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../../../../matlabicon.gif)">
</ul>
<!-- crossreference -->



<h2><a name="_source"></a>SOURCE CODE</h2>
<div class="fragment"><pre>0001 <span class="comment">%% S_MULTISTEP_wLOADHIST : script for multi-step incremental analysis including initialization</span>
0002 <span class="comment">%                          under given load history(ies)</span>
0003 <span class="comment">%</span>
0004 <span class="comment">%  =========================================================================================</span>
0005 <span class="comment">%  FEDEASLab - Release 5.1, July 2020</span>
0006 <span class="comment">%  Matlab Finite Elements for Design, Evaluation and Analysis of Structures</span>
0007 <span class="comment">%  Professor Filip C. Filippou (filippou@berkeley.edu)</span>
0008 <span class="comment">%  Department of Civil and Environmental Engineering, UC Berkeley</span>
0009 <span class="comment">%  Copyright(c) 1998-2020. The Regents of the University of California. All Rights Reserved.</span>
0010 <span class="comment">%  =========================================================================================</span>
0011 
0012 <span class="comment">%%  ****************************************************************************************</span>
0013 <span class="comment">%   BEFORE INVOKING THE SCRIPT YOU NEED TO:</span>
0014 <span class="comment">%   DEFINE parameters in SolStrat</span>
0015 <span class="comment">%   DEFINE end time Tmax for completion of analysis</span>
0016 <span class="comment">%   NOTE : the plot counter variable pc is set to one, if not present in the workspace</span>
0017 <span class="comment">%%  ****************************************************************************************</span>
0018 
0019 <span class="comment">%% initialize state</span>
0020 <span class="keyword">if</span> ~exist(<span class="string">'State'</span>,<span class="string">'var'</span>), State = Initialize_State(Model,ElemData); <span class="keyword">end</span>
0021 [State,SolStrat] = Initialize (Model,ElemData,Loading,State,SolStrat);
0022 <span class="keyword">if</span> ~exist(<span class="string">'pc'</span>,<span class="string">'var'</span>)
0023    pc = 1;    <span class="comment">% initialize plot counter</span>
0024    State    = Structure (<span class="string">'forc'</span>,Model,ElemData,State);
0025    Post(pc) = Structure (<span class="string">'post'</span>,Model,ElemData,State);
0026 <span class="keyword">end</span>
0027 
0028 <span class="comment">%% perform multi-step incremental analysis</span>
0029 <span class="keyword">while</span> ( State.Time&lt;Tmax )
0030    [State,SolStrat] = Increment (Model,ElemData,Loading,State,SolStrat);
0031    <span class="keyword">if</span> State.ConvFlag
0032       [State,SolStrat] = Iterate (Model,ElemData,Loading,State,SolStrat);
0033    <span class="keyword">else</span>
0034       SolStrat.ConvFlag = false;
0035    <span class="keyword">end</span>
0036    <span class="keyword">if</span> (SolStrat.ConvFlag)
0037       State = Update_State (Model,ElemData,State);
0038       GoodState = State;
0039       <span class="comment">% update plot counter and store results</span>
0040       pc = pc+1;
0041       Post(pc) = Structure (<span class="string">'post'</span>,Model,ElemData,State);
0042    <span class="keyword">else</span>
0043       State = GoodState;
0044       fprintf (<span class="string">'\nNo convergence at time step %6.4g; last good state saved \n\n'</span>,State.Time);
0045       <span class="keyword">break</span>
0046    <span class="keyword">end</span>
0047 <span class="keyword">end</span></pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->