
<!-- <a name="_top"></a>
<div><a href="../../../index.md">Home</a> &gt;  <a href="#">src</a> &gt; <a href="../index.md">Utilities</a> &gt; <a href="index.md">PreProcessing</a> &gt; Create_MRFrame.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for src\Utilities\PreProcessing&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `Create_MRFrame`
<!-- <h1>Create_MRFrame
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

CREATE_FRAME generation of nodes and elements for regular N-story, M-bay MR frame

<!-- <div class="box"><strong>CREATE_FRAME generation of nodes and elements for regular N-story, M-bay MR frame</strong></div> -->

## <a name="_synopsis"></a>Syntax

`function Frame = Create_MRFrame (Lbv,Hsv,nsub)` 
## <a name="_description"></a>Description

<pre class="comment">CREATE_FRAME generation of nodes and elements for regular N-story, M-bay MR frame    
 FRAME = CREATE_MRFRAME (LBV,HSV,NSUB)
  function generates the node coordinates XYZ and element connectivity CON
  for a regular N-story, M-bay frame with bay spans in row vector LBV and
  story heights in row vector HSV; the optional row vector NSUB specifies
  the number of subelements for each frame girder 
  the function returns the generated information in data structure FRAME
  with fields XYZ (node coordinates), CON (element connectivity),
  CINDX (column index by story), GINDX (girder index by floor),
  NBY (no of bays), NST (no of stories), NC (no of columns), NG (no of girders)
  NN (no of nodes), NE (no of elements)</pre>
<!-- <div class="fragment"><pre class="comment">CREATE_FRAME generation of nodes and elements for regular N-story, M-bay MR frame    
 FRAME = CREATE_MRFRAME (LBV,HSV,NSUB)
  function generates the node coordinates XYZ and element connectivity CON
  for a regular N-story, M-bay frame with bay spans in row vector LBV and
  story heights in row vector HSV; the optional row vector NSUB specifies
  the number of subelements for each frame girder 
  the function returns the generated information in data structure FRAME
  with fields XYZ (node coordinates), CON (element connectivity),
  CINDX (column index by story), GINDX (girder index by floor),
  NBY (no of bays), NST (no of stories), NC (no of columns), NG (no of girders)
  NN (no of nodes), NE (no of elements)</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="../../../src/Other/Create_PanelZone.md" class="code" title="">Create_PanelZone</a>	% Clear memory and close any open windows</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Tue 14-Jul-2020 22:59:26 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->