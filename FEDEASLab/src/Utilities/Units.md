
<!-- <a name="_top"></a>
<div><a href="../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="index.md">Utilities</a> &gt; Units.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../index.md"><img alt="<" border="0" src="../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Utilities&nbsp;<img alt=">" border="0" src="../../../../../right.png"></a></td></tr></table>-->
# `Units`
<!-- <h1>Units
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

% Script file for common unit definition with Imperial units as default

<!-- <div class="box"><strong>% Script file for common unit definition with Imperial units as default</strong></div> -->

## <a name="_synopsis"></a>Syntax

`This is a script file.` 
## <a name="_description"></a>Description

<pre class="comment">% Script file for common unit definition with Imperial units as default</pre>
<!-- <div class="fragment"><pre class="comment">% Script file for common unit definition with Imperial units as default</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../../../../matlabicon.gif)">
<li><a href="../../../../../../../FEDEASLab/src/Other/Create_PanelZone.md" class="code" title="">Create_PanelZone</a>	% Clear memory and close any open windows</li></ul>
<!-- crossreference -->



<h2><a name="_source"></a>SOURCE CODE</h2>
<div class="fragment"><pre>0001 <span class="comment">%% Script file for common unit definition with Imperial units as default</span>
0002 
0003 <span class="comment">%  =========================================================================================</span>
0004 <span class="comment">%  FEDEASLab - Release 5.1, July 2020</span>
0005 <span class="comment">%  Matlab Finite Elements for Design, Evaluation and Analysis of Structures</span>
0006 <span class="comment">%  Professor Filip C. Filippou (filippou@berkeley.edu)</span>
0007 <span class="comment">%  Department of Civil and Environmental Engineering, UC Berkeley</span>
0008 <span class="comment">%  Copyright(c) 1998-2020. The Regents of the University of California. All Rights Reserved.</span>
0009 <span class="comment">%  =========================================================================================</span>
0010 
0011 <span class="comment">%% Basic U.S. units</span>
0012 
0013 in  = 1.;
0014 kip = 1.;
0015 sec = 1.;
0016 
0017 <span class="comment">%% Derived U.S. units</span>
0018 
0019 <span class="comment">% length, area, volume units</span>
0020 ft  = 12*in;
0021 in2 = in*in;
0022 in3 = in2*in;
0023 in4 = in2*in2;
0024 ft2 = ft*ft;
0025 ft4 = ft2*ft2;
0026 
0027 <span class="comment">% force related units</span>
0028 lb      = kip/1000;
0029 psi     = lb/in2;
0030 kipin   = kip*in;
0031 kipft   = kip*ft;
0032 kip_in  = kip/in;
0033 kip_ft  = kip/ft;
0034 ksi     = kip/in2;
0035 kip_ft2 = kip/ft2;
0036 
0037 <span class="comment">% acceleration of gravity</span>
0038 g  = 386.0886*in/sec^2;
0039 
0040 <span class="comment">%% Derived SI or metric units</span>
0041 
0042 <span class="comment">% length units</span>
0043 mm = in/25.4;
0044 cm = in/2.54;
0045 m  = 1000*mm;
0046 
0047 <span class="comment">% area and volume units</span>
0048 mm2 = mm*mm;
0049 mm3 = mm2*mm;
0050 mm4 = mm2*mm2;
0051 cm2 = cm*cm;
0052 cm4 = cm2*cm2;
0053 m2  = m*m;
0054 m4  = m2*m2;
0055 
0056 <span class="comment">% force related units</span>
0057 kN  = kip/4.4482216;
0058 N   = kN/1000;
0059 MN  = 1000*kN;
0060 MPa = MN/m2;
0061 kPa = MPa/1000;
0062 GPa = 1000*MPa;
0063 Nm  = N*m;
0064 kNm = kN*m;</pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->