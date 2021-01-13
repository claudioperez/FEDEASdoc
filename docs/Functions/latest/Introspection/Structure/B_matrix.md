
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Introspection</a> &gt; <a href="_index.md">Structure</a> &gt; B_matrix.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Introspection\Structure&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `B_matrix`
<!-- <h1>B_matrix
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

B_MATRIX equilibrium matrix of structural model with 2d/3d truss and 2d frame elements

<!-- <div class="box"><strong>B_MATRIX equilibrium matrix of structural model with 2d/3d truss and 2d frame elements</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function B = B_matrix (Model)` 
## <a name="_description"></a>Description

<pre class="comment">B_MATRIX equilibrium matrix of structural model with 2d/3d truss and 2d frame elements
  B = B_MATRIX (MODEL)
  the function forms the equilibrium matrix B for all degrees of freedom (DOFs) and
  all basic forces of the structural model specified in data structure MODEL;
  this version is limited to 2d/3d truss and 2d frame elements</pre>
<!-- <div class="fragment"><pre class="comment">B_MATRIX equilibrium matrix of structural model with 2d/3d truss and 2d frame elements
  B = B_MATRIX (MODEL)
  the function forms the equilibrium matrix B for all degrees of freedom (DOFs) and
  all basic forces of the structural model specified in data structure MODEL;
  this version is limited to 2d/3d truss and 2d frame elements</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="../../../latest/Introspection/Frame/ElmLenOr" class="code" title="function [L,dcx] = ElmLenOr (xyz)">ElmLenOr</a>	ELMLENOR element length and x-axis orientation (direction cosines)</li><li><a href="../../../latest/Introspection/Frame/Localize" class="code" title="function [xyz,id] = Localize (Model,el)">Localize</a>	LOCALIZE returns the node coordinates and id array of element</li></ul>
This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="../../../latest/Solution_Library/Plastic_Analysis/PlasticAnalysis_wLBT.md" class="code" title="function [lamdac,Qc] = PlasticAnalysis_wLBT (Bf,Qpl,Pref,Pcf,Options)">PlasticAnalysis_wLBT</a>	PLASTICANALYSIS_wLBT collapse load factor and basic element forces by lower bound theorem of plastic analysis</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Sun 20-Dec-2020 19:28:50 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->