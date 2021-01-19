
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Utilities</a> &gt; <a href="_index.md">Plotting</a> &gt; Draw_Arrow.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Utilities\Plotting&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `Draw_Arrow`
<!-- <h1>Draw_Arrow
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

DRAW_ARROW draws 2d or 3d arrow

<!-- <div class="box"><strong>DRAW_ARROW draws 2d or 3d arrow</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function varargout = Draw_Arrow (Astr,Aend,Aln,PlotOpt)` 
## <a name="_description"></a>Description

<pre class="comment">DRAW_ARROW draws 2d or 3d arrow
  AEND = DRAW_ARROW (ASTR,AEND,ALN,PLOTOPT)
  the function draws an arrow with starting point ASTR and end point AEND, if ALN is empty;
  if ALN is specified, then it represents the arrow length
  with AEND interpreted as the arrow direction; in this case the function returns
  the end point coordinates of the arrow in vector AEND
  PLOTOPT is a data structure for controlling the arrow display with the following fields:
         TipSF: scale factor for controlling the size of the arrow tip (default = 1);
         ArWth: line width of arrow shaft (default = 1);
         ArClr: color of arrow shaft and tip (default = 'k');
         AbsSF: true or false to indicate absolute or relative to arrow length scaling</pre>
<!-- <div class="fragment"><pre class="comment">DRAW_ARROW draws 2d or 3d arrow
  AEND = DRAW_ARROW (ASTR,AEND,ALN,PLOTOPT)
  the function draws an arrow with starting point ASTR and end point AEND, if ALN is empty;
  if ALN is specified, then it represents the arrow length
  with AEND interpreted as the arrow direction; in this case the function returns
  the end point coordinates of the arrow in vector AEND
  PLOTOPT is a data structure for controlling the arrow display with the following fields:
         TipSF: scale factor for controlling the size of the arrow tip (default = 1);
         ArWth: line width of arrow shaft (default = 1);
         ArClr: color of arrow shaft and tip (default = 'k');
         AbsSF: true or false to indicate absolute or relative to arrow length scaling</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="../../../latest/Introspection/Frame/ElmLenOr" class="code" title="function [L,dcx] = ElmLenOr (xyz)">ElmLenOr</a>	ELMLENOR element length and x-axis orientation (direction cosines)</li></ul>
This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Sun 20-Dec-2020 19:28:50 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->