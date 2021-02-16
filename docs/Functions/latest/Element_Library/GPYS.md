
<!-- <a name="_top"></a>
<div><a href="../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="_index.md">Element_Library</a> &gt; GPYS.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../_index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Element_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `GPYS`
<!-- <h1>GPYS
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

GPYS function value, gradient and Hessian of polynomial yield surface

<!-- <div class="box"><strong>GPYS function value, gradient and Hessian of polynomial yield surface</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [f,g,h] = GPYS (GPYSC,xyz,ScVec)` 
## <a name="_description"></a>Description

<pre class="comment">GPYS function value, gradient and Hessian of polynomial yield surface    
  [F,G,H] = GPYS (GPYSC,XYZ,SCVEC)
  the function determines the value F(X,Y,Z), the gradient G(X,Y,Z), and
  the Hessian matrix (2nd derivative) H(X,Y,Z) of F at a point XYZ
  for a general polynomial yield surface with coefficients GPYSC
  SCVEC is a scale vector for the variables X, Y, and Z
   G = the gradient (normal)   of the yield surface = [dF/dX; dF/dY; dF/dZ]
   H = the Hessian (2nd deriv) of the yield surface = dG/dXYZ
     = [d2(F)/d(X)^2    d2(F)/d(X)d(Y) d2(F)/d(X)d(Z);
        d2(F)/d(Y)d(X)  d2(F)/d(Y)^2   d2(F)/d(Y)d(Z);
        d2(F)/d(Z)d(X)  d2(F)/d(Z)d(Y) d2(F)/d(Z)^2]

  The coefficients of the polynomial yield surface are specified as follows
  general 3d case
           GPYSC = [d1 a1 b1 c1; d2 a2 b2 c2; d3 a3 b3 c3; ...]
          for  F = Sum_i (di*(X^ai)*(Y^bi)*(Z^ci))
  general 2d case
           GPYSC = [c1 a1 b1; c2 a2 b2; c3 a3 b3; ...]
       for     F = Sum_i (ci*(X^ai)*(Y^bi))</pre>
<!-- <div class="fragment"><pre class="comment">GPYS function value, gradient and Hessian of polynomial yield surface    
  [F,G,H] = GPYS (GPYSC,XYZ,SCVEC)
  the function determines the value F(X,Y,Z), the gradient G(X,Y,Z), and
  the Hessian matrix (2nd derivative) H(X,Y,Z) of F at a point XYZ
  for a general polynomial yield surface with coefficients GPYSC
  SCVEC is a scale vector for the variables X, Y, and Z
   G = the gradient (normal)   of the yield surface = [dF/dX; dF/dY; dF/dZ]
   H = the Hessian (2nd deriv) of the yield surface = dG/dXYZ
     = [d2(F)/d(X)^2    d2(F)/d(X)d(Y) d2(F)/d(X)d(Z);
        d2(F)/d(Y)d(X)  d2(F)/d(Y)^2   d2(F)/d(Y)d(Z);
        d2(F)/d(Z)d(X)  d2(F)/d(Z)d(Y) d2(F)/d(Z)^2]

  The coefficients of the polynomial yield surface are specified as follows
  general 3d case
           GPYSC = [d1 a1 b1 c1; d2 a2 b2 c2; d3 a3 b3 c3; ...]
          for  F = Sum_i (di*(X^ai)*(Y^bi)*(Z^ci))
  general 2d case
           GPYSC = [c1 a1 b1; c2 a2 b2; c3 a3 b3; ...]
       for     F = Sum_i (ci*(X^ai)*(Y^bi))</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="BInel2dFrm_wEPLHNMYS.md" class="code" title="function BElemResp = BInel2dFrm_wEPLHNMYS (action,L,BElemData,BElemState)">BInel2dFrm_wEPLHNMYS</a>	BINELP2dFRM_WEPLHNMYS 2d elasto-plastic, linear hardening basic frame element</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->