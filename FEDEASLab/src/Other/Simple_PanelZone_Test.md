
<!-- <a name="_top"></a>
<div><a href="../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="index.md">Other</a> &gt; Simple_PanelZone_Test.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../index.md"><img alt="<" border="0" src="../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Other&nbsp;<img alt=">" border="0" src="../../../../../right.png"></a></td></tr></table>-->
# `Simple_PanelZone_Test`
<!-- <h1>Simple_PanelZone_Test
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

%

<!-- <div class="box"><strong>%</strong></div> -->

## <a name="_synopsis"></a>Syntax

`This is a script file.` 
## <a name="_description"></a>Description

<pre class="comment">%</pre>
<!-- <div class="fragment"><pre class="comment">%</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../../../matlabicon.gif)">
<li><a href="../../../../../../../FEDEASLab/src/Utilities/CleanStart" class="code" title="">CleanStart</a>	CLEANSTART initializes workspace for new analysis</li></ul>
This function is called by:
<ul style="list-style-image:url(../../../../../matlabicon.gif)">
</ul>
<!-- crossreference -->



<h2><a name="_source"></a>SOURCE CODE</h2>
<div class="fragment"><pre>0001 <span class="comment">%%</span>
0002 
0003 <span class="comment">%% Clear workspace memory and close all windows</span>
0004 <a href="../../../../../../../FEDEASLab/src/Utilities/CleanStart.md" class="code" title="">CleanStart</a>
0005 
0006 <span class="comment">%% Model definition</span>
0007 <span class="comment">% input data</span>
0008 XYZ (1,:) = [   0    0 ];
0009 XYZ (2,:) = [ 14.5   0 ];
0010 XYZ (3,:) = [ 15.5   0 ];
0011 XYZ (4,:) = [ 30.0   0 ];
0012 XYZ (5,:) = [ 15   -0.6];
0013 XYZ (6,:) = [ 15  -10.0];
0014 XYZ (7,:) = [ 15    0.6];
0015 XYZ (8,:) = [ 15   10.0];
0016 
0017 <span class="comment">% connectivity array</span>
0018 CON{1} = [ 1 2 ];
0019 CON{2} = [ 3 4 ];
0020 CON{3} = [ 5 6 ];
0021 CON{4} = [ 7 8 ];
0022 CON{5} = [ 5 3 7 2 ];
0023 <span class="comment">% CON{5} = [ 2 5 ];</span>
0024 <span class="comment">% CON{6} = [ 3 5 ];</span>
0025 <span class="comment">% CON{7} = [ 2 7 ];</span>
0026 <span class="comment">% CON{8} = [ 3 7 ];</span>
0027 
0028 <span class="comment">% boundary conditions (1 = restrained,  0 = free)</span>
0029 BOUN(1,:) = [ 1 1 0 ];
0030 BOUN(4,:) = [ 0 1 0 ];
0031 BOUN(6,:) = [ 0 1 0 ];
0032 <span class="comment">% BOUN(8,:) = [ 1 0 0 ];</span>
0033 
0034 <span class="comment">% specify element type</span>
0035 [ElemName{1:4}] = deal(<span class="string">'LE2dFrm'</span>);
0036  ElemName{5}    = <span class="string">'InelPanelZone'</span>;
0037 <span class="comment">% [ElemName{1:8}] = deal('LE2dFrm');</span>
0038 
0039 Model = Create_Model (XYZ,CON,BOUN,ElemName);
0040 
0041 <span class="comment">% plot parameters</span>
0042 <span class="comment">% -------------------------------------------------------------------------</span>
0043 WinXr = 0.40;  <span class="comment">% X-ratio of plot window to screen size</span>
0044 WinYr = 0.80;  <span class="comment">% Y-ratio of plot window to screen size</span>
0045 <span class="comment">% -------------------------------------------------------------------------</span>
0046 <span class="comment">%% Post-processing functions on Model (optional)</span>
0047 <span class="comment">% plot and label model for checking (optional)</span>
0048 Create_Window (WinXr,WinYr);       <span class="comment">% open figure window</span>
0049 PlotOpt.PlBnd = <span class="string">'yes'</span>;
0050 <span class="comment">% PlotOpt.PlNod = 'yes';</span>
0051 Plot_Model  (Model,[],PlotOpt);    <span class="comment">% plot model (optional)</span>
0052 Label_Model (Model);               <span class="comment">% label model (optional)</span>
0053 clear PlotOpt
0054 
0055 <span class="comment">%% Element Properties</span>
0056 <span class="keyword">for</span> el=1:4
0057   ElemData{el}.E = 1000;
0058   ElemData{el}.A = 10;
0059   ElemData{el}.I = 80;
0060 <span class="keyword">end</span>
0061 ElemData{5}.t = 2;
0062 ElemData{5}.d = [ 0.5 ; 0.6 ];
0063 ElemData{5}.nIP = 2;
0064 ElemData{5}.MatName = <span class="string">'LEIso2dMat'</span>;
0065 ElemData{5}.MatData.E  = 1000;
0066 ElemData{5}.MatData.nu = 0.3;
0067 
0068 <span class="comment">% check element property data</span>
0069 ElemData = Structure (<span class="string">'chec'</span>,Model,ElemData);
0070 
0071 <span class="comment">%% Loading specification</span>
0072 Pe(8,1) = 50;
0073 Loading = Create_Loading (Model,Pe);
0074 
0075 <span class="comment">%% perform linear elastic analysis</span>
0076 <span class="comment">% perform single linear step</span>
0077 State = LinearStep (Model, ElemData, Loading);
0078 
0079 <span class="comment">%% post-processing</span>
0080 <span class="comment">% store element response for later post-processing, if necessary</span>
0081 Post = Structure (<span class="string">'post'</span>,Model,ElemData,State);
0082 
0083 <span class="comment">% plot deformed shape of structural model</span>
0084 <span class="comment">% PlotOpt.MAGF = 10;                 % magnification factor for deformed configuration</span>
0085 <span class="comment">% Create_Window (WinXr,WinYr);       % open figure window</span>
0086 <span class="comment">% Plot_Model(Model);</span>
0087 <span class="comment">% Plot_Model(Model,State.U);</span>
0088 <span class="comment">% Plot_DeformedStructure (Model,ElemData,Post.U,Post,PlotOpt);</span></pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->