
<!-- <a name="_top"></a>
<div><a href="../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="_index.md">Material_Library</a> &gt; BilinInel1dMat.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../_index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Material_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `BilinInel1dMat`
<!-- <h1>BilinInel1dMat
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

BILININEL1dMAT uniaxial stress-strain relation for bilinear inelastic material

<!-- <div class="box"><strong>BILININEL1dMAT uniaxial stress-strain relation for bilinear inelastic material</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function MatResp = BilinInel1dMat (action,MatNo,MatData,MatState)` 
## <a name="_description"></a>Description

<pre class="comment">BILININEL1dMAT uniaxial stress-strain relation for bilinear inelastic material    
  MATRESP = BILININEL1dMAT (ACTION,MATNO,MATDATA,MATSTATE)
  function determines the uniaxial stress-strain relation for  bilinear inelastic material
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  the character variable ACTION should have one of the following values
  ACTION = 'chec' function checks material property data for omissions and returns default values in MATDATA
           'init' function returns the material history variables in MATSTATE
           'forc' function returns the material stress (tensor) in MATSTATE
           'stif' function returns the material tangent modulus and the stress (tensor) in MATSTATE
           'post' function returns data structure MATPOST with post-processing information
  depending on the value of character variable ACTION the function returns information in data structure MATRESP
  for the material with number MAT_NO; data structure MATDATA supplies the material property data
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  data structure MATRESP stands for one of the following data objects depending on value of ACTION 
  MATRESP = MATDATA   for action = 'chec'
  MATRESP = MATSTATE  for action = 'init'
  MATRESP = MATSTATE  for action = 'stif'
  MATRESP = MATSTATE  for action = 'forc'
  MATRESP = MATPOST   for action = 'post'
  MATRESP is empty    for unsupported keywords
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATSTATE is a data structure with information about the current material state in fields
         eps    = total strain (tensor for 2d or 3d)
         Deps   = strain increments from last convergence
         DDeps  = strain increments from last iteration
         epsdot = strain rate (tensor for 2d or 3d)
         km     = material stiffness matrix; returned under ACTION = 'stif'
         sig    = stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'
         Past   = material history variables at last converged state
         Pres   = current values of material history variables
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATDATA is a data structure with material property information; it has the fields
         E  = initial modulus
         fy = yield strength
         Eh = post-yield modulus
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATPOST is a data structure with material response information for post-processing in fields
         eps = total strain
         sig = uniaxial stress</pre>
<!-- <div class="fragment"><pre class="comment">BILININEL1dMAT uniaxial stress-strain relation for bilinear inelastic material    
  MATRESP = BILININEL1dMAT (ACTION,MATNO,MATDATA,MATSTATE)
  function determines the uniaxial stress-strain relation for  bilinear inelastic material
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  the character variable ACTION should have one of the following values
  ACTION = 'chec' function checks material property data for omissions and returns default values in MATDATA
           'init' function returns the material history variables in MATSTATE
           'forc' function returns the material stress (tensor) in MATSTATE
           'stif' function returns the material tangent modulus and the stress (tensor) in MATSTATE
           'post' function returns data structure MATPOST with post-processing information
  depending on the value of character variable ACTION the function returns information in data structure MATRESP
  for the material with number MAT_NO; data structure MATDATA supplies the material property data
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  data structure MATRESP stands for one of the following data objects depending on value of ACTION 
  MATRESP = MATDATA   for action = 'chec'
  MATRESP = MATSTATE  for action = 'init'
  MATRESP = MATSTATE  for action = 'stif'
  MATRESP = MATSTATE  for action = 'forc'
  MATRESP = MATPOST   for action = 'post'
  MATRESP is empty    for unsupported keywords
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATSTATE is a data structure with information about the current material state in fields
         eps    = total strain (tensor for 2d or 3d)
         Deps   = strain increments from last convergence
         DDeps  = strain increments from last iteration
         epsdot = strain rate (tensor for 2d or 3d)
         km     = material stiffness matrix; returned under ACTION = 'stif'
         sig    = stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'
         Past   = material history variables at last converged state
         Pres   = current values of material history variables
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATDATA is a data structure with material property information; it has the fields
         E  = initial modulus
         fy = yield strength
         Eh = post-yield modulus
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATPOST is a data structure with material response information for post-processing in fields
         eps = total strain
         sig = uniaxial stress</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->