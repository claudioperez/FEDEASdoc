---
title: "LoadFactorControl"
id: "LoadFactorControl"
description: "LOADFACTORCONTROL determine load factor increment under load control strategy"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href=".autoindex.md">Static</a> &gt; 
<!-- LoadFactorControl.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../.autoindex.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Analysis_Functions\Static&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `LoadFactorControl`



## <a name="_name"></a>Purpose


LOADFACTORCONTROL determine load factor increment under load control strategy

<!-- <div class="box"><strong>LOADFACTORCONTROL determine load factor increment under load control strategy</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function SolStrat = LoadFactorControl (action,SolStrat,detKf,Pref,Ut,DUr)` 

## Description


<pre class="comment"> LOADFACTORCONTROL determine load factor increment under load control strategy
  SOLSTRAT = LOADFACTORCONTROL(ACTION,SOLSTRAT,KL,KU,PREF,UT,DUR)
  the function determines the load factor increment in field DLAM of data structure SOLSTRAT
  under the specified load control strategy in field LCTYPE of SOLSTRAT;
  ACTION is a character variable that distinguishes various load control stages, i.e.
  initialization, incrementation and iteration; accordingly, the choices are
  ACTION = 'init': initialization of load control parameters in field HIST of SOLSTRAT
  ACTION = 'incr': determination of DLAM during load incrementation; parameter update in HIST
  ACTION = 'iter': determination of DLAM during equilibrium iteration (the following load
                   control methods are currently supported: 'MinDispNorm' and 'KeyDOF'
  KL and KU are the lower and upper diagonal LU components of the tangent stiffness matrix,
  PREF is the reference force vector and UT the corresponding displacement vector under PREF,
  DUR is the vector of displacement increments under the current unbalance force vector</pre>
<!-- <div class="fragment"><pre class="comment"> LOADFACTORCONTROL determine load factor increment under load control strategy
  SOLSTRAT = LOADFACTORCONTROL(ACTION,SOLSTRAT,KL,KU,PREF,UT,DUR)
  the function determines the load factor increment in field DLAM of data structure SOLSTRAT
  under the specified load control strategy in field LCTYPE of SOLSTRAT;
  ACTION is a character variable that distinguishes various load control stages, i.e.
  initialization, incrementation and iteration; accordingly, the choices are
  ACTION = 'init': initialization of load control parameters in field HIST of SOLSTRAT
  ACTION = 'incr': determination of DLAM during load incrementation; parameter update in HIST
  ACTION = 'iter': determination of DLAM during equilibrium iteration (the following load
                   control methods are currently supported: 'MinDispNorm' and 'KeyDOF'
  KL and KU are the lower and upper diagonal LU components of the tangent stiffness matrix,
  PREF is the reference force vector and UT the corresponding displacement vector under PREF,
  DUR is the vector of displacement increments under the current unbalance force vector</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>

This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="Increment.md" class="code" title="function [State,SolStrat] = Increment(Model,ElemData,Loading,State,SolStrat)">Increment</a>	INCREMENT load incrementation and state advance under static conditions</li><li><a href="Initialize.md" class="code" title="function [State,SolStrat] = Initialize (Model,ElemData,Loading,State,SolStrat)">Initialize</a>	INITIALIZE initialize analysis variables in STATE and load control parameters in SOLSTRAT</li><li><a href="OneIteration.md" class="code" title="function [State,SolStrat] = OneIteration (Model,ElemData,Loading,State,SolStrat)">OneIteration</a>	ONEITERATION single equilibrium iteration under static conditions</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->