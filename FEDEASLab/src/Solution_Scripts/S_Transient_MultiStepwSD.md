
<!-- <a name="_top"></a>
<div><a href="../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="index.md">Solution_Scripts</a> &gt; S_Transient_MultiStepwSD.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../index.md"><img alt="<" border="0" src="../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Solution_Scripts&nbsp;<img alt=">" border="0" src="../../../../../right.png"></a></td></tr></table>-->
# `S_Transient_MultiStepwSD`
<!-- <h1>S_Transient_MultiStepwSD
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

% S_TRANSIENT_MULTISTEPwSD : script for multi-step transient analysis including initialization

<!-- <div class="box"><strong>% S_TRANSIENT_MULTISTEPwSD : script for multi-step transient analysis including initialization</strong></div> -->

## <a name="_synopsis"></a>Syntax

`This is a script file.` 
## <a name="_description"></a>Description

<pre class="comment">% S_TRANSIENT_MULTISTEPwSD : script for multi-step transient analysis including initialization
                             under given load history(ies) with automatic time step division and rescaling 

  =========================================================================================
  FEDEASLab - Release 5.1, July 2020
  Matlab Finite Elements for Design, Evaluation and Analysis of Structures
  Professor Filip C. Filippou (filippou@berkeley.edu)
  Department of Civil and Environmental Engineering, UC Berkeley
  Copyright(c) 1998-2020. The Regents of the University of California. All Rights Reserved.
  =========================================================================================</pre>
<!-- <div class="fragment"><pre class="comment">% S_TRANSIENT_MULTISTEPwSD : script for multi-step transient analysis including initialization
                             under given load history(ies) with automatic time step division and rescaling 

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
<div class="fragment"><pre>0001 <span class="comment">%% S_TRANSIENT_MULTISTEPwSD : script for multi-step transient analysis including initialization</span>
0002 <span class="comment">%                             under given load history(ies) with automatic time step division and rescaling</span>
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
0016 <span class="comment">%   DEFINE parameters RescaleFac, SubdivFac and maxsubdiv in the script</span>
0017 <span class="comment">%   NOTE : the plot counter variable pc is set to one, if not present in the workspace</span>
0018 <span class="comment">%%  ****************************************************************************************</span>
0019 
0020 <span class="comment">%% initialize state (if necessary)</span>
0021 <span class="keyword">if</span> ~exist(<span class="string">'State'</span>,<span class="string">'var'</span>), State = Initialize_State(Model,ElemData); <span class="keyword">end</span>
0022 State = TransientInitialize (Model,ElemData,Loading,State);
0023 <span class="keyword">if</span> ~exist(<span class="string">'pc'</span>,<span class="string">'var'</span>)
0024    pc = 1;    <span class="comment">% initialize plot counter</span>
0025    State    = Structure (<span class="string">'forc'</span>,Model,ElemData,State);
0026    Post(pc) = Structure (<span class="string">'post'</span>,Model,ElemData,State);
0027 <span class="keyword">end</span>
0028 <span class="keyword">if</span> ~exist(<span class="string">'RescaleFac'</span>,<span class="string">'var'</span>), RescaleFac = 1.7; <span class="keyword">end</span>
0029 <span class="keyword">if</span> ~exist(<span class="string">'SubdivFac'</span>, <span class="string">'var'</span>), SubdivFac  = 1.7; <span class="keyword">end</span>
0030 <span class="keyword">if</span> ~exist(<span class="string">'maxsubdiv'</span>, <span class="string">'var'</span>), maxsubdiv  = 5; <span class="keyword">end</span>
0031 <span class="comment">%% retrieve time step increment</span>
0032 Deltat   = SolStrat.TimeStrat.Deltat;
0033 DeltatOr = Deltat;
0034 subcount = 0;
0035 <span class="comment">%% perform multi-step transient analysis</span>
0036 <span class="keyword">while</span> ( State.Time &lt; Tmax )
0037    [State,SolStrat] = TransientIncrement (Model,ElemData,Loading,State,SolStrat);
0038    <span class="keyword">if</span> State.ConvFlag 
0039       [State,SolStrat] = TransientIterate (Model,ElemData,Loading,State,SolStrat);
0040    <span class="keyword">else</span>
0041       SolStrat.ConvFlag = false;
0042    <span class="keyword">end</span>
0043    <span class="keyword">if</span> (SolStrat.ConvFlag)
0044       subcount = 0;
0045       Deltat   = min ([Deltat*RescaleFac DeltatOr]);
0046       SolStrat.TimeStrat.Deltat = Deltat;
0047       State = Update_TransientState (Model,ElemData,State,SolStrat);
0048       GoodState = State;
0049       <span class="comment">% update plot counter and store results</span>
0050       pc = pc+1;
0051       Post(pc) = Structure (<span class="string">'post'</span>,Model,ElemData,State);
0052    <span class="keyword">else</span>
0053       fprintf(<span class="string">'\nSubdividing time step and trying again \n'</span>);
0054       Time   = State.Time;
0055       State  = GoodState;
0056       State.Time = Time - Deltat;
0057       Deltat = Deltat/SubdivFac;
0058       SolStrat.TimeStrat.Deltat = Deltat;
0059       subcount = subcount + 1;
0060       <span class="keyword">if</span> (subcount&gt;maxsubdiv)
0061          fprintf (<span class="string">'\nNo convergence at time step %10.5e; last good state saved \n\n'</span>,State.Time);
0062          <span class="keyword">break</span>
0063       <span class="keyword">else</span>
0064          <span class="keyword">continue</span>
0065       <span class="keyword">end</span>
0066    <span class="keyword">end</span>
0067 <span class="keyword">end</span></pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->