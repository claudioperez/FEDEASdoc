<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
                "http://www.w3.org/TR/REC-html40/loose.dtd">
<html>

<body>
<a name="_top"></a>
<div><a href="../FEDEASLab/">Home</a> &gt;  <a href="FEDEASLab/">Element_Library</a> &gt; Check3dFrmAxes.m</div>

<!--<table width="100%"><tr><td align="left"><a href="../FEDEASLab/"><img alt="<" border="0" src="../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="FEDEASLab/">Index for Element_Library&nbsp;<img alt=">" border="0" src="../right.png"></a></td></tr></table>-->

<h1>Check3dFrmAxes
</h1>

<h2><a name="_name"></a>PURPOSE <a href="#_top"><img alt="^" border="0" src="../up.png"></a></h2>
<div class="box"><strong>CHECK3dFRMAXES check that y-axis is not co-linear with element chord</strong></div>

<h2><a name="_synopsis"></a>SYNOPSIS <a href="#_top"><img alt="^" border="0" src="../up.png"></a></h2>
<div class="box"><strong>function y = Check3dFrmAxes (el,y,xyz) </strong></div>

<h2><a name="_description"></a>DESCRIPTION <a href="#_top"><img alt="^" border="0" src="../up.png"></a></h2>
<div class="fragment"><pre >CHECK3dFRMAXES check that y-axis is not co-linear with element chord
  Y = CHECK3dFRMAXES(EL,Y,XYZ)
  the function checks that the specified Y-axis for the element EL 
  with end node coordinates XYZ is not colinear with the element chord;
  if colinearity is detected, the function returns a unit vector in the global
  Y- or Z-axis and issues a warning message with information about the change;
  if not, the function returns the normalized vector Y</pre></div>

<!-- crossreference -->
<h2><a name="_cross"></a>CROSS-REFERENCE INFORMATION <a href="#_top"><img alt="^" border="0" src="../up.png"></a></h2>
This function calls:
<ul style="list-style-image:url(../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../matlabicon.gif)">
<li><a href="LE3dFrm/" class="code" title="function ElemResp = LE3dFrm (action,el_no,xyz,ElemData,ElemState)">LE3dFrm</a>	LE3dFRM 3d linear frame element under linear or nonlinear geometry</li></ul>
<!-- crossreference -->




<hr><address>Generated on Wed 22-Jan-2020 08:42:48 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address>
</body>
</html>