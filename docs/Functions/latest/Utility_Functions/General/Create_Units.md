
<!-- <a name="_top"></a>
<div><a href="../../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="#">Utility_Functions</a> &gt; <a href="_index.md">General</a> &gt; Create_Units.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../_index.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Utility_Functions\General&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `Create_Units`
<!-- <h1>Create_Units
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

CREATE_UNITS create time, length, mass and force units

<!-- <div class="box"><strong>CREATE_UNITS create time, length, mass and force units</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function Units = Create_Units (UnOption)` 
## <a name="_description"></a>Description

<pre class="comment">CREATE_UNITS create time, length, mass and force units
  UNITS = CREATE_UNITS (UNOPTION)
  the function creates the data structure UNITS with time, length, mass and force units
  including the value of the acceleration of gravity g for both the SI and the U.S. system;
  the optional input argument UNOPTION specifies the unit system to select for unit values:
  UNOPTION = 'US' means that sec, in and kip have unit value for deriving the remaining units
  UNOPTION = 'SI' means that sec, m and kg   have unit value for deriving the remaining units</pre>
<!-- <div class="fragment"><pre class="comment">CREATE_UNITS create time, length, mass and force units
  UNITS = CREATE_UNITS (UNOPTION)
  the function creates the data structure UNITS with time, length, mass and force units
  including the value of the acceleration of gravity g for both the SI and the U.S. system;
  the optional input argument UNOPTION specifies the unit system to select for unit values:
  UNOPTION = 'US' means that sec, in and kip have unit value for deriving the remaining units
  UNOPTION = 'SI' means that sec, m and kg   have unit value for deriving the remaining units</pre></div> -->

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