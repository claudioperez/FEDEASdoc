
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Solution_Library</a> &gt; <a href="_index.md">Plastic_Analysis</a> &gt; PlasticAnalysis_wUBT.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Solution_Library\Plastic_Analysis&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `PlasticAnalysis_wUBT`
<!-- <h1>PlasticAnalysis_wUBT
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

PLASTICANALYSIS_wUBT collapse load factor and deformation increments by upper bound theorem of plastic analysis

<!-- <div class="box"><strong>PLASTICANALYSIS_wUBT collapse load factor and deformation increments by upper bound theorem of plastic analysis</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [lamdac,DUf,DVhp] = PlasticAnalysis_wUBT (Af,Qpl,Pref,Pcf,Options)` 
## <a name="_description"></a>Description

<pre class="comment">PLASTICANALYSIS_wUBT collapse load factor and deformation increments by upper bound theorem of plastic analysis
  [LAMDAC,DUF,DVHP] = PLASTICANALYSIS_wUBT (AF,QPL,PREF,PCF)
  the function uses the upper bound theorem of plastic analysis
  to determine the collapse load factor LAMDAC, and the displacement and plastic deformation
  increments of the collapse mechanism DUF and DVHP, respectively,
  of a structural model under reference load vector PREF and force vector PCF at free dofs;
  the reference force vector PREF represents the load pattern to be factored, while
  the force vector PFC represents the load pattern that remains unfactored;
  for the sign of PFU note that the equilibrium equations are: lambda Pref + Pcf = Bf Q;
  there are two options for supplying the kinematic matrix Af:
  (a) as data structure Model with information about the structural model, that is used
      to set up the kinematic matrix Af of the structure automatically, or
  (b) as nq by nf matrix where nq = total number of deformations and nf = no of free dofs;
  there are two options for supplying the plastic capacities QPL:
  (a) as cell array ELEMDATA with plastic capacities in fields Np for axial and Mp for flexural
  (b) as one column vector for the case that positive and negative capacities are the same,
       or, as two column array with positive plastic capacities in the first column
       and negative plastic capacities in the second (in absolute value) (signs matching Q!)
  NOTE: mixing of options (a) and (b) is not supported!</pre>
<!-- <div class="fragment"><pre class="comment">PLASTICANALYSIS_wUBT collapse load factor and deformation increments by upper bound theorem of plastic analysis
  [LAMDAC,DUF,DVHP] = PLASTICANALYSIS_wUBT (AF,QPL,PREF,PCF)
  the function uses the upper bound theorem of plastic analysis
  to determine the collapse load factor LAMDAC, and the displacement and plastic deformation
  increments of the collapse mechanism DUF and DVHP, respectively,
  of a structural model under reference load vector PREF and force vector PCF at free dofs;
  the reference force vector PREF represents the load pattern to be factored, while
  the force vector PFC represents the load pattern that remains unfactored;
  for the sign of PFU note that the equilibrium equations are: lambda Pref + Pcf = Bf Q;
  there are two options for supplying the kinematic matrix Af:
  (a) as data structure Model with information about the structural model, that is used
      to set up the kinematic matrix Af of the structure automatically, or
  (b) as nq by nf matrix where nq = total number of deformations and nf = no of free dofs;
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
<li><a href="../../../latest/Introspection/Structure/A_matrix" class="code" title="function A = A_matrix (Model)">A_matrix</a>	A_MATRIX kinematic matrix of structural model with 2d/3d truss and 2d frame elements</li></ul>
This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Sun 20-Dec-2020 19:28:50 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->