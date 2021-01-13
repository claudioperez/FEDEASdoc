
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Introspection</a> &gt; <a href="_index.md">Structure</a> &gt; Q0_vector.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Introspection\Structure&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `Q0_vector`
<!-- <h1>Q0_vector
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

Q0_VECTOR initial (fixed-end) force vector for structural model

<!-- <div class="box"><strong>Q0_VECTOR initial (fixed-end) force vector for structural model</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function Q0 = Q0_vector (Model,ElemData)` 
## <a name="_description"></a>Description

<pre class="comment">Q0_VECTOR initial (fixed-end) force vector for structural model
  Q0 = Q0_VECTOR (MODEL,ELEMDATA)
  the function sets up the initial (fixed-end) force vector Q0 for the structural model
  specified in data structure MODEL with element property information in cell array ELEMDATA</pre>
<!-- <div class="fragment"><pre class="comment">Q0_VECTOR initial (fixed-end) force vector for structural model
  Q0 = Q0_VECTOR (MODEL,ELEMDATA)
  the function sets up the initial (fixed-end) force vector Q0 for the structural model
  specified in data structure MODEL with element property information in cell array ELEMDATA</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="../../../latest/Introspection/Frame/ElmLenOr" class="code" title="function [L,dcx] = ElmLenOr (xyz)">ElmLenOr</a>	ELMLENOR element length and x-axis orientation (direction cosines)</li><li><a href="../../../latest/Introspection/Frame/Localize" class="code" title="function [xyz,id] = Localize (Model,el)">Localize</a>	LOCALIZE returns the node coordinates and id array of element</li></ul>
This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Sun 20-Dec-2020 19:28:50 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->