
<!-- <a name="_top"></a>
<div><a href="../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="_index.md">Element_Library</a> &gt; BInel2dFrm_wEPLHM.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../_index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Element_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `BInel2dFrm_wEPLHM`
<!-- <h1>BInel2dFrm_wEPLHM
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

BINELP2dFRM_WEPLHM 2d elasto-plastic, linear hardening basic frame element with hinge offsets

<!-- <div class="box"><strong>BINELP2dFRM_WEPLHM 2d elasto-plastic, linear hardening basic frame element with hinge offsets</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function BElemResp = BInel2dFrm_wEPLHM (action,L,BElemData,BElemState)` 
## <a name="_description"></a>Description

<pre class="comment">BINELP2dFRM_WEPLHM 2d elasto-plastic, linear hardening basic frame element with hinge offsets
  BELEMRESP = BINELP2dFRM_WEPLHM (ACTION,L,BELEMDATA,BELEMSTATE)
  the function determines the 2d response of an elasto-plastic basic frame element of length L 
  with linear elastic axial response and elasto-plasic flexural response
  with linear isotropic and kinematic hardening at two plastic hinges
  that may be offset from the element ends (series model)
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
         Mp  = plastic moment capacity at plastic hinges near ends i, j ( Mp = [Mpi , Mpj] )
         Hir = isotropic plastic modulus ratio
         Hkr = kinematic modulus ratio
         w   = uniformly distributed element load [wx;wy];
         YFtol = yield criterion tolerance (default = 1e-12)
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  BELEMSTATE is a data structure with the current basic element state; it has the fields
         v     = vector of total element deformations
         ke    = basic element stiffness matrix; updated under ACTION = 'stif'
         q     = basic element forces; updated under ACTION = 'stif' or 'forc'
         Past  = element history variables at last converged state
         Pres  = current element history variables
         the element history variables of this element are
             ehp   = plastic hinge   deformations   (2x1 array)
             vp    = plastic element deformations   (3x1 array)
             qbk   = flexural back forces           (2x1 array)
             alpha = isotropic hardening variable   (2x1 array)</pre>
<!-- <div class="fragment"><pre class="comment">BINELP2dFRM_WEPLHM 2d elasto-plastic, linear hardening basic frame element with hinge offsets
  BELEMRESP = BINELP2dFRM_WEPLHM (ACTION,L,BELEMDATA,BELEMSTATE)
  the function determines the 2d response of an elasto-plastic basic frame element of length L 
  with linear elastic axial response and elasto-plasic flexural response
  with linear isotropic and kinematic hardening at two plastic hinges
  that may be offset from the element ends (series model)
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
         Mp  = plastic moment capacity at plastic hinges near ends i, j ( Mp = [Mpi , Mpj] )
         Hir = isotropic plastic modulus ratio
         Hkr = kinematic modulus ratio
         w   = uniformly distributed element load [wx;wy];
         YFtol = yield criterion tolerance (default = 1e-12)
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  BELEMSTATE is a data structure with the current basic element state; it has the fields
         v     = vector of total element deformations
         ke    = basic element stiffness matrix; updated under ACTION = 'stif'
         q     = basic element forces; updated under ACTION = 'stif' or 'forc'
         Past  = element history variables at last converged state
         Pres  = current element history variables
         the element history variables of this element are
             ehp   = plastic hinge   deformations   (2x1 array)
             vp    = plastic element deformations   (3x1 array)
             qbk   = flexural back forces           (2x1 array)
             alpha = isotropic hardening variable   (2x1 array)</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="ElementLoading" class="code" title="function wC = ElementLoading (w0,lamda,LdId)">ElementLoading</a>	ELEMENTLOADING determines current distributed element load value</li></ul>
This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->