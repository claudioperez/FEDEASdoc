---
title: "ModalAnalysis"
id: "ModalAnalysis"
description: "MODALANALYSIS determines modal response history for given transient loading"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href=".autoindex.md">Dynamic</a> &gt; 
<!-- ModalAnalysis.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../.autoindex.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Analysis_Functions\Dynamic&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `ModalAnalysis`



## <a name="_name"></a>Purpose


MODALANALYSIS determines modal response history for given transient loading

<!-- <div class="box"><strong>MODALANALYSIS determines modal response history for given transient loading</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [omega,Ueig,Y_t,Ydot_t,Yddot_t] = ModalAnalysis (option,Kf,M,Loading,Deltat,zeta,nmod)` 

## Description


<pre class="comment">MODALANALYSIS determines modal response history for given transient loading
  [OMEGA,UEIG,Y_T,YDOT_T,YDDOT_T] = MODALANALYSIS (OPTION,KF,M,LOADING,DELTAT,ZETA,NMOD)
  the function determines the response history of a multi-dof structural model
  with stiffness matrix at free dofs KF and consistent mass matrix or lumped mass vector M
  under given transient loading in data structure LOADING
  for the lowest NMOD (default=all) eigenmodes or NMOD Ritz vectors
  with damping ratios in row vector ZETA (default=0);
  the time step of integration is DELTAT;
        OPTION = 'eig'  uses nmod eigenvectors,
  while OPTION = 'Ritz' uses nmod Ritz vectors in the modal analysis; 
  the function returns NMOD eigenfrequencies of the structural model in row vector OMEGA,
  the eigenmode or Ritz vector shapes in array UEIG arranged columnwise (column no=mode no),
  and the response history of each eigenmode or Ritz vector
  in array Y_T arranged columnwise (column no=mode no),
  the velocity history of each eigenmode or Ritz vector in array YDOT_t, and
  the acceleration history of each eigenmode or Ritz vector in array YDDOT_t
  the data structure LOADING has the following fields
  LOADING.Uddref = vector of reference acceleration values at model dofs
          Pref   = vector of reference load         values at model dofs
          U0     = vector of initial displacement   values at model dofs
          Udot0  = vector of initial velocity       values at model dofs
          FrcHst = force time history in field Value
          AccHst = acceleration time history in field Value</pre>
<!-- <div class="fragment"><pre class="comment">MODALANALYSIS determines modal response history for given transient loading
  [OMEGA,UEIG,Y_T,YDOT_T,YDDOT_T] = MODALANALYSIS (OPTION,KF,M,LOADING,DELTAT,ZETA,NMOD)
  the function determines the response history of a multi-dof structural model
  with stiffness matrix at free dofs KF and consistent mass matrix or lumped mass vector M
  under given transient loading in data structure LOADING
  for the lowest NMOD (default=all) eigenmodes or NMOD Ritz vectors
  with damping ratios in row vector ZETA (default=0);
  the time step of integration is DELTAT;
        OPTION = 'eig'  uses nmod eigenvectors,
  while OPTION = 'Ritz' uses nmod Ritz vectors in the modal analysis; 
  the function returns NMOD eigenfrequencies of the structural model in row vector OMEGA,
  the eigenmode or Ritz vector shapes in array UEIG arranged columnwise (column no=mode no),
  and the response history of each eigenmode or Ritz vector
  in array Y_T arranged columnwise (column no=mode no),
  the velocity history of each eigenmode or Ritz vector in array YDOT_t, and
  the acceleration history of each eigenmode or Ritz vector in array YDDOT_t
  the data structure LOADING has the following fields
  LOADING.Uddref = vector of reference acceleration values at model dofs
          Pref   = vector of reference load         values at model dofs
          U0     = vector of initial displacement   values at model dofs
          Udot0  = vector of initial velocity       values at model dofs
          FrcHst = force time history in field Value
          AccHst = acceleration time history in field Value</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="/Functions/EigenMode" class="code" title="function [omega,Ueig] = EigenMode (Kf,M,nmod)">EigenMode</a>	EIGENMODE determines eigenfrequencies and eigenmodes of structural model</li><li><a href="/Functions/LSDOF_LinearWilson" class="code" title="function [u,udot,uddot] = LSDOF_LinearWilson (Deltat,omega,p,zeta,u0,udot0)">LSDOF_LinearWilson</a>	LSDOF_LINEARWILSON transient response of linear SDOF system by exact integration of piecewise linear excitation</li><li><a href="/Functions/ModeDecomposition" class="code" title="function [Mmod,Ymod,Vmod] = ModeDecomposition (M,Ueig,V)">ModeDecomposition</a>	MODEDECOMPOSITION determines eigenmode participation factors of given vector V</li></ul>

This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->