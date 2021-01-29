
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href="_index.md">Dynamic</a> &gt; TimeIntegrationConstants.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Analysis_Functions\Dynamic&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `TimeIntegrationConstants`
<!-- <h1>TimeIntegrationConstants
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

TIMEINTEGRATIONCONSTANTS constants of time integration strategy

<!-- <div class="box"><strong>TIMEINTEGRATIONCONSTANTS constants of time integration strategy</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function Int_Constants = TimeIntegrationConstants (TimeStrat,option)` 
## <a name="_description"></a>Description

<pre class="comment">TIMEINTEGRATIONCONSTANTS constants of time integration strategy
  INT_CONSTANTS = TIMEINTEGRATIONCONSTANTS (TIMESTRAT)
  the function determines the constants of the time integration strategy speficied in field
  Type of data structure TIMESTRAT and returns them in vector INT_CONSTRANTS
  the data structure TIMESTRAT contains information about the integration strategy in fiels
      DELTAT = time step (scalar)
      TYPE   = name of integration method (character variable)
      PARAM  = parameters of integration method (vector)</pre>
<!-- <div class="fragment"><pre class="comment">TIMEINTEGRATIONCONSTANTS constants of time integration strategy
  INT_CONSTANTS = TIMEINTEGRATIONCONSTANTS (TIMESTRAT)
  the function determines the constants of the time integration strategy speficied in field
  Type of data structure TIMESTRAT and returns them in vector INT_CONSTRANTS
  the data structure TIMESTRAT contains information about the integration strategy in fiels
      DELTAT = time step (scalar)
      TYPE   = name of integration method (character variable)
      PARAM  = parameters of integration method (vector)</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="OneTransientIteration.md" class="code" title="function [State,SolStrat] = OneTransientIteration (Model,ElemData,Loading,State,SolStrat)">OneTransientIteration</a>	ONETRANSIENTITERATION single equilibrium iteration under transient conditions</li><li><a href="TransientIncrement.md" class="code" title="function [State,SolStrat] = TransientIncrement(Model,ElemData,Loading,State,SolStrat)">TransientIncrement</a>	TRANSIENTINCREMENT load incrementation and state advance under transient conditions</li><li><a href="Update_TransientState.md" class="code" title="function State = Update_TransientState (Model,ElemData,State,SolStrat)">Update_TransientState</a>	UPDATE_TRANSIENTSTATE final state determination under transient conditions, reset increments and history</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->