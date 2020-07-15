
<!-- <a name="_top"></a>
<div><a href="../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="index.md">Material_Library</a> &gt; GMP1dMat.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../index.md"><img alt="<" border="0" src="../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Material_Library&nbsp;<img alt=">" border="0" src="../../../../../right.png"></a></td></tr></table>-->
# `GMP1dMat`
<!-- <h1>GMP1dMat
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

GMP1DMAT uniaxial stress-strain relation for Giuffre-Menegotto-Pinto hysteretic material

<!-- <div class="box"><strong>GMP1DMAT uniaxial stress-strain relation for Giuffre-Menegotto-Pinto hysteretic material</strong></div> -->

## <a name="_synopsis"></a>Syntax

`function MatResp = GMP1dMat (action,MatNo,MatData,MatState)` 
## <a name="_description"></a>Description

<pre class="comment">GMP1DMAT uniaxial stress-strain relation for Giuffre-Menegotto-Pinto hysteretic material    
  MATRESP = GMP1DMAT (ACTION,MATNO,MATDATA,MATSTATE)
  function determines the uniaxial stress-strain relation for Giuffre-Menegotto-Pinto hysteretic material
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
  MATRESP is empty    for unsupported keywords
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATSTATE is a data structure with information about the current material state in fields
         eps    = total strain (tensor for 2d or 3d)
         Deps   = strain increments from last convergence
         DDeps  = strain increments from last iteration
         epsdot = strain rate (tensor for 2d or 3d)
         km     = material tangent modulus; returned under ACTION = 'stif'
         sig    = stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'
         Past   = material history variables at last converged state
         Pres   = current values of material history variables
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATDATA is a data structure with material property information in fields
         E  = initial modulus
         fy = yield strength
         b   = strain hardening ratio
         R0  = exp transition elastic-plastic (default value 20)
         cR1 = coefficient for variation of R0 (default value 0.925)
         cR2 = coefficient for variation of R0 (default value 0.15)
         a1  = isotropic hardening (IH) coefficient in compression (default value 0)
         a2  = trigger strain ductility for IH      in compression (default value 0)
         a3  = isotropic hardening (IH) coefficient in tension     (default value 0)
         a4  = trigger strain ductility for IH      in tension     (default value 0)
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATPOST is a data structure with material response information for post-processing in fields
         eps = total strain
         sig = uniaxial stress</pre>
<!-- <div class="fragment"><pre class="comment">GMP1DMAT uniaxial stress-strain relation for Giuffre-Menegotto-Pinto hysteretic material    
  MATRESP = GMP1DMAT (ACTION,MATNO,MATDATA,MATSTATE)
  function determines the uniaxial stress-strain relation for Giuffre-Menegotto-Pinto hysteretic material
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
  MATRESP is empty    for unsupported keywords
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATSTATE is a data structure with information about the current material state in fields
         eps    = total strain (tensor for 2d or 3d)
         Deps   = strain increments from last convergence
         DDeps  = strain increments from last iteration
         epsdot = strain rate (tensor for 2d or 3d)
         km     = material tangent modulus; returned under ACTION = 'stif'
         sig    = stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'
         Past   = material history variables at last converged state
         Pres   = current values of material history variables
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATDATA is a data structure with material property information in fields
         E  = initial modulus
         fy = yield strength
         b   = strain hardening ratio
         R0  = exp transition elastic-plastic (default value 20)
         cR1 = coefficient for variation of R0 (default value 0.925)
         cR2 = coefficient for variation of R0 (default value 0.15)
         a1  = isotropic hardening (IH) coefficient in compression (default value 0)
         a2  = trigger strain ductility for IH      in compression (default value 0)
         a3  = isotropic hardening (IH) coefficient in tension     (default value 0)
         a4  = trigger strain ductility for IH      in tension     (default value 0)
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATPOST is a data structure with material response information for post-processing in fields
         eps = total strain
         sig = uniaxial stress</pre></div> -->

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
<li><a href="#_sub1" class="code">function [sig,Et] = Bauschinger (epex,ep0,epy,R0,cR1,cR2,epss,epr,b,s0,sr,E)</a></li></ul>

<h2><a name="_source"></a>SOURCE CODE</h2>
<div class="fragment"><pre>0001 <a name="_sub0" href="#_subfunctions" class="code">function MatResp = GMP1dMat (action,MatNo,MatData,MatState)</a>
0002 <span class="comment">%GMP1DMAT uniaxial stress-strain relation for Giuffre-Menegotto-Pinto hysteretic material</span>
0003 <span class="comment">%  MATRESP = GMP1DMAT (ACTION,MATNO,MATDATA,MATSTATE)</span>
0004 <span class="comment">%  function determines the uniaxial stress-strain relation for Giuffre-Menegotto-Pinto hysteretic material</span>
0005 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0006 <span class="comment">%  the character variable ACTION should have one of the following values</span>
0007 <span class="comment">%  ACTION = 'chec' function checks material property data for omissions and returns default values in MATDATA</span>
0008 <span class="comment">%           'init' function returns the material history variables in MATSTATE</span>
0009 <span class="comment">%           'forc' function returns the material stress (tensor) in MATSTATE</span>
0010 <span class="comment">%           'stif' function returns the material tangent modulus and the stress (tensor) in MATSTATE</span>
0011 <span class="comment">%           'post' function returns data structure MATPOST with post-processing information</span>
0012 <span class="comment">%  depending on the value of character variable ACTION the function returns information in data structure MATRESP</span>
0013 <span class="comment">%  for the material with number MAT_NO; data structure MATDATA supplies the material property data</span>
0014 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0015 <span class="comment">%  data structure MATRESP stands for one of the following data objects depending on value of ACTION</span>
0016 <span class="comment">%  MATRESP = MATDATA   for action = 'chec'</span>
0017 <span class="comment">%  MATRESP = MATSTATE  for action = 'init'</span>
0018 <span class="comment">%  MATRESP = MATSTATE  for action = 'stif'</span>
0019 <span class="comment">%  MATRESP = MATSTATE  for action = 'forc'</span>
0020 <span class="comment">%  MATRESP = MATPOST   for action = 'post'</span>
0021 <span class="comment">%  MATRESP is empty    for unsupported keywords</span>
0022 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0023 <span class="comment">%  MATSTATE is a data structure with information about the current material state in fields</span>
0024 <span class="comment">%         eps    = total strain (tensor for 2d or 3d)</span>
0025 <span class="comment">%         Deps   = strain increments from last convergence</span>
0026 <span class="comment">%         DDeps  = strain increments from last iteration</span>
0027 <span class="comment">%         epsdot = strain rate (tensor for 2d or 3d)</span>
0028 <span class="comment">%         km     = material tangent modulus; returned under ACTION = 'stif'</span>
0029 <span class="comment">%         sig    = stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'</span>
0030 <span class="comment">%         Past   = material history variables at last converged state</span>
0031 <span class="comment">%         Pres   = current values of material history variables</span>
0032 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0033 <span class="comment">%  MATDATA is a data structure with material property information in fields</span>
0034 <span class="comment">%         E  = initial modulus</span>
0035 <span class="comment">%         fy = yield strength</span>
0036 <span class="comment">%         b   = strain hardening ratio</span>
0037 <span class="comment">%         R0  = exp transition elastic-plastic (default value 20)</span>
0038 <span class="comment">%         cR1 = coefficient for variation of R0 (default value 0.925)</span>
0039 <span class="comment">%         cR2 = coefficient for variation of R0 (default value 0.15)</span>
0040 <span class="comment">%         a1  = isotropic hardening (IH) coefficient in compression (default value 0)</span>
0041 <span class="comment">%         a2  = trigger strain ductility for IH      in compression (default value 0)</span>
0042 <span class="comment">%         a3  = isotropic hardening (IH) coefficient in tension     (default value 0)</span>
0043 <span class="comment">%         a4  = trigger strain ductility for IH      in tension     (default value 0)</span>
0044 <span class="comment">%  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>
0045 <span class="comment">%  MATPOST is a data structure with material response information for post-processing in fields</span>
0046 <span class="comment">%         eps = total strain</span>
0047 <span class="comment">%         sig = uniaxial stress</span>
0048 
0049 <span class="comment">%  =========================================================================================</span>
0050 <span class="comment">%  FEDEASLab - Release 5.1, July 2020</span>
0051 <span class="comment">%  Matlab Finite Elements for Design, Evaluation and Analysis of Structures</span>
0052 <span class="comment">%  Professor Filip C. Filippou (filippou@berkeley.edu)</span>
0053 <span class="comment">%  Department of Civil and Environmental Engineering, UC Berkeley</span>
0054 <span class="comment">%  Copyright(c) 1998-2020. The Regents of the University of California. All Rights Reserved.</span>
0055 <span class="comment">%  =========================================================================================</span>
0056 
0057 <span class="comment">%% check material data, set default values, if any, and retrieve data</span>
0058 <span class="keyword">switch</span> action
0059 <span class="keyword">case</span> <span class="string">'chec'</span>
0060    <span class="keyword">if</span> ~isfield(MatData,<span class="string">'E'</span>),  disp(<span class="string">'Material'</span>);disp(MatNo); error(<span class="string">'Young modulus missing'</span>); <span class="keyword">end</span>
0061    <span class="keyword">if</span> ~isfield(MatData,<span class="string">'fy'</span>), disp(<span class="string">'Material'</span>);disp(MatNo); error(<span class="string">'yield strength missing'</span>); <span class="keyword">end</span>
0062    <span class="keyword">if</span> ~isfield(MatData,<span class="string">'b'</span>),   MatData.b   = 0;     <span class="keyword">end</span>
0063    <span class="keyword">if</span> ~isfield(MatData,<span class="string">'R0'</span>),  MatData.R0  = 20.;   <span class="keyword">end</span>
0064    <span class="keyword">if</span> ~isfield(MatData,<span class="string">'cR1'</span>), MatData.cR1 = 0.925; <span class="keyword">end</span>
0065    <span class="keyword">if</span> ~isfield(MatData,<span class="string">'cR2'</span>), MatData.cR2 = 0.15;  <span class="keyword">end</span>
0066    <span class="keyword">if</span> ~isfield(MatData,<span class="string">'a1'</span>),  MatData.a1  = 0.;    <span class="keyword">end</span>
0067    <span class="keyword">if</span> ~isfield(MatData,<span class="string">'a2'</span>),  MatData.a2  = 0.;    <span class="keyword">end</span>
0068    <span class="keyword">if</span> ~isfield(MatData,<span class="string">'a3'</span>),  MatData.a3  = 0.;    <span class="keyword">end</span>
0069    <span class="keyword">if</span> ~isfield(MatData,<span class="string">'a4'</span>),  MatData.a4  = 0.;    <span class="keyword">end</span>
0070    MatResp = MatData;
0071 <span class="keyword">otherwise</span>   
0072    <span class="comment">% extract material properties</span>
0073    E   = MatData.E;
0074    fy  = MatData.fy;
0075    b   = MatData.b;
0076    R0  = MatData.R0;
0077    cR1 = MatData.cR1;
0078    cR2 = MatData.cR2;
0079    a1  = MatData.a1;
0080    a2  = MatData.a2;   
0081    a3  = MatData.a3;
0082    a4  = MatData.a4;   
0083    <span class="comment">% compute some material parameters</span>
0084    Eh = b*E;         <span class="comment">% hardening modulus</span>
0085    ey = fy/E;        <span class="comment">% yield strain</span>
0086 <span class="keyword">end</span>
0087 <span class="comment">%% material actions</span>
0088 <span class="keyword">switch</span> action
0089 <span class="comment">%% initialization and specification of history variables</span>
0090    <span class="keyword">case</span> <span class="string">'init'</span>
0091       MatState.sig = 0;
0092       MatState.km  = E;
0093       MatState.Pres.sig   =  0;
0094       MatState.Pres.Et    =  E;
0095       MatState.Pres.epmin = -ey;   <span class="comment">% epmin : max strain in compression</span>
0096       MatState.Pres.epmax =  ey;   <span class="comment">% epmax : max strain in tension</span>
0097       MatState.Pres.epex  =  0;    <span class="comment">% epex  : plastic excursion</span>
0098       MatState.Pres.ep0   =  0;    <span class="comment">% ep0   : strain at asymptotes intersection</span>
0099       MatState.Pres.s0    =  0;    <span class="comment">% s0    : stress at asymptotes intersection</span>
0100       MatState.Pres.epr   =  0;    <span class="comment">% epr   : strain at last inversion point</span>
0101       MatState.Pres.sr    =  0;    <span class="comment">% sr    : stress at last inversion point</span>
0102       MatState.Pres.kon   =  0;    <span class="comment">% kon   : index for loading/unloading</span>
0103       MatResp = MatState;
0104 <span class="comment">%% state determination</span>
0105    <span class="keyword">case</span> {<span class="string">'stif'</span>,<span class="string">'forc'</span>}
0106       <span class="comment">% Retrieve history variables from Past</span>
0107       sig   = MatState.Past.sig;
0108       Et    = MatState.Past.Et;
0109       epmin = MatState.Past.epmin;
0110       epmax = MatState.Past.epmax;
0111       epex  = MatState.Past.epex;
0112       ep0   = MatState.Past.ep0;
0113       s0    = MatState.Past.s0;
0114       epr   = MatState.Past.epr;
0115       sr    = MatState.Past.sr;
0116       kon   = MatState.Past.kon;
0117       sigp  = sig;
0118 
0119       epm   = max(abs(epmin),abs(epmax));
0120       epss  = MatState.eps;  <span class="comment">% total strain</span>
0121       depss = MatState.Deps; <span class="comment">% total strain increment from last convergence</span>
0122 
0123       <span class="keyword">if</span> kon==0 <span class="comment">% the material is virgin</span>
0124          <span class="keyword">if</span> depss == 0
0125             sig  = 0;
0126             Et   = E;
0127          <span class="keyword">end</span>
0128          <span class="keyword">if</span> (depss&gt;0)
0129             kon  = 1;
0130             ep0  = epm;
0131             s0   = fy;
0132             epex = epm;
0133             [sig,Et] = <a href="#_sub1" class="code" title="subfunction [sig,Et] = Bauschinger (epex,ep0,epy,R0,cR1,cR2,epss,epr,b,s0,sr,E)">Bauschinger</a>(epex,ep0,ey,R0,cR1,cR2,epss,epr,b,s0,sr,E);
0134          <span class="keyword">end</span>
0135          <span class="keyword">if</span> (depss&lt;0)
0136             kon  = 2;
0137             ep0  = -epm;
0138             s0   = -fy;
0139             epex = -epm;
0140             [sig,Et] = <a href="#_sub1" class="code" title="subfunction [sig,Et] = Bauschinger (epex,ep0,epy,R0,cR1,cR2,epss,epr,b,s0,sr,E)">Bauschinger</a>(epex,ep0,ey,R0,cR1,cR2,epss,epr,b,s0,sr,E);
0141          <span class="keyword">end</span>
0142       <span class="keyword">else</span> <span class="comment">% material is damaged</span>
0143          <span class="keyword">if</span> (kon==1 &amp;&amp; depss&gt;0) ||(kon==2 &amp;&amp; depss&lt;0) <span class="comment">% keep loading in the previous step direction</span>
0144             [sig,Et] = <a href="#_sub1" class="code" title="subfunction [sig,Et] = Bauschinger (epex,ep0,epy,R0,cR1,cR2,epss,epr,b,s0,sr,E)">Bauschinger</a>(epex,ep0,ey,R0,cR1,cR2,epss,epr,b,s0,sr,E);
0145          <span class="keyword">elseif</span> (kon==1 &amp;&amp; depss&lt;0) <span class="comment">% inversion from tensile to compressive</span>
0146             kon  = 2;
0147             epr  = epss-depss;
0148             sr   = sigp;
0149             <span class="keyword">if</span> (epr&gt;epmax),  epmax = epr; <span class="keyword">end</span>
0150             epm  = max(abs(epmin),abs(epmax));
0151             sst  = fy*a1*(epm/ey-a2);
0152             sst  = max(sst,0);
0153             ep0  = (sr+fy+sst-(E*epr+Eh*ey))/(Eh-E);
0154             s0   = Eh*(ep0+ey)-fy-sst;
0155             epex = epmin;
0156             [sig,Et] = <a href="#_sub1" class="code" title="subfunction [sig,Et] = Bauschinger (epex,ep0,epy,R0,cR1,cR2,epss,epr,b,s0,sr,E)">Bauschinger</a>(epex,ep0,ey,R0,cR1,cR2,epss,epr,b,s0,sr,E);
0157          <span class="keyword">elseif</span> (kon==2 &amp;&amp; depss&gt;0) <span class="comment">% inversion from compressive to tensile</span>
0158             kon  = 1;
0159             epr  = epss-depss;
0160             sr   = sigp;
0161             <span class="keyword">if</span> (epr&lt;epmin),  epmin = epr; <span class="keyword">end</span>
0162             epm  = max(abs(epmin),abs(epmax));
0163             sst  = fy*a3*(epm/ey-a4);
0164             sst  = max(sst,0);
0165             ep0  = (sr+Eh*ey-(E*epr+fy+sst))/(Eh-E);
0166             s0   = fy+sst+Eh*(ep0-ey);
0167             epex = epmax;
0168             [sig,Et] = <a href="#_sub1" class="code" title="subfunction [sig,Et] = Bauschinger (epex,ep0,epy,R0,cR1,cR2,epss,epr,b,s0,sr,E)">Bauschinger</a>(epex,ep0,ey,R0,cR1,cR2,epss,epr,b,s0,sr,E);
0169          <span class="keyword">end</span>
0170       <span class="keyword">end</span>
0171       <span class="comment">% return current state</span>
0172       MatState.sig = sig;
0173       <span class="keyword">if</span> strcmp(action,<span class="string">'stif'</span>), MatState.km = Et; <span class="keyword">end</span>
0174       <span class="comment">% save material history variables</span>
0175       MatState.Pres.sig   = sig;
0176       MatState.Pres.Et    = Et;
0177       MatState.Pres.epmin = epmin;
0178       MatState.Pres.epmax = epmax;
0179       MatState.Pres.epex  = epex;
0180       MatState.Pres.ep0   = ep0;
0181       MatState.Pres.s0    = s0;
0182       MatState.Pres.epr   = epr;
0183       MatState.Pres.sr    = sr;
0184       MatState.Pres.kon   = kon;
0185       MatResp = MatState;
0186 <span class="comment">%% post-processing</span>
0187    <span class="keyword">case</span> <span class="string">'post'</span>
0188       sig  = MatState.Pres.sig;
0189       MatPost.eps = MatState.eps;
0190       MatPost.sig = sig;
0191       MatResp = MatPost;
0192 <span class="comment">%% add other actions</span>
0193    <span class="keyword">otherwise</span>
0194 <span class="keyword">end</span>
0195 
0196 <span class="comment">%% ------- function Bauschinger ------------------------------------------------------------</span>
0197 <a name="_sub1" href="#_subfunctions" class="code">function [sig,Et] = Bauschinger (epex,ep0,epy,R0,cR1,cR2,epss,epr,b,s0,sr,E)</a>
0198 <span class="comment">% calculate stress and moduls</span>
0199 
0200 xi    = abs((epex-ep0)/epy);
0201 R     = R0*(1-(cR1*xi)/(cR2+xi));
0202 eden  = ep0-epr;
0203 <span class="keyword">if</span> abs(eden)&gt;1e-16
0204   e_str = (epss-epr)/eden;
0205   dum1  = 1+abs(e_str)^R;
0206   dum2  = dum1^(1/R);
0207   s_str = b*e_str+(1-b)*e_str/dum2;
0208   sig   = s_str*(s0-sr)+sr; <span class="comment">%</span>
0209   
0210   dSdE  = b + (1-b) /(dum1*dum2);
0211   Et    = dSdE*(s0-sr)/(ep0-epr);
0212 <span class="keyword">else</span>
0213   sig = sr;
0214   Et  = E;
0215 <span class="keyword">end</span></pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->