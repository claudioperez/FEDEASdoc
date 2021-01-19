
<!-- <a name="_top"></a>
<div><a href="../../index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="index.md">Introspection</a> &gt; BbariBbarx_matrix.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for latest\Introspection&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `BbariBbarx_matrix`
<!-- <h1>BbariBbarx_matrix
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

BBARIBBARX_MATRIX force influence matrices of primary structure from equilibrium matrix Bf

<!-- <div class="box"><strong>BBARIBBARX_MATRIX force influence matrices of primary structure from equilibrium matrix Bf</strong></div> -->

## <a name="_synopsis"></a>Syntax

`function [Bbari,Bbarx,ind_x] = BbariBbarx_matrix (Bf,ind_r)` 
## <a name="_description"></a>Description

<pre class="comment">BBARIBBARX_MATRIX force influence matrices of primary structure from equilibrium matrix Bf
  [BBARI,BBARX,IND_X] = BBARIBBARX_MATRIX (BF,IND_R)
  the function determines the force influence matrices BBARI and BBARX
  of the primary structure from the equilibrium matrix BF at the free DOFs;
  the optional argument IND_R specifies the index for the selected redundant basic forces;
  BBARI is the force influence matrix for the applied forces at the free DOFs,
  and BBARX is the force influence matrix for the redundant basic forces;
  IND_X is the redundant force index vector into the basic forces of the structure</pre>
<!-- <div class="fragment"><pre class="comment">BBARIBBARX_MATRIX force influence matrices of primary structure from equilibrium matrix Bf
  [BBARI,BBARX,IND_X] = BBARIBBARX_MATRIX (BF,IND_R)
  the function determines the force influence matrices BBARI and BBARX
  of the primary structure from the equilibrium matrix BF at the free DOFs;
  the optional argument IND_R specifies the index for the selected redundant basic forces;
  BBARI is the force influence matrix for the applied forces at the free DOFs,
  and BBARX is the force influence matrix for the redundant basic forces;
  IND_X is the redundant force index vector into the basic forces of the structure</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Sat 19-Dec-2020 21:58:36 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->