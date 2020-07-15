
<!-- <a name="_top"></a>
<div><a href="../../../../../index.md">Home</a> &gt;  <a href="#">..</a> &gt; <a href="#">..</a> &gt; <a href="#">FEDEASLab</a> &gt; <a href="#">src</a> &gt; <a href="index.md">Other</a> &gt; Plot_SingularModes.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../../../index.md"><img alt="<" border="0" src="../../../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for ..\..\FEDEASLab\src\Other&nbsp;<img alt=">" border="0" src="../../../../../right.png"></a></td></tr></table>-->
# `Plot_SingularModes`
<!-- <h1>Plot_SingularModes
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->



<!-- <div class="box"><strong></strong></div> -->

## <a name="_synopsis"></a>Syntax

`This is a script file.` 
## <a name="_description"></a>Description

<pre class="comment"></pre>
<!-- <div class="fragment"><pre class="comment"></pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../../../../matlabicon.gif)">
</ul>
<!-- crossreference -->



<h2><a name="_source"></a>SOURCE CODE</h2>
<div class="fragment"><pre>0001 [U,S,V] = svds(State.Kf);
0002 
0003 PlotOpt.MAGF = 10;                 <span class="comment">% magnification factor for deformed configuration</span>
0004 Create_Window (WinXr,WinYr);       <span class="comment">% open figure window</span>
0005 Plot_Model(Model);
0006 Plot_Model(Model,U(:,1));
0007 
0008 Create_Window (WinXr,WinYr);       <span class="comment">% open figure window</span>
0009 Plot_Model(Model);
0010 Plot_Model(Model,U(:,2));
0011 
0012 Create_Window (WinXr,WinYr);       <span class="comment">% open figure window</span>
0013 Plot_Model(Model);
0014 Plot_Model(Model,U(:,3));</pre></div>
<!-- <hr><address>Generated on Wed 15-Jul-2020 00:16:13 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->