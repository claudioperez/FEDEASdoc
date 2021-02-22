---
title: "Create_NodalMass"
id: "Create_NodalMass"
description: "CREATE_NODALMASS free dof lumped mass vector for structural model"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">General_Functions</a> &gt; 
<!-- Create_NodalMass.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\General_Functions&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Create_NodalMass`



## <a name="_name"></a>Purpose


CREATE_NODALMASS free dof lumped mass vector for structural model

<!-- <div class="box"><strong>CREATE_NODALMASS free dof lumped mass vector for structural model</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function Ml = Create_NodalMass (Model,Me)` 

## Description


<pre class="comment">CREATE_NODALMASS free dof lumped mass vector for structural model
  ML = CREATE_NODALMASS (MODEL,ME)
  the function sets up the free dof lumped mass vector ML for the structural model
  specified in data structure MODEL from the specified nodal lumped mass values in array ME
  in which rows correspond to node numbers and columns to dof direction
  Example: ME(5,:) = [20 20 0]; lumped mass value in X and Y at node 5; no rotary inertia</pre>
<!-- <div class="fragment"><pre class="comment">CREATE_NODALMASS free dof lumped mass vector for structural model
  ML = CREATE_NODALMASS (MODEL,ME)
  the function sets up the free dof lumped mass vector ML for the structural model
  specified in data structure MODEL from the specified nodal lumped mass values in array ME
  in which rows correspond to node numbers and columns to dof direction
  Example: ME(5,:) = [20 20 0]; lumped mass value in X and Y at node 5; no rotary inertia</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="Add_Mass2Model.md" class="code" title="function Model = Add_Mass2Model (Model,Me,ElemData,option)">Add_Mass2Model</a>	ADD_MASS2MODEL sets up lumped or consistent mass in Model.M</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->