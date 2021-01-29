
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Utility_Functions</a> &gt; <a href="_index.md">Plotting</a> &gt; Get_HngPos4DefoElem.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Utility_Functions\Plotting&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `Get_HngPos4DefoElem`
<!-- <h1>Get_HngPos4DefoElem
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

GET_HNGPOS4DEFOELEM determine axial and flexural hinge position for deformed element

<!-- <div class="box"><strong>GET_HNGPOS4DEFOELEM determine axial and flexural hinge position for deformed element</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [AxHngCoor,FlHngCoor] = Get_HngPos4DefoElem (XYiod,XYjod,xyd,HngOpt)` 
## <a name="_description"></a>Description

<pre class="comment">GET_HNGPOS4DEFOELEM determine axial and flexural hinge position for deformed element
  [AXHNGCOOR,FLHNGCOOR] = GET_HNGPOS4DEFOELEM(XYIOD,XYJOD,XYD,HNGOPT)
  the function determines the axial hinge coordinates AXHNGCOOR and the
  flexural hinge coordinates FLHNGCOOR for a deformed truss or frame element
  from the end node coordinates XYIOD and XYJOD of the deformed configuration
  and the local deformed coordinates XYD of the deformed shape;
  the data structure HNGOPT has the fields HngSz for the hinge size and
  HngOf for the offset of the hinge location from the element end</pre>
<!-- <div class="fragment"><pre class="comment">GET_HNGPOS4DEFOELEM determine axial and flexural hinge position for deformed element
  [AXHNGCOOR,FLHNGCOOR] = GET_HNGPOS4DEFOELEM(XYIOD,XYJOD,XYD,HNGOPT)
  the function determines the axial hinge coordinates AXHNGCOOR and the
  flexural hinge coordinates FLHNGCOOR for a deformed truss or frame element
  from the end node coordinates XYIOD and XYJOD of the deformed configuration
  and the local deformed coordinates XYD of the deformed shape;
  the data structure HNGOPT has the fields HngSz for the hinge size and
  HngOf for the offset of the hinge location from the element end</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->