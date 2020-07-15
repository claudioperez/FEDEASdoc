
<!-- <a name="_top"></a>
<div><a href="../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="index.md">Element_Library</a> &gt; InelTruss.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../index.md"><img alt="<" border="0" src="../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Element_Library&nbsp;<img alt=">" border="0" src="../../../../../right.png"></a></td></tr></table>-->
# `InelTruss`
<!-- <h1>InelTruss
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

INELTRUSS 2d/3d inelastic truss element under linear or nonlinear geometry

<!-- <div class="box"><strong>INELTRUSS 2d/3d inelastic truss element under linear or nonlinear geometry</strong></div> -->

## <a name="_synopsis"></a>Syntax

`function ElemResp = InelTruss (action,el_no,xyz,ElemData,ElemState)` 
## <a name="_description"></a>Description

<pre class="comment">INELTRUSS 2d/3d inelastic truss element under linear or nonlinear geometry   
  ELEMRESP = INELTRUSS (ACTION,EL_NO,XYZ,ELEMDATA,ELEMSTATE)
  response of 2d/3d inelastic truss element;
  the element accounts for linear and nonlinear geometry for the nodal dof transformations; 
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
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The data structure ELEMRESP stands for the following data object(s) for each ACTION:
  ELEMRESP = ARSZ        for action = 'size' 
  ELEMRESP = ELEMDATA    for action = 'chec'
  ELEMRESP = ELEMSTATE   for action = 'init'
  ELEMRESP = ELEMSTATE   for action = 'stif'
  ELEMRESP = ELEMSTATE   for action = 'forc'
  ELEMRESP = ELEMMASS    for action = 'mass'
  ELEMRESP = ELEMPOST    for action = 'post'
  ELEMRESP is empty      for unsupported keywords
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ARSZ   is an Boolean array of size NDF x NEN,
         where NDF = number of DOFs/node, NEN = number of nodes,
         with unit values corresponding to the active element DOFs
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ELDATA is a data structure with element property information in fields
         Geom    = character variable for geometric transformation of node variables
                   (linear, PDelta or corotational) (default=linear)
         A       = cross sectional area
         MatName = function for material stress-strain response
         MatData = material property data
         s0      = initial force (default = 0)
         e0      = initial deformation (default = 0)
         jntoff  = rigid joint offsets in global X and Y at element ends; column 1 for node i, column 2 for node j
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
         v     = element deformations
         q     = element basic forces
         Mat   = material response information for post-processing (see material function with MatName)</pre>
<!-- <div class="fragment"><pre class="comment">INELTRUSS 2d/3d inelastic truss element under linear or nonlinear geometry   
  ELEMRESP = INELTRUSS (ACTION,EL_NO,XYZ,ELEMDATA,ELEMSTATE)
  response of 2d/3d inelastic truss element;
  the element accounts for linear and nonlinear geometry for the nodal dof transformations; 
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
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The data structure ELEMRESP stands for the following data object(s) for each ACTION:
  ELEMRESP = ARSZ        for action = 'size' 
  ELEMRESP = ELEMDATA    for action = 'chec'
  ELEMRESP = ELEMSTATE   for action = 'init'
  ELEMRESP = ELEMSTATE   for action = 'stif'
  ELEMRESP = ELEMSTATE   for action = 'forc'
  ELEMRESP = ELEMMASS    for action = 'mass'
  ELEMRESP = ELEMPOST    for action = 'post'
  ELEMRESP is empty      for unsupported keywords
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ARSZ   is an Boolean array of size NDF x NEN,
         where NDF = number of DOFs/node, NEN = number of nodes,
         with unit values corresponding to the active element DOFs
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ELDATA is a data structure with element property information in fields
         Geom    = character variable for geometric transformation of node variables
                   (linear, PDelta or corotational) (default=linear)
         A       = cross sectional area
         MatName = function for material stress-strain response
         MatData = material property data
         s0      = initial force (default = 0)
         e0      = initial deformation (default = 0)
         jntoff  = rigid joint offsets in global X and Y at element ends; column 1 for node i, column 2 for node j
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
         v     = element deformations
         q     = element basic forces
         Mat   = material response information for post-processing (see material function with MatName)</pre></div> -->

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
<div class="fragment"><pre>0001 <a name="_sub0" href="#_subfunctions" class="code">function ElemResp = InelTruss (action,el_no,xyz,ElemData,ElemState)</a>
0002 <span class="comment">%INELTRUSS 2d/3d inelastic truss element under linear or nonlinear geometry</span>
0003 <span class="comment">%  ELEMRESP = INELTRUSS (ACTION,EL_NO,XYZ,ELEMDATA,ELEMSTATE)</span>
0004 <span class="comment">%  response of 2d/3d inelastic truss element;</span>
0005 <span class="comment">%  the element accounts for linear and nonlinear geometry for the nodal dof transformations;</span>
0006 <span class="comment">%  depending on the value of the character variable ACTION the function returns information</span>
0007 <span class="comment">%  in data structure ELEMRESP for the element with number EL_NO, end node coordinates XYZ,</span>
0008 <span class="comment">%  and material and loading properties in the data structure ELEMDATA.</span>
0009 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0010 <span class="comment">%  When the character variable ACTION has one of the following values,</span>
0011 <span class="comment">%  the function performs the listed operations and returns the results in ELEMRESP:</span>
0012 <span class="comment">%  ACTION = 'size': report size of element arrays</span>
0013 <span class="comment">%           'chec': check element property data for omissions and assign default values</span>
0014 <span class="comment">%           'init': initialize element history variables</span>
0015 <span class="comment">%           'forc': report element resisting forces</span>
0016 <span class="comment">%           'stif': report element stiffness matrix and resisting forces</span>
0017 <span class="comment">%           'mass': report lumped mass vector and consistent mass matrix</span>
0018 <span class="comment">%           'post': report post-processing information</span>
0019 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0020 <span class="comment">%  The data structure ELEMRESP stands for the following data object(s) for each ACTION:</span>
0021 <span class="comment">%  ELEMRESP = ARSZ        for action = 'size'</span>
0022 <span class="comment">%  ELEMRESP = ELEMDATA    for action = 'chec'</span>
0023 <span class="comment">%  ELEMRESP = ELEMSTATE   for action = 'init'</span>
0024 <span class="comment">%  ELEMRESP = ELEMSTATE   for action = 'stif'</span>
0025 <span class="comment">%  ELEMRESP = ELEMSTATE   for action = 'forc'</span>
0026 <span class="comment">%  ELEMRESP = ELEMMASS    for action = 'mass'</span>
0027 <span class="comment">%  ELEMRESP = ELEMPOST    for action = 'post'</span>
0028 <span class="comment">%  ELEMRESP is empty      for unsupported keywords</span>
0029 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0030 <span class="comment">%  ARSZ   is an Boolean array of size NDF x NEN,</span>
0031 <span class="comment">%         where NDF = number of DOFs/node, NEN = number of nodes,</span>
0032 <span class="comment">%         with unit values corresponding to the active element DOFs</span>
0033 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0034 <span class="comment">%  ELDATA is a data structure with element property information in fields</span>
0035 <span class="comment">%         Geom    = character variable for geometric transformation of node variables</span>
0036 <span class="comment">%                   (linear, PDelta or corotational) (default=linear)</span>
0037 <span class="comment">%         A       = cross sectional area</span>
0038 <span class="comment">%         MatName = function for material stress-strain response</span>
0039 <span class="comment">%         MatData = material property data</span>
0040 <span class="comment">%         s0      = initial force (default = 0)</span>
0041 <span class="comment">%         e0      = initial deformation (default = 0)</span>
0042 <span class="comment">%         jntoff  = rigid joint offsets in global X and Y at element ends; column 1 for node i, column 2 for node j</span>
0043 <span class="comment">%   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0044 <span class="comment">%  ELEMSTATE is a data structure with the current element state; it has the fields</span>
0045 <span class="comment">%         u     = vector of total element displacements in global reference</span>
0046 <span class="comment">%         Du    = vector of element displacement increments from last convergence</span>
0047 <span class="comment">%         DDu   = vector of element displacement increments from last iteration</span>
0048 <span class="comment">%         ke    = element stiffness matrix in global reference; updated under ACTION = 'stif'</span>
0049 <span class="comment">%         p     = element resisting force vector in global reference; updated under ACTION = 'stif' or 'forc'</span>
0050 <span class="comment">%         Past  = element history variables at last converged state</span>
0051 <span class="comment">%         Pres  = current element history variables</span>
0052 <span class="comment">%         lamda = row vector of current load factor(s)</span>
0053 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0054 <span class="comment">%  ELEMPOST is a data structure with element response information for post-processing in fields</span>
0055 <span class="comment">%         v     = element deformations</span>
0056 <span class="comment">%         q     = element basic forces</span>
0057 <span class="comment">%         Mat   = material response information for post-processing (see material function with MatName)</span>
0058 
0059 <span class="comment">%  =========================================================================================</span>
0060 <span class="comment">%  FEDEASLab - Release 5.1, July 2020</span>
0061 <span class="comment">%  Matlab Finite Elements for Design, Evaluation and Analysis of Structures</span>
0062 <span class="comment">%  Professor Filip C. Filippou (filippou@berkeley.edu)</span>
0063 <span class="comment">%  Department of Civil and Environmental Engineering, UC Berkeley</span>
0064 <span class="comment">%  Copyright(c) 1998-2020. The Regents of the University of California. All Rights Reserved.</span>
0065 <span class="comment">%  =========================================================================================</span>
0066 
0067 <span class="comment">%%</span>
0068 ndm = size(xyz,1);    <span class="comment">% element dimension</span>
0069 ndf = ndm;
0070 
0071 <span class="comment">%% report size of element arrays, check element data; else retrieve element data</span>
0072 <span class="keyword">switch</span> action
0073   <span class="keyword">case</span> <span class="string">'size'</span>
0074     arsz = ones(2,ndm);
0075     ElemResp = arsz;  <span class="comment">% return size of element arrays</span>
0076     <span class="keyword">return</span>
0077   <span class="keyword">case</span> <span class="string">'chec'</span>
0078     <span class="comment">%% check element data; assign default values, if necessary</span>
0079     <span class="keyword">if</span> ~isfield(ElemData,<span class="string">'Geom'</span>),   ElemData.Geom       = <span class="string">'linear'</span>; <span class="keyword">end</span>
0080     <span class="keyword">if</span> ~isfield(ElemData,<span class="string">'A'</span>),  disp(<span class="string">'Element'</span>);disp(el_no); error(<span class="string">'area missing'</span>); <span class="keyword">end</span>
0081     <span class="keyword">if</span> ~isfield(ElemData,<span class="string">'s0'</span>),       ElemData.s0       = 0;        <span class="keyword">end</span>
0082     <span class="keyword">if</span> ~isfield(ElemData,<span class="string">'e0'</span>),       ElemData.e0       = 0;        <span class="keyword">end</span>
0083     <span class="comment">%       if ~isfield(ElemData,'jntoff'), ElemData.jntoff = zeros(ndm,2); end</span>
0084     <span class="keyword">if</span> ~isfield(ElemData,<span class="string">'rho'</span>),      ElemData.rho      = 0;        <span class="keyword">end</span>
0085     <span class="keyword">if</span> ~isfield(ElemData,<span class="string">'SubDivNo'</span>), ElemData.SubDivNo = 5;        <span class="keyword">end</span>
0086     MatData = feval (ElemData.MatName,<span class="string">'chec'</span>,1,ElemData.MatData);
0087     ElemData.MatData = MatData;
0088     ElemResp = ElemData;
0089     <span class="keyword">return</span>
0090   <span class="keyword">otherwise</span>
0091     <span class="comment">%% extract element properties</span>
0092     A        = ElemData.A;
0093     rho      = ElemData.rho;
0094     s0       = ElemData.s0;
0095     e0       = ElemData.e0;
0096     MatName  = ElemData.MatName;
0097     MatData  = ElemData.MatData;
0098 <span class="keyword">end</span>
0099 
0100 <span class="comment">% ==========================================================================================</span>
0101 <span class="comment">%% element actions</span>
0102 ElemResp = [];  <span class="comment">% if not otherwise specified, ElemResp is empty</span>
0103 <span class="keyword">switch</span> action
0104   <span class="keyword">case</span> <span class="string">'init'</span>
0105     <span class="comment">%% initialization and specification of history variables</span>
0106     MatState = feval (MatName,<span class="string">'init'</span>,1,MatData);
0107     ElemState.Pres.Mat = MatState.Pres;       <span class="comment">% history variables only from material</span>
0108     ElemResp = ElemState;
0109 <span class="comment">% ==========================================================================================</span>
0110   <span class="keyword">case</span> {<span class="string">'stif'</span>,<span class="string">'forc'</span>}
0111     <span class="comment">%% state determination</span>
0112     ElemState.ConvFlag = true;       <span class="comment">% initialize convergence flag</span>
0113     <span class="comment">% undeformed element length</span>
0114     L   = ElmLenOr(xyz);
0115     <span class="comment">% extract displacements from ElemState and reshape to array</span>
0116     nen = size(xyz,2);
0117     [u,Du,DDu] = ExtrReshu(ElemState,ndf,nen);
0118     <span class="comment">% transform end displacements from global reference to basic system</span>
0119     [ag,bg,v,Dv,DDv] = GeomTran_Truss (ElemData.Geom,xyz,u,Du,DDu);
0120     <span class="comment">%% basic force-deformation</span>
0121     <span class="comment">% extract material state from element including initial deformation</span>
0122     MatState.eps   =  v./L - e0;
0123     MatState.Deps  = Dv/L;
0124     MatState.DDeps = DDv/L;
0125     MatState.Pres  = ElemState.Pres.Mat;
0126     MatState.Past  = ElemState.Past.Mat;
0127     MatState = feval (MatName,<span class="string">'stif'</span>,1,MatData,MatState);
0128     ElemState.Pres.Mat = MatState.Pres;
0129     <span class="keyword">if</span> (isfield(MatState,<span class="string">'ConvFlag'</span>)), ElemState.ConvFlag = MatState.ConvFlag; <span class="keyword">end</span>
0130     Et  = MatState.km;
0131     sig = MatState.sig;
0132     <span class="comment">% basic stiffness k</span>
0133     k = Et*A/L;
0134     <span class="comment">% element force</span>
0135     q = sig*A + s0;
0136     <span class="comment">%% transform stiffness and forces of basic system to global coordinates</span>
0137     <span class="comment">% transform basic forces to global coordinates and add end forces due to w</span>
0138     p = bg * q;
0139     <span class="keyword">if</span> (strcmp(action,<span class="string">'stif'</span>))
0140       <span class="comment">% determine consistent geometric stiffness matrix</span>
0141       kg = kg_Truss (ElemData.Geom,xyz,u,q);
0142       <span class="comment">% transform stiffness matrix to global coordinates and add geometric stiffness</span>
0143       ke = ag' * k * ag + kg;
0144       ElemState.ke = ke;
0145     <span class="keyword">end</span>
0146     ElemState.p = p;
0147     ElemResp = ElemState;
0148 <span class="comment">% ==========================================================================================</span>
0149   <span class="keyword">case</span> <span class="string">'mass'</span>
0150     <span class="comment">%% lumped mass vector and consistent mass matrix</span>
0151     <span class="comment">% determine element length and orientation (direction cosines)</span>
0152     L  = ElmLenOr (xyz);
0153     tm = rho*A*L;     <span class="comment">% total mass of truss element</span>
0154     <span class="comment">% lumped mass matrix</span>
0155     ml = 0.5*tm.*ones(2*ndm,1);
0156     vm = tm.*ones(ndm,1);
0157     mc = [diag(vm)./3 diag(vm)./6;
0158       diag(vm)./6 diag(vm)./3];
0159     ElemMass.ml = ml;
0160     ElemMass.mc = mc;
0161     ElemResp    = ElemMass;
0162 <span class="comment">% ==========================================================================================</span>
0163   <span class="keyword">case</span> <span class="string">'post'</span>
0164     <span class="comment">%% post-processing information</span>
0165     <span class="comment">% undeformed element length</span>
0166     L   = ElmLenOr(xyz);
0167     <span class="comment">% extract displacements from ElemState and reshape to array</span>
0168     nen = size(xyz,2);
0169     [u,Du,DDu] = ExtrReshu(ElemState,ndf,nen);
0170     <span class="comment">% transform end displacements from global reference to basic system</span>
0171     [~,~,v,Dv,DDv] = GeomTran_Truss (ElemData.Geom,xyz,u,Du,DDu);
0172     <span class="comment">% extract material state from element including initial deformation</span>
0173     MatState.eps   =  v./L - e0;
0174     MatState.Deps  = Dv/L;
0175     MatState.DDeps = DDv/L;
0176     MatState.Pres  = ElemState.Pres.Mat;
0177     MatState.Past  = ElemState.Past.Mat;
0178     ElemPost.Mat   = feval (MatName,<span class="string">'post'</span>,1,MatData,MatState);
0179     <span class="comment">% element force</span>
0180     q  = ElemPost.Mat.sig*A;
0181     <span class="comment">% post-processing information</span>
0182     ElemPost.v = v;
0183     ElemPost.q = q;
0184     ElemResp   = ElemPost;
0185 <span class="comment">% ==========================================================================================</span>
0186   <span class="keyword">otherwise</span>
0187     <span class="comment">%% other actions not supported</span>
0188     warning(<span class="string">'off'</span>,<span class="string">'backtrace'</span>);
0189     warning(<span class="string">'E:W'</span>,[<span class="string">'&gt;&gt; Element '</span>,num2str(el_no,<span class="string">'%i'</span>),<span class="string">': Action &quot;'</span>,action,<span class="string">'&quot; not supported for InelTruss element'</span>]);
0190     warning(<span class="string">'on'</span>,<span class="string">'backtrace'</span>);
0191 <span class="keyword">end</span></pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->