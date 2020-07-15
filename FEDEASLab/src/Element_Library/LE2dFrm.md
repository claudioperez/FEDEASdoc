
<!-- <a name="_top"></a>
<div><a href="../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="index.md">Element_Library</a> &gt; LE2dFrm.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../index.md"><img alt="<" border="0" src="../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Element_Library&nbsp;<img alt=">" border="0" src="../../../../../right.png"></a></td></tr></table>-->
# `LE2dFrm`
<!-- <h1>LE2dFrm
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

LE2dFRM 2d LE frame element under linear or nonlinear geometry

<!-- <div class="box"><strong>LE2dFRM 2d LE frame element under linear or nonlinear geometry</strong></div> -->

## <a name="_synopsis"></a>Syntax

`function ElemResp = LE2dFrm (action,el_no,xyz,ElemData,ElemState)` 
## <a name="_description"></a>Description

<pre class="comment">LE2dFRM 2d LE frame element under linear or nonlinear geometry   
  ELEMRESP = LE2dFRM (ACTION,EL_NO,XYZ,ELEMDATA,ELEMSTATE)
  response of 2d linear elastic frame element;
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
           'defo': report function handle for deformed shape
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The data structure ELEMRESP stands for the following data object(s) for each ACTION:
  ELEMRESP = ARSZ        for action = 'size' 
  ELEMRESP = ELEMDATA    for action = 'chec'
  ELEMRESP = ELEMSTATE   for action = 'init'
  ELEMRESP = ELEMSTATE   for action = 'stif'
  ELEMRESP = ELEMSTATE   for action = 'forc'
  ELEMRESP = ELEMMASS    for action = 'mass'
  ELEMRESP = ELEMPOST    for action = 'post'
  ELEMRESP = FunHandle   for action = 'defo'
  ELEMRESP is empty      for unsupported keywords
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ARSZ   is an Boolean array of size NDF x NEN,
         where NDF = number of DOFs/node, NEN = number of nodes,
         with unit values corresponding to the active element DOFs
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ELEMDATA is a data structure with element property information in fields
         Geom    = character variable for geometric transformation of node variables
                   (linear, PDelta or corotational) (default=linear)
         A       = cross sectional area
         E       = modulus of elasticity
         I       = moment of inertia
         rho     = mass density
         w       = uniform element load ( w(1) = longitudinal, w(2) = transverse )
         e0      = initial deformations (default = 0)
         jntoff  = rigid joint offsets in global X and Y at element ends; column 1 for node i, column 2 for node j
         Release = axial and end flexural releases in column vector (0=cont,1=hinge) (default=[0;0;0])
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
  ELEMMASS is a data structure with element mass information in fields
         ml    = lumped mass vector
         mc    = consistent mass matrix
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ELEMPOST is a data structure with element response information for post-processing in fields
         v     = element deformations
         q     = element basic forces</pre>
<!-- <div class="fragment"><pre class="comment">LE2dFRM 2d LE frame element under linear or nonlinear geometry   
  ELEMRESP = LE2dFRM (ACTION,EL_NO,XYZ,ELEMDATA,ELEMSTATE)
  response of 2d linear elastic frame element;
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
           'defo': report function handle for deformed shape
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The data structure ELEMRESP stands for the following data object(s) for each ACTION:
  ELEMRESP = ARSZ        for action = 'size' 
  ELEMRESP = ELEMDATA    for action = 'chec'
  ELEMRESP = ELEMSTATE   for action = 'init'
  ELEMRESP = ELEMSTATE   for action = 'stif'
  ELEMRESP = ELEMSTATE   for action = 'forc'
  ELEMRESP = ELEMMASS    for action = 'mass'
  ELEMRESP = ELEMPOST    for action = 'post'
  ELEMRESP = FunHandle   for action = 'defo'
  ELEMRESP is empty      for unsupported keywords
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ARSZ   is an Boolean array of size NDF x NEN,
         where NDF = number of DOFs/node, NEN = number of nodes,
         with unit values corresponding to the active element DOFs
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ELEMDATA is a data structure with element property information in fields
         Geom    = character variable for geometric transformation of node variables
                   (linear, PDelta or corotational) (default=linear)
         A       = cross sectional area
         E       = modulus of elasticity
         I       = moment of inertia
         rho     = mass density
         w       = uniform element load ( w(1) = longitudinal, w(2) = transverse )
         e0      = initial deformations (default = 0)
         jntoff  = rigid joint offsets in global X and Y at element ends; column 1 for node i, column 2 for node j
         Release = axial and end flexural releases in column vector (0=cont,1=hinge) (default=[0;0;0])
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
  ELEMMASS is a data structure with element mass information in fields
         ml    = lumped mass vector
         mc    = consistent mass matrix
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ELEMPOST is a data structure with element response information for post-processing in fields
         v     = element deformations
         q     = element basic forces</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../../../../matlabicon.gif)">
</ul>
<!-- crossreference -->

<h2><a name="_subfunctions"></a>Subfunctions<a href="#_top"><img alt="^" border="0" src="../../../../../up.png"></a></h2>
<ul style="list-style-image:url(../../../../../matlabicon.gif)">
<li><a href="#_sub1" class="code">function [q,k] = BasicLE2dFrm (L,ElemData,v)</a></li></ul>

<h2><a name="_source"></a>SOURCE CODE</h2>
<div class="fragment"><pre>0001 <a name="_sub0" href="#_subfunctions" class="code">function ElemResp = LE2dFrm (action,el_no,xyz,ElemData,ElemState)</a>
0002 <span class="comment">%LE2dFRM 2d LE frame element under linear or nonlinear geometry</span>
0003 <span class="comment">%  ELEMRESP = LE2dFRM (ACTION,EL_NO,XYZ,ELEMDATA,ELEMSTATE)</span>
0004 <span class="comment">%  response of 2d linear elastic frame element;</span>
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
0019 <span class="comment">%           'defo': report function handle for deformed shape</span>
0020 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0021 <span class="comment">%  The data structure ELEMRESP stands for the following data object(s) for each ACTION:</span>
0022 <span class="comment">%  ELEMRESP = ARSZ        for action = 'size'</span>
0023 <span class="comment">%  ELEMRESP = ELEMDATA    for action = 'chec'</span>
0024 <span class="comment">%  ELEMRESP = ELEMSTATE   for action = 'init'</span>
0025 <span class="comment">%  ELEMRESP = ELEMSTATE   for action = 'stif'</span>
0026 <span class="comment">%  ELEMRESP = ELEMSTATE   for action = 'forc'</span>
0027 <span class="comment">%  ELEMRESP = ELEMMASS    for action = 'mass'</span>
0028 <span class="comment">%  ELEMRESP = ELEMPOST    for action = 'post'</span>
0029 <span class="comment">%  ELEMRESP = FunHandle   for action = 'defo'</span>
0030 <span class="comment">%  ELEMRESP is empty      for unsupported keywords</span>
0031 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0032 <span class="comment">%  ARSZ   is an Boolean array of size NDF x NEN,</span>
0033 <span class="comment">%         where NDF = number of DOFs/node, NEN = number of nodes,</span>
0034 <span class="comment">%         with unit values corresponding to the active element DOFs</span>
0035 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0036 <span class="comment">%  ELEMDATA is a data structure with element property information in fields</span>
0037 <span class="comment">%         Geom    = character variable for geometric transformation of node variables</span>
0038 <span class="comment">%                   (linear, PDelta or corotational) (default=linear)</span>
0039 <span class="comment">%         A       = cross sectional area</span>
0040 <span class="comment">%         E       = modulus of elasticity</span>
0041 <span class="comment">%         I       = moment of inertia</span>
0042 <span class="comment">%         rho     = mass density</span>
0043 <span class="comment">%         w       = uniform element load ( w(1) = longitudinal, w(2) = transverse )</span>
0044 <span class="comment">%         e0      = initial deformations (default = 0)</span>
0045 <span class="comment">%         jntoff  = rigid joint offsets in global X and Y at element ends; column 1 for node i, column 2 for node j</span>
0046 <span class="comment">%         Release = axial and end flexural releases in column vector (0=cont,1=hinge) (default=[0;0;0])</span>
0047 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0048 <span class="comment">%  ELEMSTATE is a data structure with the current element state; it has the fields</span>
0049 <span class="comment">%         u     = vector of total element displacements in global reference</span>
0050 <span class="comment">%         Du    = vector of element displacement increments from last convergence</span>
0051 <span class="comment">%         DDu   = vector of element displacement increments from last iteration</span>
0052 <span class="comment">%         ke    = element stiffness matrix in global reference; updated under ACTION = 'stif'</span>
0053 <span class="comment">%         p     = element resisting force vector in global reference; updated under ACTION = 'stif' or 'forc'</span>
0054 <span class="comment">%         Past  = element history variables at last converged state</span>
0055 <span class="comment">%         Pres  = current element history variables</span>
0056 <span class="comment">%         lamda = row vector of current load factor(s)</span>
0057 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0058 <span class="comment">%  ELEMMASS is a data structure with element mass information in fields</span>
0059 <span class="comment">%         ml    = lumped mass vector</span>
0060 <span class="comment">%         mc    = consistent mass matrix</span>
0061 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0062 <span class="comment">%  ELEMPOST is a data structure with element response information for post-processing in fields</span>
0063 <span class="comment">%         v     = element deformations</span>
0064 <span class="comment">%         q     = element basic forces</span>
0065 
0066 <span class="comment">%  =========================================================================================</span>
0067 <span class="comment">%  FEDEASLab - Release 5.1, July 2020</span>
0068 <span class="comment">%  Matlab Finite Elements for Design, Evaluation and Analysis of Structures</span>
0069 <span class="comment">%  Professor Filip C. Filippou (filippou@berkeley.edu)</span>
0070 <span class="comment">%  Department of Civil and Environmental Engineering, UC Berkeley</span>
0071 <span class="comment">%  Copyright(c) 1998-2020. The Regents of the University of California. All Rights Reserved.</span>
0072 <span class="comment">%  =========================================================================================</span>
0073 
0074 <span class="comment">%%</span>
0075 ndf = 3;          <span class="comment">% no of element DOFs per node (2-node, 2d frame element)</span>
0076 
0077 <span class="comment">%% report size of element arrays, check element data; else retrieve element data</span>
0078 <span class="keyword">switch</span> action
0079   <span class="keyword">case</span> <span class="string">'size'</span>
0080     arsz = ones(2,ndf);
0081     ElemResp = arsz;  <span class="comment">% return size of element arrays</span>
0082     <span class="keyword">return</span>
0083   <span class="keyword">case</span> <span class="string">'chec'</span>
0084     <span class="comment">%% check element data; assign default values, if necessary</span>
0085     <span class="keyword">if</span> ~isfield(ElemData,<span class="string">'Geom'</span>),    ElemData.Geom    = <span class="string">'linear'</span>;   <span class="keyword">end</span>
0086     <span class="keyword">if</span> ~isfield(ElemData,<span class="string">'E'</span>), disp(<span class="string">'Element'</span>); disp(el_no); error(<span class="string">'Young modulus missing'</span>); <span class="keyword">end</span>
0087     <span class="keyword">if</span> ~isfield(ElemData,<span class="string">'A'</span>), disp(<span class="string">'Element'</span>); disp(el_no); error(<span class="string">'area missing'</span>); <span class="keyword">end</span>
0088     <span class="keyword">if</span> ~isfield(ElemData,<span class="string">'I'</span>), disp(<span class="string">'Element'</span>); disp(el_no); error(<span class="string">'moment of inertia missing'</span>); <span class="keyword">end</span>
0089     <span class="keyword">if</span> ~isfield(ElemData,<span class="string">'w'</span>),       ElemData.w       = [0;0];      <span class="keyword">end</span>
0090     <span class="keyword">if</span> ~isfield(ElemData,<span class="string">'e0'</span>),      ElemData.e0      = [0;0];      <span class="keyword">end</span>
0091     <span class="keyword">if</span> ~isfield(ElemData,<span class="string">'jntoff'</span>),  ElemData.jntoff  = [0 0; 0 0]; <span class="keyword">end</span>
0092     <span class="keyword">if</span> ~isfield(ElemData,<span class="string">'Release'</span>), ElemData.Release = zeros(3,1); <span class="keyword">end</span>
0093     <span class="comment">% introduce release indices RI: 0 indicates no hinge, 1 indicates hinge</span>
0094     RI = zeros(3,1);
0095     <span class="keyword">if</span> ~isfield(ElemData,<span class="string">'MR'</span>)
0096       RI(ElemData.Release==1) = 1;
0097     <span class="keyword">else</span>
0098       RI(2:3) = ElemData.MR;
0099     <span class="keyword">end</span>
0100     ElemData.RI = RI;
0101     <span class="keyword">if</span> ~isfield(ElemData,<span class="string">'rho'</span>),     ElemData.rho     = 0;          <span class="keyword">end</span>
0102     ElemResp = ElemData;
0103     <span class="keyword">return</span>
0104   <span class="keyword">otherwise</span>
0105     <span class="comment">%% put joint offset information to GeomData</span>
0106     GeomData.jntoff = ElemData.jntoff;
0107     w  = ElemData.w;
0108     e0 = ElemData.e0;
0109 <span class="keyword">end</span>
0110 
0111 <span class="comment">% ==========================================================================================</span>
0112 <span class="comment">%% element actions</span>
0113 ElemResp = [];  <span class="comment">% if not otherwise specified, ElemResp is empty</span>
0114 <span class="keyword">switch</span> action
0115   <span class="keyword">case</span> <span class="string">'init'</span>
0116     <span class="comment">%% initialization and specification of history variables</span>
0117     ElemState.Pres = []; <span class="comment">% history array is empty for linear element</span>
0118     ElemResp       = ElemState;
0119 <span class="comment">% ==========================================================================================</span>
0120   <span class="keyword">case</span> {<span class="string">'stif'</span>,<span class="string">'forc'</span>}
0121     <span class="comment">%% state determination</span>
0122     <span class="comment">% undeformed element length</span>
0123     L   = ElmLenOr(xyz+GeomData.jntoff);
0124     <span class="comment">% extract displacements from ElemState and reshape to array</span>
0125     nen = size(xyz,2);
0126     u   = ExtrReshu(ElemState,ndf,nen);
0127     <span class="comment">% transform end displacements from global reference to basic system</span>
0128     [ag,bg,ab,v] = GeomTran_2dFrm (ElemData.Geom,xyz,GeomData,u);
0129     <span class="comment">%% basic force-deformation</span>
0130     [q,k] = <a href="#_sub1" class="code" title="subfunction [q,k] = BasicLE2dFrm (L,ElemData,v)">BasicLE2dFrm</a> (L,ElemData,v);
0131     <span class="comment">%% transform stiffness and forces of basic system to global coordinates</span>
0132     <span class="comment">% determine equilibrium forces of basic system under element loads</span>
0133     pbw = [-w(1)*L; -w(2)*L/2;  0;  0; -w(2)*L/2;  0];
0134     <span class="comment">% transform basic forces to global coordinates and add end forces due to w</span>
0135     p = bg * q + ab' * pbw;
0136     <span class="keyword">if</span> (strcmp(action,<span class="string">'stif'</span>))
0137       <span class="comment">% determine consistent geometric stiffness matrix</span>
0138       kg = kg_2dFrm (ElemData.Geom,xyz,u,q);
0139       <span class="comment">% transform stiffness matrix to global coordinates and add geometric stiffness</span>
0140       ke = ag' * k * ag + kg;
0141       ElemState.ke = ke;
0142     <span class="keyword">end</span>
0143     ElemState.p = p;
0144     ElemState.ConvFlag = true;       <span class="comment">% element does not involve iterations</span>
0145     ElemResp = ElemState;
0146 <span class="comment">% ==========================================================================================</span>
0147   <span class="keyword">case</span> <span class="string">'mass'</span>
0148     <span class="comment">%% lumped mass vector and consistent mass matrix</span>
0149     ElemMass = Mass4Prism2dFrm (xyz,ElemData);
0150     ElemResp = ElemMass;
0151 <span class="comment">% ==========================================================================================</span>
0152   <span class="keyword">case</span> <span class="string">'post'</span>
0153     <span class="comment">%% post-processing information - coordinates of deformed shape</span>
0154     <span class="comment">% undeformed element length</span>
0155     L   = ElmLenOr(xyz+GeomData.jntoff);
0156     <span class="comment">% extract displacements from ElemState and reshape to array</span>
0157     nen = size(xyz,2);
0158     u   = reshape(ElemState.u,ndf,nen);
0159     <span class="comment">% transform end displacements from global reference to basic system</span>
0160     [~,~,~,v] = GeomTran_2dFrm (ElemData.Geom,xyz,GeomData,u);
0161     <span class="comment">% basic force-deformation</span>
0162     q = <a href="#_sub1" class="code" title="subfunction [q,k] = BasicLE2dFrm (L,ElemData,v)">BasicLE2dFrm</a> (L,ElemData,v);
0163     <span class="comment">% determine deformations ve in the presence of releases, if any</span>
0164     E = ElemData.E;
0165     A = ElemData.A;
0166     I = ElemData.I;
0167     f = blkdiag(L/(E*A),L/(6*E*I).*[2 -1; -1 2]);  <span class="comment">% flexibility matrix</span>
0168     <span class="comment">% initial deformations under uniformly distributed element loads and uniform initial deformations</span>
0169     v0 = [w(1)*L^2/(2*E*A);
0170           w(2)*L^3/(24*E*I);
0171          -w(2)*L^3/(24*E*I)] + [e0(1)*L ; e0(2)*L/2.*[-1;1] ];
0172     <span class="comment">% element deformations ve</span>
0173     ve = f*q + v0;
0174     <span class="comment">% post-processing information</span>
0175     ElemPost.v  = v;
0176     ElemPost.q  = q;
0177     ElemPost.ve = ve;
0178     ElemResp = ElemPost;
0179 <span class="comment">% ==========================================================================================</span>
0180   <span class="keyword">case</span> <span class="string">'defo'</span>
0181     ElemResp = str2func(<span class="string">'DeformShape2dFrm'</span>);    
0182 <span class="comment">% ==========================================================================================</span>
0183   <span class="keyword">otherwise</span>
0184     <span class="comment">%% other actions not supported</span>
0185     warning(<span class="string">'off'</span>,<span class="string">'backtrace'</span>);
0186     warning(<span class="string">'E:W'</span>,[<span class="string">'&gt;&gt; Element '</span>,num2str(el_no,<span class="string">'%i'</span>),<span class="string">': Action &quot;'</span>,action,<span class="string">'&quot; not supported for LE2dFrm element'</span>]);
0187     warning(<span class="string">'on'</span>,<span class="string">'backtrace'</span>);
0188 <span class="keyword">end</span>
0189 
0190 <span class="comment">%% ---- function BasicLE2dFrm --------------------------------------------------------------</span>
0191 <a name="_sub1" href="#_subfunctions" class="code">function [q,k] = BasicLE2dFrm (L,ElemData,v)</a>
0192 <span class="comment">% state determination of basic 2d frame element</span>
0193 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0194 <span class="comment">%  ELEMDATA is a data structure with element property information in fields</span>
0195 <span class="comment">%         A   = cross sectional area</span>
0196 <span class="comment">%         E   = modulus of elasticity</span>
0197 <span class="comment">%         I   = moment of inertia</span>
0198 <span class="comment">%         rho = mass density</span>
0199 <span class="comment">%         w   = uniform element load ( w(1) = longitudinal, w(2) = transverse )</span>
0200 <span class="comment">%         e0  = initial deformations (default = 0)</span>
0201 
0202 A  = ElemData.A;
0203 I  = ElemData.I;
0204 E  = ElemData.E;
0205 w  = ElemData.w;
0206 e0 = ElemData.e0;
0207 RI = ElemData.RI;
0208 
0209 <span class="comment">%% set up stiffness matrix in basic system</span>
0210 EA = E * A;
0211 EI = E * I;
0212 k  = [ EA/L       0       0;
0213          0    4*EI/L  2*EI/L;
0214          0    2*EI/L  4*EI/L];
0215 
0216 <span class="comment">%%    compatibility matrix in the presence of axial and/or moment releases</span>
0217 ah = [ 1-RI(1)       0                    0;
0218         0            1-RI(2)        -0.5*(1-RI(3))*RI(2);
0219         0      -0.5*(1-RI(2))*RI(3)       1-RI(3)        ];
0220 
0221 <span class="comment">%% transform stiffness matrix for the presence of releases</span>
0222 k  = ah'*k*ah;
0223 <span class="comment">% initial element deformations due to element loading and non-mechanical effects</span>
0224 v0      = zeros(3,1);
0225 v0(1)   = w(1)*L*L/(2*EA) + e0(1)*L;
0226 v0(2:3) = w(2)*L^3/(24*EI).*[1;-1] + e0(2)*L/2.*[-1;1];
0227 
0228 <span class="comment">%%    basic force-deformation relation</span>
0229 q = k*(v-v0);</pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->