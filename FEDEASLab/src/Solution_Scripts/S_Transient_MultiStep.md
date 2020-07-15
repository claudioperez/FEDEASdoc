
<!-- <a name="_top"></a>
<div><a href="../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="index.md">Solution_Scripts</a> &gt; S_Transient_MultiStep.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../index.md"><img alt="<" border="0" src="../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Solution_Scripts&nbsp;<img alt=">" border="0" src="../../../../../right.png"></a></td></tr></table>-->
# `S_Transient_MultiStep`
<!-- <h1>S_Transient_MultiStep
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

% S_TRANSIENT_MULTISTEP : script for multi-step transient analysis including initialization

<!-- <div class="box"><strong>% S_TRANSIENT_MULTISTEP : script for multi-step transient analysis including initialization</strong></div> -->

## <a name="_synopsis"></a>Syntax

`This is a script file.` 
## <a name="_description"></a>Description

<pre class="comment">% S_TRANSIENT_MULTISTEP : script for multi-step transient analysis including initialization
                          under given load history(ies) 

  =========================================================================================
  FEDEASLab - Release 5.1, July 2020
  Matlab Finite Elements for Design, Evaluation and Analysis of Structures
  Professor Filip C. Filippou (filippou@berkeley.edu)
  Department of Civil and Environmental Engineering, UC Berkeley
  Copyright(c) 1998-2020. The Regents of the University of California. All Rights Reserved.
  =========================================================================================</pre>
<!-- <div class="fragment"><pre class="comment">% S_TRANSIENT_MULTISTEP : script for multi-step transient analysis including initialization
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
<div class="fragment"><pre>0001 <span class="comment">%% S_TRANSIENT_MULTISTEP : script for multi-step transient analysis including initialization</span>
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
0019 <span class="comment">%% initialize state (if necessary)</span>
0020 <span class="keyword">if</span> ~exist(<span class="string">'State'</span>,<span class="string">'var'</span>), State = Initialize_State(Model,ElemData); <span class="keyword">end</span>
0021 State = TransientInitialize (Model,ElemData,Loading,State);
0022 <span class="keyword">if</span> ~exist(<span class="string">'pc'</span>,<span class="string">'var'</span>)
0023   pc = 1;    <span class="comment">% initialize plot counter</span>
0024   State    = Structure (<span class="string">'forc'</span>,Model,ElemData,State);
0025   Post(pc) = Structure (<span class="string">'post'</span>,Model,ElemData,State);
0026 <span class="keyword">end</span>
0027 
0028 FName = <span class="string">'PostFile'</span>;
0029 fcoun = 1;
0030 <span class="comment">%% perform multi-step transient analysis</span>
0031 <span class="keyword">while</span> ( State.Time&lt;Tmax )
0032   fprintf(<span class="string">'\n'</span>)
0033   disp ([<span class="string">'Time '</span>,num2str(State.Time)])  
0034   [State,SolStrat] = TransientIncrement (Model,ElemData,Loading,State,SolStrat);
0035   <span class="keyword">if</span> State.ConvFlag
0036     [State,SolStrat] = TransientIterate (Model,ElemData,Loading,State,SolStrat);
0037   <span class="keyword">else</span>
0038     SolStrat.ConvFlag = false;
0039   <span class="keyword">end</span>
0040   <span class="keyword">if</span> (SolStrat.ConvFlag)
0041     State = Update_TransientState (Model,ElemData,State,SolStrat);
0042     GoodState = State;
0043     <span class="comment">% update plot counter and store results</span>
0044     pc = pc+1;
0045     Post(pc) = Structure (<span class="string">'post'</span>,Model,ElemData,State);
0046     <span class="keyword">if</span> pc==2000
0047       Fstore = [FName num2str(fcoun)];
0048       save(Fstore,<span class="string">'Post'</span>);
0049       pc = 0;
0050       fcoun = fcoun+1;
0051       clearvars Post
0052     <span class="keyword">end</span>
0053   <span class="keyword">else</span>
0054     State = GoodState;
0055     fprintf (<span class="string">'\nNo convergence at time step %6.4g; last good state saved \n\n'</span>,State.Time);
0056     <span class="keyword">break</span>
0057   <span class="keyword">end</span>
0058 <span class="keyword">end</span></pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->