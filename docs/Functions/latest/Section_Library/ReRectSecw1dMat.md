---
title: "ReRectSecw1dMat"
id: "ReRectSecw1dMat"
description: "RERECTSECw1dMAT response of reinforced rectangular section with uniaxial materials"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">Section_Library</a> &gt; 
<!-- ReRectSecw1dMat.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Section_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `ReRectSecw1dMat`



## <a name="_name"></a>Purpose


RERECTSECw1dMAT response of reinforced rectangular section with uniaxial materials

<!-- <div class="box"><strong>RERECTSECw1dMAT response of reinforced rectangular section with uniaxial materials</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function SecResp = ReRectSecw1dMat (action,SecNo,ndm,SecData,SecState)` 

## Description


<pre class="comment">RERECTSECw1dMAT response of reinforced rectangular section with uniaxial materials    
  SECRESP = RERECTSECw1dMAT (ACTION,SECNO,NDM,SECDATA,SECSTATE)
  the function determines the response of a reinforced rectangular section with uniaxial materials
       by integration in y-direction for 2d, and in y- and z- direction for 3d response
      (section resisting forces are N-Mz for NDM=2 and N-Mz-My for NDM=3)
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  When the character variable ACTION has one of the following values,
  the function performs the listed operations and returns the results in SECRESP:
  ACTION = 'chec': check section property data for omissions and assign default values
           'init': initialize section history variables
           'forc': report section resisting forces
           'stif': report section stiffness matrix and resisting forces
           'post': report post-processing information
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The data structure SECRESP stands for the following data object(s) for each ACTION:
  SECRESP = SECDATA    for action = 'chec'
  SECRESP = SECSTATE   for action = 'init'
  SECRESP = SECSTATE   for action = 'stif'
  SECRESP = SECSTATE   for action = 'forc'
  SECRESP = SECPOST    for action = 'post'
  SECRESP is empty     for unsupported keywords
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  SECDATA is a data structure with section property information; it has the fields
         d        = section depth
         b        = section width
         cv(1:2)  = top/bottom and side cover (default=[0,0])
         ny       = no of integration points (fibers) in y (default = 10)
         nz       = no of integration points (fibers) in z (default = 1 for 2d and 10 for 3d)
         ncl      = no of integration points along cover   (default = 10)
         nct      = no of integration points across cover  (default = 2)
         IntTyp   = function name for section integration
         MatName  = cell array with function names for uniaxial stress-strain relations (1=core,2=cover)
         MatData  = cell array with properties for uniaxial stress-strain relations (1=core,2=cover)
         BMatName = function name for uniaxial stress-strain relation of reinforcing bars
         BMatData = data structure with material property data for reinforcing bars
         BarAyz   = array with y-z coordinates and area of each reinforcing bar;
                    y-coordinate in first column, z-coordinate in second, area in third 
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  SECSTATE is a data structure with information about the current section state; it has the fields
         e     = vector of total section deformations
         De    = vector of section deformation increments from last convergence
         DDe   = vector of section deformation increments from last iteration
         edot  = vector of section deformation rates
         ks    = section stiffness matrix; returned under ACTION = 'stif'
         s     = section resisting force vector; returned under ACTION = 'stif' or 'forc'
         Past  = section history variables at last converged state
         Pres  = current section history variables
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  SECPOST is a data structure with section response information for post-processing; it has the fields
         e      = section deformations
         s      = section stress resultants
         Mat{i} = material response information for post-processing (see material function with MatName)</pre>
<!-- <div class="fragment"><pre class="comment">RERECTSECw1dMAT response of reinforced rectangular section with uniaxial materials    
  SECRESP = RERECTSECw1dMAT (ACTION,SECNO,NDM,SECDATA,SECSTATE)
  the function determines the response of a reinforced rectangular section with uniaxial materials
       by integration in y-direction for 2d, and in y- and z- direction for 3d response
      (section resisting forces are N-Mz for NDM=2 and N-Mz-My for NDM=3)
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  When the character variable ACTION has one of the following values,
  the function performs the listed operations and returns the results in SECRESP:
  ACTION = 'chec': check section property data for omissions and assign default values
           'init': initialize section history variables
           'forc': report section resisting forces
           'stif': report section stiffness matrix and resisting forces
           'post': report post-processing information
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The data structure SECRESP stands for the following data object(s) for each ACTION:
  SECRESP = SECDATA    for action = 'chec'
  SECRESP = SECSTATE   for action = 'init'
  SECRESP = SECSTATE   for action = 'stif'
  SECRESP = SECSTATE   for action = 'forc'
  SECRESP = SECPOST    for action = 'post'
  SECRESP is empty     for unsupported keywords
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  SECDATA is a data structure with section property information; it has the fields
         d        = section depth
         b        = section width
         cv(1:2)  = top/bottom and side cover (default=[0,0])
         ny       = no of integration points (fibers) in y (default = 10)
         nz       = no of integration points (fibers) in z (default = 1 for 2d and 10 for 3d)
         ncl      = no of integration points along cover   (default = 10)
         nct      = no of integration points across cover  (default = 2)
         IntTyp   = function name for section integration
         MatName  = cell array with function names for uniaxial stress-strain relations (1=core,2=cover)
         MatData  = cell array with properties for uniaxial stress-strain relations (1=core,2=cover)
         BMatName = function name for uniaxial stress-strain relation of reinforcing bars
         BMatData = data structure with material property data for reinforcing bars
         BarAyz   = array with y-z coordinates and area of each reinforcing bar;
                    y-coordinate in first column, z-coordinate in second, area in third 
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  SECSTATE is a data structure with information about the current section state; it has the fields
         e     = vector of total section deformations
         De    = vector of section deformation increments from last convergence
         DDe   = vector of section deformation increments from last iteration
         edot  = vector of section deformation rates
         ks    = section stiffness matrix; returned under ACTION = 'stif'
         s     = section resisting force vector; returned under ACTION = 'stif' or 'forc'
         Past  = section history variables at last converged state
         Pres  = current section history variables
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  SECPOST is a data structure with section response information for post-processing; it has the fields
         e      = section deformations
         s      = section stress resultants
         Mat{i} = material response information for post-processing (see material function with MatName)</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="/Functions/Extract_Sec2MatState" class="code" title="function MatState = Extract_Sec2MatState (m,as,SecState)">Extract_Sec2MatState</a>	EXTRACT_SEC2MATSTATE extract material state from section state</li></ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->