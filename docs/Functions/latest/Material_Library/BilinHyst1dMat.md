---
title: "BilinHyst1dMat"
id: "BilinHyst1dMat"
description: "BILINHYST1dMAT bilinear hysteretic force-deformation relation with pinching"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">Material_Library</a> &gt; 
<!-- BilinHyst1dMat.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Material_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `BilinHyst1dMat`



## <a name="_name"></a>Purpose


BILINHYST1dMAT bilinear hysteretic force-deformation relation with pinching

<!-- <div class="box"><strong>BILINHYST1dMAT bilinear hysteretic force-deformation relation with pinching</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function MatResp = BilinHyst1dMat (action,MatNo,MatData,MatState)` 

## Description


<pre class="comment">BILINHYST1dMAT bilinear hysteretic force-deformation relation with pinching    
  MATRESP = BILINHYST1dMAT (ACTION,MATNO,MATDATA,MATSTATE)
  function for bilinear hysteretic force-deformation relation with pinching
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
         km     = material tangent modulus; returned under ACTION = 'stif'
         sig    = stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'
         Past   = material history variables at last converged state
         Pres   = current values of material history variables
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATDATA is a data structure with material property information in fields
         sig1p  = positive stress at first transition
         eps1p  = positive strain at first transition
         sig2p  = ultimate positive stress
         eps2p  = ultimate positive strain
         sig1n  = negative stress at first transition
         eps1n  = negative strain at first transition
         sig2n  = ultimate negative stress
         eps2n  = ultimate negative strain
         pnchx(+ve ; -ve) = x-pinching parameters under +ve and -ve deformation 
         pnchy(+ve ; -ve) = y-pinching parameters under +ve and -ve deformation
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATPOST is a data structure with material response information for post-processing in fields
         eps = total strain
         sig = uniaxial stress</pre>
<!-- <div class="fragment"><pre class="comment">BILINHYST1dMAT bilinear hysteretic force-deformation relation with pinching    
  MATRESP = BILINHYST1dMAT (ACTION,MATNO,MATDATA,MATSTATE)
  function for bilinear hysteretic force-deformation relation with pinching
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
         km     = material tangent modulus; returned under ACTION = 'stif'
         sig    = stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'
         Past   = material history variables at last converged state
         Pres   = current values of material history variables
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATDATA is a data structure with material property information in fields
         sig1p  = positive stress at first transition
         eps1p  = positive strain at first transition
         sig2p  = ultimate positive stress
         eps2p  = ultimate positive strain
         sig1n  = negative stress at first transition
         eps1n  = negative strain at first transition
         sig2n  = ultimate negative stress
         eps2n  = ultimate negative strain
         pnchx(+ve ; -ve) = x-pinching parameters under +ve and -ve deformation 
         pnchy(+ve ; -ve) = y-pinching parameters under +ve and -ve deformation
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




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->