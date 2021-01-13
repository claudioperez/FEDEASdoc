[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Section_Library](FEDEASLab.html) \>
HomoWFSecw1dMat.m

</div>

# HomoWFSecw1dMat

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**HOMOWFSECw1dMAT response of homogeneous wide flange (WF) section with
uniaxial material**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function SecResp = HomoWFSecw1dMat
(action,SecNo,ndm,SecData,SecState)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
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
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [Extract_Sec2MatState](Extract_Sec2MatState.html "function MatState = Extract_Sec2MatState (m,as,SecState)"){.code}
    EXTRACT_SEC2MATSTATE extract material state from section state

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
