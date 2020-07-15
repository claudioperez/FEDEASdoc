
<!-- <a name="_top"></a>
<div><a href="../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="index.md">Material_Library</a> &gt; LEIso2dMat.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../index.md"><img alt="<" border="0" src="../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Material_Library&nbsp;<img alt=">" border="0" src="../../../../../right.png"></a></td></tr></table>-->
# `LEIso2dMat`
<!-- <h1>LEIso2dMat
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

LEISO2dMAT linear elastic, isotropic 2d material model under general plane stress or strain conditions

<!-- <div class="box"><strong>LEISO2dMAT linear elastic, isotropic 2d material model under general plane stress or strain conditions</strong></div> -->

## <a name="_synopsis"></a>Syntax

`function MatResp = LEIso2dMat (action,MatNo,MatData,MatState)` 
## <a name="_description"></a>Description

<pre class="comment">LEISO2dMAT linear elastic, isotropic 2d material model under general plane stress or strain conditions 
  MATRESP = LEISO2dMAT (ACTION,MATNO,MATDATA,MATSTATE)
  function determines the response of a linear elastic, isotropic material
           under general plane stress or strain conditions
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  the character variable ACTION should have one of the following values
  ACTION = 'chec' function checks material property data for omissions and returns default values in MATDATA
           'init' function returns the material history variables in MATSTATE
           'forc' function returns the material stress (tensor) in MATSTATE
           'stif' function returns the material tangent modulus and the stress (tensor) in MATSTATE
           'post' function returns data structure MATPOST with post-processing information
  depending on the value of character variable ACTION the function returns information in data structure MATRESP
  for the material with number MAT_NO; data structure MATDATA supplies the material property data
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  data structure MATRESP stands for one of the following data objects depending on value of ACTION 
  MATRESP = MATDATA   for action = 'chec'
  MATRESP = MATSTATE  for action = 'init'
  MATRESP = MATSTATE  for action = 'stif'
  MATRESP = MATSTATE  for action = 'forc'
  MATRESP = MATPOST   for action = 'post'
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATSTATE is a data structure with information about the current material state in fields
         eps    = total strain tensor in 4x1 vector form in the order 11, 22, 33, 12
         Deps   = strain increments from last convergence
         DDeps  = strain increments from last iteration
         epsdot = strain rate tensor in 4x1 vector form in the order 11, 22, 33, 12
         km     = material stiffness matrix; returned under ACTION = 'stif'
         sig    = stress tensor in 4x1 vector form; returned under ACTION = 'stif' or 'forc'
         Past   = material history variables at last converged state
         Pres   = current values of material history variables
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATDATA is a data structure with material property information; it has the fields
         E    = Young modulus
         nu   = Poisson ratio
         eps0 = initial strain tensor in 4x1 vector form in the order 11, 22, 33, 12
         sig0 = initial stress tensor in 4x1 vector form in the order 11, 22, 33, 12
         Case = 'stress' or 'strain'
         irs  = stress or strain components to be retained depending on Case
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATPOST is a data structure with material response information for post-processing in fields
         eps = strain tensor in 4x1 vector form in the order 11, 22, 33, 12
         sig = stress tensor in 4x1 vector form in the order 11, 22, 33, 12</pre>
<!-- <div class="fragment"><pre class="comment">LEISO2dMAT linear elastic, isotropic 2d material model under general plane stress or strain conditions 
  MATRESP = LEISO2dMAT (ACTION,MATNO,MATDATA,MATSTATE)
  function determines the response of a linear elastic, isotropic material
           under general plane stress or strain conditions
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  the character variable ACTION should have one of the following values
  ACTION = 'chec' function checks material property data for omissions and returns default values in MATDATA
           'init' function returns the material history variables in MATSTATE
           'forc' function returns the material stress (tensor) in MATSTATE
           'stif' function returns the material tangent modulus and the stress (tensor) in MATSTATE
           'post' function returns data structure MATPOST with post-processing information
  depending on the value of character variable ACTION the function returns information in data structure MATRESP
  for the material with number MAT_NO; data structure MATDATA supplies the material property data
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  data structure MATRESP stands for one of the following data objects depending on value of ACTION 
  MATRESP = MATDATA   for action = 'chec'
  MATRESP = MATSTATE  for action = 'init'
  MATRESP = MATSTATE  for action = 'stif'
  MATRESP = MATSTATE  for action = 'forc'
  MATRESP = MATPOST   for action = 'post'
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATSTATE is a data structure with information about the current material state in fields
         eps    = total strain tensor in 4x1 vector form in the order 11, 22, 33, 12
         Deps   = strain increments from last convergence
         DDeps  = strain increments from last iteration
         epsdot = strain rate tensor in 4x1 vector form in the order 11, 22, 33, 12
         km     = material stiffness matrix; returned under ACTION = 'stif'
         sig    = stress tensor in 4x1 vector form; returned under ACTION = 'stif' or 'forc'
         Past   = material history variables at last converged state
         Pres   = current values of material history variables
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATDATA is a data structure with material property information; it has the fields
         E    = Young modulus
         nu   = Poisson ratio
         eps0 = initial strain tensor in 4x1 vector form in the order 11, 22, 33, 12
         sig0 = initial stress tensor in 4x1 vector form in the order 11, 22, 33, 12
         Case = 'stress' or 'strain'
         irs  = stress or strain components to be retained depending on Case
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATPOST is a data structure with material response information for post-processing in fields
         eps = strain tensor in 4x1 vector form in the order 11, 22, 33, 12
         sig = stress tensor in 4x1 vector form in the order 11, 22, 33, 12</pre></div> -->

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
<div class="fragment"><pre>0001 <a name="_sub0" href="#_subfunctions" class="code">function MatResp = LEIso2dMat (action,MatNo,MatData,MatState)</a>
0002 <span class="comment">%LEISO2dMAT linear elastic, isotropic 2d material model under general plane stress or strain conditions</span>
0003 <span class="comment">%  MATRESP = LEISO2dMAT (ACTION,MATNO,MATDATA,MATSTATE)</span>
0004 <span class="comment">%  function determines the response of a linear elastic, isotropic material</span>
0005 <span class="comment">%           under general plane stress or strain conditions</span>
0006 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0007 <span class="comment">%  the character variable ACTION should have one of the following values</span>
0008 <span class="comment">%  ACTION = 'chec' function checks material property data for omissions and returns default values in MATDATA</span>
0009 <span class="comment">%           'init' function returns the material history variables in MATSTATE</span>
0010 <span class="comment">%           'forc' function returns the material stress (tensor) in MATSTATE</span>
0011 <span class="comment">%           'stif' function returns the material tangent modulus and the stress (tensor) in MATSTATE</span>
0012 <span class="comment">%           'post' function returns data structure MATPOST with post-processing information</span>
0013 <span class="comment">%  depending on the value of character variable ACTION the function returns information in data structure MATRESP</span>
0014 <span class="comment">%  for the material with number MAT_NO; data structure MATDATA supplies the material property data</span>
0015 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0016 <span class="comment">%  data structure MATRESP stands for one of the following data objects depending on value of ACTION</span>
0017 <span class="comment">%  MATRESP = MATDATA   for action = 'chec'</span>
0018 <span class="comment">%  MATRESP = MATSTATE  for action = 'init'</span>
0019 <span class="comment">%  MATRESP = MATSTATE  for action = 'stif'</span>
0020 <span class="comment">%  MATRESP = MATSTATE  for action = 'forc'</span>
0021 <span class="comment">%  MATRESP = MATPOST   for action = 'post'</span>
0022 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0023 <span class="comment">%  MATSTATE is a data structure with information about the current material state in fields</span>
0024 <span class="comment">%         eps    = total strain tensor in 4x1 vector form in the order 11, 22, 33, 12</span>
0025 <span class="comment">%         Deps   = strain increments from last convergence</span>
0026 <span class="comment">%         DDeps  = strain increments from last iteration</span>
0027 <span class="comment">%         epsdot = strain rate tensor in 4x1 vector form in the order 11, 22, 33, 12</span>
0028 <span class="comment">%         km     = material stiffness matrix; returned under ACTION = 'stif'</span>
0029 <span class="comment">%         sig    = stress tensor in 4x1 vector form; returned under ACTION = 'stif' or 'forc'</span>
0030 <span class="comment">%         Past   = material history variables at last converged state</span>
0031 <span class="comment">%         Pres   = current values of material history variables</span>
0032 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0033 <span class="comment">%  MATDATA is a data structure with material property information; it has the fields</span>
0034 <span class="comment">%         E    = Young modulus</span>
0035 <span class="comment">%         nu   = Poisson ratio</span>
0036 <span class="comment">%         eps0 = initial strain tensor in 4x1 vector form in the order 11, 22, 33, 12</span>
0037 <span class="comment">%         sig0 = initial stress tensor in 4x1 vector form in the order 11, 22, 33, 12</span>
0038 <span class="comment">%         Case = 'stress' or 'strain'</span>
0039 <span class="comment">%         irs  = stress or strain components to be retained depending on Case</span>
0040 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0041 <span class="comment">%  MATPOST is a data structure with material response information for post-processing in fields</span>
0042 <span class="comment">%         eps = strain tensor in 4x1 vector form in the order 11, 22, 33, 12</span>
0043 <span class="comment">%         sig = stress tensor in 4x1 vector form in the order 11, 22, 33, 12</span>
0044 
0045 <span class="comment">%  =========================================================================================</span>
0046 <span class="comment">%  FEDEASLab - Release 5.1, July 2020</span>
0047 <span class="comment">%  Matlab Finite Elements for Design, Evaluation and Analysis of Structures</span>
0048 <span class="comment">%  Professor Filip C. Filippou (filippou@berkeley.edu)</span>
0049 <span class="comment">%  Department of Civil and Environmental Engineering, UC Berkeley</span>
0050 <span class="comment">%  Copyright(c) 1998-2020. The Regents of the University of California. All Rights Reserved.</span>
0051 <span class="comment">%  =========================================================================================</span>
0052 
0053 <span class="keyword">switch</span> action
0054   <span class="keyword">case</span> <span class="string">'chec'</span>
0055      <span class="comment">%% check material data; set default values, if necessary</span>
0056     <span class="keyword">if</span> ~isfield(MatData,<span class="string">'E'</span>),  disp(<span class="string">'Material'</span>);disp(MatNo); error(<span class="string">'Young modulus missing'</span>);<span class="keyword">end</span>
0057     <span class="keyword">if</span> ~isfield(MatData,<span class="string">'nu'</span>),    MatData.nu = 0; <span class="keyword">end</span>
0058     <span class="keyword">if</span> ~isfield(MatData,<span class="string">'eps0'</span>),  MatData.eps0 = zeros(4,1); <span class="keyword">end</span>
0059     <span class="keyword">if</span> ~isfield(MatData,<span class="string">'sig0'</span>),  MatData.sig0 = zeros(4,1); <span class="keyword">end</span>
0060     <span class="keyword">if</span> ~isfield(MatData,<span class="string">'Case'</span>),  MatData.Case = <span class="string">'stress'</span>;   <span class="keyword">end</span>
0061     <span class="keyword">if</span> ~isfield(MatData,<span class="string">'irs'</span>)
0062        MatData.irs = [1 2 4];
0063        MatData.ics = 3;
0064     <span class="keyword">else</span>
0065        MatData.ics = setdiff(1:4,MatData.irs);
0066     <span class="keyword">end</span>
0067     MatResp = MatData;
0068     <span class="keyword">return</span>
0069   <span class="keyword">otherwise</span>
0070      <span class="comment">%% extract material properties from MatData</span>
0071     E    = MatData.E;         <span class="comment">% elastic modulus</span>
0072     nu   = MatData.nu;        <span class="comment">% Poisson ratio</span>
0073     eps0 = MatData.eps0;      <span class="comment">% initial strain</span>
0074     sig0 = MatData.sig0;      <span class="comment">% initial stress</span>
0075     ir   = MatData.irs;       <span class="comment">% strain or stress components to retain</span>
0076     ic   = MatData.ics;       <span class="comment">% strain or stress components to set to zero</span>
0077 <span class="keyword">end</span>
0078 
0079 <span class="comment">% material compliance modulus</span>
0080 C = zeros(4);
0081 <span class="comment">% insert common term</span>
0082 C(1:3,1:3) = -nu;
0083 <span class="comment">% correct diagonal terms</span>
0084 C = C + diag((1+nu).*[1;1;1;2]);
0085 C = C./E;
0086 
0087 <span class="keyword">switch</span> MatData.Case
0088    <span class="keyword">case</span> <span class="string">'strain'</span>
0089       <span class="comment">%% plane strain conditions</span>
0090       [Cp,epsr0] = Condense_MV(C,ir,eps0);
0091    <span class="keyword">case</span> <span class="string">'stress'</span>
0092       <span class="comment">%% plane stress conditions</span>
0093       Cp    = C(ir,ir);
0094       epsr0 = eps0(ir) - C(ir,ic)*sig0(ic);
0095 <span class="keyword">end</span>
0096 
0097 <span class="comment">%% material actions</span>
0098 <span class="keyword">switch</span> action
0099    <span class="keyword">case</span> <span class="string">'init'</span>
0100       <span class="comment">%% initialization and specification of history variables</span>
0101       MatState.sig  = 0;
0102       MatState.km   = inv(Cp);
0103       MatState.Pres = [];       <span class="comment">% the material is path-independent with no history variables</span>
0104       MatResp = MatState;
0105    <span class="keyword">case</span> <span class="string">'stif'</span>
0106       <span class="comment">%% state determination</span>
0107       <span class="comment">% compute stress</span>
0108       sig = Cp \ (MatState.eps - epsr0) + sig0(ir);
0109       MatState.sig = sig;       <span class="comment">% current stress</span>
0110       MatState.km  = inv(Cp);
0111       MatResp = MatState;
0112    <span class="keyword">case</span> <span class="string">'forc'</span>
0113       <span class="comment">%% state determination</span>
0114       <span class="comment">% compute stress</span>
0115       sig = Cp \ (MatState.eps - epsr0) + sig0(ir);
0116       MatState.sig = sig;               <span class="comment">% current stress</span>
0117       MatResp = MatState;
0118    <span class="keyword">case</span> <span class="string">'post'</span>
0119       <span class="comment">%% post-processing</span>
0120       sig = Cp \ (MatState.eps - epsr0) + sig0(ir);
0121       <span class="keyword">switch</span> MatData.Case
0122          <span class="keyword">case</span> <span class="string">'strain'</span>
0123             <span class="comment">% recover extra stress components for plane strain</span>
0124             sigr     = zeros(4,1);
0125             sigr(ir) = sig;
0126             sigr(ic) = -C(ic,ic)\(C(ic,ir)*(sig-sig0(ir))+ eps0(ic)) + sig0(ic);
0127             epsi     = zeros(4,1);
0128             epsi(ir) = MatState.eps;
0129          <span class="keyword">case</span> <span class="string">'stress'</span>
0130             <span class="comment">% recover extra strain components for plane stress</span>
0131             sigr     = zeros(4,1);
0132             sigr(ir) = sig;
0133             epsi     = zeros(4,1);
0134             epsi(ir) = MatState.eps;
0135             epsi(ic) = C(ic,ir)*(sig-sig0(ir)) + eps0(ic);
0136       <span class="keyword">end</span>
0137       MatPost.eps = epsi;
0138       MatPost.sig = sigr;
0139       MatResp     = MatPost;
0140    <span class="keyword">otherwise</span>
0141       <span class="comment">%% add other actions</span>
0142 <span class="keyword">end</span></pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->