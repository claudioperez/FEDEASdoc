
<!-- <a name="_top"></a>
<div><a href="../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="_index.md">General_Functions</a> &gt; Condense_MV.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../_index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\General_Functions&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Condense_MV`
<!-- <h1>Condense_MV
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

CONDENSE_MV condense matrix Kf and vector Pf to a reduced set idr of degrees of freedom

<!-- <div class="box"><strong>CONDENSE_MV condense matrix Kf and vector Pf to a reduced set idr of degrees of freedom</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [Kfc,Pfc] = Condense_MV (Kf,idr,Pf)` 
## <a name="_description"></a>Description

<pre class="comment">CONDENSE_MV condense matrix Kf and vector Pf to a reduced set idr of degrees of freedom
  [KFC,PFC] = CONDENSE_MV (KF,IDR,PF)
  function condenses free dof stiffness matrix KF and applied force vector PF
  to a reduced set of dofs as specified in list or row vector IDR;
  the condensed stiffness matrix is KFC and the initial force vector is PFC</pre>
<!-- <div class="fragment"><pre class="comment">CONDENSE_MV condense matrix Kf and vector Pf to a reduced set idr of degrees of freedom
  [KFC,PFC] = CONDENSE_MV (KF,IDR,PF)
  function condenses free dof stiffness matrix KF and applied force vector PF
  to a reduced set of dofs as specified in list or row vector IDR;
  the condensed stiffness matrix is KFC and the initial force vector is PFC</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="../../latest/Analysis_Functions/Dynamic/EigenMode.md" class="code" title="function [omega,Ueig] = EigenMode (Kf,M,nmod)">EigenMode</a>	EIGENMODE determines eigenfrequencies and eigenmodes of structural model</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->