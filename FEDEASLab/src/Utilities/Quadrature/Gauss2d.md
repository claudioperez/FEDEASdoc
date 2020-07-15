
<!-- <a name="_top"></a>
<div><a href="../../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="../index.md">Utilities</a> &gt; <a href="index.md">Quadrature</a> &gt; Gauss2d.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../../index.md"><img alt="<" border="0" src="../../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Utilities\Quadrature&nbsp;<img alt=">" border="0" src="../../../../../../right.png"></a></td></tr></table>-->
# `Gauss2d`
<!-- <h1>Gauss2d
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

GAUSS2D Gauss integration rule in two dimensions

<!-- <div class="box"><strong>GAUSS2D Gauss integration rule in two dimensions</strong></div> -->

## <a name="_synopsis"></a>Syntax

`function [xIP,wIP] = Gauss2d (nIP)` 
## <a name="_description"></a>Description

<pre class="comment"> GAUSS2D Gauss integration rule in two dimensions
 [XIP,WIP] = GAUSS2D (NIP) locations and weights of 2d Gauss-Legendre integration scheme   
  the function determines the locations in the intervals -1&lt;xi&lt;1, -1&lt;eta&lt;1, and the weights
  of the Gauss-Legendre integration scheme for NIP integration points;
  the locations are reported in vector XIP and the weights in vector WIP</pre>
<!-- <div class="fragment"><pre class="comment"> GAUSS2D Gauss integration rule in two dimensions
 [XIP,WIP] = GAUSS2D (NIP) locations and weights of 2d Gauss-Legendre integration scheme   
  the function determines the locations in the intervals -1&lt;xi&lt;1, -1&lt;eta&lt;1, and the weights
  of the Gauss-Legendre integration scheme for NIP integration points;
  the locations are reported in vector XIP and the weights in vector WIP</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../../../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../../../../../matlabicon.gif)">
<li><a href="../../../../../../../../FEDEASLab/src/Other/InelPanelZone.md" class="code" title="function ElemResp = InelPanelZone (action,el_no,xyz,ElemData,ElemState)">InelPanelZone</a>	INELPANELZONE 4-node panel zone element with inelastic material</li></ul>
<!-- crossreference -->



<h2><a name="_source"></a>SOURCE CODE</h2>
<div class="fragment"><pre>0001 <a name="_sub0" href="#_subfunctions" class="code">function [xIP,wIP] = Gauss2d (nIP)</a>
0002 <span class="comment">% GAUSS2D Gauss integration rule in two dimensions</span>
0003 <span class="comment">% [XIP,WIP] = GAUSS2D (NIP) locations and weights of 2d Gauss-Legendre integration scheme</span>
0004 <span class="comment">%  the function determines the locations in the intervals -1&lt;xi&lt;1, -1&lt;eta&lt;1, and the weights</span>
0005 <span class="comment">%  of the Gauss-Legendre integration scheme for NIP integration points;</span>
0006 <span class="comment">%  the locations are reported in vector XIP and the weights in vector WIP</span>
0007 
0008 <span class="comment">%  =========================================================================================</span>
0009 <span class="comment">%  FEDEASLab - Release 5.1, July 2020</span>
0010 <span class="comment">%  Matlab Finite Elements for Design, Evaluation and Analysis of Structures</span>
0011 <span class="comment">%  Professor Filip C. Filippou (filippou@berkeley.edu)</span>
0012 <span class="comment">%  Department of Civil and Environmental Engineering, UC Berkeley</span>
0013 <span class="comment">%  Copyright(c) 1998-2020. The Regents of the University of California. All Rights Reserved.</span>
0014 <span class="comment">%  =========================================================================================</span>
0015 
0016 [xIP,wIP] = Gauss(nIP);
0017 [xIPy,xIPx] = meshgrid(xIP);
0018 xIP = [xIPx(:) xIPy(:)];
0019 wIP = wIP*wIP';
0020 wIP = wIP(:);</pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->