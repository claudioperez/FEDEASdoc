---
title: "LSDOF_Newmark"
id: "LSDOF_Newmark"
description: "LSDOF_NEWMARK determines the response of linear SDOF system to acceleration history with Newmark's method"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href=".autoindex.md">Dynamic</a> &gt; 
<!-- LSDOF_Newmark.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../.autoindex.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Analysis_Functions\Dynamic&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `LSDOF_Newmark`



## <a name="_name"></a>Purpose


LSDOF_NEWMARK determines the response of linear SDOF system to acceleration history with Newmark's method

<!-- <div class="box"><strong>LSDOF_NEWMARK determines the response of linear SDOF system to acceleration history with Newmark's method</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [u,udot,uddot] = LSDOF_Newmark (Deltat,omega,p,zeta,u0,udot0)` 

## Description


<pre class="comment">LSDOF_NEWMARK determines the response of linear SDOF system to acceleration history with Newmark's method
  [U,UDOT,UDDOT] = LSDOF_NEWMARK (DELTAT,OMEGA,P,ZETA,U0,UDOT0)
  function determines the transient response history of linear SDOF system(s) with eigenfrequency(ies)
  in row vector OMEGA, to acceleration history (force/mass) in vector P,
  for damping ratio(s) in row vector ZETA (default=0),
  and initial conditions in row vectors U0 (displacement) and UDOT0 (velocity) (default values=0);
  the time step of integration is DELTAT;
  N.M. Newmark's method from 1959 is used for the numerical integration of the equations of motion;
  the function returns the displacement history(ies) in array U, the velocity history(ies)
  in array UDOT and the acceleration history(ies) in array UDDOT arranged columnwise (column no=frequency no);
  Reference: A.K.Chopra, Dynamics of Structures, 2nd edition, pp. 174-180</pre>
<!-- <div class="fragment"><pre class="comment">LSDOF_NEWMARK determines the response of linear SDOF system to acceleration history with Newmark's method
  [U,UDOT,UDDOT] = LSDOF_NEWMARK (DELTAT,OMEGA,P,ZETA,U0,UDOT0)
  function determines the transient response history of linear SDOF system(s) with eigenfrequency(ies)
  in row vector OMEGA, to acceleration history (force/mass) in vector P,
  for damping ratio(s) in row vector ZETA (default=0),
  and initial conditions in row vectors U0 (displacement) and UDOT0 (velocity) (default values=0);
  the time step of integration is DELTAT;
  N.M. Newmark's method from 1959 is used for the numerical integration of the equations of motion;
  the function returns the displacement history(ies) in array U, the velocity history(ies)
  in array UDOT and the acceleration history(ies) in array UDDOT arranged columnwise (column no=frequency no);
  Reference: A.K.Chopra, Dynamics of Structures, 2nd edition, pp. 174-180</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>

This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->