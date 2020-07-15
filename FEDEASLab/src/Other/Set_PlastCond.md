
<!-- <a name="_top"></a>
<div><a href="../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="index.md">Other</a> &gt; Set_PlastCond.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../index.md"><img alt="<" border="0" src="../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Other&nbsp;<img alt=">" border="0" src="../../../../../right.png"></a></td></tr></table>-->
# `Set_PlastCond`
<!-- <h1>Set_PlastCond
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

separate truss and frame elements

<!-- <div class="box"><strong>separate truss and frame elements</strong></div> -->

## <a name="_synopsis"></a>Syntax

`function Ain = Set_PlastCond (Model,ElemData)` 
## <a name="_description"></a>Description

<pre class="comment"> separate truss and frame elements</pre>
<!-- <div class="fragment"><pre class="comment"> separate truss and frame elements</pre></div> -->

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
<div class="fragment"><pre>0001 <a name="_sub0" href="#_subfunctions" class="code">function Ain = Set_PlastCond (Model,ElemData)</a>
0002 
0003 <span class="comment">% separate truss and frame elements</span>
0004 iNp = cellfun(@(x) contains(x,<span class="string">'Truss'</span>),Model.ElemName);
0005 iMp = cellfun(@(x) contains(x,<span class="string">'2dFrm'</span>),Model.ElemName);
0006 el  = 1:Model.ne;
0007 tel = el(iNp);
0008 fel = el(iMp);
0009 
0010 LimitSurf = cell(Model.ne,1);
0011 <span class="comment">% for frame elements</span>
0012 <span class="keyword">for</span> el = fel
0013   Npv = ElemData{el}.Np;
0014   <span class="keyword">if</span> isscalar(Npv),  Np = [Npv Npv]; <span class="keyword">else</span>, Np = Npv; <span class="keyword">end</span>
0015   Mp = ElemData{el}.Mp;
0016   <span class="keyword">if</span> size(Mp,2)==1, Mp = repmat(Mp,1,2); <span class="keyword">end</span>
0017   <span class="keyword">if</span> size(Mp,1)==1, Mp = repmat(Mp,2,1); <span class="keyword">end</span>
0018   Mpi = Mp(:,1);
0019   Mpj = Mp(:,2);
0020   <span class="keyword">if</span> isfield(ElemData{el},<span class="string">'NMOpt'</span>)
0021     NMOpt = ElemData{el}.NMOpt;
0022   <span class="keyword">else</span>
0023     NMOpt = <span class="string">'None'</span>;
0024   <span class="keyword">end</span>
0025   <span class="comment">%% limit surfaces for frame elements</span>
0026   <span class="keyword">switch</span> NMOpt
0027     <span class="keyword">case</span> {<span class="string">'None'</span>,<span class="string">'none'</span>}
0028       LimitSurf{el} = [ diag([1/Np(1);1/Mpi(2);1/Mpj(1)]);
0029                        -diag([1/Np(2);1/Mpi(1);1/Mpj(2)])];
0030     <span class="keyword">case</span> <span class="string">'Dmnd'</span>
0031       LimitSurf{el} = [ 1/Np(1)   1/Mpi(2)    0;
0032                        -1/Np(2)   1/Mpi(2)    0;
0033                         1/Np(1)  -1/Mpi(1)    0;
0034                        -1/Np(2)  -1/Mpi(1)    0;
0035                         1/Np(1)    0         1/Mpj(1);
0036                        -1/Np(2)    0         1/Mpj(1);
0037                         1/Np(1)    0        -1/Mpj(2);
0038                        -1/Np(2)    0        -1/Mpj(2)];
0039     <span class="keyword">case</span> <span class="string">'AISC'</span>
0040       LimitSurf{el} = [  1/Np(1)   (8/9)/Mpi(2)      0;
0041                        1/2/Np(1)       1/Mpi(2)      0;
0042                         -1/Np(2)   (8/9)/Mpi(2)      0;
0043                       -1/2/Np(2)       1/Mpi(2)      0;
0044                          1/Np(1)  -(8/9)/Mpi(1)      0;
0045                        1/2/Np(1)      -1/Mpi(1)      0;
0046                         -1/Np(2)  -(8/9)/Mpi(1)      0;
0047                       -1/2/Np(2)      -1/Mpi(1)      0;
0048                          1/Np(1)        0       (8/9)/Mpj(1);
0049                        1/2/Np(1)        0           1/Mpj(1);
0050                         -1/Np(2)        0       (8/9)/Mpj(1);
0051                       -1/2/Np(2)        0           1/Mpj(1);
0052                          1/Np(1)        0      -(8/9)/Mpj(2);
0053                        1/2/Np(1)        0          -1/Mpj(2);
0054                         -1/Np(2)        0      -(8/9)/Mpj(2);
0055                       -1/2/Np(2)        0          -1/Mpj(2)];
0056   <span class="keyword">end</span>
0057 <span class="keyword">end</span>
0058 <span class="comment">% for truss elements</span>
0059 <span class="keyword">for</span> el = tel
0060   Npv = ElemData{el}.Np;
0061   <span class="keyword">if</span> isscalar(Npv),  Np = [Npv Npv]; <span class="keyword">else</span>, Np = Npv; <span class="keyword">end</span>
0062   LimitSurf{el} = [ 1/Np(1) ; -1/Np(2) ];
0063 <span class="keyword">end</span>
0064 Ain = blkdiag (LimitSurf{:});</pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->