
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Utility_Functions</a> &gt; <a href="_index.md">Plotting</a> &gt; Get_ModelScale.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Utility_Functions\Plotting&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `Get_ModelScale`
<!-- <h1>Get_ModelScale
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

GET_MODELSCALE determines maximum and minimum element length in Model

<!-- <div class="box"><strong>GET_MODELSCALE determines maximum and minimum element length in Model</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [ModSc,maxL,minL] = Get_ModelScale (Model,Ratio)` 
## <a name="_description"></a>Description

<pre class="comment">GET_MODELSCALE determines maximum and minimum element length in Model
  [MODSC,MAXL,MINL] = GET_MODELSCALE(MODEL,RATIO)
  the function determines a critical scale for the structural model
  in data structure MODEL from the maximum distance MAXL and
  the minimum distance MINL between nodes i and j of line elements;
  the maximum distance MAXL is divided by RATIO (default = 1.5-0.5*MINL/MAXL);
  depending on the value of RATIO the model scale is equal
  to the largest (RATIO&lt;MAXL/MINL) or smallest distance (RATIO&gt;MAXL/MINL)</pre>
<!-- <div class="fragment"><pre class="comment">GET_MODELSCALE determines maximum and minimum element length in Model
  [MODSC,MAXL,MINL] = GET_MODELSCALE(MODEL,RATIO)
  the function determines a critical scale for the structural model
  in data structure MODEL from the maximum distance MAXL and
  the minimum distance MINL between nodes i and j of line elements;
  the maximum distance MAXL is divided by RATIO (default = 1.5-0.5*MINL/MAXL);
  depending on the value of RATIO the model scale is equal
  to the largest (RATIO&lt;MAXL/MINL) or smallest distance (RATIO&gt;MAXL/MINL)</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="Label_Model.md" class="code" title="function Label_Model (Model,LblOpt)">Label_Model</a>	LABEL_MODEL displays element and node numbers and global axes in the current window</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->