
<!-- <a name="_top"></a>
<div><a href="../../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="../index.md">Utilities</a> &gt; <a href="index.md">PreProcessing</a> &gt; Create_MRFrame.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../../index.md"><img alt="<" border="0" src="../../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Utilities\PreProcessing&nbsp;<img alt=">" border="0" src="../../../../../../right.png"></a></td></tr></table>-->
# `Create_MRFrame`
<!-- <h1>Create_MRFrame
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

CREATE_FRAME generation of nodes and elements for regular N-story, M-bay MR frame

<!-- <div class="box"><strong>CREATE_FRAME generation of nodes and elements for regular N-story, M-bay MR frame</strong></div> -->

## <a name="_synopsis"></a>Syntax

`function Frame = Create_MRFrame (Lbv,Hsv,nsub)` 
## <a name="_description"></a>Description

<pre class="comment">CREATE_FRAME generation of nodes and elements for regular N-story, M-bay MR frame    
 FRAME = CREATE_MRFRAME (LBV,HSV,NSUB)
  function generates the node coordinates XYZ and element connectivity CON
  for a regular N-story, M-bay frame with bay spans in row vector LBV and
  story heights in row vector HSV; the optional row vector NSUB specifies
  the number of subelements for each frame girder 
  the function returns the generated information in data structure FRAME
  with fields XYZ (node coordinates), CON (element connectivity),
  CINDX (column index by story), GINDX (girder index by floor),
  NBY (no of bays), NST (no of stories), NC (no of columns), NG (no of girders)
  NN (no of nodes), NE (no of elements)</pre>
<!-- <div class="fragment"><pre class="comment">CREATE_FRAME generation of nodes and elements for regular N-story, M-bay MR frame    
 FRAME = CREATE_MRFRAME (LBV,HSV,NSUB)
  function generates the node coordinates XYZ and element connectivity CON
  for a regular N-story, M-bay frame with bay spans in row vector LBV and
  story heights in row vector HSV; the optional row vector NSUB specifies
  the number of subelements for each frame girder 
  the function returns the generated information in data structure FRAME
  with fields XYZ (node coordinates), CON (element connectivity),
  CINDX (column index by story), GINDX (girder index by floor),
  NBY (no of bays), NST (no of stories), NC (no of columns), NG (no of girders)
  NN (no of nodes), NE (no of elements)</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../../../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../../../../../matlabicon.gif)">
<li><a href="../../../../../../../../FEDEASLab/src/Other/Create_PanelZone.md" class="code" title="">Create_PanelZone</a>	% Clear memory and close any open windows</li></ul>
<!-- crossreference -->



<h2><a name="_source"></a>SOURCE CODE</h2>
<div class="fragment"><pre>0001 <a name="_sub0" href="#_subfunctions" class="code">function Frame = Create_MRFrame (Lbv,Hsv,nsub)</a>
0002 <span class="comment">%CREATE_FRAME generation of nodes and elements for regular N-story, M-bay MR frame</span>
0003 <span class="comment">% FRAME = CREATE_MRFRAME (LBV,HSV,NSUB)</span>
0004 <span class="comment">%  function generates the node coordinates XYZ and element connectivity CON</span>
0005 <span class="comment">%  for a regular N-story, M-bay frame with bay spans in row vector LBV and</span>
0006 <span class="comment">%  story heights in row vector HSV; the optional row vector NSUB specifies</span>
0007 <span class="comment">%  the number of subelements for each frame girder</span>
0008 <span class="comment">%  the function returns the generated information in data structure FRAME</span>
0009 <span class="comment">%  with fields XYZ (node coordinates), CON (element connectivity),</span>
0010 <span class="comment">%  CINDX (column index by story), GINDX (girder index by floor),</span>
0011 <span class="comment">%  NBY (no of bays), NST (no of stories), NC (no of columns), NG (no of girders)</span>
0012 <span class="comment">%  NN (no of nodes), NE (no of elements)</span>
0013 
0014 <span class="comment">%  =========================================================================================</span>
0015 <span class="comment">%  FEDEASLab - Release 5.1, July 2020</span>
0016 <span class="comment">%  Matlab Finite Elements for Design, Evaluation and Analysis of Structures</span>
0017 <span class="comment">%  Professor Filip C. Filippou (filippou@berkeley.edu)</span>
0018 <span class="comment">%  Department of Civil and Environmental Engineering, UC Berkeley</span>
0019 <span class="comment">%  Copyright(c) 1998-2020. The Regents of the University of California. All Rights Reserved.</span>
0020 <span class="comment">%  =========================================================================================</span>
0021 <span class="comment">%  function added                                                                    05-2015</span>
0022 <span class="comment">%  -----------------------------------------------------------------------------------------</span>
0023 
0024 <span class="comment">%%</span>
0025 <span class="comment">% number of stories nst</span>
0026 nst = length(Hsv);
0027 <span class="comment">% number of bays</span>
0028 nby = length(Lbv);
0029 
0030 <span class="keyword">if</span> nargin&lt;3
0031    nsub = ones(1,nby);
0032 <span class="keyword">else</span>
0033    <span class="keyword">if</span> isempty(nsub), nsub = ones(1,nby); <span class="keyword">end</span>
0034 <span class="keyword">end</span>
0035 <span class="keyword">if</span> length(nsub)==1, nsub = nsub.*ones(1,nby); <span class="keyword">end</span>
0036 Frame.nsub = nsub;
0037 
0038 <span class="comment">%% generate node coordinates</span>
0039 <span class="comment">% subdivide each girder element ng into nsub(ng) subelements, if required</span>
0040 Lbs = cell(1,nby);
0041 Lg  = Lbv./nsub;
0042 <span class="keyword">for</span> ng = 1:nby
0043    Lbs{ng} = repmat(Lg(ng),1,nsub(ng));
0044 <span class="keyword">end</span>
0045 Lbs = [Lbs{:}];
0046 <span class="comment">% generate X-coordinates Xco at bay ends (origin assumed to be zero)</span>
0047 Xco = cumsum([0 Lbv]);
0048 <span class="comment">% X-coordinates Xcs at subdivided girder ends</span>
0049 Xcs = cumsum([0 Lbs]);
0050 
0051 <span class="comment">% generate Y-coordinate Ycb at base (ground level assumed to be zero)</span>
0052 Ycb = 0;
0053 <span class="comment">% generate Y-coordinate Ycb at story levels</span>
0054 Yco = cumsum(Hsv);
0055 
0056 <span class="comment">% generate mesh grid for base node coordinates</span>
0057 [Ymb,Xmb] = meshgrid(Ycb',Xco');
0058 <span class="comment">% generate mesh grid for frame stories</span>
0059 [Ym,Xm]   = meshgrid(Yco',Xcs');
0060 
0061 <span class="comment">% store node coordinates in array XYZ</span>
0062 XYZ = [ [Xmb(:);Xm(:)] [Ymb(:);Ym(:)] ];
0063 
0064 <span class="comment">%% generate element connectivity</span>
0065 nc   = nby+1;     <span class="comment">% no of columns per story</span>
0066 nstr = 1;         <span class="comment">% start element counter</span>
0067 <span class="comment">% ng   = nby*nsub;  % number of girder elements</span>
0068 ng   = sum(nsub);
0069 
0070 <span class="comment">% generate columns for first story</span>
0071 CIndx = cell(nst,1); 
0072 ncm   = 1;
0073 ncs   = ncm + nc;
0074 ncp   = ncs + ng + 1;
0075 CON(nstr:nstr+nby,:) = [ (1:ncs-1)' [ncs;ncs+cumsum(nsub)'] ];
0076 nend = size(CON,1);
0077 nstr = nend+1;
0078 CIndx{1} = 1:nend;
0079 <span class="comment">% generate columns for second to nst story</span>
0080 <span class="keyword">for</span> m = 2:nst
0081    ncm = ncs;
0082    ncs = ncp;
0083    ncp = ncs + ng + 1;
0084    CON(nstr:nstr+nby,:) = [ [ncm; ncm+cumsum(nsub)'] [ncs;ncs+cumsum(nsub)'] ];
0085    nend = size(CON,1);
0086    CIndx{m} = nstr:nend;
0087    nstr = nend+1;
0088 <span class="keyword">end</span>
0089 <span class="comment">% store in Frame column index CIndx</span>
0090 Frame.CIndx = CIndx;
0091 
0092 <span class="comment">% generate girders</span>
0093 GIndx = cell(nst,1);
0094 ncp = nc;
0095 <span class="keyword">for</span> m = 1:nst
0096    ncs = ncp + 1;
0097    ncp = ncs + ng;
0098    CON(nstr:nstr+(ng-1),:) = [ (ncs:ncp-1)' (ncs+1:ncp)' ];
0099    nend = size(CON,1);
0100    GIndx{m} = nstr:nend;
0101    nstr = nend+1;
0102 <span class="keyword">end</span>
0103 <span class="comment">% store in Frame girder index GIndx</span>
0104 Frame.GIndx = GIndx;
0105 
0106 <span class="comment">% store number of stories, bays, columns and girders in Frame</span>
0107 Frame.nst = nst;
0108 Frame.nby = nby;
0109 Frame.nc  = nc;
0110 Frame.ng  = ng;
0111 <span class="comment">% store number of nodes and number of elements</span>
0112 Frame.nn = size(XYZ,1);
0113 Frame.ne = length(CON);
0114 <span class="comment">% store node coordinates and connectivity information in Frame</span>
0115 Frame.XYZ = XYZ;
0116 Frame.CON = CON;
0117 <span class="comment">% store story heights and bay spans in Frame</span>
0118 Frame.Hsv = Hsv;
0119 Frame.Lbv = Lbv;</pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->