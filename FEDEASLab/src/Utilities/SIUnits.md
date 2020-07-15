
<!-- <a name="_top"></a>
<div><a href="../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="index.md">Utilities</a> &gt; SIUnits.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../index.md"><img alt="<" border="0" src="../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Utilities&nbsp;<img alt=">" border="0" src="../../../../../right.png"></a></td></tr></table>-->
# `SIUnits`
<!-- <h1>SIUnits
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

% Script file for common unit definition with SI units as default

<!-- <div class="box"><strong>% Script file for common unit definition with SI units as default</strong></div> -->

## <a name="_synopsis"></a>Syntax

`This is a script file.` 
## <a name="_description"></a>Description

<pre class="comment">% Script file for common unit definition with SI units as default</pre>
<!-- <div class="fragment"><pre class="comment">% Script file for common unit definition with SI units as default</pre></div> -->

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
<div class="fragment"><pre>0001 <span class="comment">%% Script file for common unit definition with SI units as default</span>
0002 
0003 <span class="comment">%  =========================================================================================</span>
0004 <span class="comment">%  FEDEASLab - Release 5.1, July 2020</span>
0005 <span class="comment">%  Matlab Finite Elements for Design, Evaluation and Analysis of Structures</span>
0006 <span class="comment">%  Professor Filip C. Filippou (filippou@berkeley.edu)</span>
0007 <span class="comment">%  Department of Civil and Environmental Engineering, UC Berkeley</span>
0008 <span class="comment">%  Copyright(c) 1998-2020. The Regents of the University of California. All Rights Reserved.</span>
0009 <span class="comment">%  =========================================================================================</span>
0010 
0011 <span class="comment">%% Basic SI units</span>
0012 
0013 mm  = 1;
0014 N   = 1;
0015 sec = 1.;
0016 
0017 <span class="comment">%% Derived SI or metric units</span>
0018 
0019 cm = 10*mm;
0020 m  = 1000*mm;
0021 
0022 mm2 = mm*mm;
0023 mm4 = mm2*mm2;
0024 cm2 = cm*cm;
0025 cm4 = cm2*cm2;
0026 m2  = m*m;
0027 m4  = m2*m2;
0028 
0029 kN  = 1000*N;
0030 MN  = 1000*kN;
0031 MPa = MN/m2;
0032 kPa = MPa/1000;
0033 GPa = 1000*MPa;
0034 Nm  = N*m;
0035 kNm = kN*m;
0036 
0037 <span class="comment">% acceleration of gravity</span>
0038 g  = 9.80665*m/sec^2;
0039 
0040 <span class="comment">%% Derived U.S. units</span>
0041 
0042 in  = 25.4*mm;
0043 kip = 4.4482216*kN;
0044 
0045 ft  = 12*in;
0046 in2 = in*in;
0047 in3 = in2*in;
0048 in4 = in2*in2;
0049 ft2 = ft*ft;
0050 ft4 = ft2*ft2;
0051 
0052 lb      = kip/1000;
0053 psi     = lb/in2;
0054 kipin   = kip*in;
0055 kip_ft  = kip/ft;
0056 kipft   = kip*ft;
0057 ksi     = kip/in2;
0058 kip_ft2 = kip/ft2;</pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->