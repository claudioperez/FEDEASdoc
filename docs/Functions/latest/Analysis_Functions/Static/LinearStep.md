---
title: "LinearStep"
id: "LinearStep"
description: "LINEARSTEP sets up and solves the structure equilibrium equations for single load step"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href=".autoindex.md">Static</a> &gt; 
<!-- LinearStep.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../.autoindex.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Analysis_Functions\Static&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `LinearStep`



## <a name="_name"></a>Purpose


LINEARSTEP sets up and solves the structure equilibrium equations for single load step

<!-- <div class="box"><strong>LINEARSTEP sets up and solves the structure equilibrium equations for single load step</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function State = LinearStep (Model,ElemData,Loading)` 

## Description


<pre class="comment">LINEARSTEP sets up and solves the structure equilibrium equations for single load step
  STATE = LINEARSTEP (MODEL,ELEMDATA,LOADING)
  function sets up and solves the structure equilibrium equations for single load step
  by direct assembly of element stiffness matrices; the structural response is contained
  in data structure STATE with fields U for the global dof displacement vector, Pr for the
  resisting force vector and Kf for the stiffness matrix at the free dofs of the structure;
  information about the structural model is supplied in data structure MODEL,
  the element properties are supplied in cell array ELEMDATA and loading information is
  given in data structure LOADING with fields Pref and Uref for a single applied force and
  a single imposed displacement vector, respectively</pre>
<!-- <div class="fragment"><pre class="comment">LINEARSTEP sets up and solves the structure equilibrium equations for single load step
  STATE = LINEARSTEP (MODEL,ELEMDATA,LOADING)
  function sets up and solves the structure equilibrium equations for single load step
  by direct assembly of element stiffness matrices; the structural response is contained
  in data structure STATE with fields U for the global dof displacement vector, Pr for the
  resisting force vector and Kf for the stiffness matrix at the free dofs of the structure;
  information about the structural model is supplied in data structure MODEL,
  the element properties are supplied in cell array ELEMDATA and loading information is
  given in data structure LOADING with fields Pref and Uref for a single applied force and
  a single imposed displacement vector, respectively</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="/Functions/Initialize_State" class="code" title="function State = Initialize_State (Model,ElemData)">Initialize_State</a>	INITIALIZE_STATE initialize state variables of structural model and create STATE</li><li><a href="/Functions/../../../latest/General_Functions/Structure" class="code" title="function Resp = Structure (action,Model,ElemData,State,ElemList)">Structure</a>	STRUCTURE performs requested action on group of elements</li></ul>

This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->