---
title: "Create_NodalForces"
id: "Create_NodalForces"
description: "CREATE_NODALFORCES set up reference vector of applied forces"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">General_Functions</a> &gt; 
<!-- Create_NodalForces.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\General_Functions&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Create_NodalForces`



## <a name="_name"></a>Purpose


CREATE_NODALFORCES set up reference vector of applied forces

<!-- <div class="box"><strong>CREATE_NODALFORCES set up reference vector of applied forces</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function Pref = Create_NodalForces (Model,Pe)` 

## Description


<pre class="comment">CREATE_NODALFORCES set up reference vector of applied forces
  PREF = CREATE_NODALFORCES (MODEL,PE)
  the function sets up the vector of applied forces PREF at the free dofs of the model;
  model information is supplied in data structure MODEL and the applied forces in array PE;
  in array PE rows correspond to node numbers and columns to dofs
  Example: PE(3,:) = [10 0 50] means applied forces at node 3 in X,Y and Z direction</pre>
<!-- <div class="fragment"><pre class="comment">CREATE_NODALFORCES set up reference vector of applied forces
  PREF = CREATE_NODALFORCES (MODEL,PE)
  the function sets up the vector of applied forces PREF at the free dofs of the model;
  model information is supplied in data structure MODEL and the applied forces in array PE;
  in array PE rows correspond to node numbers and columns to dofs
  Example: PE(3,:) = [10 0 50] means applied forces at node 3 in X,Y and Z direction</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->