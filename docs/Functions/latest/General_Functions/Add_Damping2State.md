---
title: "Add_Damping2State"
id: "Add_Damping2State"
description: "ADD_DAMPING2STATE setup damping matrix of structural model as field of data structure STATE"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">General_Functions</a> &gt; 
<!-- Add_Damping2State.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\General_Functions&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Add_Damping2State`



## <a name="_name"></a>Purpose


ADD_DAMPING2STATE setup damping matrix of structural model as field of data structure STATE

<!-- <div class="box"><strong>ADD_DAMPING2STATE setup damping matrix of structural model as field of data structure STATE</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function State = Add_Damping2State (type,Model,State,zeta,mode)` 

## Description


<pre class="comment">ADD_DAMPING2STATE setup damping matrix of structural model as field of data structure STATE
  STATE = ADD_DAMPING2STATE (TYPE,MODEL,STATE,ZETA,MODE)
  function sets up structural damping matrix C according to character variable TYPE
  as field of data structure STATE; the free dof stiffness matrix is field Kf of STATE
  and the free dof lumped mass vector is field Ml of MODEL;
  the damping matrix is calibrated so that the mode numbers in row vector MODE have
  damping ratios as specified in row vector ZETA;
  character variable TYPE should be either 'StifProp' or 'Caughey'
  Note: Caughey with one mode reduces to mass proportional damping matrix and with
        two modes reduces to Rayleigh damping</pre>
<!-- <div class="fragment"><pre class="comment">ADD_DAMPING2STATE setup damping matrix of structural model as field of data structure STATE
  STATE = ADD_DAMPING2STATE (TYPE,MODEL,STATE,ZETA,MODE)
  function sets up structural damping matrix C according to character variable TYPE
  as field of data structure STATE; the free dof stiffness matrix is field Kf of STATE
  and the free dof lumped mass vector is field Ml of MODEL;
  the damping matrix is calibrated so that the mode numbers in row vector MODE have
  damping ratios as specified in row vector ZETA;
  character variable TYPE should be either 'StifProp' or 'Caughey'
  Note: Caughey with one mode reduces to mass proportional damping matrix and with
        two modes reduces to Rayleigh damping</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="/Functions/Create_Damping" class="code" title="function C = Create_Damping (type,Kf,Ml,zeta,mode)">Create_Damping</a>	CREATE_DAMPING setup damping matrix of structural model</li></ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->