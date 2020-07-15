
<!-- <a name="_top"></a>
<div><a href="../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="index.md">Solution_Scripts</a> &gt; S_MultiStep.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../index.md"><img alt="<" border="0" src="../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Solution_Scripts&nbsp;<img alt=">" border="0" src="../../../../../right.png"></a></td></tr></table>-->
# `S_MultiStep`
<!-- <h1>S_MultiStep
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

% S_MULTISTEP : script for multi-step incremental analysis including initialization

<!-- <div class="box"><strong>% S_MULTISTEP : script for multi-step incremental analysis including initialization</strong></div> -->

## <a name="_synopsis"></a>Syntax

`This is a script file.` 
## <a name="_description"></a>Description

<pre class="comment">% S_MULTISTEP : script for multi-step incremental analysis including initialization

  =========================================================================================
  FEDEASLab - Release 5.1, July 2020
  Matlab Finite Elements for Design, Evaluation and Analysis of Structures
  Professor Filip C. Filippou (filippou@berkeley.edu)
  Department of Civil and Environmental Engineering, UC Berkeley
  Copyright(c) 1998-2020. The Regents of the University of California. All Rights Reserved.
  =========================================================================================</pre>
<!-- <div class="fragment"><pre class="comment">% S_MULTISTEP : script for multi-step incremental analysis including initialization

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
<div class="fragment"><pre>0001 <span class="comment">%% S_MULTISTEP : script for multi-step incremental analysis including initialization</span>
0002 <span class="comment">%</span>
0003 <span class="comment">%  =========================================================================================</span>
0004 <span class="comment">%  FEDEASLab - Release 5.1, July 2020</span>
0005 <span class="comment">%  Matlab Finite Elements for Design, Evaluation and Analysis of Structures</span>
0006 <span class="comment">%  Professor Filip C. Filippou (filippou@berkeley.edu)</span>
0007 <span class="comment">%  Department of Civil and Environmental Engineering, UC Berkeley</span>
0008 <span class="comment">%  Copyright(c) 1998-2020. The Regents of the University of California. All Rights Reserved.</span>
0009 <span class="comment">%  =========================================================================================</span>
0010 
0011 <span class="comment">%%  ****************************************************************************************</span>
0012 <span class="comment">%   BEFORE INVOKING THE SCRIPT YOU NEED TO:</span>
0013 <span class="comment">%   DEFINE parameters in SolStrat</span>
0014 <span class="comment">%   DEFINE no of load steps (nostep)</span>
0015 <span class="comment">%   NOTE : the plot counter variable pc is set to one, if not present in the workspace</span>
0016 <span class="comment">%%  ****************************************************************************************</span>
0017 
0018 <span class="comment">%% initialize state</span>
0019 <span class="keyword">if</span> ~exist(<span class="string">'State'</span>,<span class="string">'var'</span>), State = Initialize_State (Model,ElemData); <span class="keyword">end</span>
0020 [State,SolStrat] = Initialize (Model,ElemData,Loading,State,SolStrat);
0021 <span class="keyword">if</span> ~exist(<span class="string">'pc'</span>,<span class="string">'var'</span>)
0022   pc = 1;    <span class="comment">% initialize plot counter</span>
0023   State    = Structure (<span class="string">'forc'</span>,Model,ElemData,State);
0024   Post(pc) = Structure (<span class="string">'post'</span>,Model,ElemData,State);
0025 <span class="keyword">end</span>
0026 
0027 <span class="comment">%% multi-step incremental analysis (nostep load steps)</span>
0028 <span class="keyword">for</span> k = 1:nostep
0029   fprintf(<span class="string">'\n'</span>)
0030   disp ([<span class="string">'Load Step '</span>,num2str(k)])
0031   [State,SolStrat] = Increment (Model,ElemData,Loading,State,SolStrat);
0032   <span class="keyword">if</span> State.ConvFlag
0033     [State,SolStrat] = Iterate (Model,ElemData,Loading,State,SolStrat);
0034   <span class="keyword">else</span>
0035     SolStrat.ConvFlag = false;
0036   <span class="keyword">end</span>
0037   <span class="keyword">if</span> (SolStrat.ConvFlag)
0038     State = Update_State (Model,ElemData,State);
0039     GoodState = State;
0040     <span class="comment">% update plot counter and store results</span>
0041     pc = pc+1;
0042     Post(pc) = Structure (<span class="string">'post'</span>,Model,ElemData,State);
0043   <span class="keyword">else</span>
0044     <span class="keyword">if</span> exist(<span class="string">'GoodState'</span>,<span class="string">'var'</span>)
0045       State = GoodState;
0046       fprintf (<span class="string">'\nNo convergence in step %d ; last good state saved \n'</span>,k);
0047     <span class="keyword">else</span>
0048       fprintf (<span class="string">'\nNo convergence in step %d \n'</span>,k);
0049     <span class="keyword">end</span>
0050     <span class="keyword">break</span>
0051   <span class="keyword">end</span>
0052 <span class="keyword">end</span></pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->