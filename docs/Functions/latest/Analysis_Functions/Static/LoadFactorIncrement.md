---
title: "LoadFactorIncrement"
id: "LoadFactorIncrement"
description: "LOADFACTORINCREMENT load factor increment(s) for given load histories"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href=".autoindex.md">Static</a> &gt; 
<!-- LoadFactorIncrement.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../.autoindex.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Analysis_Functions\Static&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `LoadFactorIncrement`



## <a name="_name"></a>Purpose


LOADFACTORINCREMENT load factor increment(s) for given load histories

<!-- <div class="box"><strong>LOADFACTORINCREMENT load factor increment(s) for given load histories</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function Dlam = LoadFactorIncrement (History,Time,Deltat)` 

## Description


<pre class="comment">LOADFACTORINCREMENT load factor increment(s) for given load histories
  DLAM = LOADFACTORINCREMENT(HISTORY,TIME,DELTAT)
  the function determines the load factor increment(s) in vector DLAM for the number of
  time histories in data structure HISTORY with fields TIME and VALUE; linear interpolation
  with current time TIME and time step DELTAT gives the load factor increment(s)</pre>
<!-- <div class="fragment"><pre class="comment">LOADFACTORINCREMENT load factor increment(s) for given load histories
  DLAM = LOADFACTORINCREMENT(HISTORY,TIME,DELTAT)
  the function determines the load factor increment(s) in vector DLAM for the number of
  time histories in data structure HISTORY with fields TIME and VALUE; linear interpolation
  with current time TIME and time step DELTAT gives the load factor increment(s)</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>

This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="../../../latest/Analysis_Functions/Dynamic/TransientIncrement.md" class="code" title="function [State,SolStrat] = TransientIncrement(Model,ElemData,Loading,State,SolStrat)">TransientIncrement</a>	TRANSIENTINCREMENT load incrementation and state advance under transient conditions</li><li><a href="Increment.md" class="code" title="function [State,SolStrat] = Increment(Model,ElemData,Loading,State,SolStrat)">Increment</a>	INCREMENT load incrementation and state advance under static conditions</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->