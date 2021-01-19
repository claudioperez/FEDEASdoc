
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Solution_Library</a> &gt; <a href="_index.md">Plastic_Analysis</a> &gt; PlasticAnalysis_wLBT.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Solution_Library\Plastic_Analysis&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `PlasticAnalysis_wLBT`
<!-- <h1>PlasticAnalysis_wLBT
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

PLASTICANALYSIS_wLBT collapse load factor and basic element forces by lower bound theorem of plastic analysis

<!-- <div class="box"><strong>PLASTICANALYSIS_wLBT collapse load factor and basic element forces by lower bound theorem of plastic analysis</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [lamdac,Qc] = PlasticAnalysis_wLBT (Bf,Qpl,Pref,Pcf,Options)` 
## <a name="_description"></a>Description

<pre class="comment">PLASTICANALYSIS_wLBT collapse load factor and basic element forces by lower bound theorem of plastic analysis
  [LAMDAC,QC] = PLASTICANALYSIS_wLBT (BF,QPL,PREF,PCF,OPTIONS)
  the function uses the lower bound theorem of plastic analysis
  to determine the collapse load factor LAMDAC and the basic forces QC at collapse
  of a structural model under reference load vector PREF and force vector PCF at free dofs;
  the reference force vector PREF represents the load pattern to be factored, while
  the force vector PCF represents the load pattern that remains unfactored;
  for the sign of PCF note that the equilibrium equations are: lambda Pref + Pcf = Bf Q;
  there are two options for supplying the static matrix Bf:
  (a) as data structure Model with information about the structural model, that is used
      to set up the static matrix Bf of the structure automatically, or
  (b) as nf by nq matrix where nf = no of free dofs and nq = total number of basic forces;
  there are two options for supplying the plastic capacities QPL:
  (a) as cell array ELEMDATA with plastic capacities in fields Np for axial and Mp for flexural
  (b) as one column vector for the case that positive and negative capacities are the same,
       or, as two column array with positive plastic capacities in the first column
       and negative plastic capacities in the second (in absolute value) (signs matching Q!)
  NOTE: mixing of options (a) and (b) is not supported!</pre>
<!-- <div class="fragment"><pre class="comment">PLASTICANALYSIS_wLBT collapse load factor and basic element forces by lower bound theorem of plastic analysis
  [LAMDAC,QC] = PLASTICANALYSIS_wLBT (BF,QPL,PREF,PCF,OPTIONS)
  the function uses the lower bound theorem of plastic analysis
  to determine the collapse load factor LAMDAC and the basic forces QC at collapse
  of a structural model under reference load vector PREF and force vector PCF at free dofs;
  the reference force vector PREF represents the load pattern to be factored, while
  the force vector PCF represents the load pattern that remains unfactored;
  for the sign of PCF note that the equilibrium equations are: lambda Pref + Pcf = Bf Q;
  there are two options for supplying the static matrix Bf:
  (a) as data structure Model with information about the structural model, that is used
      to set up the static matrix Bf of the structure automatically, or
  (b) as nf by nq matrix where nf = no of free dofs and nq = total number of basic forces;
  there are two options for supplying the plastic capacities QPL:
  (a) as cell array ELEMDATA with plastic capacities in fields Np for axial and Mp for flexural
  (b) as one column vector for the case that positive and negative capacities are the same,
       or, as two column array with positive plastic capacities in the first column
       and negative plastic capacities in the second (in absolute value) (signs matching Q!)
  NOTE: mixing of options (a) and (b) is not supported!</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="../../../latest/Introspection/Structure/B_matrix" class="code" title="function B = B_matrix (Model)">B_matrix</a>	B_MATRIX equilibrium matrix of structural model with 2d/3d truss and 2d frame elements</li></ul>
This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Sun 20-Dec-2020 19:28:50 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->