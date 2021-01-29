
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href="_index.md">Dynamic</a> &gt; ModeDecomposition.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Analysis_Functions\Dynamic&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `ModeDecomposition`
<!-- <h1>ModeDecomposition
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

MODEDECOMPOSITION determines eigenmode participation factors of given vector V

<!-- <div class="box"><strong>MODEDECOMPOSITION determines eigenmode participation factors of given vector V</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [Mmod,Ymod,Vmod] = ModeDecomposition (M,Ueig,V)` 
## <a name="_description"></a>Description

<pre class="comment">MODEDECOMPOSITION determines eigenmode participation factors of given vector V
  [MMOD,YMOD,VMOD] = MODEDECOMPOSITION (M,UEIG,V)
  the function determines the mode participation factors of vector V
  for a structural model with free dof consistent mass matrix or lumped mass vector M
  for the modes in array UEIG arranged columnwise (column no=mode no);
  the function returns the modal mass terms in row vector MMOD,
  the mode participation factors in row vector YMOD and the
  inertial force decomposition vectors in array VMOD arranged columwise
  the size of the consistent mass matrix or the length of lumped mass vector M,
  the length of vector V and the number of rows of arrays UEIG
  and VMOD is equal to the number of free dofs of the structural model;
  the length of row vectors MMOD and YMOD is equal
  to the number of non-zero mass terms in the lumped mass vector M or
  the number of free dofs of the structural model for the case of consistent mass matrix M</pre>
<!-- <div class="fragment"><pre class="comment">MODEDECOMPOSITION determines eigenmode participation factors of given vector V
  [MMOD,YMOD,VMOD] = MODEDECOMPOSITION (M,UEIG,V)
  the function determines the mode participation factors of vector V
  for a structural model with free dof consistent mass matrix or lumped mass vector M
  for the modes in array UEIG arranged columnwise (column no=mode no);
  the function returns the modal mass terms in row vector MMOD,
  the mode participation factors in row vector YMOD and the
  inertial force decomposition vectors in array VMOD arranged columwise
  the size of the consistent mass matrix or the length of lumped mass vector M,
  the length of vector V and the number of rows of arrays UEIG
  and VMOD is equal to the number of free dofs of the structural model;
  the length of row vectors MMOD and YMOD is equal
  to the number of non-zero mass terms in the lumped mass vector M or
  the number of free dofs of the structural model for the case of consistent mass matrix M</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="ModalAnalysis.md" class="code" title="function [omega,Ueig,Y_t,Ydot_t,Yddot_t] = ModalAnalysis (option,Kf,M,Loading,Deltat,zeta,nmod)">ModalAnalysis</a>	MODALANALYSIS determines modal response history for given transient loading</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->