
<!-- <a name="_top"></a>
<div><a href="../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="_index.md">Section_Library</a> &gt; HomoWFSecw1dMat.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../_index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\Section_Library&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `HomoWFSecw1dMat`
<!-- <h1>HomoWFSecw1dMat
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

HOMOWFSECw1dMAT response of homogeneous wide flange (WF) section with uniaxial material

<!-- <div class="box"><strong>HOMOWFSECw1dMAT response of homogeneous wide flange (WF) section with uniaxial material</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function SecResp = HomoWFSecw1dMat (action,SecNo,ndm,SecData,SecState)` 
## <a name="_description"></a>Description

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
<li><a href="Extract_Sec2MatState" class="code" title="function MatState = Extract_Sec2MatState (m,as,SecState)">Extract_Sec2MatState</a>	EXTRACT_SEC2MATSTATE extract material state from section state</li></ul>
This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->