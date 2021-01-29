
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href="_index.md">Dynamic</a> &gt; LSDOF_LinearWilson.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Analysis_Functions\Dynamic&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `LSDOF_LinearWilson`
<!-- <h1>LSDOF_LinearWilson
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

LSDOF_LINEARWILSON transient response of linear SDOF system by exact integration of piecewise linear excitation

<!-- <div class="box"><strong>LSDOF_LINEARWILSON transient response of linear SDOF system by exact integration of piecewise linear excitation</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [u,udot,uddot] = LSDOF_LinearWilson (Deltat,omega,p,zeta,u0,udot0)` 
## <a name="_description"></a>Description

<pre class="comment">LSDOF_LINEARWILSON transient response of linear SDOF system by exact integration of piecewise linear excitation
  [U,UDOT,UDDOT] = LSDOF_LINEARWILSON (DELTAT,OMEGA,P,ZETA,U0,UDOT0)
  function determines the transient response history of linear SDOF system(s) with eigenfrequency(ies)
  in row vector OMEGA, to acceleration history (force/mass) in vector P,
  for damping ratio(s) in row vector ZETA (default=0),
  and initial conditions in row vectors U0 (displacement) and UDOT0 (velocity) (default values=0);
  the time step of integration is DELTAT;
  the function integrates exactly the equations of motion for piecewise linear interpolation of excitation;
  the function returns the displacement history(ies) in array U, the velocity history(ies)
  in array UDOT and the acceleration history(ies) in array UDDOT arranged columnwise (column no=frequency no);
  Reference: A.K.Chopra, Dynamics of Structures, 2nd edition, pp. 167-171</pre>
<!-- <div class="fragment"><pre class="comment">LSDOF_LINEARWILSON transient response of linear SDOF system by exact integration of piecewise linear excitation
  [U,UDOT,UDDOT] = LSDOF_LINEARWILSON (DELTAT,OMEGA,P,ZETA,U0,UDOT0)
  function determines the transient response history of linear SDOF system(s) with eigenfrequency(ies)
  in row vector OMEGA, to acceleration history (force/mass) in vector P,
  for damping ratio(s) in row vector ZETA (default=0),
  and initial conditions in row vectors U0 (displacement) and UDOT0 (velocity) (default values=0);
  the time step of integration is DELTAT;
  the function integrates exactly the equations of motion for piecewise linear interpolation of excitation;
  the function returns the displacement history(ies) in array U, the velocity history(ies)
  in array UDOT and the acceleration history(ies) in array UDDOT arranged columnwise (column no=frequency no);
  Reference: A.K.Chopra, Dynamics of Structures, 2nd edition, pp. 167-171</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="ElasticResponseSpectrum.md" class="code" title="function [D,Psv,Psa] = ElasticResponseSpectrum (Acceleration,T,zeta)">ElasticResponseSpectrum</a>	ELASTICRESPONSESPECTRUM determines the elastic response spectrum for given acceleration history</li><li><a href="ModalAnalysis.md" class="code" title="function [omega,Ueig,Y_t,Ydot_t,Yddot_t] = ModalAnalysis (option,Kf,M,Loading,Deltat,zeta,nmod)">ModalAnalysis</a>	MODALANALYSIS determines modal response history for given transient loading</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->