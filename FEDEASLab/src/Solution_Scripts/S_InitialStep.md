
<!-- <a name="_top"></a>
<div><a href="../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="index.md">Solution_Scripts</a> &gt; S_InitialStep.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../index.md"><img alt="<" border="0" src="../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Solution_Scripts&nbsp;<img alt=">" border="0" src="../../../../../right.png"></a></td></tr></table>-->
# `S_InitialStep`
<!-- <h1>S_InitialStep
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

% S_INITIALSTEP : script for initial step of incremental analysis

<!-- <div class="box"><strong>% S_INITIALSTEP : script for initial step of incremental analysis</strong></div> -->

## <a name="_synopsis"></a>Syntax

`This is a script file.` 
## <a name="_description"></a>Description

<pre class="comment">% S_INITIALSTEP : script for initial step of incremental analysis

  =========================================================================================
  FEDEASLab - Release 5.1, July 2020
  Matlab Finite Elements for Design, Evaluation and Analysis of Structures
  Professor Filip C. Filippou (filippou@berkeley.edu)
  Department of Civil and Environmental Engineering, UC Berkeley
  Copyright(c) 1998-2020. The Regents of the University of California. All Rights Reserved.
  =========================================================================================</pre>
<!-- <div class="fragment"><pre class="comment">% S_INITIALSTEP : script for initial step of incremental analysis

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
<div class="fragment"><pre>0001 <span class="comment">%% S_INITIALSTEP : script for initial step of incremental analysis</span>
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
0012 <span class="comment">%   BEFORE INVOKING THE SCRIPT YOU NEED TO</span>
0013 <span class="comment">%   DEFINE parameters in SolStrat</span>
0014 <span class="comment">%%  ****************************************************************************************</span>
0015 
0016 <span class="comment">%% initialize state</span>
0017 State = Initialize_State(Model,ElemData);
0018 [State,SolStrat] = Initialize (Model,ElemData,Loading,State,SolStrat);
0019 
0020 pc = 1;    <span class="comment">% plot counter</span>
0021 State    = Structure (<span class="string">'forc'</span>,Model,ElemData,State);
0022 Post(pc) = Structure (<span class="string">'post'</span>,Model,ElemData,State);
0023 
0024 <span class="comment">%% perform single load step</span>
0025 [State,SolStrat] = Increment (Model,ElemData,Loading,State,SolStrat);
0026 <span class="keyword">if</span> State.ConvFlag
0027    [State,SolStrat] = Iterate (Model,ElemData,Loading,State,SolStrat);
0028 <span class="keyword">else</span>
0029    SolStrat.ConvFlag = false;
0030 <span class="keyword">end</span>
0031 <span class="keyword">if</span> (SolStrat.ConvFlag)
0032    State = Update_State (Model,ElemData,State);    
0033    GoodState = State;
0034    <span class="comment">% update plot counter and store results</span>
0035    pc = pc+1;
0036    Post(pc) = Structure (<span class="string">'post'</span>,Model,ElemData,State);
0037 <span class="keyword">else</span>
0038    fprintf (<span class="string">'\nNo convergence in initial step; check data and/or no of iterations \n'</span>);
0039 <span class="keyword">end</span></pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->