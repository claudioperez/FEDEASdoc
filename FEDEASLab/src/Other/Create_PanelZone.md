
<!-- <a name="_top"></a>
<div><a href="../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="index.md">Other</a> &gt; Create_PanelZone.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../index.md"><img alt="<" border="0" src="../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Other&nbsp;<img alt=">" border="0" src="../../../../../right.png"></a></td></tr></table>-->
# `Create_PanelZone`
<!-- <h1>Create_PanelZone
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

% Clear memory and close any open windows

<!-- <div class="box"><strong>% Clear memory and close any open windows</strong></div> -->

## <a name="_synopsis"></a>Syntax

`This is a script file.` 
## <a name="_description"></a>Description

<pre class="comment">% Clear memory and close any open windows</pre>
<!-- <div class="fragment"><pre class="comment">% Clear memory and close any open windows</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../../../matlabicon.gif)">
<li><a href="../../../../../../../FEDEASLab/src/Utilities/CleanStart" class="code" title="">CleanStart</a>	CLEANSTART initializes workspace for new analysis</li><li><a href="../../../../../../../FEDEASLab/src/Utilities/PreProcessing/Create_MRFrame" class="code" title="function Frame = Create_MRFrame (Lbv,Hsv,nsub)">Create_MRFrame</a>	CREATE_FRAME generation of nodes and elements for regular N-story, M-bay MR frame</li><li><a href="../../../../../../../FEDEASLab/src/Utilities/Units" class="code" title="">Units</a>	% Script file for common unit definition with Imperial units as default</li></ul>
This function is called by:
<ul style="list-style-image:url(../../../../../matlabicon.gif)">
</ul>
<!-- crossreference -->



<h2><a name="_source"></a>SOURCE CODE</h2>
<div class="fragment"><pre>0001 <span class="comment">%% Clear memory and close any open windows</span>
0002 <a href="../../../../../../../FEDEASLab/src/Utilities/CleanStart.md" class="code" title="">CleanStart</a>
0003 <span class="comment">% insert file of units</span>
0004 <a href="../../../../../../../FEDEASLab/src/Utilities/Units.md" class="code" title="">Units</a>
0005 
0006 <span class="comment">% save name of script in variable ModelName</span>
0007 ModelName = mfilename;
0008 
0009 <span class="comment">%% no of stories nst</span>
0010 nst = 4;
0011 <span class="comment">%% no of bays nby</span>
0012 nby = 3;
0013 
0014 <span class="comment">%% typical story height</span>
0015 Hs  = 13*ft;
0016 <span class="comment">% specify individual story heights in row vector</span>
0017 Hsv = [Hs+2*ft repmat(Hs,1,nst-1)];
0018 
0019 <span class="comment">%% typical bay length</span>
0020 Lb = 20*ft;
0021 <span class="comment">% specify individual bay lengths in row vector</span>
0022 Lbv = repmat(Lb,1,nby);
0023 <span class="comment">% number of girder subelements</span>
0024 nsub = 1;
0025 
0026 <span class="comment">%% call function to generate node coordinates, element connectivity</span>
0027 Frame = <a href="../../../../../../../FEDEASLab/src/Utilities/PreProcessing/Create_MRFrame.md" class="code" title="function Frame = Create_MRFrame (Lbv,Hsv,nsub)">Create_MRFrame</a> (Lbv,Hsv,nsub);
0028 
0029 ElemSize_4S3BFrame
0030 
0031 nn  = Frame.nn;
0032 ne  = Frame.ne;
0033 XYZ = Frame.XYZ;
0034 CON = Frame.CON;
0035 
0036 JntOff = Create_JntOffsets (Frame,<span class="string">'AISC_Section'</span>);
0037 
0038 <span class="comment">% [XYZ,CON] = Add_PanelZone(XYZ,CON,JntOff);</span>
0039 
0040 <span class="comment">%% the following commands have been incorporated in the function Add_PanelZone</span>
0041 <span class="comment">% ------------------------------------------------------------------------------------------</span>
0042 <span class="comment">% create data structure for panel connectivity</span>
0043 Panel(1:nn) = struct(<span class="string">'CON'</span>,[]);
0044 
0045 nc = nn;
0046 <span class="comment">% loop over elements and add additional nodes for panel zone</span>
0047 <span class="keyword">for</span> el = 1:ne
0048   ni  = CON(el,1);
0049   nj  = CON(el,2);
0050   xyz = XYZ([ni nj],:);
0051   xyzAdd = xyz + JntOff{el}';
0052   xyzTmp = [xyz;xyzAdd];
0053   [~,iA] = unique(xyzTmp,<span class="string">'rows'</span>);
0054   IAdd = any(iA==3);
0055   JAdd = any(iA==4);
0056   <span class="keyword">if</span> IAdd
0057     nc = nc+1;
0058     CON(el,1) = nc;
0059     Panel(ni).CON = [ Panel(ni).CON  nc ];
0060     XYZ(nc,:) = xyzTmp(3,:);
0061   <span class="keyword">end</span>
0062   <span class="keyword">if</span> JAdd
0063     nc = nc+1;
0064     CON(el,2) = nc;
0065     Panel(nj).CON = [ Panel(nj).CON  nc ];
0066     XYZ(nc,:) = xyzTmp(4,:);
0067   <span class="keyword">end</span>
0068 <span class="keyword">end</span>
0069 
0070 <span class="comment">% remove nodes without elements connecting to them</span>
0071 <span class="comment">% RetInd = index of nodes to retain</span>
0072 RetInd = arrayfun (@(nd) isempty(Panel(nd).CON),1:nn,<span class="string">'UniformOutput'</span>,false);
0073 RetInd = [RetInd{:}];
0074 NodOr  = 1:nn;
0075 <span class="comment">% node numbers to retain</span>
0076 RetNd  = NodOr(RetInd);
0077 
0078 nnTot  = size(XYZ,1);
0079 NodInd = [RetNd nn+1:nnTot];
0080 <span class="comment">% update coordinate array with</span>
0081 XYZ    = XYZ(NodInd,:);
0082 
0083 NdRem = nn-length(RetNd);
0084 NdIx  = CON&gt;NdRem;
0085 CON(NdIx) = CON(NdIx)-NdRem;
0086 
0087 RemInd = ~RetInd;
0088 Panel  = Panel(RemInd);
0089 
0090 nPan   = length(Panel);
0091 <span class="keyword">for</span> np = 1:nPan
0092   NdId = Panel(np).CON-NdRem;
0093   xyzp = XYZ(NdId,:);
0094   [~,N1] = max(xyzp(:,1));
0095   [~,N2] = max(xyzp(:,2));
0096   [~,N3] = min(xyzp(:,1));
0097   [~,N4] = min(xyzp(:,2));
0098   CONTmp = NdId ([ N1 N2 N3 N4 ]);
0099   
0100   <span class="keyword">if</span> N3==N4, CONTmp(3) = 0; <span class="keyword">end</span>
0101   <span class="keyword">if</span> N1==N4, CONTmp(1) = 0; <span class="keyword">end</span>
0102   <span class="keyword">if</span> N1==N2 || N2==N3, CONTmp(2) = 0; <span class="keyword">end</span>
0103   Panel(np).CON = CONTmp;
0104 <span class="keyword">end</span>
0105 
0106 <span class="comment">% if ~iscell(CON), CON = num2cell(CON,2); end</span>
0107 <span class="comment">% [CON{ne+1:ne+nPan}] = Panel(:).CON;</span>
0108 
0109 <span class="comment">%-------------------------------------------------------------------------------------------</span>
0110 
0111 <span class="comment">%% boundary conditions for fixed base of frame</span>
0112 <span class="comment">% find nodes at base</span>
0113 Bnodes = find(XYZ(:,2)==0);
0114 BOUN( Bnodes,:) = repmat([1 1 1],length(Bnodes),1);
0115 
0116 <span class="comment">%% specify element type (can change later)</span>
0117 ne = length(CON);
0118 [ElemName{1:ne}] = deal (<span class="string">'LE2dFrm'</span>);       <span class="comment">% 2d linear frame element</span>
0119 
0120 <span class="comment">%% generate Model data structure</span>
0121 Model = Create_SimpleModel (XYZ,CON,BOUN,ElemName);
0122 
0123 <span class="comment">% plot parameters</span>
0124 <span class="comment">% -------------------------------------------------------------------------</span>
0125 WinXr = 0.40;    <span class="comment">% X-ratio of plot window to screen size</span>
0126 WinYr = 0.80;    <span class="comment">% Y-ratio of plot window to screen size</span>
0127 <span class="comment">% -------------------------------------------------------------------------</span>
0128 
0129 Create_Window(WinXr,WinYr);
0130 PlotOpt.PlNod = <span class="string">'yes'</span>;
0131 PlotOpt.PlBnd = <span class="string">'yes'</span>;
0132 PlotOpt.LnWth = 1;
0133 PlotOpt.NodSF = 0.3;
0134 Plot_Model (Model,[],PlotOpt);    <span class="comment">% plot model</span>
0135 <span class="comment">% PlotOpt.FntSF = 0.4;</span>
0136 <span class="comment">% Label_Model (Model,PlotOpt);       % label model</span>
0137 
0138 clear PlotOpt
0139 
0140 <span class="comment">% el = 1:Frame.ne;</span>
0141 <span class="comment">% if ~iscell(Frame.CON), CON = num2cell(Frame.CON,2); end</span>
0142 <span class="comment">% ID = arrayfun (@(el) Frame.XYZ(CON{el},:),el,'UniformOutput',false);</span>
0143 <span class="comment">%</span>
0144 <span class="comment">% XYZAdd = ([ID{:}]+[JntOff{:}])';</span></pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->