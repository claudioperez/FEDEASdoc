
<!-- <a name="_top"></a>
<div><a href="../../index.md">Home</a> &gt;  <a href="#">src</a> &gt; <a href="index.md">Other</a> &gt; shape2d.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for src\Other&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# shape2d
<!-- <h1>shape2d
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

SHAPE2D shape functions for 4-9 node quadrilateral element

<!-- <div class="box"><strong>SHAPE2D shape functions for 4-9 node quadrilateral element</strong></div> -->

## <a name="_synopsis"></a>Syntax

`function [N,dNdx,J] = shape2d (nat,xyz,nodix)` 
## <a name="_description"></a>Description

<pre class="comment">SHAPE2D shape functions for 4-9 node quadrilateral element
 [N, dNdx, J] = SHAPE2D (NAT,XYZ,NODIX) shape functions for 4-9 node quadrilateral element
%
 Input Parameters
 ----------------
 nat   = [ xi eta ] natural coordinates of point of interest
 xyz   = nodal coordinates for element (row i for node i)
 nodix = node index, e.g. [1:4 7 8] if nodes 1 through 4 (always), if 7 and 8 are present 
 ----------------
 Return Variables
 ----------------
 N     = shape function values for point of interest
 dNdx  = dNdx(i,j) = derivative of shape function j with respect to geometric coordinate x_i
 J     = Jacobian of transformation from geometric to natural coordinates

  Reference: T.J.R. Hughes, The Finite Element Method, pp. 135</pre>
<!-- <div class="fragment"><pre class="comment">SHAPE2D shape functions for 4-9 node quadrilateral element
 [N, dNdx, J] = SHAPE2D (NAT,XYZ,NODIX) shape functions for 4-9 node quadrilateral element
%
 Input Parameters
 ----------------
 nat   = [ xi eta ] natural coordinates of point of interest
 xyz   = nodal coordinates for element (row i for node i)
 nodix = node index, e.g. [1:4 7 8] if nodes 1 through 4 (always), if 7 and 8 are present 
 ----------------
 Return Variables
 ----------------
 N     = shape function values for point of interest
 dNdx  = dNdx(i,j) = derivative of shape function j with respect to geometric coordinate x_i
 J     = Jacobian of transformation from geometric to natural coordinates

  Reference: T.J.R. Hughes, The Finite Element Method, pp. 135</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="InelPanelZone.md" class="code" title="function ElemResp = InelPanelZone (action,el_no,xyz,ElemData,ElemState)">InelPanelZone</a>	INELPANELZONE 4-node panel zone element with inelastic material</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 09-Jul-2020 17:36:54 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->