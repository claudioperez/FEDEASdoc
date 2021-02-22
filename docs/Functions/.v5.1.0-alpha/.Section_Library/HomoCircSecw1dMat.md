[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Section_Library](FEDEASLab.html) \>
HomoCircSecw1dMat.m

</div>

# HomoCircSecw1dMat

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**HOMOCIRCSECw1dMAT response of homogeneous circular section with
uniaxial material**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function SecResp = HomoCircSecw1dMat
(action,SecNo,ndm,SecData,SecState)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
HOMOCIRCSECw1dMAT response of homogeneous circular section with uniaxial material    
  SECRESP = HOMOCIRCSECw1dMAT (ACTION,SECNO,NDM,SECDATA,SECSTATE)
  the function determines the response of a homogeneous circular section with uniaxial material
      by midpoint integration in y-direction for 2d, and in y- and z- direction for 3d response
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
         R(1:2)  = outer radius and inner radius of section (default = R(1) only)
         nr      = no of integration points (fibers) over radius (default=5)(thus 2 x nr across diameter)
         nth     = no of integration points (fibers) in circumferential direction (used for 3d only),(default=10) 
         Rdrat   = ratio of inner to outer radius for switching to uniform dicretization
         IntTyp  = function name for section integration ('Midpoint' or 'Cubature')
         MatName = function name for material uniaxial stress-strain relation
         MatData = data structure with material property data
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
         Mat{i} = material response information for post-processing (see material function with MatName)
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
