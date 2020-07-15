
<!-- <a name="_top"></a>
<div><a href="../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="index.md">Material_Library</a> &gt; InelJ2PwLH3dMat.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../index.md"><img alt="<" border="0" src="../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Material_Library&nbsp;<img alt=">" border="0" src="../../../../../right.png"></a></td></tr></table>-->
# `InelJ2PwLH3dMat`
<!-- <h1>InelJ2PwLH3dMat
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

INELJ2PwLH3DMAT inelastic 3d material model with J2 plasticity and linear kinematic and isotropic hardening

<!-- <div class="box"><strong>INELJ2PwLH3DMAT inelastic 3d material model with J2 plasticity and linear kinematic and isotropic hardening</strong></div> -->

## <a name="_synopsis"></a>Syntax

`function MatResp = InelJ2PwLH3dMat (action,MatNo,MatData,MatState)` 
## <a name="_description"></a>Description

<pre class="comment">INELJ2PwLH3DMAT inelastic 3d material model with J2 plasticity and linear kinematic and isotropic hardening
  MATRESP = INELJ2PwLH3DMAT (ACTION,MAT_NO,MATDATA,MATSTATE)
  function determines the stress-strain relation for an inelastic 3d material model
           based on J2 plasticity with isotropic and kinematic hardening
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
         eps    = total strain tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23
         Deps   = strain increments from last convergence
         DDeps  = strain increments from last iteration
         epsdot = strain rate tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23
         km     = material stiffness matrix; returned under ACTION = 'stif'
         sig    = stress tensor in 6x1 vector form; returned under ACTION = 'stif' or 'forc'
         Past   = material history variables at last converged state
         Pres   = current values of material history variables
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATDATA is a data structure with material property information; it has the fields
         E  = initial modulus
         fy = yield strength
         nu = Poisson ratio               (default = 0)
         Hk = kinematic hardening modulus (default = 0)
         Hi = isotropic hardening modulus (default = 0)
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATPOST is a data structure with material response information for post-processing in fields
         eps   =         strain tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23
         sig   =         stress tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23
         eps_p = plastic strain tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23</pre>
<!-- <div class="fragment"><pre class="comment">INELJ2PwLH3DMAT inelastic 3d material model with J2 plasticity and linear kinematic and isotropic hardening
  MATRESP = INELJ2PwLH3DMAT (ACTION,MAT_NO,MATDATA,MATSTATE)
  function determines the stress-strain relation for an inelastic 3d material model
           based on J2 plasticity with isotropic and kinematic hardening
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
         eps    = total strain tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23
         Deps   = strain increments from last convergence
         DDeps  = strain increments from last iteration
         epsdot = strain rate tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23
         km     = material stiffness matrix; returned under ACTION = 'stif'
         sig    = stress tensor in 6x1 vector form; returned under ACTION = 'stif' or 'forc'
         Past   = material history variables at last converged state
         Pres   = current values of material history variables
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATDATA is a data structure with material property information; it has the fields
         E  = initial modulus
         fy = yield strength
         nu = Poisson ratio               (default = 0)
         Hk = kinematic hardening modulus (default = 0)
         Hi = isotropic hardening modulus (default = 0)
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATPOST is a data structure with material response information for post-processing in fields
         eps   =         strain tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23
         sig   =         stress tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23
         eps_p = plastic strain tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23</pre></div> -->

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
<div class="fragment"><pre>0001 <a name="_sub0" href="#_subfunctions" class="code">function MatResp = InelJ2PwLH3dMat (action,MatNo,MatData,MatState)</a>
0002 <span class="comment">%INELJ2PwLH3DMAT inelastic 3d material model with J2 plasticity and linear kinematic and isotropic hardening</span>
0003 <span class="comment">%  MATRESP = INELJ2PwLH3DMAT (ACTION,MAT_NO,MATDATA,MATSTATE)</span>
0004 <span class="comment">%  function determines the stress-strain relation for an inelastic 3d material model</span>
0005 <span class="comment">%           based on J2 plasticity with isotropic and kinematic hardening</span>
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
0024 <span class="comment">%         eps    = total strain tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23</span>
0025 <span class="comment">%         Deps   = strain increments from last convergence</span>
0026 <span class="comment">%         DDeps  = strain increments from last iteration</span>
0027 <span class="comment">%         epsdot = strain rate tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23</span>
0028 <span class="comment">%         km     = material stiffness matrix; returned under ACTION = 'stif'</span>
0029 <span class="comment">%         sig    = stress tensor in 6x1 vector form; returned under ACTION = 'stif' or 'forc'</span>
0030 <span class="comment">%         Past   = material history variables at last converged state</span>
0031 <span class="comment">%         Pres   = current values of material history variables</span>
0032 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0033 <span class="comment">%  MATDATA is a data structure with material property information; it has the fields</span>
0034 <span class="comment">%         E  = initial modulus</span>
0035 <span class="comment">%         fy = yield strength</span>
0036 <span class="comment">%         nu = Poisson ratio               (default = 0)</span>
0037 <span class="comment">%         Hk = kinematic hardening modulus (default = 0)</span>
0038 <span class="comment">%         Hi = isotropic hardening modulus (default = 0)</span>
0039 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0040 <span class="comment">%  MATPOST is a data structure with material response information for post-processing in fields</span>
0041 <span class="comment">%         eps   =         strain tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23</span>
0042 <span class="comment">%         sig   =         stress tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23</span>
0043 <span class="comment">%         eps_p = plastic strain tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23</span>
0044 
0045 <span class="comment">%  =========================================================================================</span>
0046 <span class="comment">%  FEDEASLab - Release 5.1, July 2020</span>
0047 <span class="comment">%  Matlab Finite Elements for Design, Evaluation and Analysis of Structures</span>
0048 <span class="comment">%  Professor Filip C. Filippou (filippou@berkeley.edu)</span>
0049 <span class="comment">%  Department of Civil and Environmental Engineering, UC Berkeley</span>
0050 <span class="comment">%  Copyright(c) 1998-2020. The Regents of the University of California. All Rights Reserved.</span>
0051 <span class="comment">%  =========================================================================================</span>
0052 <span class="comment">%  function by Afsin Saritas(c)                                                      11-2001</span>
0053 <span class="comment">%  -----------------------------------------------------------------------------------------</span>
0054 
0055 <span class="keyword">switch</span> action
0056    <span class="keyword">case</span> <span class="string">'chec'</span>
0057       <span class="comment">%% check material data; set default values, if necessary</span>
0058       <span class="keyword">if</span> ~isfield(MatData,<span class="string">'E'</span>),  disp(<span class="string">'Material'</span>);disp(MatNo); error(<span class="string">'Young modulus missing'</span>); <span class="keyword">end</span>
0059       <span class="keyword">if</span> ~isfield(MatData,<span class="string">'fy'</span>), disp(<span class="string">'Material'</span>);disp(MatNo); error(<span class="string">'yield stress missing'</span>); <span class="keyword">end</span>
0060       <span class="keyword">if</span> ~isfield(MatData,<span class="string">'nu'</span>),    MatData.nu = 0;           <span class="keyword">end</span>
0061       <span class="keyword">if</span> ~isfield(MatData,<span class="string">'Hi'</span>),    MatData.Hi = 0;           <span class="keyword">end</span>
0062       <span class="keyword">if</span> ~isfield(MatData,<span class="string">'Hk'</span>),    MatData.Hk = 0;           <span class="keyword">end</span>
0063       <span class="keyword">if</span> ~isfield(MatData,<span class="string">'yftol'</span>), MatData.yftol = 1000*eps; <span class="keyword">end</span>
0064       MatResp = MatData;
0065    <span class="keyword">otherwise</span>
0066       <span class="comment">%% extract material properties from MatData</span>
0067       E   = MatData.E;     <span class="comment">% elastic modulus</span>
0068       fy  = MatData.fy;
0069       nu  = MatData.nu;    <span class="comment">% Poisson ratio</span>
0070       Hi  = MatData.Hi;    <span class="comment">% isotropic hardening modulus</span>
0071       Hk  = MatData.Hk;    <span class="comment">% kinematic hardening modulus</span>
0072       <span class="comment">% additional material parameters</span>
0073       G   = E/2/(1+nu);    <span class="comment">% shear modulus</span>
0074       TG  = 2*G;
0075       K   = E/3/(1-2*nu);  <span class="comment">% bulk  modulus</span>
0076       <span class="comment">% useful vectors and matrices</span>
0077       Iv6 = [1 1 1 0 0 0]';           <span class="comment">% 2nd order volumetric 6x1 vector</span>
0078       Ivp = [ ones(3) zeros(3);       <span class="comment">% Iv6*Iv6' volumetric projection</span>
0079               zeros(3) zeros(3)];      
0080       Idp = eye(6) - Ivp./3;          <span class="comment">% deviatoric projection</span>
0081       I   = diag([ones(1,3) 0.5.*ones(1,3)]);
0082       Id  = I-Ivp./3;
0083 
0084       <span class="comment">% generate projection matrix for transformation from 9 to 6 component vectors</span>
0085       <span class="comment">% (Note: FE programs provide strain and stress tensors as 6 component vectors)</span>
0086       ix  = [1:10:31 42 53];
0087       Pvt = zeros(1,54);
0088       Pvt(ix(1:3)) = 1;
0089       Pvt([ix(4:6) ix(4:6)+1]) = 0.5;
0090       P = reshape(Pvt,9,6);
0091 <span class="keyword">end</span>
0092 <span class="comment">%% material actions</span>
0093 <span class="keyword">switch</span> action
0094    <span class="keyword">case</span> <span class="string">'init'</span>
0095       <span class="comment">%% initialization and specification of history variables</span>
0096       sig = zeros(6,1);
0097       Ce  = K.*Ivp + TG.*Id;
0098       MatState.sig = sig;
0099       MatState.km  = Ce;
0100       MatState.Pres.sig   = sig;           <span class="comment">% for post-processing</span>
0101       MatState.Pres.alpha = 0;             <span class="comment">% equivalent plastic strain</span>
0102       MatState.Pres.eps_p = zeros(6,1);    <span class="comment">% plastic strain</span>
0103       MatState.Pres.sig_b = zeros(9,1);    <span class="comment">% backstress (9x1, affects deviatoric stress only)</span>
0104       MatResp = MatState;
0105    <span class="keyword">case</span>{<span class="string">'stif'</span>,<span class="string">'forc'</span>}
0106       <span class="comment">%% state determination</span>
0107       <span class="comment">% retrieve history variables from last convergence</span>
0108       eps_p = MatState.Past.eps_p ;        <span class="comment">% plastic deviatoric strain</span>
0109       sig_b = MatState.Past.sig_b;         <span class="comment">% back stress as 9x1 vector</span>
0110       alpha = MatState.Past.alpha;         <span class="comment">% strain hardening variable</span>
0111       <span class="comment">% update strain tensor; compute trial elastic stress</span>
0112       eps_d  = Idp*MatState.eps;           <span class="comment">% deviatoric strain vector</span>
0113       eps_v  = Iv6'*MatState.eps;          <span class="comment">% volumetric strain (scalar)</span>
0114       sid_tr = TG.*P*(eps_d - eps_p);      <span class="comment">% trial 9x1 deviatoric stress</span>
0115       <span class="comment">% check location of trial stress</span>
0116       sig_nrm = norm(sid_tr - sig_b);
0117       yf_tr   = sig_nrm - sqrt(2/3)*(fy + Hi*alpha);
0118       <span class="keyword">if</span> yf_tr &lt;= MatData.yftol
0119          <span class="comment">% trial state is admissible (falls inside yield surface)</span>
0120          sid = sid_tr;
0121          <span class="comment">% algorithmic elastoplastic tangent</span>
0122          Ct  = K.*Ivp + TG.*Id;
0123       <span class="keyword">else</span>
0124          H = Hi+Hk;
0125          <span class="comment">% trial state is inadmissible (falls outside yield surface)</span>
0126          Gp   = G + H/3;
0127          Dlam = yf_tr /(2*Gp);                  <span class="comment">% Dlam is determined in closed form</span>
0128          n    = (sid_tr - sig_b)./sig_nrm;       <span class="comment">% normal to yield surface</span>
0129          <span class="comment">% determine plastic strain increment and correct trial stress</span>
0130          Deps_p = Dlam*n;
0131          sid    = sid_tr- TG*Deps_p;
0132          <span class="comment">% update plastic strain, alpha and back stress values</span>
0133          eps_p = eps_p + I\(P'*Deps_p);
0134          alpha = alpha + sqrt(2/3)*Dlam;
0135          sig_b = sig_b + 2/3*Hk*Deps_p;
0136          <span class="comment">% algorithmic elasto-plastic tangent</span>
0137          n  = P'*n;                              <span class="comment">% projection to 6 component vector</span>
0138          Ct = K.*Ivp + TG.*(1-TG*Dlam/sig_nrm).*(Id-n*n') + (TG*H/(3*Gp)).*(n*n');
0139       <span class="keyword">end</span>
0140       <span class="comment">% update stress and plastic strain after projecting stress to 6 component vector</span>
0141       sig = P'*sid + (K*eps_v).*Iv6;
0142       <span class="comment">% return current state</span>
0143       MatState.sig = sig;
0144       MatState.Pres.sig = sig;     <span class="comment">% for post-processing</span>
0145       <span class="keyword">if</span> strcmp(action,<span class="string">'stif'</span>), MatState.km = Ct; <span class="keyword">end</span>
0146       <span class="comment">% update history variables</span>
0147       MatState.Pres.alpha = alpha;
0148       MatState.Pres.eps_p = eps_p;
0149       MatState.Pres.sig_b = sig_b;
0150       MatResp = MatState;
0151    <span class="keyword">case</span> <span class="string">'post'</span>
0152       <span class="comment">%% post-processing</span>
0153       MatPost.eps   = MatState.eps;
0154       MatPost.sig   = MatState.Pres.sig;
0155       MatPost.eps_p = MatState.Pres.eps_p;
0156       MatPost.sig_b = MatState.Pres.sig_b;
0157       MatPost.alpha = MatState.Pres.alpha;      
0158       MatResp = MatPost;
0159    <span class="keyword">otherwise</span>
0160       <span class="comment">%% add other actions</span>
0161 <span class="keyword">end</span></pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->