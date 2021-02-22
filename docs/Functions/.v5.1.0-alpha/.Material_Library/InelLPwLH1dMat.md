[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [Material_Library](FEDEASLab.html) \>
InelLPwLH1dMat.m

</div>

# InelLPwLH1dMat

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**INELLPwLH1dMAT inelastic linear-plastic 1d model with linear kinematic
and isotropic hardening**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function MatResp = InelLPwLH1dMat (action,MatNo,MatData,MatState)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
INELLPwLH1dMAT inelastic linear-plastic 1d model with linear kinematic and isotropic hardening
  MATRESP = INELLPwLH1dMAT (ACTION,MAT_NO,MATDATA,MATSTATE)
  the function determines the current material state under total strain EPSI
  for an inelastic linear-plastic 1d model with linear kinematic and isotropic hardening
  with the return map algorithm; the plastic strain EPS_P, the back stress SIG_B and the
  isotropic hardening variable ALPHA are the history variables of the model
  Reference: JC Simo and TJR Hughes, Computational Inelasticity, pp. 43-45
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
  MATRESP = MATSTATE  for action = 'hist'
  MATRESP = MATSTATE  for action = 'stif'
  MATRESP = MATSTATE  for action = 'forc'
  MATRESP = MATPOST   for action = 'post'
  MATRESP is empty    for unsupported keywords
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATSTATE is a data structure with information about the current material state in fields
         eps    = total strain
         Deps   = strain increments from last convergence
         DDeps  = strain increments from last iteration
         epsdot = strain rate
         km     = material stiffness matrix; returned under ACTION = 'stif'
         sig    = stress; returned under ACTION = 'stif' or 'forc'
         Past   = material history variables at last converged state
         Pres   = current values of material history variables
             Past and Pres contain the following history variable(s):
             eps_p = plastic strain
             alpha = isotropic hardening variable
             sig_b = back stress (for kinematic hardening)
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATDATA is a data structure with material property information; it has the fields
         E  = initial modulus
         fy = yield strength
         Hi = isotropic plastic   modulus
         Hk = kinematic hardening modulus
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  MATPOST is a data structure with material response information for post-processing in fields
         eps   = total strain
         sig   = uniaxial stress
         eps_p = plastic strain
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
