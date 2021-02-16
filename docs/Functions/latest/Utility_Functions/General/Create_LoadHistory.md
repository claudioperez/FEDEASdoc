
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Utility_Functions</a> &gt; <a href="_index.md">General</a> &gt; Create_LoadHistory.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Utility_Functions\General&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `Create_LoadHistory`
<!-- <h1>Create_LoadHistory
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

CREATE_LOADHIST generate time and value pairs of a displacement cycle with normal force

<!-- <div class="box"><strong>CREATE_LOADHIST generate time and value pairs of a displacement cycle with normal force</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function LoadHist = Create_LoadHistory (RevVal,LHCase,T_Rev)` 
## <a name="_description"></a>Description

<pre class="comment">CREATE_LOADHIST generate time and value pairs of a displacement cycle with normal force    
  LOADHIST = CREATE_LOADHIST (REVVAL,LHCASE,T_REV)
  the function creates load history time and value pairs in fields Time and Value of the
  structure LOADHIST, respectively; the row vector REVVAL contains the load reversal values
  and the variable T_REV the period of reversals;
  the character variable LHCASE supports two cases:
  'A' stands for the case that the Nth reversal occurs at N*T_REV,
  'B' stands for the case that the reversal times are adjusted so that the rate of change
  for the load value is constant between reversals</pre>
<!-- <div class="fragment"><pre class="comment">CREATE_LOADHIST generate time and value pairs of a displacement cycle with normal force    
  LOADHIST = CREATE_LOADHIST (REVVAL,LHCASE,T_REV)
  the function creates load history time and value pairs in fields Time and Value of the
  structure LOADHIST, respectively; the row vector REVVAL contains the load reversal values
  and the variable T_REV the period of reversals;
  the character variable LHCASE supports two cases:
  'A' stands for the case that the Nth reversal occurs at N*T_REV,
  'B' stands for the case that the reversal times are adjusted so that the rate of change
  for the load value is constant between reversals</pre></div> -->

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