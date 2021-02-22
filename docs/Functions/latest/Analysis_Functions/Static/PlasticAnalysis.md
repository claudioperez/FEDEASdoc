---
title: "PlasticAnalysis"
id: "PlasticAnalysis"
description: "PLASTICANALYSIS collapse load factor, basic forces, and collapse mechanism by plastic analysis"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href=".autoindex.md">Static</a> &gt; 
<!-- PlasticAnalysis.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../.autoindex.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Analysis_Functions\Static&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `PlasticAnalysis`



## <a name="_name"></a>Purpose


PLASTICANALYSIS collapse load factor, basic forces, and collapse mechanism by plastic analysis

<!-- <div class="box"><strong>PLASTICANALYSIS collapse load factor, basic forces, and collapse mechanism by plastic analysis</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [lamdac,Qc,DUf,DVpl] = PlasticAnalysis (Model,ElemData,Loading,LPOpt)` 

## Description


<pre class="comment">PLASTICANALYSIS collapse load factor, basic forces, and collapse mechanism by plastic analysis
  [LAMDAC,QC,DUF,DVPL] = PLASTICANALYSIS (MODEL,ELEMDATA,LOADING,LPOPT)
  the function determines the collapse load factor LAMDAC of a structural model under loading
  information in data structure LOADING; the latter should have the field PREF for the
  load pattern to be factored, and may include a field Pcf for the load pattern to remain constant;
  the data structure MODEL contains information about the structural model, and
  element property information is provided in cell array ELEMDATA;
  the function also returns the basic forces at incipient collapse in vector QC, the
  displacement increments of the collapse mechanism in vector DUF, and the plastic
  deformation increments of the collapse mechanism in vector DVPL
  LPOPT is an optional data structure for selecting options of
  the linear programming algorithm; these options are discussed in the
  Matlab manual pages for the linprog function
  the function uses 'dual-simplex' and 'LargeScale' by default; 
  the tolerance variable tol refers to OptimalityTolerance of the dual-simplex
  algorithm with default value 1e-7</pre>
<!-- <div class="fragment"><pre class="comment">PLASTICANALYSIS collapse load factor, basic forces, and collapse mechanism by plastic analysis
  [LAMDAC,QC,DUF,DVPL] = PLASTICANALYSIS (MODEL,ELEMDATA,LOADING,LPOPT)
  the function determines the collapse load factor LAMDAC of a structural model under loading
  information in data structure LOADING; the latter should have the field PREF for the
  load pattern to be factored, and may include a field Pcf for the load pattern to remain constant;
  the data structure MODEL contains information about the structural model, and
  element property information is provided in cell array ELEMDATA;
  the function also returns the basic forces at incipient collapse in vector QC, the
  displacement increments of the collapse mechanism in vector DUF, and the plastic
  deformation increments of the collapse mechanism in vector DVPL
  LPOPT is an optional data structure for selecting options of
  the linear programming algorithm; these options are discussed in the
  Matlab manual pages for the linprog function
  the function uses 'dual-simplex' and 'LargeScale' by default; 
  the tolerance variable tol refers to OptimalityTolerance of the dual-simplex
  algorithm with default value 1e-7</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="/Functions/../../../latest/General_Functions/A_matrix" class="code" title="function A = A_matrix (Model)">A_matrix</a>	A_MATRIX kinematic matrix of structural model with 2d/3d truss and 2d frame elements</li><li><a href="/Functions/../../../latest/General_Functions/Aj_matrix" class="code" title="function Aj = Aj_matrix (Model)">Aj_matrix</a>	AJ_MATRIX kinematic matrix of structural model with 2d/3d truss and 2d frame elements</li><li><a href="/Functions/../../../latest/General_Functions/Localize" class="code" title="function [xyz,id] = Localize (Model,el)">Localize</a>	LOCALIZE returns the node coordinates and id array of element</li></ul>

This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->