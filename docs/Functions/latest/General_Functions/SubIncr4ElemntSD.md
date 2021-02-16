---
title: "SubIncr4ElemntSD"
id: "SubIncr4ElemntSD"
description: "SUBINCR4ELMNTSD element displacement increment subdivision for state determination"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">General_Functions</a> &gt; 
<!-- SubIncr4ElemntSD.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\General_Functions&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `SubIncr4ElemntSD`



## <a name="_name"></a>Purpose


SUBINCR4ELMNTSD element displacement increment subdivision for state determination

<!-- <div class="box"><strong>SUBINCR4ELMNTSD element displacement increment subdivision for state determination</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function ElemState = SubIncr4ElemntSD (el,ElemName,xyz,ElemData,ElemState)` 

## Description


<pre class="comment">SUBINCR4ELMNTSD element displacement increment subdivision for state determination
ELEMSTATE = SUBINCR4ELMNTSD (EL,ELEMNAME,XYZ,ELEMDATA,ELEMSTATE)
  function calls the state determination function for all elements in the structural model
  with the option of subdividing the displacement increment in case of non-convergence;
  the latter case is represented by the logical variable CONVFLAG in ELEMSTATE;
  to activate the option of element displacement increment subdivision, the variable
  SUBDIVNO must be set in the element property data structure ELEMDATA</pre>
<!-- <div class="fragment"><pre class="comment">SUBINCR4ELMNTSD element displacement increment subdivision for state determination
ELEMSTATE = SUBINCR4ELMNTSD (EL,ELEMNAME,XYZ,ELEMDATA,ELEMSTATE)
  function calls the state determination function for all elements in the structural model
  with the option of subdividing the displacement increment in case of non-convergence;
  the latter case is represented by the logical variable CONVFLAG in ELEMSTATE;
  to activate the option of element displacement increment subdivision, the variable
  SUBDIVNO must be set in the element property data structure ELEMDATA</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="Structure.md" class="code" title="function Resp = Structure (action,Model,ElemData,State,ElemList)">Structure</a>	STRUCTURE performs requested action on group of elements</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->