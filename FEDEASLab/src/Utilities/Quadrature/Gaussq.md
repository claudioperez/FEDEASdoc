
<!-- <a name="_top"></a>
<div><a href="../../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="../index.md">Utilities</a> &gt; <a href="index.md">Quadrature</a> &gt; Gaussq.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../../index.md"><img alt="<" border="0" src="../../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Utilities\Quadrature&nbsp;<img alt=">" border="0" src="../../../../../../right.png"></a></td></tr></table>-->
# `Gaussq`
<!-- <h1>Gaussq
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

returns the locations y_i and weights w_i for Gauss quadrature of order n

<!-- <div class="box"><strong>returns the locations y_i and weights w_i for Gauss quadrature of order n</strong></div> -->

## <a name="_synopsis"></a>Syntax

`function [yi,wi] = Gaussq (n)` 
## <a name="_description"></a>Description

<pre class="comment"> returns the locations y_i and weights w_i for Gauss quadrature of order n
 Requirements: n \in N</pre>
<!-- <div class="fragment"><pre class="comment"> returns the locations y_i and weights w_i for Gauss quadrature of order n
 Requirements: n \in N</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../../../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../../../../../matlabicon.gif)">
</ul>
<!-- crossreference -->



<h2><a name="_source"></a>SOURCE CODE</h2>
<div class="fragment"><pre>0001 <a name="_sub0" href="#_subfunctions" class="code">function [yi,wi] = Gaussq (n)</a>
0002 <span class="comment">% returns the locations y_i and weights w_i for Gauss quadrature of order n</span>
0003 <span class="comment">% Requirements: n \in N</span>
0004 
0005 <span class="comment">% set up matrix A</span>
0006 i = 1:(n-1);
0007 v = i./sqrt(4.*i.^2-1);
0008 A = diag(v,1)+diag(v,-1);
0009 <span class="comment">% determine eigenvalues and eigenvectors of A</span>
0010 [Q,Y] = eig(A);
0011 <span class="comment">% the eigenvalues give the locations</span>
0012 yi = diag(Y)';
0013 <span class="comment">% the first term of the eigenvectors gives the weight</span>
0014 wi = 2.*Q(1,:).^2;</pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->