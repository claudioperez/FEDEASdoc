
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href="_index.md">Dynamic</a> &gt; InelSDOF_Newmark.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Analysis_Functions\Dynamic&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `InelSDOF_Newmark`
<!-- <h1>InelSDOF_Newmark
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

INELSDOF_NEWMARK inelastic response of SDOF system to acceleration history with Newmark's method

<!-- <div class="box"><strong>INELSDOF_NEWMARK inelastic response of SDOF system to acceleration history with Newmark's method</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [u,udot,uddot,pr] = InelSDOF_Newmark (Deltat,omega,p,InelSDFData,zeta,u0,udot0)` 
## <a name="_description"></a>Description

<pre class="comment">INELSDOF_NEWMARK inelastic response of SDOF system to acceleration history with Newmark's method
  [U,UDOT,UDDOT,PR] = INELSDOF_NEWMARK (DELT,OMEGA,P,INELSDFDATA,ZETA,U0,UDOT0)
  the function determines the transient response history of an inelastic SDOF system
  to the acceleration history (force/mass) in vector P
  with Newmark's constant average acceleration method (1959)
  with time step of integration DELTAT;
  row vector OMEGA contains the eigenfrequency(ies) of the SDOF system,
  and row vector ZETA the optional damping ratio(s) (default = 0);
  the optional initial conditions are specified in row vectors U0 for the displacement
  and UDOT0 for the velocity (default values for both = 0);
  INELSDFDATA carries the force-deformation properties for the inelastic SDOF system:
  MatName = function name for 1d relation (default = InelLPwLH1dMat)
  uy      = yield displacement         (default = 1)
  eta     = post-yield stiffness ratio (default = 0)
  the function returns the displacement history(ies) in array U,
  the velocity history(ies) in array UDOT,
  the acceleration history(ies) in array UDDOT,
  and the resisting force history(ies) in array PR (also in the form force/mass!);
  these arrays are arranged columnwise (column no=frequency no)</pre>
<!-- <div class="fragment"><pre class="comment">INELSDOF_NEWMARK inelastic response of SDOF system to acceleration history with Newmark's method
  [U,UDOT,UDDOT,PR] = INELSDOF_NEWMARK (DELT,OMEGA,P,INELSDFDATA,ZETA,U0,UDOT0)
  the function determines the transient response history of an inelastic SDOF system
  to the acceleration history (force/mass) in vector P
  with Newmark's constant average acceleration method (1959)
  with time step of integration DELTAT;
  row vector OMEGA contains the eigenfrequency(ies) of the SDOF system,
  and row vector ZETA the optional damping ratio(s) (default = 0);
  the optional initial conditions are specified in row vectors U0 for the displacement
  and UDOT0 for the velocity (default values for both = 0);
  INELSDFDATA carries the force-deformation properties for the inelastic SDOF system:
  MatName = function name for 1d relation (default = InelLPwLH1dMat)
  uy      = yield displacement         (default = 1)
  eta     = post-yield stiffness ratio (default = 0)
  the function returns the displacement history(ies) in array U,
  the velocity history(ies) in array UDOT,
  the acceleration history(ies) in array UDDOT,
  and the resisting force history(ies) in array PR (also in the form force/mass!);
  these arrays are arranged columnwise (column no=frequency no)</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->