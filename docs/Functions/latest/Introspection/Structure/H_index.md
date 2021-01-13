
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Introspection</a> &gt; <a href="_index.md">Structure</a> &gt; H_index.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Introspection\Structure&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `H_index`
<!-- <h1>H_index
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

H_INDEX cell array of indices into structure arrays for continuous element deformations

<!-- <div class="box"><strong>H_INDEX cell array of indices into structure arrays for continuous element deformations</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function iced = H_index (Model,ElemData)` 
## <a name="_description"></a>Description

<pre class="comment">H_INDEX cell array of indices into structure arrays for continuous element deformations
  ICED = H_INDEX (MODEL,ELEMDATA)
  the function sets up the cell array ICED of indices for continuous element deformations
  based on release information for elements of the structural model in data structure MODEL;
  the location of element releases is specified in field RELEASE of cell array ELEMDATA
  ELEMDATA{2}.RELEASE = [0;1;0] :   a flexural release is present at end i of element 2
  ELEMDATA{3}.RELEASE = [1;0;1] : an axial and a flexural release at end j of element 3
  the function supports only truss and 2d frame elements at present</pre>
<!-- <div class="fragment"><pre class="comment">H_INDEX cell array of indices into structure arrays for continuous element deformations
  ICED = H_INDEX (MODEL,ELEMDATA)
  the function sets up the cell array ICED of indices for continuous element deformations
  based on release information for elements of the structural model in data structure MODEL;
  the location of element releases is specified in field RELEASE of cell array ELEMDATA
  ELEMDATA{2}.RELEASE = [0;1;0] :   a flexural release is present at end i of element 2
  ELEMDATA{3}.RELEASE = [1;0;1] : an axial and a flexural release at end j of element 3
  the function supports only truss and 2d frame elements at present</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Sun 20-Dec-2020 19:28:50 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->