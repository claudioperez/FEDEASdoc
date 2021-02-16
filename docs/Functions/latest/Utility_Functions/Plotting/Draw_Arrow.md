---
title: "Draw_Arrow"
id: "Draw_Arrow"
description: "DRAW_ARROW draws 2d or 3d arrow"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href="#">Utility_Functions</a> &gt; <a href=".autoindex.md">Plotting</a> &gt; 
<!-- Draw_Arrow.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../.autoindex.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Utility_Functions\Plotting&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `Draw_Arrow`



## <a name="_name"></a>Purpose


DRAW_ARROW draws 2d or 3d arrow

<!-- <div class="box"><strong>DRAW_ARROW draws 2d or 3d arrow</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function varargout = Draw_Arrow (Astr,Aend,Aln,PlotOpt)` 

## Description


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
</ul>

This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="Label_Model.md" class="code" title="function Label_Model (Model,LblOpt)">Label_Model</a>	LABEL_MODEL displays element and node numbers and global axes in the current window</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->