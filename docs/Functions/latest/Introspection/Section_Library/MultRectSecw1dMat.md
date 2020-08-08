[]{#_top}

<div>

[Home](../FEDEASLab.html) &gt; [Section\_Library](FEDEASLab.html) &gt;
MultRectSecw1dMat.m

</div>

MultRectSecw1dMat
=================

[]{#_name}PURPOSE [![\^](../up.png)](#_top)
-------------------------------------------

<div class="box">

**MULTRECTSECw1dMAT response for section of rectangular patches and bars
with uniaxial material**

</div>

[]{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)
------------------------------------------------

<div class="box">

**function SecResp = MultRectSecw1dMat
(action,SecNo,ndm,SecData,SecState)**

</div>

[]{#_description}DESCRIPTION [![\^](../up.png)](#_top)
------------------------------------------------------

<div class="fragment">

``` {.comment}
MULTRECTSECw1dMAT response for section of rectangular patches and bars with uniaxial material
  SECRESP = MULTRECTSECw1dMAT (ACTION,SECNO,NDM,SECDATA,SECSTATE)
  the function determines the response of a section made up of rectangular patches and bars
      with uniaxial material by integration in y for 2d, and in y and z for 3d response
      (section resisting forces are N-Mz for NDM=2 and N-Mz-My for NDM=3)

  Coordinate system:
                                   ^ y
                                   |
                               |---+---------------|
                               |   |    o o o o o  |
                               |   |   |-----------|
                         z <---+---+   |
                               |       |
                               | o o o |
                               |--------
     
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  When the character variable ACTION has one of the following values,
  the function performs the listed operations and returns the results in SECRESP:
  ACTION = 'chec': check section property data for omissions and assign default values
           'init': initialize section history variables
           'forc': report section resisting forces
           'stif': report section stiffness matrix and resisting forces
           'post': report post-processing information
           'defo': report section displacements for deformed shape
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The data structure SECRESP stands for the following data object(s) for each ACTION:
  SECRESP = SECDATA    for action = 'chec'
  SECRESP = SECSTATE   for action = 'init'
  SECRESP = SECSTATE   for action = 'stif'
  SECRESP = SECSTATE   for action = 'forc'
  SECRESP = SECPOST    for action = 'post'
  SECRESP = SECDISP    for action = 'defo'
  SECRESP is empty     for unsupported keywords
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  SECDATA is a data structure with section property information in fields
     FibAyz(1:NF,3) = coordinates and area (weight) of NF IPs or fibers for contiguous shape
     FMatName{:}    = cell array of material names for portions of contiguous shape
     FMatData{:}    = cell array with material property data for portions of contiguous shape
     FMatID(1:NF)   =      array with material ID for NF fibers of contiguous shape
     BarAyz(1:NB,3) = coordinates and area (weight) of NB bars
     BMatName{:}    = cell array of material names for bars
     BMatData{:}    = cell array with material property data for bars
     BMatID(1:NB)   =      array with material ID for NB bars
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  SECSTATE is a data structure with the current section state; it has the fields
         e     = vector of total section deformations
         De    = vector of section deformation increments from last convergence
         DDe   = vector of section deformation increments from last iteration
         edot  = vector of section deformation rates
         ks    = section stiffness matrix; returned under ACTION = 'stif'
         s     = section resisting force vector; returned under ACTION = 'stif' or 'forc'
         Past  = section history variables at last converged state
         Pres  = current section history variables
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  SECPOST is a data structure with section response information for post-processing in fields
         e    = section deformations
         s    = section force resultants
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  SECDISP is a data structure with the section displacements in fields

  =========================================================================================
  FEDEASLab - Release 5.1, July 2020
  Matlab Finite Elements for Design, Evaluation and Analysis of Structures
  Professor Filip C. Filippou (filippou@berkeley.edu)
  Department of Civil and Environmental Engineering, UC Berkeley
  Copyright(c) 1998-2020. The Regents of the University of California. All Rights Reserved.
  =========================================================================================
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
