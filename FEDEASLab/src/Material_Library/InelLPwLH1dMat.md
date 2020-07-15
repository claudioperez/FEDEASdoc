
<!-- <a name="_top"></a>
<div><a href="../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="index.md">Material_Library</a> &gt; InelLPwLH1dMat.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../index.md"><img alt="<" border="0" src="../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Material_Library&nbsp;<img alt=">" border="0" src="../../../../../right.png"></a></td></tr></table>-->
# `InelLPwLH1dMat`
<!-- <h1>InelLPwLH1dMat
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

INELLPwLH1dMAT inelastic linear-plastic 1d model with linear kinematic and isotropic hardening

<!-- <div class="box"><strong>INELLPwLH1dMAT inelastic linear-plastic 1d model with linear kinematic and isotropic hardening</strong></div> -->

## <a name="_synopsis"></a>Syntax

`function MatResp = InelLPwLH1dMat (action,MatNo,MatData,MatState)` 
## <a name="_description"></a>Description

<pre class="comment">INELLPwLH1dMAT inelastic linear-plastic 1d model with linear kinematic and isotropic hardening
  MATRESP = INELLPwLH1dMAT (ACTION,MAT_NO,MATDATA,MATSTATE)
  the function determines the current material state under total strain EPSI
  for an inelastic linear-plastic 1d model with linear kinematic and isotropic hardening
  with the return map algorithm; the plastic strain EPS_P, the back stress SIG_B and the
  isotropic hardening variable ALPHA are the history variables of the model
  Reference: JC Simo and TJR Hughes, Computational Inelasticity, pp. 43-45
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
  MATRESP = MATSTATE  for action = 'hist'
  MATRESP = MATSTATE  for action = 'stif'
  MATRESP = MATSTATE  for action = 'forc'
  MATRESP = MATPOST   for action = 'post'
  MATRESP is empty    for unsupported keywords
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATSTATE is a data structure with information about the current material state in fields
         eps    = total strain
         Deps   = strain increments from last convergence
         DDeps  = strain increments from last iteration
         epsdot = strain rate
         km     = material stiffness matrix; returned under ACTION = 'stif'
         sig    = stress; returned under ACTION = 'stif' or 'forc'
         Past   = material history variables at last converged state
         Pres   = current values of material history variables
             Past and Pres contain the following history variable(s):
             eps_p = plastic strain
             alpha = isotropic hardening variable
             sig_b = back stress (for kinematic hardening)
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATDATA is a data structure with material property information; it has the fields
         E  = initial modulus
         fy = yield strength
         Hi = isotropic plastic   modulus
         Hk = kinematic hardening modulus
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATPOST is a data structure with material response information for post-processing in fields
         eps   = total strain
         sig   = uniaxial stress
         eps_p = plastic strain</pre>
<!-- <div class="fragment"><pre class="comment">INELLPwLH1dMAT inelastic linear-plastic 1d model with linear kinematic and isotropic hardening
  MATRESP = INELLPwLH1dMAT (ACTION,MAT_NO,MATDATA,MATSTATE)
  the function determines the current material state under total strain EPSI
  for an inelastic linear-plastic 1d model with linear kinematic and isotropic hardening
  with the return map algorithm; the plastic strain EPS_P, the back stress SIG_B and the
  isotropic hardening variable ALPHA are the history variables of the model
  Reference: JC Simo and TJR Hughes, Computational Inelasticity, pp. 43-45
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
  MATRESP = MATSTATE  for action = 'hist'
  MATRESP = MATSTATE  for action = 'stif'
  MATRESP = MATSTATE  for action = 'forc'
  MATRESP = MATPOST   for action = 'post'
  MATRESP is empty    for unsupported keywords
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATSTATE is a data structure with information about the current material state in fields
         eps    = total strain
         Deps   = strain increments from last convergence
         DDeps  = strain increments from last iteration
         epsdot = strain rate
         km     = material stiffness matrix; returned under ACTION = 'stif'
         sig    = stress; returned under ACTION = 'stif' or 'forc'
         Past   = material history variables at last converged state
         Pres   = current values of material history variables
             Past and Pres contain the following history variable(s):
             eps_p = plastic strain
             alpha = isotropic hardening variable
             sig_b = back stress (for kinematic hardening)
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATDATA is a data structure with material property information; it has the fields
         E  = initial modulus
         fy = yield strength
         Hi = isotropic plastic   modulus
         Hk = kinematic hardening modulus
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATPOST is a data structure with material response information for post-processing in fields
         eps   = total strain
         sig   = uniaxial stress
         eps_p = plastic strain</pre></div> -->

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
<div class="fragment"><pre>0001 <a name="_sub0" href="#_subfunctions" class="code">function MatResp = InelLPwLH1dMat (action,MatNo,MatData,MatState)</a>
0002 <span class="comment">%INELLPwLH1dMAT inelastic linear-plastic 1d model with linear kinematic and isotropic hardening</span>
0003 <span class="comment">%  MATRESP = INELLPwLH1dMAT (ACTION,MAT_NO,MATDATA,MATSTATE)</span>
0004 <span class="comment">%  the function determines the current material state under total strain EPSI</span>
0005 <span class="comment">%  for an inelastic linear-plastic 1d model with linear kinematic and isotropic hardening</span>
0006 <span class="comment">%  with the return map algorithm; the plastic strain EPS_P, the back stress SIG_B and the</span>
0007 <span class="comment">%  isotropic hardening variable ALPHA are the history variables of the model</span>
0008 <span class="comment">%  Reference: JC Simo and TJR Hughes, Computational Inelasticity, pp. 43-45</span>
0009 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0010 <span class="comment">%  the character variable ACTION should have one of the following values</span>
0011 <span class="comment">%  ACTION = 'chec' function checks material property data for omissions and returns default values in MATDATA</span>
0012 <span class="comment">%           'init' function returns the material history variables in MATSTATE</span>
0013 <span class="comment">%           'forc' function returns the material stress (tensor) in MATSTATE</span>
0014 <span class="comment">%           'stif' function returns the material tangent modulus and the stress (tensor) in MATSTATE</span>
0015 <span class="comment">%           'post' function returns data structure MATPOST with post-processing information</span>
0016 <span class="comment">%  depending on the value of character variable ACTION the function returns information in data structure MATRESP</span>
0017 <span class="comment">%  for the material with number MAT_NO; data structure MATDATA supplies the material property data</span>
0018 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0019 <span class="comment">%  data structure MATRESP stands for one of the following data objects depending on value of ACTION</span>
0020 <span class="comment">%  MATRESP = MATDATA   for action = 'chec'</span>
0021 <span class="comment">%  MATRESP = MATSTATE  for action = 'hist'</span>
0022 <span class="comment">%  MATRESP = MATSTATE  for action = 'stif'</span>
0023 <span class="comment">%  MATRESP = MATSTATE  for action = 'forc'</span>
0024 <span class="comment">%  MATRESP = MATPOST   for action = 'post'</span>
0025 <span class="comment">%  MATRESP is empty    for unsupported keywords</span>
0026 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0027 <span class="comment">%  MATSTATE is a data structure with information about the current material state in fields</span>
0028 <span class="comment">%         eps    = total strain</span>
0029 <span class="comment">%         Deps   = strain increments from last convergence</span>
0030 <span class="comment">%         DDeps  = strain increments from last iteration</span>
0031 <span class="comment">%         epsdot = strain rate</span>
0032 <span class="comment">%         km     = material stiffness matrix; returned under ACTION = 'stif'</span>
0033 <span class="comment">%         sig    = stress; returned under ACTION = 'stif' or 'forc'</span>
0034 <span class="comment">%         Past   = material history variables at last converged state</span>
0035 <span class="comment">%         Pres   = current values of material history variables</span>
0036 <span class="comment">%             Past and Pres contain the following history variable(s):</span>
0037 <span class="comment">%             eps_p = plastic strain</span>
0038 <span class="comment">%             alpha = isotropic hardening variable</span>
0039 <span class="comment">%             sig_b = back stress (for kinematic hardening)</span>
0040 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0041 <span class="comment">%  MATDATA is a data structure with material property information; it has the fields</span>
0042 <span class="comment">%         E  = initial modulus</span>
0043 <span class="comment">%         fy = yield strength</span>
0044 <span class="comment">%         Hi = isotropic plastic   modulus</span>
0045 <span class="comment">%         Hk = kinematic hardening modulus</span>
0046 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0047 <span class="comment">%  MATPOST is a data structure with material response information for post-processing in fields</span>
0048 <span class="comment">%         eps   = total strain</span>
0049 <span class="comment">%         sig   = uniaxial stress</span>
0050 <span class="comment">%         eps_p = plastic strain</span>
0051 
0052 <span class="comment">%  =========================================================================================</span>
0053 <span class="comment">%  FEDEASLab - Release 5.1, July 2020</span>
0054 <span class="comment">%  Matlab Finite Elements for Design, Evaluation and Analysis of Structures</span>
0055 <span class="comment">%  Professor Filip C. Filippou (filippou@berkeley.edu)</span>
0056 <span class="comment">%  Department of Civil and Environmental Engineering, UC Berkeley</span>
0057 <span class="comment">%  Copyright(c) 1998-2020. The Regents of the University of California. All Rights Reserved.</span>
0058 <span class="comment">%  =========================================================================================</span>
0059 <span class="comment">%  function         by Afsin Saritas                                                 10-2001</span>
0060 <span class="comment">%  tolerance option by Chin-Long Lee                                                 01-2008</span>
0061 <span class="comment">%  -----------------------------------------------------------------------------------------</span>
0062 
0063 <span class="keyword">switch</span> action
0064   <span class="keyword">case</span> <span class="string">'chec'</span>
0065     <span class="comment">%% check material data; set default values, if necessary</span>
0066     <span class="keyword">if</span> ~isfield(MatData,<span class="string">'E'</span>),  disp(<span class="string">'Material'</span>);disp(MatNo); error(<span class="string">'Young modulus missing'</span>); <span class="keyword">end</span>
0067     <span class="keyword">if</span> ~isfield(MatData,<span class="string">'fy'</span>), disp(<span class="string">'Material'</span>);disp(MatNo); error(<span class="string">'yield strength missing'</span>); <span class="keyword">end</span>
0068     E = MatData.E;
0069     <span class="keyword">if</span> ~isfield(MatData,<span class="string">'Hi'</span>),    MatData.Hi    = (1e-12)*E; <span class="keyword">end</span>
0070     <span class="keyword">if</span> ~isfield(MatData,<span class="string">'Hk'</span>),    MatData.Hk    = (1e-12)*E; <span class="keyword">end</span>
0071     <span class="keyword">if</span> ~isfield(MatData,<span class="string">'yftol'</span>), MatData.yftol = 1e-20;     <span class="keyword">end</span>
0072     MatResp = MatData;
0073   <span class="keyword">otherwise</span>
0074     <span class="comment">%% extract material properties from MatData</span>
0075     E  = MatData.E;          <span class="comment">% initial elastic modulus</span>
0076     fy = MatData.fy;         <span class="comment">% yield stress</span>
0077     Hi = MatData.Hi;         <span class="comment">% isotropic hardening parameter</span>
0078     Hk = MatData.Hk;         <span class="comment">% kinematic hardening parameter</span>
0079 <span class="keyword">end</span>
0080 <span class="comment">%% material actions</span>
0081 <span class="keyword">switch</span> action
0082   <span class="keyword">case</span> <span class="string">'init'</span>
0083     <span class="comment">%% initialization of history variables</span>
0084     MatState.sig = 0;
0085     MatState.km  = E;
0086     MatState.Pres.alpha = 0;    <span class="comment">% equivalent plastic strain for isotropic hardening</span>
0087     MatState.Pres.eps_p = 0;    <span class="comment">% plastic strains</span>
0088     MatState.Pres.sig_b = 0;    <span class="comment">% backstress</span>
0089     <span class="comment">%       MatState.Pres.km    = E;    % CLL: storing last material stiffness</span>
0090     MatResp = MatState;
0091   <span class="keyword">case</span>{<span class="string">'stif'</span>,<span class="string">'forc'</span>}
0092     <span class="comment">%% state determination</span>
0093     <span class="comment">% recover variables from material history</span>
0094     eps_p = MatState.Past.eps_p;   <span class="comment">% plastic strain from last converged state</span>
0095     sig_b = MatState.Past.sig_b;   <span class="comment">% back stress from last converged state</span>
0096     alpha = MatState.Past.alpha;   <span class="comment">% alpha from last converged state</span>
0097     
0098     <span class="comment">% trial elastic step</span>
0099     epsi    = MatState.eps(:,1);   <span class="comment">% total strain</span>
0100     sig_tr  = E*(epsi - eps_p);
0101     <span class="comment">% check location of trial stress</span>
0102     sig_nrm = abs(sig_tr - sig_b);
0103     fyh     = fy + Hi*alpha;
0104     yf_tr   = sig_nrm - fyh;
0105     
0106     <span class="keyword">if</span>  yf_tr &lt;= MatData.yftol*fyh
0107       <span class="comment">% trial state is admissible (falls inside yield surface)</span>
0108       Et  = E;
0109 <span class="comment">%       if abs(yf_tr)&lt; MatData.yftol*fyh</span>
0110 <span class="comment">%         Et  = MatState.Past.km;      % CLL: use last material stiffness</span>
0111 <span class="comment">%       end</span>
0112       sig = sig_tr;
0113     <span class="keyword">else</span>
0114       H = Hi+Hk;
0115       <span class="comment">% trial state is inadmissible (falls outside yield surface)</span>
0116       Dlam = yf_tr/(E+H);                     <span class="comment">% plastic flow parameter</span>
0117       Et   = E*H/(E+H);                       <span class="comment">% tangent modulus</span>
0118       <span class="comment">% determine plastic strain increment and correct trial stress</span>
0119       n      = sign(sig_tr-sig_b);            <span class="comment">% normal to yield surface</span>
0120       Deps_p = Dlam.*n;                       <span class="comment">% plastic strain increment</span>
0121       sig    = sig_tr - E*Deps_p;
0122       <span class="comment">% update plastic strain, alpha and back stress values</span>
0123       eps_p  = eps_p + Deps_p;
0124       alpha  = alpha + Dlam;
0125       sig_b  = sig_b + Hk*Deps_p;
0126     <span class="keyword">end</span>
0127     <span class="comment">% return current state</span>
0128     MatState.sig = sig;
0129     <span class="keyword">if</span> strcmp(action,<span class="string">'stif'</span>), MatState.km = Et; <span class="keyword">end</span>
0130     <span class="comment">% save material history variables</span>
0131     MatState.Pres.alpha = alpha;
0132     MatState.Pres.eps_p = eps_p;
0133     MatState.Pres.sig_b = sig_b;
0134 <span class="comment">%     MatState.Pres.km    = Et;      % CLL: storing last material stiffness</span>
0135     
0136     MatResp = MatState;
0137     
0138   <span class="keyword">case</span> <span class="string">'post'</span>
0139     <span class="comment">%% state determination</span>
0140     <span class="comment">% recover variables from material history</span>
0141     eps_p = MatState.Past.eps_p;   <span class="comment">% plastic strain from last converged state</span>
0142     sig_b = MatState.Past.sig_b;   <span class="comment">% back stress from last converged state</span>
0143     alpha = MatState.Past.alpha;   <span class="comment">% alpha from last converged state</span>
0144     
0145     <span class="comment">% trial elastic step</span>
0146     epsi    = MatState.eps;         <span class="comment">% total strain</span>
0147     sig_tr  = E*(epsi - eps_p);
0148     <span class="comment">% check location of trial stress</span>
0149     sig_nrm = abs(sig_tr - sig_b);
0150     fyh     = fy+Hi*alpha;
0151     yf_tr   = sig_nrm - fyh;
0152     
0153     <span class="keyword">if</span>  yf_tr &lt;= MatData.yftol*fyh
0154       <span class="comment">% trial state is admissible (falls inside yield surface)</span>
0155       sig = sig_tr;
0156     <span class="keyword">else</span>
0157       H = Hi+Hk;
0158       <span class="comment">% trial state is inadmissible (falls outside yield surface)</span>
0159       Dlam = yf_tr/(E+H);                      <span class="comment">% plastic flow parameter</span>
0160       <span class="comment">% determine plastic strain increment and correct trial stress</span>
0161       n      = sign(sig_tr-sig_b);             <span class="comment">% normal to yield surface</span>
0162       Deps_p = Dlam.*n ;                       <span class="comment">% plastic strain increment</span>
0163       sig    = sig_tr - E*Deps_p;
0164       <span class="comment">% update plastic strain, alpha and back stress values</span>
0165       eps_p  = eps_p + Deps_p;
0166     <span class="keyword">end</span>
0167     <span class="comment">% return current state</span>
0168     MatPost.eps   = MatState.eps(:,1);
0169     MatPost.sig   = sig;
0170     MatPost.eps_p = eps_p;
0171     MatPost.sig_b = sig_b;
0172     MatPost.alpha = alpha;
0173     
0174     MatResp = MatPost;
0175     
0176   <span class="keyword">otherwise</span>
0177     <span class="comment">%% add other actions</span>
0178 <span class="keyword">end</span></pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->