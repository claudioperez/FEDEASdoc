---
title: "BbariBbarx_matrix"
id: "BbariBbarx_matrix"
description: "BBARIBBARX_MATRIX force influence matrices of primary structure from equilibrium matrix Bf"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">General_Functions</a> &gt; 
<!-- BbariBbarx_matrix.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\General_Functions&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `BbariBbarx_matrix`



## <a name="_name"></a>Purpose


BBARIBBARX_MATRIX force influence matrices of primary structure from equilibrium matrix Bf

<!-- <div class="box"><strong>BBARIBBARX_MATRIX force influence matrices of primary structure from equilibrium matrix Bf</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [Bbari,Bbarx,ind_x] = BbariBbarx_matrix (Bf,ind_r,ind_rng)` 

## Description


<pre class="comment">BBARIBBARX_MATRIX force influence matrices of primary structure from equilibrium matrix Bf
  [BBARI,BBARX,IND_X] = BBARIBBARX_MATRIX (BF,IND_R,IND_RNG)
  the function determines the force influence matrices BBARI and BBARX
  of the primary structure from the equilibrium matrix BF;
  the optional argument IND_R specifies the index for the selected redundant basic forces;
  the optional argument IND_RNG selects the redundant basic forces among those in the group;
  BBARI is the force influence matrix for the applied forces at the free dofs,
  and BBARX is the force influence matrix for the redundant basic forces;
  IND_X is the redundant force index vector into the basic forces of the structure</pre>
<!-- <div class="fragment"><pre class="comment">BBARIBBARX_MATRIX force influence matrices of primary structure from equilibrium matrix Bf
  [BBARI,BBARX,IND_X] = BBARIBBARX_MATRIX (BF,IND_R,IND_RNG)
  the function determines the force influence matrices BBARI and BBARX
  of the primary structure from the equilibrium matrix BF;
  the optional argument IND_R specifies the index for the selected redundant basic forces;
  the optional argument IND_RNG selects the redundant basic forces among those in the group;
  BBARI is the force influence matrix for the applied forces at the free dofs,
  and BBARX is the force influence matrix for the redundant basic forces;
  IND_X is the redundant force index vector into the basic forces of the structure</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="../../latest/Solution_Scripts/S_ForceMethod.md" class="code" title="">S_ForceMethod</a>	% S_FORCEMETHOD script for force method of structural analysis</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->