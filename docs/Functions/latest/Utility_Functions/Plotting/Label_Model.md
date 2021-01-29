
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Utility_Functions</a> &gt; <a href="_index.md">Plotting</a> &gt; Label_Model.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Utility_Functions\Plotting&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `Label_Model`
<!-- <h1>Label_Model
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

LABEL_MODEL displays element and node numbers and global axes in the current window

<!-- <div class="box"><strong>LABEL_MODEL displays element and node numbers and global axes in the current window</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function Label_Model (Model,LblOpt)` 
## <a name="_description"></a>Description

<pre class="comment">LABEL_MODEL displays element and node numbers and global axes in the current window   
  LABEL_MODEL (MODEL,LBLOPT)
  the function displays in the current window labels for nodes and elements,
  and the global coordinate axes;
  LBLOPT is an optional data structure controlling the display;
  in its absense the function plots all items with default values;
  LBLOPT has the following fields (all optional)
    Item : character variable with values 'node','elem', 'axes' (default='all')
    FntSF: font magnification factor (default = 1)
    AxsSF: axis arrow length magnification factor (default = 1)
    LOfSF: node and element label offset magnification factor (default = 1)
    NList: list of nodes    to label (default all nodes    in the model)
    EList: list of elements to label (default all elements in the model)</pre>
<!-- <div class="fragment"><pre class="comment">LABEL_MODEL displays element and node numbers and global axes in the current window   
  LABEL_MODEL (MODEL,LBLOPT)
  the function displays in the current window labels for nodes and elements,
  and the global coordinate axes;
  LBLOPT is an optional data structure controlling the display;
  in its absense the function plots all items with default values;
  LBLOPT has the following fields (all optional)
    Item : character variable with values 'node','elem', 'axes' (default='all')
    FntSF: font magnification factor (default = 1)
    AxsSF: axis arrow length magnification factor (default = 1)
    LOfSF: node and element label offset magnification factor (default = 1)
    NList: list of nodes    to label (default all nodes    in the model)
    EList: list of elements to label (default all elements in the model)</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="Draw_Arrow" class="code" title="function varargout = Draw_Arrow (Astr,Aend,Aln,PlotOpt)">Draw_Arrow</a>	DRAW_ARROW draws 2d or 3d arrow</li><li><a href="Get_ModelScale" class="code" title="function [ModSc,maxL,minL] = Get_ModelScale (Model,Ratio)">Get_ModelScale</a>	GET_MODELSCALE determines maximum and minimum element length in Model</li></ul>
This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->