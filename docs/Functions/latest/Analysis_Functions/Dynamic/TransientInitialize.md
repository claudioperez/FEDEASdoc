
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href="_index.md">Dynamic</a> &gt; TransientInitialize.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Analysis_Functions\Dynamic&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `TransientInitialize`
<!-- <h1>TransientInitialize
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

TRANSIENTINITIALIZE initialize State variables for transient response analysis

<!-- <div class="box"><strong>TRANSIENTINITIALIZE initialize State variables for transient response analysis</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function State = TransientInitialize (Model,ElemData,Loading,State)` 
## <a name="_description"></a>Description

<pre class="comment">TRANSIENTINITIALIZE initialize State variables for transient response analysis
  STATE = TRANSIENTINITIALIZE(MODEL,ELEMDATA,LOADING,STATE)
  the function initializes variables in STATE relevant for transient response analysis and
  returns an updated data structure STATE;
  MODEL is a data structure with information about the structural model, ELEMDATA is
  a cell array with element properties, and LOADING is a data structure with information
  about applied force, imposed displacement, and imposed acceleration patterns
  with corresponding load histories;
  specifically the function adds the following fields to STATE needed for transient analysis
  STATE
       lamda   = row vector of current load factors
       Pi      = initial force vector (for load sequences)
       Time    = pseudo-or real time counter
       Ugddot  = support acceleration vector
       C       = damping matrix</pre>
<!-- <div class="fragment"><pre class="comment">TRANSIENTINITIALIZE initialize State variables for transient response analysis
  STATE = TRANSIENTINITIALIZE(MODEL,ELEMDATA,LOADING,STATE)
  the function initializes variables in STATE relevant for transient response analysis and
  returns an updated data structure STATE;
  MODEL is a data structure with information about the structural model, ELEMDATA is
  a cell array with element properties, and LOADING is a data structure with information
  about applied force, imposed displacement, and imposed acceleration patterns
  with corresponding load histories;
  specifically the function adds the following fields to STATE needed for transient analysis
  STATE
       lamda   = row vector of current load factors
       Pi      = initial force vector (for load sequences)
       Time    = pseudo-or real time counter
       Ugddot  = support acceleration vector
       C       = damping matrix</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="../../../latest/Solution_Scripts/S_Transient_MultiStep.md" class="code" title="">S_Transient_MultiStep</a>	% S_TRANSIENT_MULTISTEP script for multi-step transient analysis under given load history(ies)</li><li><a href="../../../latest/Solution_Scripts/S_Transient_MultiStepwSD.md" class="code" title="">S_Transient_MultiStepwSD</a>	% S_TRANSIENT_MULTISTEPwSD script for multi-step transient analysis under given load history(ies)</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->