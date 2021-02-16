
<!-- <a name="_top"></a>
<div><a href="../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="_index.md">General_Functions</a> &gt; Create_SimpleModel.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../_index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\General_Functions&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Create_SimpleModel`
<!-- <h1>Create_SimpleModel
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

CREATE_SIMPLEMODEL create data structure Model from node coordinates, connectivity and boundary conditions

<!-- <div class="box"><strong>CREATE_SIMPLEMODEL create data structure Model from node coordinates, connectivity and boundary conditions</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function Model = Create_SimpleModel (XYZ,CON,BOUN,ElemName)` 
## <a name="_description"></a>Description

<pre class="comment">CREATE_SIMPLEMODEL create data structure Model from node coordinates, connectivity and boundary conditions
  MODEL = CREATE_SIMPLEMODEL (XYZ,CON,BOUN,ELEMNAME)
  the function creates the data structure MODEL from the array of
  node coordinates XYZ (rows correspond to node numbers and columns to dofs),
  the numerical or cell array of element connectivity CON (rows correspond to element numbers),
  the array of boundary conditions BOUN (rows correspond to node numbers and columns to dofs),
  and the cell array of element names ELEMNAME (rows correspond to element numbers)
  Example: XYZ  (3,:) = [10 15 22];  coordinates of node 3
           BOUN (3,:) = [ 1  0  1];  boundary condition code for node 3 (0=free and 1=fixed)
           CON  (4,:) = [ 6 7]    :  element 4 connects nodes 6 and 7, or
           CON  {4}   = [ 6 7];      element 4 connects nodes 6 and 7
           ELEMNAME{4} = 'LinTruss'; element 4 is a linear elastic truss

  the data structure MODEL contains information about the structural model in the following fields
  MODEL.ndm      = dimension of structural model
        nn       = number of nodes in structural model
        ne       = number of elements
        nf       = number of free degrees of freedom
        nt       = total number of degrees of freedom
        XYZ      = node coordinates, nodes are stored columnwise
        BOUN     = boundary conditions, nodes are stored columnwise
        CON      = cell array of node connectivity 
        DOF      = array with degree of freedom numbering, nodes are stored rowwise
        ndf(el)  = no of dofs/node    for element el
        nq (el)  = no of basic forces for element el
        nen(el)  = no of nodes        for element el
        ElemName = cell array of element names</pre>
<!-- <div class="fragment"><pre class="comment">CREATE_SIMPLEMODEL create data structure Model from node coordinates, connectivity and boundary conditions
  MODEL = CREATE_SIMPLEMODEL (XYZ,CON,BOUN,ELEMNAME)
  the function creates the data structure MODEL from the array of
  node coordinates XYZ (rows correspond to node numbers and columns to dofs),
  the numerical or cell array of element connectivity CON (rows correspond to element numbers),
  the array of boundary conditions BOUN (rows correspond to node numbers and columns to dofs),
  and the cell array of element names ELEMNAME (rows correspond to element numbers)
  Example: XYZ  (3,:) = [10 15 22];  coordinates of node 3
           BOUN (3,:) = [ 1  0  1];  boundary condition code for node 3 (0=free and 1=fixed)
           CON  (4,:) = [ 6 7]    :  element 4 connects nodes 6 and 7, or
           CON  {4}   = [ 6 7];      element 4 connects nodes 6 and 7
           ELEMNAME{4} = 'LinTruss'; element 4 is a linear elastic truss

  the data structure MODEL contains information about the structural model in the following fields
  MODEL.ndm      = dimension of structural model
        nn       = number of nodes in structural model
        ne       = number of elements
        nf       = number of free degrees of freedom
        nt       = total number of degrees of freedom
        XYZ      = node coordinates, nodes are stored columnwise
        BOUN     = boundary conditions, nodes are stored columnwise
        CON      = cell array of node connectivity 
        DOF      = array with degree of freedom numbering, nodes are stored rowwise
        ndf(el)  = no of dofs/node    for element el
        nq (el)  = no of basic forces for element el
        nen(el)  = no of nodes        for element el
        ElemName = cell array of element names</pre></div> -->

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