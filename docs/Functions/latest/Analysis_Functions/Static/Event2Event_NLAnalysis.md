
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href="_index.md">Static</a> &gt; Event2Event_NLAnalysis.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Analysis_Functions\Static&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `Event2Event_NLAnalysis`
<!-- <h1>Event2Event_NLAnalysis
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

EVENT2EVENT_NLANALYSIS event-to-event incremental analysis with linear or P-DELTA geometry

<!-- <div class="box"><strong>EVENT2EVENT_NLANALYSIS event-to-event incremental analysis with linear or P-DELTA geometry</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [lamdah,Qh,Ufh,Vph,Iph] = Event2Event_NLAnalysis (opt,Model,ElemData,Loading,ConvPar)` 
## <a name="_description"></a>Description

<pre class="comment">EVENT2EVENT_NLANALYSIS event-to-event incremental analysis with linear or P-DELTA geometry
  [LAMDAH,QH,UFH,VPH,IPH] = EVENT2EVENT_NLANALYSIS (OPT,MODEL,ELEMDATA,LOADING)
  the function determines the load factor history LAMDAH of a structural model for an
  event-to-event analysis under loading information in data structure LOADING;
  the latter should have two fields, Pref for the load pattern to be factored, and
  Pcf for the load pattern to remain constant;
  each row of the load factor history vector corresponds to a different event;
  OPT is a character variable with values of LG for linear, or NG for nonlinear geometry 
  the data structure MODEL contains information about the structural model, and
  element property information is provided in cell array ELEMDATA
  the function returns the load factor history for each event in row vector LAMDAH,
  the basic force history in array QH, the free global dof displacement history in array UFH,
  the plastic element deformation history in array VPH, and the history of the index
  of plastic hinge locations in array IPH; in the array UFH the row number corresponds
  to the degree of freedom number, while in the arrays QH, VPH, and IPH the row number
  corresponds to the basic force number; in the history arrays QH, UFH, VPH,and IPH
  the column number corresponds to the event number
  -----------------------------------------------------------------------------------------
  developed by Chin-Long Lee using mixed-formulation and consistent Newton-Raphson    01/08
  -----------------------------------------------------------------------------------------</pre>
<!-- <div class="fragment"><pre class="comment">EVENT2EVENT_NLANALYSIS event-to-event incremental analysis with linear or P-DELTA geometry
  [LAMDAH,QH,UFH,VPH,IPH] = EVENT2EVENT_NLANALYSIS (OPT,MODEL,ELEMDATA,LOADING)
  the function determines the load factor history LAMDAH of a structural model for an
  event-to-event analysis under loading information in data structure LOADING;
  the latter should have two fields, Pref for the load pattern to be factored, and
  Pcf for the load pattern to remain constant;
  each row of the load factor history vector corresponds to a different event;
  OPT is a character variable with values of LG for linear, or NG for nonlinear geometry 
  the data structure MODEL contains information about the structural model, and
  element property information is provided in cell array ELEMDATA
  the function returns the load factor history for each event in row vector LAMDAH,
  the basic force history in array QH, the free global dof displacement history in array UFH,
  the plastic element deformation history in array VPH, and the history of the index
  of plastic hinge locations in array IPH; in the array UFH the row number corresponds
  to the degree of freedom number, while in the arrays QH, VPH, and IPH the row number
  corresponds to the basic force number; in the history arrays QH, UFH, VPH,and IPH
  the column number corresponds to the event number
  -----------------------------------------------------------------------------------------
  developed by Chin-Long Lee using mixed-formulation and consistent Newton-Raphson    01/08
  -----------------------------------------------------------------------------------------</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="../../../latest/General_Functions/A_matrix" class="code" title="function A = A_matrix (Model)">A_matrix</a>	A_MATRIX kinematic matrix of structural model with 2d/3d truss and 2d frame elements</li><li><a href="../../../latest/General_Functions/Aj_matrix" class="code" title="function Aj = Aj_matrix (Model)">Aj_matrix</a>	AJ_MATRIX kinematic matrix of structural model with 2d/3d truss and 2d frame elements</li><li><a href="../../../latest/General_Functions/Localize" class="code" title="function [xyz,id] = Localize (Model,el)">Localize</a>	LOCALIZE returns the node coordinates and id array of element</li><li><a href="../../../latest/General_Functions/Q0_vector" class="code" title="function Q0 = Q0_vector (Model,ElemData)">Q0_vector</a>	Q0_VECTOR initial (fixed-end) force vector for structural model</li></ul>
This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->