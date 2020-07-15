
<!-- <a name="_top"></a>
<div><a href="../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="index.md">Other</a> &gt; shape2d.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../index.md"><img alt="<" border="0" src="../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Other&nbsp;<img alt=">" border="0" src="../../../../../right.png"></a></td></tr></table>-->
# `shape2d`
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
<ul style="list-style-image:url(../../../../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../../../../matlabicon.gif)">
<li><a href="InelPanelZone.md" class="code" title="function ElemResp = InelPanelZone (action,el_no,xyz,ElemData,ElemState)">InelPanelZone</a>	INELPANELZONE 4-node panel zone element with inelastic material</li></ul>
<!-- crossreference -->



<h2><a name="_source"></a>SOURCE CODE</h2>
<div class="fragment"><pre>0001 <a name="_sub0" href="#_subfunctions" class="code">function [N,dNdx,J] = shape2d (nat,xyz,nodix)</a>
0002 <span class="comment">%SHAPE2D shape functions for 4-9 node quadrilateral element</span>
0003 <span class="comment">% [N, dNdx, J] = SHAPE2D (NAT,XYZ,NODIX) shape functions for 4-9 node quadrilateral element</span>
0004 <span class="comment">%%</span>
0005 <span class="comment">% Input Parameters</span>
0006 <span class="comment">% ----------------</span>
0007 <span class="comment">% nat   = [ xi eta ] natural coordinates of point of interest</span>
0008 <span class="comment">% xyz   = nodal coordinates for element (row i for node i)</span>
0009 <span class="comment">% nodix = node index, e.g. [1:4 7 8] if nodes 1 through 4 (always), if 7 and 8 are present</span>
0010 <span class="comment">% ----------------</span>
0011 <span class="comment">% Return Variables</span>
0012 <span class="comment">% ----------------</span>
0013 <span class="comment">% N     = shape function values for point of interest</span>
0014 <span class="comment">% dNdx  = dNdx(i,j) = derivative of shape function j with respect to geometric coordinate x_i</span>
0015 <span class="comment">% J     = Jacobian of transformation from geometric to natural coordinates</span>
0016 <span class="comment">%</span>
0017 <span class="comment">%  Reference: T.J.R. Hughes, The Finite Element Method, pp. 135</span>
0018 
0019 <span class="comment">%  =========================================================================================</span>
0020 <span class="comment">%  FEDEASLab - Release 5.1, July 2020</span>
0021 <span class="comment">%  Matlab Finite Elements for Design, Evaluation and Analysis of Structures</span>
0022 <span class="comment">%  Professor Filip C. Filippou (filippou@berkeley.edu)</span>
0023 <span class="comment">%  Department of Civil and Environmental Engineering, UC Berkeley</span>
0024 <span class="comment">%  Copyright(c) 1998-2020. The Regents of the University of California. All Rights Reserved.</span>
0025 <span class="comment">%  =========================================================================================</span>
0026 
0027 <span class="comment">%%</span>
0028 <span class="comment">% default for nodix is [1:4] for four nodes</span>
0029 <span class="keyword">if</span> nargin&lt;3, nodix = 1:4; <span class="keyword">end</span>
0030 
0031 <span class="comment">% nodal coordinates in natural coordinate system</span>
0032 natnode = [ -1 +1 +1 -1;
0033             -1 -1 +1 +1];
0034 <span class="comment">% terms in shape functions</span>
0035 xi  = 0.5 * ( 1 + natnode(1,:) .* nat(1) );
0036 eta = 0.5 * ( 1 + natnode(2,:) .* nat(2) );
0037 par = 1-nat.^2;
0038 
0039 <span class="comment">% shape functions</span>
0040 N = zeros(1,9);
0041 N(1:4) = xi .* eta;
0042 
0043 <span class="comment">% derivatives of shape functions with respect to natural coordinates</span>
0044 dN = zeros(2,9);
0045 dN(1,1:4) = 0.5 * natnode(1,:) .* eta;  <span class="comment">% dN/d-xi</span>
0046 dN(2,1:4) = 0.5 * natnode(2,:) .* xi;   <span class="comment">% dN/d-eta</span>
0047 
0048 <span class="comment">% if more than 4 nodes are present, augment shape functions and derivatives</span>
0049 <span class="comment">% set up all terms first and extract necessary terms later</span>
0050 nen = length(nodix);   <span class="comment">% number of nodes</span>
0051 <span class="keyword">if</span> (nen&gt;4)
0052    <span class="keyword">if</span> (nen==9)
0053        N(  9) =  prod(par);
0054       dN(1,9) = -2.*nat(1).*par(2);
0055       dN(2,9) = -2.*nat(2).*par(1);
0056    <span class="keyword">end</span>
0057    <span class="comment">% shape functions</span>
0058    funv = [eta(2) xi(2) eta(4) xi(4)].*[par par];
0059    iadd = nodix(nodix&lt;9);
0060    iadd = iadd(iadd&gt;4);
0061    N(iadd) = funv(iadd-4);
0062    N(5:8) = N(5:8) - N(9)./2;
0063    N(1:4) = N(1:4) - (N(5:8) + N(:,[8 5:7]))./2 - N(9)./4;
0064    <span class="comment">% derivatives of shape functions</span>
0065    funv = zeros(2,4);
0066    funv(1,[1 3]) =  -2.*nat(1).* eta([2 4]);
0067    funv(1,[2 4]) = 0.5.*par(2).* natnode(1,[2 4]);
0068    funv(2,[1 3]) = 0.5.*par(1).* natnode(2,[2 4]);
0069    funv(2,[2 4]) =  -2.*nat(2).* xi([2 4]);
0070    dN(:,iadd) = funv(:,iadd-4);
0071    dN(:,5:8)  = dN(:,5:8) - dN(:,9)*ones(1,4)./2;
0072    dN(:,1:4)  = dN(:,1:4) -(dN(:,5:8) + dN(:,[8 5:7]))./2 - dN(:,9)*ones(1,4)./4;
0073 <span class="keyword">end</span>
0074 <span class="comment">% extract necessary terms for given nodes</span>
0075  N =  N(  nodix);
0076 dN = dN(:,nodix);
0077 
0078 <span class="comment">% compute Jacobian of coordinate transformation</span>
0079 J    = dN * xyz(:,1:length(nat));
0080 <span class="comment">% compute derivatives of shape functions with respect to geometric coordinates</span>
0081 dNdx = J \ dN;</pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->