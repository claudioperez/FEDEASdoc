
<!-- <a name="_top"></a>
<div><a href="../../../index.md">Home</a> &gt;  <a href="#">src</a> &gt; <a href="../index.md">Utilities</a> &gt; <a href="index.md">Quadrature</a> &gt; Gauss2d.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for src\Utilities\Quadrature&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# Gauss2d
<!-- <h1>Gauss2d
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

GAUSS2D Gauss integration rule in two dimensions

<!-- <div class="box"><strong>GAUSS2D Gauss integration rule in two dimensions</strong></div> -->

## <a name="_synopsis"></a>Synopsis

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
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="../../../src/Other/InelPanelZone.md" class="code" title="function ElemResp = InelPanelZone (action,el_no,xyz,ElemData,ElemState)">InelPanelZone</a>	INELPANELZONE 4-node panel zone element with inelastic material</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Wed 08-Jul-2020 17:32:04 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->