---
title: "ElasticResponseSpectrum"
id: "ElasticResponseSpectrum"
description: "ELASTICRESPONSESPECTRUM determines the elastic response spectrum for given acceleration history"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href=".autoindex.md">Dynamic</a> &gt; 
<!-- ElasticResponseSpectrum.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../.autoindex.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Analysis_Functions\Dynamic&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `ElasticResponseSpectrum`



## <a name="_name"></a>Purpose


ELASTICRESPONSESPECTRUM determines the elastic response spectrum for given acceleration history

<!-- <div class="box"><strong>ELASTICRESPONSESPECTRUM determines the elastic response spectrum for given acceleration history</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [D,Psv,Psa] = ElasticResponseSpectrum (Acceleration,T,zeta)` 

## Description


<pre class="comment">ELASTICRESPONSESPECTRUM determines the elastic response spectrum for given acceleration history
  [D,PSV,PSA] = ELASTICRESPONSESPECTRUM (ACCELERATION,T,ZETA)
  the function determines the elastic response spectrum for a given acceleration history in
  data structure ACCELERATION with fields Deltat (time step size) and Value (acceleration value);
  the periods for the spectrum are specified in row vector T ( default= [0.001 0.1:0.1:5] );
  the row vector ZETA contains the damping ratio(s) ( default=0 );
  the response spectrum values for the periods in row vector T are returned
  in arrays D for displacement, PSV for pseudo-velocity, and PSA for pseudo-acceleration
  with the row number corresponding to the period and the column number to the damping ratio</pre>
<!-- <div class="fragment"><pre class="comment">ELASTICRESPONSESPECTRUM determines the elastic response spectrum for given acceleration history
  [D,PSV,PSA] = ELASTICRESPONSESPECTRUM (ACCELERATION,T,ZETA)
  the function determines the elastic response spectrum for a given acceleration history in
  data structure ACCELERATION with fields Deltat (time step size) and Value (acceleration value);
  the periods for the spectrum are specified in row vector T ( default= [0.001 0.1:0.1:5] );
  the row vector ZETA contains the damping ratio(s) ( default=0 );
  the response spectrum values for the periods in row vector T are returned
  in arrays D for displacement, PSV for pseudo-velocity, and PSA for pseudo-acceleration
  with the row number corresponding to the period and the column number to the damping ratio</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="/Functions/LSDOF_LinearWilson" class="code" title="function [u,udot,uddot] = LSDOF_LinearWilson (Deltat,omega,p,zeta,u0,udot0)">LSDOF_LinearWilson</a>	LSDOF_LINEARWILSON transient response of linear SDOF system by exact integration of piecewise linear excitation</li></ul>

This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->