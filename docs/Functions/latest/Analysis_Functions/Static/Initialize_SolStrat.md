---
title: "Initialize_SolStrat"
id: "Initialize_SolStrat"
description: "INITIALIZE_SOLSTRAT default values for most solution strategy parameters"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href="#">Analysis_Functions</a> &gt; <a href=".autoindex.md">Static</a> &gt; 
<!-- Initialize_SolStrat.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../.autoindex.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Analysis_Functions\Static&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `Initialize_SolStrat`



## <a name="_name"></a>Purpose


INITIALIZE_SOLSTRAT default values for most solution strategy parameters

<!-- <div class="box"><strong>INITIALIZE_SOLSTRAT default values for most solution strategy parameters</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function SolStrat = Initialize_SolStrat` 

## Description


<pre class="comment">INITIALIZE_SOLSTRAT default values for most solution strategy parameters
  SOLSTRAT = INITIALIZE_SOLSTRAT
  the function assigns default values to most solution strategy parameters and creates
  the data structure SOLSTRAT with corresponding information;
  SOLSTRAT contains three substructures: INCRSTRAT, ITERSTRAT and TIMESTRAT;
  these data structures contain the following fields
  INCRSTRAT
           Dlam0    = initial load factor increment(s) (row vector)
           Deltat   = pseudo-time increment (scalar)
           StifUpdt = stiffness update (character variable)
           LFCtrl   = load control (character variable)
           LCType   = load control type
           gamma    = exponent of current stiffness parameter method of load control
  ITERSTRAT
           StifUpdt = stiffness update (character variable)
           Type     = 'NR', 'ModNR', 'Krylov', 'LnSrch'
           LFCtrl   = load control (character variable)
           LCType   = load control type
           LCParam  = load control parameters
           maxiter  = maximum number of iterations for equilibrium (scalar)
           tol      = tolerance for satifaction of equilibrium equations (scalar)
  TIMESTRAT
           Delta    = time step of transient analysis (scalar)
           Type     = type of numerical integration (character variable)
           Param    = parameters of numerical time integration scheme (row vector)</pre>
<!-- <div class="fragment"><pre class="comment">INITIALIZE_SOLSTRAT default values for most solution strategy parameters
  SOLSTRAT = INITIALIZE_SOLSTRAT
  the function assigns default values to most solution strategy parameters and creates
  the data structure SOLSTRAT with corresponding information;
  SOLSTRAT contains three substructures: INCRSTRAT, ITERSTRAT and TIMESTRAT;
  these data structures contain the following fields
  INCRSTRAT
           Dlam0    = initial load factor increment(s) (row vector)
           Deltat   = pseudo-time increment (scalar)
           StifUpdt = stiffness update (character variable)
           LFCtrl   = load control (character variable)
           LCType   = load control type
           gamma    = exponent of current stiffness parameter method of load control
  ITERSTRAT
           StifUpdt = stiffness update (character variable)
           Type     = 'NR', 'ModNR', 'Krylov', 'LnSrch'
           LFCtrl   = load control (character variable)
           LCType   = load control type
           LCParam  = load control parameters
           maxiter  = maximum number of iterations for equilibrium (scalar)
           tol      = tolerance for satifaction of equilibrium equations (scalar)
  TIMESTRAT
           Delta    = time step of transient analysis (scalar)
           Type     = type of numerical integration (character variable)
           Param    = parameters of numerical time integration scheme (row vector)</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>

This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="../../../latest/Solution_Scripts/S_MomCurvAnalysis.md" class="code" title="">S_MomCurvAnalysis</a>	% S_MOMCURVANALYSIS script for moment-curvature analysis under constant axial force</li><li><a href="../../../latest/Solution_Scripts/S_NMAnalysis.md" class="code" title="">S_NMAnalysis</a>	% S_NMANALYSIS script for incremental application of N-M pair on section</li><li><a href="../../../latest/Solution_Scripts/S_NMAnalysiswSepLoadHist.md" class="code" title="">S_NMAnalysiswSepLoadHist</a>	% S_NMANALYSISwSEPLOADHIST script for application N and M with separate load histories</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->