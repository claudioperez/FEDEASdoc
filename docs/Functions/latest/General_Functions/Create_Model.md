---
title: "Create_Model"
id: "Create_Model"
description: "CREATE_MODEL creates data structure Model from node coordinates, connectivity and boundary conditions"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">General_Functions</a> &gt; 
<!-- Create_Model.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\General_Functions&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Create_Model`



## <a name="_name"></a>Purpose


CREATE_MODEL creates data structure Model from node coordinates, connectivity and boundary conditions

<!-- <div class="box"><strong>CREATE_MODEL creates data structure Model from node coordinates, connectivity and boundary conditions</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function Model = Create_Model (XYZ,CON,BOUN,ElemName)` 

## Description


<pre class="comment">CREATE_MODEL creates data structure Model from node coordinates, connectivity and boundary conditions
  MODEL = CREATE_MODEL (XYZ,CON,BOUN,ELEMNAME)
  function creates data structure MODEL with model information from the array of
  node coordinates XYZ (rows correspond to node numbers and columns to dofs),
  the cell array of element connectivity CON (rows correspond to element numbers),
  the array of boundary conditions BOUN (rows correspond to node numbers and columns to dofs),
  and the cell array of element names ELEMNAME (rows correspond to element numbers)
  Example: XYZ  (3,:)  = [10 15 22]; coordinates of node 3
           BOUN (3,:)  = [ 1  0  1]; boundary condition code for node 3 (0=free and 1=fixed)
           CON {4}     = [ 6 7];     element 4 connects nodes 6 and 7
           ELEMNAME{4} = 'LinTruss'; element 4 is a linear elastic truss

  data structure MODEL has the following fields
  MODEL.ndm      = dimension of structural model
        nn       = number of nodes in structural model
        ne       = number of elements
        nf       = number of free degrees of freedom
        nt       = total number of degrees of freedom
        XYZ      = node coordinates, nodes are stored columnwise
        BOUN     = boundary conditions, nodes are stored columnwise
        CON      = node connectivity array
        DOF      = array with degree of freedom numbering, nodes are stored columnwise
        ndf(el)  = no of dofs/node for element el
        nen(el)  = no of nodes     for element el
        ElemName = cell array of element names</pre>
<!-- <div class="fragment"><pre class="comment">CREATE_MODEL creates data structure Model from node coordinates, connectivity and boundary conditions
  MODEL = CREATE_MODEL (XYZ,CON,BOUN,ELEMNAME)
  function creates data structure MODEL with model information from the array of
  node coordinates XYZ (rows correspond to node numbers and columns to dofs),
  the cell array of element connectivity CON (rows correspond to element numbers),
  the array of boundary conditions BOUN (rows correspond to node numbers and columns to dofs),
  and the cell array of element names ELEMNAME (rows correspond to element numbers)
  Example: XYZ  (3,:)  = [10 15 22]; coordinates of node 3
           BOUN (3,:)  = [ 1  0  1]; boundary condition code for node 3 (0=free and 1=fixed)
           CON {4}     = [ 6 7];     element 4 connects nodes 6 and 7
           ELEMNAME{4} = 'LinTruss'; element 4 is a linear elastic truss

  data structure MODEL has the following fields
  MODEL.ndm      = dimension of structural model
        nn       = number of nodes in structural model
        ne       = number of elements
        nf       = number of free degrees of freedom
        nt       = total number of degrees of freedom
        XYZ      = node coordinates, nodes are stored columnwise
        BOUN     = boundary conditions, nodes are stored columnwise
        CON      = node connectivity array
        DOF      = array with degree of freedom numbering, nodes are stored columnwise
        ndf(el)  = no of dofs/node for element el
        nen(el)  = no of nodes     for element el
        ElemName = cell array of element names</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>

This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="../../latest/Solution_Scripts/S_MomCurvAnalysis.md" class="code" title="">S_MomCurvAnalysis</a>	% S_MOMCURVANALYSIS script for moment-curvature analysis under constant axial force</li><li><a href="../../latest/Solution_Scripts/S_NMAnalysis.md" class="code" title="">S_NMAnalysis</a>	% S_NMANALYSIS script for incremental application of N-M pair on section</li><li><a href="../../latest/Solution_Scripts/S_NMAnalysiswSepLoadHist.md" class="code" title="">S_NMAnalysiswSepLoadHist</a>	% S_NMANALYSISwSEPLOADHIST script for application N and M with separate load histories</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->