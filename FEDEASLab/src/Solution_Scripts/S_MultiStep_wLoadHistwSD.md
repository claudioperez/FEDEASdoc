
<!-- <a name="_top"></a>
<div><a href="../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="index.md">Solution_Scripts</a> &gt; S_MultiStep_wLoadHistwSD.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../index.md"><img alt="<" border="0" src="../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Solution_Scripts&nbsp;<img alt=">" border="0" src="../../../../../right.png"></a></td></tr></table>-->
# `S_MultiStep_wLoadHistwSD`
<!-- <h1>S_MultiStep_wLoadHistwSD
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

% S_MULTISTEP_wLOADHISTwSD : script for multi-step incremental analysis including initialization

<!-- <div class="box"><strong>% S_MULTISTEP_wLOADHISTwSD : script for multi-step incremental analysis including initialization</strong></div> -->

## <a name="_synopsis"></a>Syntax

`This is a script file.` 
## <a name="_description"></a>Description

<pre class="comment">% S_MULTISTEP_wLOADHISTwSD : script for multi-step incremental analysis including initialization
                   under given load history(ies) with automatic time step division and rescaling 

  =========================================================================================
  FEDEASLab - Release 5.1, July 2020
  Matlab Finite Elements for Design, Evaluation and Analysis of Structures
  Professor Filip C. Filippou (filippou@berkeley.edu)
  Department of Civil and Environmental Engineering, UC Berkeley
  Copyright(c) 1998-2020. The Regents of the University of California. All Rights Reserved.
  =========================================================================================</pre>
<!-- <div class="fragment"><pre class="comment">% S_MULTISTEP_wLOADHISTwSD : script for multi-step incremental analysis including initialization
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
<div class="fragment"><pre>0001 <span class="comment">%% S_MULTISTEP_wLOADHISTwSD : script for multi-step incremental analysis including initialization</span>
0002 <span class="comment">%                   under given load history(ies) with automatic time step division and rescaling</span>
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
0020 <span class="comment">%% initialize state</span>
0021 <span class="keyword">if</span> ~exist(<span class="string">'State'</span>,<span class="string">'var'</span>), State = Initialize_State (Model,ElemData); <span class="keyword">end</span>
0022 [State,SolStrat] = Initialize (Model,ElemData,Loading,State,SolStrat);
0023 <span class="comment">% ------------------------------------------------------------------------------------------</span>
0024 <span class="keyword">if</span> ~exist(<span class="string">'pc'</span>,<span class="string">'var'</span>)
0025    pc = 1;    <span class="comment">% initialize plot counter</span>
0026    State    = Structure (<span class="string">'forc'</span>,Model,ElemData,State);
0027    Post(pc) = Structure (<span class="string">'post'</span>,Model,ElemData,State);
0028 <span class="keyword">end</span>
0029 <span class="comment">% ------------------------------------------------------------------------------------------</span>
0030 dc = 0;       <span class="comment">% debug state counter</span>
0031 <span class="keyword">if</span> ~exist(<span class="string">'DebStTime'</span>,<span class="string">'var'</span>), DebStTime = Inf; <span class="keyword">end</span>    <span class="comment">% initialize debug start time</span>
0032 <span class="keyword">if</span> ~exist(<span class="string">'DebEnTime'</span>,<span class="string">'var'</span>), DebEnTime =   0; <span class="keyword">end</span>    <span class="comment">% initialize debug end   time</span>
0033 <span class="comment">% ------------------------------------------------------------------------------------------</span>
0034 <span class="keyword">if</span> exist(<span class="string">'RescaleFac'</span>,<span class="string">'var'</span>) == 0, RescaleFac = 1.7; <span class="keyword">end</span>
0035 <span class="keyword">if</span> exist(<span class="string">'SubdivFac'</span>, <span class="string">'var'</span>) == 0, SubdivFac  = 1.7; <span class="keyword">end</span>
0036 <span class="keyword">if</span> exist(<span class="string">'maxsubdiv'</span>, <span class="string">'var'</span>) == 0, maxsubdiv  =  20; <span class="keyword">end</span>
0037 <span class="comment">%% retrieve time step increment</span>
0038 Deltat   = SolStrat.IncrStrat.Deltat;
0039 DeltatOr = Deltat;
0040 subcount = 0;
0041 <span class="comment">% ------------------------------------------------------------------------------------------</span>
0042 <span class="comment">%% perform multi-step incremental analysis</span>
0043 <span class="keyword">while</span> ( State.Time+Deltat &lt;= Tmax + 1e-12 )
0044   SolStrat.Debug = (State.Time+Deltat &gt;= DebStTime &amp;&amp; State.Time+Deltat &lt;= DebEnTime + 1e-12);
0045   [State,SolStrat] = Increment (Model,ElemData,Loading,State,SolStrat);
0046   <span class="keyword">if</span> State.ConvFlag
0047     [State,SolStrat] = Iterate (Model,ElemData,Loading,State,SolStrat);
0048   <span class="keyword">else</span>
0049     SolStrat.ConvFlag = false;
0050   <span class="keyword">end</span>
0051   <span class="keyword">if</span> SolStrat.Debug
0052     dc = dc + 1;
0053     DebState (dc) = State.Debug;
0054     State = rmfield(State,<span class="string">'Debug'</span>);
0055   <span class="keyword">end</span>
0056   <span class="keyword">if</span> (SolStrat.ConvFlag)
0057     subcount = 0;
0058     Deltat   = min ([Deltat*RescaleFac DeltatOr]);
0059     SolStrat.IncrStrat.Deltat = Deltat;
0060     State = Update_State (Model,ElemData,State);
0061     GoodState = State;
0062     <span class="comment">% update plot counter and store results</span>
0063     pc = pc+1;
0064     Post(pc) = Structure (<span class="string">'post'</span>,Model,ElemData,State);
0065   <span class="keyword">else</span>
0066     fprintf(<span class="string">'\nSubdividing time step and trying again \n'</span>);
0067     Time   = State.Time;
0068     State  = GoodState;
0069     State.Time = Time - Deltat;
0070     Deltat = Deltat/SubdivFac;
0071     SolStrat.IncrStrat.Deltat = Deltat;
0072     subcount = subcount + 1;
0073     <span class="keyword">if</span> (subcount&gt;maxsubdiv)
0074       fprintf (<span class="string">'\nNo convergence at time step %10.5e; last good state saved \n\n'</span>,State.Time);
0075       <span class="keyword">break</span>
0076     <span class="keyword">else</span>
0077       <span class="keyword">continue</span>
0078     <span class="keyword">end</span>
0079   <span class="keyword">end</span>
0080 <span class="keyword">end</span></pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->