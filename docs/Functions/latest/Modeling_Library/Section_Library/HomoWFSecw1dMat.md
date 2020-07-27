[]{#_top}

<div>

[Home](../FEDEASLab.html) &gt; [Section\_Library](FEDEASLab.html) &gt;
HomoWFSecw1dMat.m

</div>

HomoWFSecw1dMat
===============

[]{#_name}PURPOSE [![\^](../up.png)](#_top)
-------------------------------------------

<div class="box">

**HOMOWFSECw1dMAT response of homogeneous wide flange (WF) section with
uniaxial material**

</div>

[]{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)
------------------------------------------------

<div class="box">

**function SecResp = HomoWFSecw1dMat
(action,SecNo,ndm,SecData,SecState)**

</div>

[]{#_description}DESCRIPTION [![\^](../up.png)](#_top)
------------------------------------------------------

<div class="fragment">

``` {.comment}
HOMOWFSECw1dMAT response of homogeneous wide flange (WF) section with uniaxial material    
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
                          z <-----+ + |     d
                                  |tw |
                               .--'   '--.
                               | tf      |
                               '---------'
                                   bf
```

</div>

[]{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)
----------------------------------------------------------------

This function calls:

-   [Extract\_Sec2MatState](Extract_Sec2MatState.html "function MatState = Extract_Sec2MatState (m,as,SecState)"){.code}
    EXTRACT\_SEC2MATSTATE extract material state from section state

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
