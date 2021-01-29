
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href="_index.md">Dynamic</a> &gt; AccelerationIntegral.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Analysis_Functions\Dynamic&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `AccelerationIntegral`
<!-- <h1>AccelerationIntegral
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

ACCELERATIONINTEGRAL determines displacement and velocity history for given acceleration history

<!-- <div class="box"><strong>ACCELERATIONINTEGRAL determines displacement and velocity history for given acceleration history</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [u,udot] = AccelerationIntegral (uddot,Deltat,nstep,u0,udot0)` 
## <a name="_description"></a>Description

<pre class="comment">ACCELERATIONINTEGRAL determines displacement and velocity history for given acceleration history 
  [U,UDOT] = ACCELERATIONINTEGRAL (UDDOT,DELTAT,NSTEP,U0,UDOT0)
  function integrates the acceleration history(ies) in array UDDOT to obtain
  the displacement history(ies) in array U and velocity history(ies) in array UDOT;
  the time step of the acceleration record is DELTAT
  and the total number of steps is NSTEP (default=no of acceleration values) 
  the initial displacement is supplied in row vector U0 and the initial velocity in row vector UDOT0 (default=0);
  histories are arranged columnwise in arrays UDDOT, U and UDOT (column no=history no);
  the displacement and velocity histories are corrected for zero end values</pre>
<!-- <div class="fragment"><pre class="comment">ACCELERATIONINTEGRAL determines displacement and velocity history for given acceleration history 
  [U,UDOT] = ACCELERATIONINTEGRAL (UDDOT,DELTAT,NSTEP,U0,UDOT0)
  function integrates the acceleration history(ies) in array UDDOT to obtain
  the displacement history(ies) in array U and velocity history(ies) in array UDOT;
  the time step of the acceleration record is DELTAT
  and the total number of steps is NSTEP (default=no of acceleration values) 
  the initial displacement is supplied in row vector U0 and the initial velocity in row vector UDOT0 (default=0);
  histories are arranged columnwise in arrays UDDOT, U and UDOT (column no=history no);
  the displacement and velocity histories are corrected for zero end values</pre></div> -->

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