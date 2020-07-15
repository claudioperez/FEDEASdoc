
<!-- <a name="_top"></a>
<div><a href="../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="index.md">Other</a> &gt; InelPanelZone.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../index.md"><img alt="<" border="0" src="../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Other&nbsp;<img alt=">" border="0" src="../../../../../right.png"></a></td></tr></table>-->
# `InelPanelZone`
<!-- <h1>InelPanelZone
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

INELPANELZONE 4-node panel zone element with inelastic material

<!-- <div class="box"><strong>INELPANELZONE 4-node panel zone element with inelastic material</strong></div> -->

## <a name="_synopsis"></a>Syntax

`function ElemResp = InelPanelZone (action,el_no,xyz,ElemData,ElemState)` 
## <a name="_description"></a>Description

<pre class="comment">INELPANELZONE 4-node panel zone element with inelastic material
 ELEMRESP = INELPANELZONE (ACTION,EL_NO,XYZ,ELEMDATA,ELEMSTATE)
  response of 4-node panel zone element with inelastic material; 
  depending on the value of the character variable ACTION the function returns information
  in data structure ELEMRESP for the element with number EL_NO, end node coordinates XYZ,
  and material and loading properties in the data structure ELEMDATA.
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  When the character variable ACTION has one of the following values,
  the function performs the listed operations and returns the results in ELEMRESP:
  ACTION = 'size': report size of element arrays
           'chec': check element property data for omissions and assign default values
           'init': initialize element history variables
           'forc': report element resisting forces
           'stif': report element stiffness matrix and resisting forces
           'mass': report lumped mass vector and consistent mass matrix
           'post': report post-processing information
           'stre': stress recovery to element nodes
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The data structure ELEMRESP stands for the following data object(s) for each ACTION:
  ELEMRESP = ARSZ        for action = 'size' 
  ELEMRESP = ELEMDATA    for action = 'chec'
  ELEMRESP = ELEMSTATE   for action = 'init'
  ELEMRESP = ELEMSTATE   for action = 'stif'
  ELEMRESP = ELEMSTATE   for action = 'forc'
  ELEMRESP = ELEMMASS    for action = 'mass'
  ELEMRESP = ELEMPOST    for action = 'post'
  ELEMRESP = STRSREC     for action = 'stre'
  ELEMRESP is empty      for unsupported keywords
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ARSZ   is an Boolean array of size NDF x NEN,
         where NDF = number of DOFs/node, NEN = number of nodes,
         with unit values corresponding to the active element DOFs
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ELEMDATA is a data structure with element property information in fields
         t       = element thickness (default t=1)
         nIP     = number of integration points (default nIP=2)
         MatName = function name for material model
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ELEMSTATE is a data structure with the current element state; it has the fields
         u     = vector of total element displacements in global reference
         Du    = vector of element displacement increments from last convergence
         DDu   = vector of element displacement increments from last iteration
         ke    = element stiffness matrix in global reference; updated under ACTION = 'stif'
         p     = element resisting force vector in global reference; updated under ACTION = 'stif' or 'forc'
         Past  = element history variables at last converged state
         Pres  = current element history variables
         lamda = row vector of current load factor(s)
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ELEMPOST is a data structure with element response information for post-processing in fields
         Mat{i}.xyz = coordinates   of integration point i
         Mat{i}.eps = strain tensor at integration point i
         Mat{i}.sig = stress tensor at integration point i
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  STRSREC is a data structure with nodal stress information in field(s)
         sigNd = nodal stresses</pre>
<!-- <div class="fragment"><pre class="comment">INELPANELZONE 4-node panel zone element with inelastic material
 ELEMRESP = INELPANELZONE (ACTION,EL_NO,XYZ,ELEMDATA,ELEMSTATE)
  response of 4-node panel zone element with inelastic material; 
  depending on the value of the character variable ACTION the function returns information
  in data structure ELEMRESP for the element with number EL_NO, end node coordinates XYZ,
  and material and loading properties in the data structure ELEMDATA.
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  When the character variable ACTION has one of the following values,
  the function performs the listed operations and returns the results in ELEMRESP:
  ACTION = 'size': report size of element arrays
           'chec': check element property data for omissions and assign default values
           'init': initialize element history variables
           'forc': report element resisting forces
           'stif': report element stiffness matrix and resisting forces
           'mass': report lumped mass vector and consistent mass matrix
           'post': report post-processing information
           'stre': stress recovery to element nodes
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The data structure ELEMRESP stands for the following data object(s) for each ACTION:
  ELEMRESP = ARSZ        for action = 'size' 
  ELEMRESP = ELEMDATA    for action = 'chec'
  ELEMRESP = ELEMSTATE   for action = 'init'
  ELEMRESP = ELEMSTATE   for action = 'stif'
  ELEMRESP = ELEMSTATE   for action = 'forc'
  ELEMRESP = ELEMMASS    for action = 'mass'
  ELEMRESP = ELEMPOST    for action = 'post'
  ELEMRESP = STRSREC     for action = 'stre'
  ELEMRESP is empty      for unsupported keywords
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ARSZ   is an Boolean array of size NDF x NEN,
         where NDF = number of DOFs/node, NEN = number of nodes,
         with unit values corresponding to the active element DOFs
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ELEMDATA is a data structure with element property information in fields
         t       = element thickness (default t=1)
         nIP     = number of integration points (default nIP=2)
         MatName = function name for material model
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ELEMSTATE is a data structure with the current element state; it has the fields
         u     = vector of total element displacements in global reference
         Du    = vector of element displacement increments from last convergence
         DDu   = vector of element displacement increments from last iteration
         ke    = element stiffness matrix in global reference; updated under ACTION = 'stif'
         p     = element resisting force vector in global reference; updated under ACTION = 'stif' or 'forc'
         Past  = element history variables at last converged state
         Pres  = current element history variables
         lamda = row vector of current load factor(s)
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ELEMPOST is a data structure with element response information for post-processing in fields
         Mat{i}.xyz = coordinates   of integration point i
         Mat{i}.eps = strain tensor at integration point i
         Mat{i}.sig = stress tensor at integration point i
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  STRSREC is a data structure with nodal stress information in field(s)
         sigNd = nodal stresses</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../../../matlabicon.gif)">
<li><a href="shape2d" class="code" title="function [N,dNdx,J] = shape2d (nat,xyz,nodix)">shape2d</a>	SHAPE2D shape functions for 4-9 node quadrilateral element</li><li><a href="../../../../../../../FEDEASLab/src/Utilities/Quadrature/Gauss2d" class="code" title="function [xIP,wIP] = Gauss2d (nIP)">Gauss2d</a>	GAUSS2D Gauss integration rule in two dimensions</li></ul>
This function is called by:
<ul style="list-style-image:url(../../../../../matlabicon.gif)">
</ul>
<!-- crossreference -->



<h2><a name="_source"></a>SOURCE CODE</h2>
<div class="fragment"><pre>0001 <a name="_sub0" href="#_subfunctions" class="code">function ElemResp = InelPanelZone (action,el_no,xyz,ElemData,ElemState)</a>
0002 <span class="comment">%INELPANELZONE 4-node panel zone element with inelastic material</span>
0003 <span class="comment">% ELEMRESP = INELPANELZONE (ACTION,EL_NO,XYZ,ELEMDATA,ELEMSTATE)</span>
0004 <span class="comment">%  response of 4-node panel zone element with inelastic material;</span>
0005 <span class="comment">%  depending on the value of the character variable ACTION the function returns information</span>
0006 <span class="comment">%  in data structure ELEMRESP for the element with number EL_NO, end node coordinates XYZ,</span>
0007 <span class="comment">%  and material and loading properties in the data structure ELEMDATA.</span>
0008 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0009 <span class="comment">%  When the character variable ACTION has one of the following values,</span>
0010 <span class="comment">%  the function performs the listed operations and returns the results in ELEMRESP:</span>
0011 <span class="comment">%  ACTION = 'size': report size of element arrays</span>
0012 <span class="comment">%           'chec': check element property data for omissions and assign default values</span>
0013 <span class="comment">%           'init': initialize element history variables</span>
0014 <span class="comment">%           'forc': report element resisting forces</span>
0015 <span class="comment">%           'stif': report element stiffness matrix and resisting forces</span>
0016 <span class="comment">%           'mass': report lumped mass vector and consistent mass matrix</span>
0017 <span class="comment">%           'post': report post-processing information</span>
0018 <span class="comment">%           'stre': stress recovery to element nodes</span>
0019 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0020 <span class="comment">%  The data structure ELEMRESP stands for the following data object(s) for each ACTION:</span>
0021 <span class="comment">%  ELEMRESP = ARSZ        for action = 'size'</span>
0022 <span class="comment">%  ELEMRESP = ELEMDATA    for action = 'chec'</span>
0023 <span class="comment">%  ELEMRESP = ELEMSTATE   for action = 'init'</span>
0024 <span class="comment">%  ELEMRESP = ELEMSTATE   for action = 'stif'</span>
0025 <span class="comment">%  ELEMRESP = ELEMSTATE   for action = 'forc'</span>
0026 <span class="comment">%  ELEMRESP = ELEMMASS    for action = 'mass'</span>
0027 <span class="comment">%  ELEMRESP = ELEMPOST    for action = 'post'</span>
0028 <span class="comment">%  ELEMRESP = STRSREC     for action = 'stre'</span>
0029 <span class="comment">%  ELEMRESP is empty      for unsupported keywords</span>
0030 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0031 <span class="comment">%  ARSZ   is an Boolean array of size NDF x NEN,</span>
0032 <span class="comment">%         where NDF = number of DOFs/node, NEN = number of nodes,</span>
0033 <span class="comment">%         with unit values corresponding to the active element DOFs</span>
0034 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0035 <span class="comment">%  ELEMDATA is a data structure with element property information in fields</span>
0036 <span class="comment">%         t       = element thickness (default t=1)</span>
0037 <span class="comment">%         nIP     = number of integration points (default nIP=2)</span>
0038 <span class="comment">%         MatName = function name for material model</span>
0039 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0040 <span class="comment">%  ELEMSTATE is a data structure with the current element state; it has the fields</span>
0041 <span class="comment">%         u     = vector of total element displacements in global reference</span>
0042 <span class="comment">%         Du    = vector of element displacement increments from last convergence</span>
0043 <span class="comment">%         DDu   = vector of element displacement increments from last iteration</span>
0044 <span class="comment">%         ke    = element stiffness matrix in global reference; updated under ACTION = 'stif'</span>
0045 <span class="comment">%         p     = element resisting force vector in global reference; updated under ACTION = 'stif' or 'forc'</span>
0046 <span class="comment">%         Past  = element history variables at last converged state</span>
0047 <span class="comment">%         Pres  = current element history variables</span>
0048 <span class="comment">%         lamda = row vector of current load factor(s)</span>
0049 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0050 <span class="comment">%  ELEMPOST is a data structure with element response information for post-processing in fields</span>
0051 <span class="comment">%         Mat{i}.xyz = coordinates   of integration point i</span>
0052 <span class="comment">%         Mat{i}.eps = strain tensor at integration point i</span>
0053 <span class="comment">%         Mat{i}.sig = stress tensor at integration point i</span>
0054 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0055 <span class="comment">%  STRSREC is a data structure with nodal stress information in field(s)</span>
0056 <span class="comment">%         sigNd = nodal stresses</span>
0057 
0058 <span class="comment">%  =========================================================================================</span>
0059 <span class="comment">%  FEDEASLab - Release 5.1, July 2020</span>
0060 <span class="comment">%  Matlab Finite Elements for Design, Evaluation and Analysis of Structures</span>
0061 <span class="comment">%  Professor Filip C. Filippou (filippou@berkeley.edu)</span>
0062 <span class="comment">%  Department of Civil and Environmental Engineering, UC Berkeley</span>
0063 <span class="comment">%  Copyright(c) 1998-2020. The Regents of the University of California. All Rights Reserved.</span>
0064 <span class="comment">%  =========================================================================================</span>
0065 <span class="comment">%  function added                                                                    02-2020</span>
0066 <span class="comment">%  -----------------------------------------------------------------------------------------</span>
0067 
0068 ndf = 3;        <span class="comment">% number of DOFs per node</span>
0069 
0070 <span class="comment">% transformation from mid-node to panel corner coordinates</span>
0071 xyzl = [ xyz(1,4) xyz(2,1);
0072          xyz(1,2) xyz(2,1);
0073          xyz(1,2) xyz(2,3);
0074          xyz(1,4) xyz(2,3)];
0075 
0076 <span class="comment">%% report size of element arrays, check element data; else retrieve element data</span>
0077 ElemResp = [];  <span class="comment">% if not otherwise specified, ElemResp is empty</span>
0078 <span class="keyword">switch</span> action
0079   <span class="keyword">case</span> <span class="string">'size'</span>
0080     arsz = ones(4,ndf);
0081     ElemResp = arsz;
0082     <span class="keyword">return</span>
0083   <span class="keyword">case</span> <span class="string">'chec'</span>
0084     <span class="comment">%% check element data; assign default values, if necessary</span>
0085     <span class="keyword">if</span> ~isfield(ElemData,<span class="string">'Geom'</span>),  ElemData.Geom = <span class="string">'linear'</span>;   <span class="keyword">end</span>
0086     <span class="keyword">if</span> ~isfield(ElemData,<span class="string">'t'</span>),     ElemData.t    = 1;          <span class="keyword">end</span>
0087     <span class="keyword">if</span> ~isfield(ElemData,<span class="string">'d'</span>),     ElemData.d    = [ 1 1 ];    <span class="keyword">end</span>
0088     <span class="keyword">if</span> ~isfield(ElemData,<span class="string">'nIP'</span>),   ElemData.nIP  = 1;          <span class="keyword">end</span>
0089     
0090     <span class="comment">% Gauss integration rule in two dimensions</span>
0091     nat  = <a href="../../../../../../../FEDEASLab/src/Utilities/Quadrature/Gauss2d.md" class="code" title="function [xIP,wIP] = Gauss2d (nIP)">Gauss2d</a> (ElemData.nIP);
0092     nIP  = size(nat,1);
0093     <span class="comment">% loop over integration points</span>
0094     <span class="keyword">for</span> i = 1:nIP        <span class="comment">% compute shape functions at integration point</span>
0095       [~,~,J] = <a href="shape2d.md" class="code" title="function [N,dNdx,J] = shape2d (nat,xyz,nodix)">shape2d</a> (nat(i,:),xyzl);
0096       <span class="keyword">if</span> ( det(J) &lt;= 0 ), disp(<span class="string">'Element'</span>); disp(el_no);
0097         error(<span class="string">'Element has non-positive Jacobian; check order of nodes'</span>);
0098       <span class="keyword">end</span>
0099     <span class="keyword">end</span>
0100     MatData = feval (ElemData.MatName,<span class="string">'chec'</span>,1,ElemData.MatData);
0101     ElemData.MatData = MatData;
0102     ElemResp = ElemData;
0103     <span class="keyword">return</span>
0104   <span class="keyword">otherwise</span>
0105     <span class="comment">%% extract element properties</span>
0106     MatName = ElemData.MatName;
0107     MatData = ElemData.MatData;
0108     t = ElemData.t;
0109     d = ElemData.d;
0110 <span class="keyword">end</span>
0111 
0112 <span class="comment">% transformation from 12 mid-node DOFs to 8 panel corner DOFs</span>
0113 ac11 = [ 1  0   0  ;  0  1 -d(1)];
0114 ac12 = [ 1  0   0  ;  0  1  d(1)];
0115 ac22 = [ 1  0  d(2);  0  1   0  ];
0116 ac23 = [ 1  0 -d(2);  0  1   0  ];
0117 Tc   = zeros(8,12);
0118 Tc(1:4,1:3) = [ ac11 ; ac12 ];
0119 Tc(3:6,4:6) = [ ac22 ; ac23 ];
0120 Tc(5:8,7:9) = [ ac12 ; ac11 ];
0121 Tc(7:8,10:12) = ac23;
0122 Tc(1:2,10:12) = ac22;
0123 
0124 <span class="comment">% ==========================================================================================</span>
0125 <span class="comment">%% element actions</span>
0126 <span class="keyword">switch</span> action
0127   <span class="keyword">case</span> <span class="string">'init'</span>
0128     <span class="comment">%% initialization and specification of history variables</span>
0129     nIP = ElemData.nIP*ElemData.nIP;
0130     <span class="keyword">for</span> j=1:nIP
0131       MatState = feval (MatName,<span class="string">'init'</span>,j,MatData);
0132       ElemState.Pres.Mat{j} = MatState.Pres;       <span class="comment">% history variables only from material</span>
0133     <span class="keyword">end</span>
0134     ElemResp = ElemState;
0135 <span class="comment">% ==========================================================================================</span>
0136   <span class="keyword">case</span> <span class="string">'stif'</span>
0137     <span class="comment">%% state determination: extract displacements</span>
0138     <span class="comment">% number of nodes and number of dofs</span>
0139     [~,nen] = size(xyz);
0140     <span class="comment">% extract displacements from ElemState and reshape to array</span>
0141     [u,Du,DDu] = ExtrReshu(ElemState,ndf,nen);
0142     <span class="comment">%% geometric transformation</span>
0143     ul   = Tc*u(:);
0144     Dul  = Tc*Du(:);
0145     DDul = Tc*DDu(:);
0146     <span class="comment">% set up local element state</span>
0147     LocElemState = ElemState;
0148     LocElemState.u   = reshape(  ul,2,nen);
0149     LocElemState.Du  = reshape( Dul,2,nen);
0150     LocElemState.DDu = reshape(DDul,2,nen);
0151     <span class="comment">%% state determination in local reference</span>
0152     <span class="comment">% initialize element response variables</span>
0153     p  = zeros(8,1);
0154     k  = zeros(8);
0155     <span class="comment">%% loop over integration points</span>
0156     <span class="comment">% Gauss integration rule in two dimensions</span>
0157     [nat,wIP] = <a href="../../../../../../../FEDEASLab/src/Utilities/Quadrature/Gauss2d.md" class="code" title="function [xIP,wIP] = Gauss2d (nIP)">Gauss2d</a> (ElemData.nIP);
0158     nIP = length(wIP);
0159     <span class="comment">% initialize strain-displacement matrix B</span>
0160     B = zeros(3,8);
0161     <span class="keyword">for</span> i = 1:nIP
0162       <span class="comment">% compute shape functions at integration point</span>
0163       [~,dNdx,J] = <a href="shape2d.md" class="code" title="function [N,dNdx,J] = shape2d (nat,xyz,nodix)">shape2d</a> (nat(i,:),xyzl,1:4);
0164       <span class="comment">% form strain displacement matrix B</span>
0165       <span class="comment">% dNdx(i,j) is derivative of shape function j with respect to x_i</span>
0166       B([1 3],1:2:8) = dNdx;
0167       B([3 2],2:2:8) = dNdx;
0168       <span class="comment">% compute strain at integration point i from displacements</span>
0169       MatState = Extract_El2MatState (i,B,LocElemState);
0170       <span class="comment">% Material state determination</span>
0171       MatState = feval(MatName,<span class="string">'stif'</span>,i,MatData,MatState);
0172       ElemHist.Pres.Mat{i} = MatState.Pres;       <span class="comment">% store history variables</span>
0173       <span class="comment">% integration point volume</span>
0174       dV = det(J) * wIP(i) * t;
0175       <span class="comment">% element nodal forces p</span>
0176       p  = p + B' * MatState.sig *dV;
0177       <span class="comment">% Form element stiffness matrix k</span>
0178       k  = k + B' * MatState.km * B *dV;
0179     <span class="keyword">end</span>
0180     <span class="comment">% transfer updated history variables back to ElemState</span>
0181     ElemState.Pres = ElemHist.Pres;
0182     <span class="comment">%% transformation to global system</span>
0183     <span class="comment">% geometric stiffness</span>
0184     ElemState.ke = Tc'*k*Tc;
0185     <span class="comment">% transform element forces to global reference</span>
0186     ElemState.p  = Tc'*p;
0187     ElemState.ConvFlag = true;       <span class="comment">% element does not involve iterations</span>
0188     ElemResp = ElemState;
0189 <span class="comment">% ==========================================================================================</span>
0190   <span class="keyword">case</span> <span class="string">'forc'</span>
0191     <span class="comment">%% state determination: extract displacements</span>
0192     <span class="comment">% number of nodes and number of dofs</span>
0193     [~,nen] = size(xyz);
0194     <span class="comment">% extract displacements from ElemState and reshape to array</span>
0195     [u,Du,DDu] = ExtrReshu(ElemState,ndf,nen);
0196     <span class="comment">%% geometric transformation</span>
0197     ul   = Tc*u(:);
0198     Dul  = Tc*Du(:);
0199     DDul = Tc*DDu(:);
0200     <span class="comment">% set up local element state</span>
0201     LocElemState = ElemState;
0202     LocElemState.u   = reshape(  ul,2,nen);
0203     LocElemState.Du  = reshape( Dul,2,nen);
0204     LocElemState.DDu = reshape(DDul,2,nen);
0205     <span class="comment">%% state determination in local reference</span>
0206     <span class="comment">% initialize element response variables</span>
0207     p = zeros(8,1);
0208     <span class="comment">%% loop over integration points</span>
0209     <span class="comment">% Gauss integration rule in two dimensions</span>
0210     [nat,wIP] = <a href="../../../../../../../FEDEASLab/src/Utilities/Quadrature/Gauss2d.md" class="code" title="function [xIP,wIP] = Gauss2d (nIP)">Gauss2d</a> (ElemData.nIP);
0211     nIP = length(wIP);
0212     <span class="comment">% initialize strain-displacement matrix B</span>
0213     B = zeros(3,8);
0214     <span class="keyword">for</span> i = 1:nIP
0215       <span class="comment">% compute shape functions at integration point</span>
0216       [~,dNdx,J] = <a href="shape2d.md" class="code" title="function [N,dNdx,J] = shape2d (nat,xyz,nodix)">shape2d</a> (nat(i,:),xyzl,1:4);
0217       <span class="comment">% form strain displacement matrix B</span>
0218       <span class="comment">% dNdx(i,j) is derivative of shape function j with respect to x_i</span>
0219       B([1 3],1:2:8) = dNdx;
0220       B([3 2],2:2:8) = dNdx;
0221       <span class="comment">% compute strain at integration point i from displacements</span>
0222       MatState = Extract_El2MatState (i,B,LocElemState);
0223       <span class="comment">% Material state determination</span>
0224       MatState = feval(MatName,<span class="string">'forc'</span>,i,MatData,MatState);
0225       ElemHist.Pres.Mat{i} = MatState.Pres;       <span class="comment">% store history variables</span>
0226       <span class="comment">% integration point volume</span>
0227       dV = det(J) * wIP(i) * t;
0228       <span class="comment">% element nodal forces p</span>
0229       p = p + B' * MatState.sig *dV;
0230     <span class="keyword">end</span>
0231     <span class="comment">% transfer updated history variables back to ElemState</span>
0232     ElemState.Pres = ElemHist.Pres;
0233     <span class="comment">%% transformation to global system</span>
0234     <span class="comment">% transform element forces to global reference</span>
0235     ElemState.p = Tc'*p;
0236     ElemState.ConvFlag = true;       <span class="comment">% element does not involve iterations</span>
0237     ElemResp = ElemState;
0238 <span class="comment">% ==========================================================================================</span>
0239   <span class="keyword">case</span> <span class="string">'post'</span>
0240     <span class="comment">%% post-processing</span>
0241     <span class="comment">% number of nodes and number of dofs</span>
0242     [~,nen] = size(xyz);
0243     <span class="comment">% extract displacements from ElemState and reshape to array</span>
0244     [u,Du,DDu] = ExtrReshu(ElemState,ndf,nen);
0245     <span class="comment">%% geometric transformation</span>
0246     ul   = Tc*u(:);
0247     Dul  = Tc*Du(:);
0248     DDul = Tc*DDu(:);
0249     <span class="comment">% set up local element state</span>
0250     LocElemState = ElemState;
0251     LocElemState.u   = reshape(  ul,2,nen);
0252     LocElemState.Du  = reshape( Dul,2,nen);
0253     LocElemState.DDu = reshape(DDul,2,nen);
0254     <span class="comment">%% stress output: determination in local and transformation to global reference</span>
0255     <span class="comment">% loop over integration points</span>
0256     <span class="comment">% Gauss integration rule in two dimensions</span>
0257     [nat,wIP] = <a href="../../../../../../../FEDEASLab/src/Utilities/Quadrature/Gauss2d.md" class="code" title="function [xIP,wIP] = Gauss2d (nIP)">Gauss2d</a> (ElemData.nIP);
0258     nIP = length(wIP);
0259     <span class="comment">% initialize strain-displacement matrix B</span>
0260     B = zeros(3,8);
0261     <span class="keyword">for</span> i = 1:nIP
0262       <span class="comment">% compute shape functions at integration point</span>
0263       [N,dNdx] = <a href="shape2d.md" class="code" title="function [N,dNdx,J] = shape2d (nat,xyz,nodix)">shape2d</a> (nat(i,:),xyzl,1:4);
0264       <span class="comment">% form strain displacement matrix B</span>
0265       <span class="comment">% dNdx(i,j) is derivative of shape function j with respect to x_i</span>
0266       B([1 3],1:2:8) = dNdx;
0267       B([3 2],2:2:8) = dNdx;
0268       <span class="comment">% set up material state at integration point i from displacements and element state</span>
0269       MatState = Extract_El2MatState (i,B,LocElemState);
0270       <span class="comment">% Material state determination</span>
0271       MatPost = feval(MatName,<span class="string">'post'</span>,i,MatData,MatState);
0272       sig  = MatPost.sig;
0273       epsi = MatPost.eps;
0274       <span class="comment">% express strain and stress in global coordinates</span>
0275 <span class="comment">%       [epsi,sig] = TransformStr2GL (ndm,Tr0,epsi,sig);</span>
0276       <span class="comment">% store position of integration point and strain and stress in global reference</span>
0277 <span class="comment">%       ElemPost.Mat{i}.xyz = Tr0*xyzl*N'+xyz(:,1);</span>
0278       ElemPost.Mat{i}.xyz = (N*xyzl)'+xyz(:,1);
0279       ElemPost.Mat{i}.eps = epsi;
0280       ElemPost.Mat{i}.sig = sig;
0281     <span class="keyword">end</span>
0282     ElemResp = ElemPost;
0283 <span class="comment">% ==========================================================================================</span>
0284   <span class="keyword">case</span> <span class="string">'stre'</span>
0285     <span class="comment">%%  element patch stress recovery for node stress determination</span>
0286 <span class="comment">% ==========================================================================================</span>
0287   <span class="keyword">otherwise</span>
0288     <span class="comment">%% other actions not supported</span>
0289     warning(<span class="string">'off'</span>,<span class="string">'backtrace'</span>);
0290     warning(<span class="string">'E:W'</span>,[<span class="string">'&gt;&gt; Element '</span>,num2str(el_no,<span class="string">'%i'</span>),<span class="string">': Action &quot;'</span>,action,<span class="string">'&quot; not supported for Inel4to9nodeQuad element'</span>]);
0291     warning(<span class="string">'on'</span>,<span class="string">'backtrace'</span>);
0292 <span class="keyword">end</span></pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->