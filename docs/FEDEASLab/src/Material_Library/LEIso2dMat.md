
<!-- <a name="_top"></a>
<div><a href="../../index.md">Home</a> &gt;  <a href="#">src</a> &gt; <a href="index.md">Material_Library</a> &gt; LEIso2dMat.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="index.md">Index for src\Material_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `LEIso2dMat`
<!-- <h1>LEIso2dMat
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

LEISO2dMAT linear elastic, isotropic 2d material model under general plane stress or strain conditions

<!-- <div class="box"><strong>LEISO2dMAT linear elastic, isotropic 2d material model under general plane stress or strain conditions</strong></div> -->

## <a name="_synopsis"></a>Syntax

`function MatResp = LEIso2dMat (action,MatNo,MatData,MatState)` 
## <a name="_description"></a>Description

<pre class="comment">LEISO2dMAT linear elastic, isotropic 2d material model under general plane stress or strain conditions 
  MATRESP = LEISO2dMAT (ACTION,MATNO,MATDATA,MATSTATE)
  function determines the response of a linear elastic, isotropic material
           under general plane stress or strain conditions
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
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATSTATE is a data structure with information about the current material state in fields
         eps    = total strain tensor in 4x1 vector form in the order 11, 22, 33, 12
         Deps   = strain increments from last convergence
         DDeps  = strain increments from last iteration
         epsdot = strain rate tensor in 4x1 vector form in the order 11, 22, 33, 12
         km     = material stiffness matrix; returned under ACTION = 'stif'
         sig    = stress tensor in 4x1 vector form; returned under ACTION = 'stif' or 'forc'
         Past   = material history variables at last converged state
         Pres   = current values of material history variables
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATDATA is a data structure with material property information; it has the fields
         E    = Young modulus
         nu   = Poisson ratio
         eps0 = initial strain tensor in 4x1 vector form in the order 11, 22, 33, 12
         sig0 = initial stress tensor in 4x1 vector form in the order 11, 22, 33, 12
         Case = 'stress' or 'strain'
         irs  = stress or strain components to be retained depending on Case
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATPOST is a data structure with material response information for post-processing in fields
         eps = strain tensor in 4x1 vector form in the order 11, 22, 33, 12
         sig = stress tensor in 4x1 vector form in the order 11, 22, 33, 12</pre>
<!-- <div class="fragment"><pre class="comment">LEISO2dMAT linear elastic, isotropic 2d material model under general plane stress or strain conditions 
  MATRESP = LEISO2dMAT (ACTION,MATNO,MATDATA,MATSTATE)
  function determines the response of a linear elastic, isotropic material
           under general plane stress or strain conditions
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
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATSTATE is a data structure with information about the current material state in fields
         eps    = total strain tensor in 4x1 vector form in the order 11, 22, 33, 12
         Deps   = strain increments from last convergence
         DDeps  = strain increments from last iteration
         epsdot = strain rate tensor in 4x1 vector form in the order 11, 22, 33, 12
         km     = material stiffness matrix; returned under ACTION = 'stif'
         sig    = stress tensor in 4x1 vector form; returned under ACTION = 'stif' or 'forc'
         Past   = material history variables at last converged state
         Pres   = current values of material history variables
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATDATA is a data structure with material property information; it has the fields
         E    = Young modulus
         nu   = Poisson ratio
         eps0 = initial strain tensor in 4x1 vector form in the order 11, 22, 33, 12
         sig0 = initial stress tensor in 4x1 vector form in the order 11, 22, 33, 12
         Case = 'stress' or 'strain'
         irs  = stress or strain components to be retained depending on Case
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATPOST is a data structure with material response information for post-processing in fields
         eps = strain tensor in 4x1 vector form in the order 11, 22, 33, 12
         sig = stress tensor in 4x1 vector form in the order 11, 22, 33, 12</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Tue 14-Jul-2020 22:59:26 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->