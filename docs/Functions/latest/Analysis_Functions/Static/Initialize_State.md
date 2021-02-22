---
title: "Initialize_State"
id: "Initialize_State"
description: "INITIALIZE_STATE initialize state variables of structural model and create STATE"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href=".autoindex.md">Static</a> &gt; 
<!-- Initialize_State.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../.autoindex.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Analysis_Functions\Static&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `Initialize_State`



## <a name="_name"></a>Purpose


INITIALIZE_STATE initialize state variables of structural model and create STATE

<!-- <div class="box"><strong>INITIALIZE_STATE initialize state variables of structural model and create STATE</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function State = Initialize_State (Model,ElemData)` 

## Description


<pre class="comment">INITIALIZE_STATE initialize state variables of structural model and create STATE    
  INITIALIZE_STATE (MODEL,ELEMDATA)
  function initializes the displacement, velocity and acceleration vectors
  for the structural model with information in data structure MODEL;
  the cell array ELEMDATA supplies the element property data for element history initialization;
  the function returns data structure STATE with the following fields
  STATE.U       = global dof total displacement vector
        DU      = global dof displacement increments from last convergence
        DDU     = global dof displacement increments from last iteration
        Udot    = global dof velocity vector
        Udotdot = global dof acceleration vector
        Past    = data structure of last    element history variables in cell array Elem
        Pres    = data structure of current element history variables in cell array Elem</pre>
<!-- <div class="fragment"><pre class="comment">INITIALIZE_STATE initialize state variables of structural model and create STATE    
  INITIALIZE_STATE (MODEL,ELEMDATA)
  function initializes the displacement, velocity and acceleration vectors
  for the structural model with information in data structure MODEL;
  the cell array ELEMDATA supplies the element property data for element history initialization;
  the function returns data structure STATE with the following fields
  STATE.U       = global dof total displacement vector
        DU      = global dof displacement increments from last convergence
        DDU     = global dof displacement increments from last iteration
        Udot    = global dof velocity vector
        Udotdot = global dof acceleration vector
        Past    = data structure of last    element history variables in cell array Elem
        Pres    = data structure of current element history variables in cell array Elem</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="/Functions/../../../latest/General_Functions/Structure" class="code" title="function Resp = Structure (action,Model,ElemData,State,ElemList)">Structure</a>	STRUCTURE performs requested action on group of elements</li></ul>

This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="LinearStep.md" class="code" title="function State = LinearStep (Model,ElemData,Loading)">LinearStep</a>	LINEARSTEP sets up and solves the structure equilibrium equations for single load step</li><li><a href="../../../latest/Solution_Scripts/S_InitialStep.md" class="code" title="">S_InitialStep</a>	% S_INITIALSTEP script for initial step of incremental analysis</li><li><a href="../../../latest/Solution_Scripts/S_MultiStep.md" class="code" title="">S_MultiStep</a>	% S_MULTISTEP script for multi-step incremental analysis after load factor initialization</li><li><a href="../../../latest/Solution_Scripts/S_MultiStep_wLoadHist.md" class="code" title="">S_MultiStep_wLoadHist</a>	% S_MULTISTEP_wLOADHIST script for multi-step incremental analysis under given load history(ies)</li><li><a href="../../../latest/Solution_Scripts/S_MultiStep_wLoadHistwSD.md" class="code" title="">S_MultiStep_wLoadHistwSD</a>	% S_MULTISTEP_wLOADHISTwSD script for multi-step incremental analysis under given load history(ies)</li><li><a href="../../../latest/Solution_Scripts/S_Transient_MultiStep.md" class="code" title="">S_Transient_MultiStep</a>	% S_TRANSIENT_MULTISTEP script for multi-step transient analysis under given load history(ies)</li><li><a href="../../../latest/Solution_Scripts/S_Transient_MultiStepwSD.md" class="code" title="">S_Transient_MultiStepwSD</a>	% S_TRANSIENT_MULTISTEPwSD script for multi-step transient analysis under given load history(ies)</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->