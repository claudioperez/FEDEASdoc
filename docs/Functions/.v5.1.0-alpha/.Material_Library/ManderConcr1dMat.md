[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Material_Library](FEDEASLab.html) \>
ManderConcr1dMat.m

</div>

# ManderConcr1dMat

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**MANDERCONCR1DMAT hysteretic concrete stress-strain relation after
Mander**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function MatResp = ManderConcr1dMat (action,MatNo,MatData,MatState)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
MANDERCONCR1DMAT hysteretic concrete stress-strain relation after Mander
  MATRESP = MANDERCONCR1DMAT (ACTION,MATNO,MATDATA,MATSTATE)
  function determines the uniaxial stress-strain relation for Mander material model
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  the character variable ACTION should have one of the following values
  ACTION = 'chec' function checks material property data for omissions and returns default values in MATDATA
           'init' function returns the material history variables in MATSTATE
           'forc' function returns the material stress (tensor) in MATSTATE
           'stif' function returns the material tangent modulus and the stress (tensor) in MATSTATE
           'post' function returns data structure MATPOST with post-processing information
  depending on the value of character variable ACTION the function returns information in data structure MATRESP
  for the material with number MAT_NO; data structure MATDATA supplies the material property data
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  data structure MATRESP stands for one of the following data objects depending on value of ACTION 
  MATRESP = MATDATA   for action = 'chec'
  MATRESP = MATSTATE  for action = 'init'
  MATRESP = MATSTATE  for action = 'stif'
  MATRESP = MATSTATE  for action = 'forc'
  MATRESP = MATPOST   for action = 'post'
  MATRESP is empty    for unsupported keywords
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATSTATE is a data structure with information about the current material state in fields
         eps    = total strain (tensor for 2d or 3d)
         Deps   = strain increments from last convergence
         DDeps  = strain increments from last iteration
         epsdot = strain rate (tensor for 2d or 3d)
         km     = material tangent modulus; returned under ACTION = 'stif'
         sig    = stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'
         Past   = material history variables at last converged state
         Pres   = current values of material history variables
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATDATA is a data structure with material property information in fields
         fc    = compressive strength for unconfined concrete
         epc0  = strain at compressive strength for unconfined concrete
         Ec    = initial modulus for unconfined concrete
         Kfc   = ratio of confined to unconfined concrete strength
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATPOST is a data structure with material response information for post-processing in fields
         eps = total strain
         sig = uniaxial stress
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
