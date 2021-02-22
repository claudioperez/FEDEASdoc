---
title: "HomoWFSecw1dMat"
id: "HomoWFSecw1dMat"
description: "HOMOWFSECw1dMAT response of homogeneous wide flange (WF) section with uniaxial material"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href=".autoindex.md">Section_Library</a> &gt; 
<!-- HomoWFSecw1dMat.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../.autoindex.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Section_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `HomoWFSecw1dMat`



## <a name="_name"></a>Purpose


HOMOWFSECw1dMAT response of homogeneous wide flange (WF) section with uniaxial material

<!-- <div class="box"><strong>HOMOWFSECw1dMAT response of homogeneous wide flange (WF) section with uniaxial material</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function SecResp = HomoWFSecw1dMat (action,SecNo,ndm,SecData,SecState)` 

## Description


<pre class="comment">HOMOWFSECw1dMAT response of homogeneous wide flange (WF) section with uniaxial material    
  SECRESP = HOMOWFSECw1dMAT (ACTION,SECNO,NDM,SECDATA,SECSTATE)
  the function determines the response of homogeneous wide flange (WF) section with uniaxial material
      by midpoint integration in y-direction for 2d, and in y- and z- direction for 3d response
     (section resisting forces are N-Mz for NDM=2 and N-Mz-My for NDM=3)

  Coordinate system:
                                  y ^
                                    |
                               .----+----.
                               |    |    |
                               '--. | .--'
                                  | | |
                          z &lt;-----+ + |     d
                                  |tw |
                               .--'   '--.
                               | tf      |
                               '---------'
                                   bf</pre>
<!-- <div class="fragment"><pre class="comment">HOMOWFSECw1dMAT response of homogeneous wide flange (WF) section with uniaxial material    
  SECRESP = HOMOWFSECw1dMAT (ACTION,SECNO,NDM,SECDATA,SECSTATE)
  the function determines the response of homogeneous wide flange (WF) section with uniaxial material
      by midpoint integration in y-direction for 2d, and in y- and z- direction for 3d response
     (section resisting forces are N-Mz for NDM=2 and N-Mz-My for NDM=3)

  Coordinate system:
                                  y ^
                                    |
                               .----+----.
                               |    |    |
                               '--. | .--'
                                  | | |
                          z &lt;-----+ + |     d
                                  |tw |
                               .--'   '--.
                               | tf      |
                               '---------'
                                   bf</pre></div> -->

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