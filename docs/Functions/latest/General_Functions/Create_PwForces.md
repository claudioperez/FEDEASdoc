---
title: "Create_PwForces"
id: "Create_PwForces"
description: "CREATE_PWFORCES set up equivalent nodal forces due to uniform element loading w"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">General_Functions</a> &gt; 
<!-- Create_PwForces.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\General_Functions&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Create_PwForces`



## <a name="_name"></a>Purpose


CREATE_PWFORCES set up equivalent nodal forces due to uniform element loading w

<!-- <div class="box"><strong>CREATE_PWFORCES set up equivalent nodal forces due to uniform element loading w</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function Pw = Create_PwForces (Model,ElemData)` 

## Description


<pre class="comment">CREATE_PWFORCES set up equivalent nodal forces due to uniform element loading w
  PW = CREATE_PWFORCES (MODEL,ELEMDATA)
  the function sets up the vector of equivalent nodal forces PW due to uniform element loading w;
  model information is supplied in data structure MODEL,
  and the magnitude of w is supplied for each element in field W of ELEMDATA</pre>
<!-- <div class="fragment"><pre class="comment">CREATE_PWFORCES set up equivalent nodal forces due to uniform element loading w
  PW = CREATE_PWFORCES (MODEL,ELEMDATA)
  the function sets up the vector of equivalent nodal forces PW due to uniform element loading w;
  model information is supplied in data structure MODEL,
  and the magnitude of w is supplied for each element in field W of ELEMDATA</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="/Functions/Localize" class="code" title="function [xyz,id] = Localize (Model,el)">Localize</a>	LOCALIZE returns the node coordinates and id array of element</li></ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="../../latest/Solution_Scripts/S_DisplMethod.md" class="code" title="">S_DisplMethod</a>	% S_DISPLMETHOD script for displacement method of structural analysis</li><li><a href="../../latest/Solution_Scripts/S_ForceMethod.md" class="code" title="">S_ForceMethod</a>	% S_FORCEMETHOD script for force method of structural analysis</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->