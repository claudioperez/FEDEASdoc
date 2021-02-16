
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href="_index.md">Dynamic</a> &gt; EigenMode.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Analysis_Functions\Dynamic&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `EigenMode`
<!-- <h1>EigenMode
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

EIGENMODE determines eigenfrequencies and eigenmodes of structural model

<!-- <div class="box"><strong>EIGENMODE determines eigenfrequencies and eigenmodes of structural model</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [omega,Ueig] = EigenMode (Kf,M,nmod)` 
## <a name="_description"></a>Description

<pre class="comment">EIGENMODE determines eigenfrequencies and eigenmodes of structural model
  [OMEGA UEIG] = EIGENMODE(KF,M,NMOD)
  function determines the lowest NMOD (default=all) eigenfrequencies in row vector OMEGA
  and corresponding eigenmodes in array UEIG for a structure with free dof stiffness matrix KF
  and free dof lumped mass vector or consistent mass matrix M;
  the eigenmodes in array UEIG are arranged columnwise (column no=mode no)</pre>
<!-- <div class="fragment"><pre class="comment">EIGENMODE determines eigenfrequencies and eigenmodes of structural model
  [OMEGA UEIG] = EIGENMODE(KF,M,NMOD)
  function determines the lowest NMOD (default=all) eigenfrequencies in row vector OMEGA
  and corresponding eigenmodes in array UEIG for a structure with free dof stiffness matrix KF
  and free dof lumped mass vector or consistent mass matrix M;
  the eigenmodes in array UEIG are arranged columnwise (column no=mode no)</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="../../../latest/General_Functions/Condense_MV" class="code" title="function [Kfc,Pfc] = Condense_MV (Kf,idr,Pf)">Condense_MV</a>	CONDENSE_MV condense matrix Kf and vector Pf to a reduced set idr of degrees of freedom</li></ul>
This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="ModalAnalysis.md" class="code" title="function [omega,Ueig,Y_t,Ydot_t,Yddot_t] = ModalAnalysis (option,Kf,M,Loading,Deltat,zeta,nmod)">ModalAnalysis</a>	MODALANALYSIS determines modal response history for given transient loading</li><li><a href="../../../latest/General_Functions/Create_Damping.md" class="code" title="function C = Create_Damping (type,Kf,Ml,zeta,mode)">Create_Damping</a>	CREATE_DAMPING setup damping matrix of structural model</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->