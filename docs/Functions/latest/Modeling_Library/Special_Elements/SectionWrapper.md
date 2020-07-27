---
description: |
    SECTIONWRAPPER wrapper element that passes on arguments to the section
    state determination
generator: 'm2html v1.5 © 2003-2005 Guillaume Flandin'
keywords: SectionWrapper
robots: 'index, follow'
title: Description of SectionWrapper
---

[]{#_top}

<div>

[Home](../FEDEASLab.html) &gt; [Element\_Library](FEDEASLab.html) &gt;
SectionWrapper.m

</div>

SectionWrapper
==============

[]{#_name}PURPOSE [![\^](../up.png)](#_top)
-------------------------------------------

<div class="box">

**SECTIONWRAPPER wrapper element that passes on arguments to the section
state determination**

</div>

[]{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)
------------------------------------------------

<div class="box">

**function ElemResp = SectionWrapper
(action,el\_no,xyz,ElemData,ElemState)**

</div>

[]{#_description}DESCRIPTION [![\^](../up.png)](#_top)
------------------------------------------------------

<div class="fragment">

``` {.comment}
SECTIONWRAPPER wrapper element that passes on arguments to the section state determination
  ELEMRESP = SECTIONWRAPPER (ACTION,EL_NO,XYZ,ELEMDATA,ELEMSTATE)
  the function determines the response of the section SECNAME in ELEMDATA
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  When the character variable ACTION has one of the following values,
  the function performs the listed operations and returns the results in ELEMRESP:
  ACTION = 'size': report size of element arrays
           'chec': check element property data for omissions and assign default values
           'init': initialize element history variables
           'forc': report element resisting forces
           'stif': report element stiffness matrix and resisting forces
           'mass': report lumped mass vector and consistent mass matrix
           'post': report post-processing information
           'defo': report function handle for deformed shape
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The data structure ELEMRESP stands for the following data object(s) for each ACTION:
  ELEMRESP = ARSZ        for action = 'size' 
  ELEMRESP = ELEMDATA    for action = 'chec'
  ELEMRESP = ELEMSTATE   for action = 'init'
  ELEMRESP = ELEMSTATE   for action = 'stif'
  ELEMRESP = ELEMSTATE   for action = 'forc'
  ELEMRESP = ELEMMASS    for action = 'mass'
  ELEMRESP = ELEMPOST    for action = 'post'
  ELEMRESP is empty      for unsupported keywords
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ARSZ   is an Boolean array of size NDF x NEN,
         where NDF = number of DOFs/node, NEN = number of nodes,
         with unit values corresponding to the active element DOFs
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ELEMSTATE is a data structure with the current element state; it has the fields
         u     = vector of total element displacements in global reference
         Du    = vector of element displacement increments from last convergence
         DDu   = vector of element displacement increments from last iteration
         ke    = element stiffness matrix in global reference; updated under ACTION = 'stif'
         p     = element resisting force vector in global reference; updated under ACTION = 'stif' or 'forc'
         Past  = element history variables at last converged state
         Pres  = current element history variables
         lamda = row vector of current load factor(s)
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ELEMPOST is a data structure with element response information for post-processing in fields
         v     = e = section deformations
         q     = s = section forces
```

</div>

[]{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)
----------------------------------------------------------------

This function calls:

-   [Extract\_El2SecState](Extract_El2SecState.html "function SecState = Extract_El2SecState (sec,ae,ElemState)"){.code}
    EXTRACT\_EL2SECSTATE extract section state from element state

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
