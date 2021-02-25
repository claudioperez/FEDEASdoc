[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Material_Library](FEDEASLab.html) \>
InelJ2PwLH3dMat.m

</div>

# InelJ2PwLH3dMat

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**INELJ2PwLH3DMAT inelastic 3d material model with J2 plasticity and
linear kinematic and isotropic hardening**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function MatResp = InelJ2PwLH3dMat (action,MatNo,MatData,MatState)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
INELJ2PwLH3DMAT inelastic 3d material model with J2 plasticity and linear kinematic and isotropic hardening
  MATRESP = INELJ2PwLH3DMAT (ACTION,MAT_NO,MATDATA,MATSTATE)
  function determines the stress-strain relation for an inelastic 3d material model
           based on J2 plasticity with isotropic and kinematic hardening
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
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATSTATE is a data structure with information about the current material state in fields
         eps    = total strain tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23
         Deps   = strain increments from last convergence
         DDeps  = strain increments from last iteration
         epsdot = strain rate tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23
         km     = material stiffness matrix; returned under ACTION = 'stif'
         sig    = stress tensor in 6x1 vector form; returned under ACTION = 'stif' or 'forc'
         Past   = material history variables at last converged state
         Pres   = current values of material history variables
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATDATA is a data structure with material property information; it has the fields
         E  = initial modulus
         fy = yield strength
         nu = Poisson ratio               (default = 0)
         Hk = kinematic hardening modulus (default = 0)
         Hi = isotropic hardening modulus (default = 0)
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATPOST is a data structure with material response information for post-processing in fields
         eps   =         strain tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23
         sig   =         stress tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23
         eps_p = plastic strain tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
