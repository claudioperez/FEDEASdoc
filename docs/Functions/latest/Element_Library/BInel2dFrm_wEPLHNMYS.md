---
title: "BInel2dFrm_wEPLHNMYS"
id: "BInel2dFrm_wEPLHNMYS"
description: "BINELP2dFRM_WEPLHNMYS 2d elasto-plastic, linear hardening basic frame element"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">Element_Library</a> &gt; 
<!-- BInel2dFrm_wEPLHNMYS.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Element_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `BInel2dFrm_wEPLHNMYS`



## <a name="_name"></a>Purpose


BINELP2dFRM_WEPLHNMYS 2d elasto-plastic, linear hardening basic frame element

<!-- <div class="box"><strong>BINELP2dFRM_WEPLHNMYS 2d elasto-plastic, linear hardening basic frame element</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function BElemResp = BInel2dFrm_wEPLHNMYS (action,L,BElemData,BElemState)` 

## Description


<pre class="comment">BINELP2dFRM_WEPLHNMYS 2d elasto-plastic, linear hardening basic frame element
  BELEMRESP = BINELP2dFRM_WEPLHNMYS (ACTION,L,BELEMDATA,BELEMSTATE)
  the function determines the 2d response of an elasto-plastic basic frame element of length L 
  with elasto-plastic behavior with linear isotropic and kinematic hardening
  under axial force (N) - bending moment (M) interaction at two plastic hinges at ends i and j
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  When the character variable ACTION has one of the following values,
  the function performs the listed operations and returns the results in BELEMRESP:
  ACTION = 'chec': check element property data for omissions and assign default values
           'init': initialize element history variables
           'forc': report basic element forces
           'stif': report basic element stiffness matrix and basic element forces
           'post': report post-processing information
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The data structure BELEMRESP stands for the following data object(s) for each ACTION:
  BELEMRESP = BELEMDATA    for action = 'chec'
  BELEMRESP = BELEMSTATE   for action = 'init'
  BELEMRESP = BELEMSTATE   for action = 'stif'
  BELEMRESP = BELEMSTATE   for action = 'forc'
  BELEMRESP = BELEMPOST    for action = 'post'
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  BELEMDATA is a data structure with basic element property information; it has the fields
         E   = Young's Modulus
         A   = cross-sectional area
         I   = moment of inertia
         Np  = plastic axial capacity
         Nb  = axial force at balance point (default = 0)
         Mp  = plastic moment capacity at plastic hinges near ends i, j ( Mp = [Mpi , Mpj] )
         Hir = isotropic plastic modulus ratio (default = [ 0 0 ] )
         Hkr = kinematic modulus ratio (default = [ 0 0 0 ] )
         w   = uniformly distributed element load [wx;wy] (default = [ 0 0 ] )
         GPYSC = coefficients for polynomial yield surface
                 (default = [ 1.2 2 0 ; 1 0 2 ; 3.5 2 2 ; -1 0 0 ] )
         YFtol = yield criterion tolerance (default = 1e-12)
         Wtol  = work tolerance for return map algorithm (default = 1e-16)
         MaxIter = max no of iterations for return map algorithm (default = 15)         
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  BELEMSTATE is a data structure with the current basic element state; it has the fields
         v     = vector of total element deformations
         ke    = basic element stiffness matrix; updated under ACTION = 'stif'
         q     = basic element forces; updated under ACTION = 'stif' or 'forc'
         Past  = element history variables at last converged state
         Pres  = current element history variables
         the element history variables of this element are
             ehp   = plastic hinge   deformations   (2x2 array)
             vp    = plastic element deformations   (3x1 array)
             qbk   = element back forces            (3x1 array)
             alpha = isotropic hardening variable   (2x1 array)</pre>
<!-- <div class="fragment"><pre class="comment">BINELP2dFRM_WEPLHNMYS 2d elasto-plastic, linear hardening basic frame element
  BELEMRESP = BINELP2dFRM_WEPLHNMYS (ACTION,L,BELEMDATA,BELEMSTATE)
  the function determines the 2d response of an elasto-plastic basic frame element of length L 
  with elasto-plastic behavior with linear isotropic and kinematic hardening
  under axial force (N) - bending moment (M) interaction at two plastic hinges at ends i and j
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  When the character variable ACTION has one of the following values,
  the function performs the listed operations and returns the results in BELEMRESP:
  ACTION = 'chec': check element property data for omissions and assign default values
           'init': initialize element history variables
           'forc': report basic element forces
           'stif': report basic element stiffness matrix and basic element forces
           'post': report post-processing information
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The data structure BELEMRESP stands for the following data object(s) for each ACTION:
  BELEMRESP = BELEMDATA    for action = 'chec'
  BELEMRESP = BELEMSTATE   for action = 'init'
  BELEMRESP = BELEMSTATE   for action = 'stif'
  BELEMRESP = BELEMSTATE   for action = 'forc'
  BELEMRESP = BELEMPOST    for action = 'post'
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  BELEMDATA is a data structure with basic element property information; it has the fields
         E   = Young's Modulus
         A   = cross-sectional area
         I   = moment of inertia
         Np  = plastic axial capacity
         Nb  = axial force at balance point (default = 0)
         Mp  = plastic moment capacity at plastic hinges near ends i, j ( Mp = [Mpi , Mpj] )
         Hir = isotropic plastic modulus ratio (default = [ 0 0 ] )
         Hkr = kinematic modulus ratio (default = [ 0 0 0 ] )
         w   = uniformly distributed element load [wx;wy] (default = [ 0 0 ] )
         GPYSC = coefficients for polynomial yield surface
                 (default = [ 1.2 2 0 ; 1 0 2 ; 3.5 2 2 ; -1 0 0 ] )
         YFtol = yield criterion tolerance (default = 1e-12)
         Wtol  = work tolerance for return map algorithm (default = 1e-16)
         MaxIter = max no of iterations for return map algorithm (default = 15)         
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  BELEMSTATE is a data structure with the current basic element state; it has the fields
         v     = vector of total element deformations
         ke    = basic element stiffness matrix; updated under ACTION = 'stif'
         q     = basic element forces; updated under ACTION = 'stif' or 'forc'
         Past  = element history variables at last converged state
         Pres  = current element history variables
         the element history variables of this element are
             ehp   = plastic hinge   deformations   (2x2 array)
             vp    = plastic element deformations   (3x1 array)
             qbk   = element back forces            (3x1 array)
             alpha = isotropic hardening variable   (2x1 array)</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="/Functions/ElementLoading" class="code" title="function wC = ElementLoading (w0,lamda,LdId)">ElementLoading</a>	ELEMENTLOADING determines current distributed element load value</li><li><a href="/Functions/GPYS" class="code" title="function [f,g,h] = GPYS (GPYSC,xyz,ScVec)">GPYS</a>	GPYS function value, gradient and Hessian of polynomial yield surface</li></ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->