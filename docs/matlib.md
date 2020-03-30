# Nonlinear Material Modeling

## Overview

Material formulations

  1. Rigorous 3D.

  2. Hysteretic with strength/stiffness deterioration.
    1. **polygonal**. Piecewise linear
    2. **smooth**.

  3. Damage index models.

Response relations

  1. Moment-curvature   [FL     vs  L^-1  ]
  2. Moment-rotation    [FL     vs   -    ]
  3. Force-deformation  [F      vs   L    ]
  4. Stress-strain      [FL^-2  vs   -    ]

## Basic Data Structures

MATSTATE is a data structure with information about the current material state in fields
      eps    = total strain (tensor for 2d or 3d)
      Deps   = strain increments from last convergence
      DDeps  = strain increments from last iteration
      epsdot = strain rate (tensor for 2d or 3d)
      km     = material stiffness matrix; returned under ACTION = 'stif'
      sig    = stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'
      Past   = material history variables at last converged state
      Pres   = current values of material history variables

MATDATA is a data structure with material property information; it has the fields
      E  = initial modulus
      fy = yield strength
      Eh = post-yield modulus

MATPOST is a data structure with material response information for post-processing in fields
      eps = total strain
      sig = uniaxial stress

## BiLinElastic1dMat

uniaxial stress-strain relation for a bilinear elastic material

  MATRESP = BILINELASTIC1dMAT (ACTION,MATNO,MATDATA,MATSTATE)

  Uniaxial stress-strain relation for a bilinear elastic material

### Action

  the character variable ACTION should have one of the following values
  ACTION = 'chec' function checks material property data for omissions and returns default values in MATDATA
           'init' function returns the material history variables in MATSTATE
           'forc' function returns the material stress (tensor) in MATSTATE
           'stif' function returns the material tangent modulus and the stress (tensor) in MATSTATE
           'post' function returns data structure MATPOST with post-processing information
  depending on the value of character variable ACTION the function returns information in data structure MATRESP
  for the material with number MAT_NO; data structure MATDATA supplies the material property data

### Response

  data structure MATRESP stands for one of the following data objects depending on value of ACTION
  MATRESP = MATDATA   for action = 'chec'
  MATRESP = MATSTATE  for action = 'init'
  MATRESP = MATSTATE  for action = 'stif'
  MATRESP = MATSTATE  for action = 'forc'
  MATRESP = MATPOST   for action = 'post'
  MATRESP is empty    for unsupported keywords

### State

MATSTATE is a data structure with information about the current material state in fields

- eps    = total strain (tensor for 2d or 3d)
- Deps   = strain increments from last convergence
- DDeps  = strain increments from last iteration
- epsdot = strain rate (tensor for 2d or 3d)
- km     = material stiffness matrix; returned under ACTION = 'stif'
- sig    = stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'
- Past   = material history variables at last converged state
- Pres   = current values of material history variables

### Data

  MATDATA is a data structure with material property information; it has the fields
        E  = initial modulus
        fy = yield strength
        Eh = post-yield modulus

### Post

  MATPOST is a data structure with material response information for post-processing in fields
        eps = total strain
        sig = uniaxial stress

## BiLinHyst1dMat 

Bilinear hysteretic force-deformation relation with pinching

  >MATRESP = BILINHYST1dMAT (ACTION,MATNO,MATDATA,MATSTATE)

### Action

  the character variable ACTION should have one of the following values
  ACTION = 'chec' function checks material property data for omissions and returns default values in MATDATA
           'init' function returns the material history variables in MATSTATE
           'forc' function returns the material stress (tensor) in MATSTATE
           'stif' function returns the material tangent modulus and the stress (tensor) in MATSTATE
           'post' function returns data structure MATPOST with post-processing information
  depending on the value of character variable ACTION the function returns information in data structure MATRESP
  for the material with number MAT_NO; data structure MATDATA supplies the material property data

### Response
  
  data structure MATRESP stands for one of the following data objects depending on value of ACTION 
  MATRESP = MATDATA   for action = 'chec'
  MATRESP = MATSTATE  for action = 'init'
  MATRESP = MATSTATE  for action = 'stif'
  MATRESP = MATSTATE  for action = 'forc'
  MATRESP = MATPOST   for action = 'post'
  MATRESP is empty    for unsupported keywords

### State
  
MATSTATE is a data structure with information about the current material state in fields

- eps    : total strain (tensor for 2d or 3d)
- Deps   : strain increments from last convergence
- DDeps  : strain increments from last iteration
- epsdot : strain rate (tensor for 2d or 3d)
- km     : material tangent modulus; returned under ACTION = 'stif'
- sig    : stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'
- Past   : material history variables at last converged state
- Pres   : current values of material history variables
  
### Data
  
MATDATA is a data structure with material property information in fields

- sig1p  = positive stress at first transition
- eps1p  = positive strain at first transition
- sig2p  = ultimate positive stress
- eps2p  = ultimate positive strain
- sig1n  = negative stress at first transition
- eps1n  = negative strain at first transition
- sig2n  = ultimate negative stress
- eps2n  = ultimate negative strain
- pnchx(+ve ; -ve) = x-pinching parameters under +ve and -ve deformation 
- pnchy(+ve ; -ve) = y-pinching parameters under +ve and -ve deformation

### Post
  
MATPOST is a data structure with material response information for post-processing in fields

- eps = total strain
- sig = uniaxial stress

## BiLinInel1dMat

uniaxial stress-strain relation for bilinear inelastic material

  MATRESP = BiLinINEL1dMAT (ACTION,MATNO,MATDATA,MATSTATE)
  function determines the uniaxial stress-strain relation for  bilinear inelastic material
  
### Action
  
  the character variable ACTION should have one of the following values
  ACTION = 'chec' function checks material property data for omissions and returns default values in MATDATA
           'init' function returns the material history variables in MATSTATE
           'forc' function returns the material stress (tensor) in MATSTATE
           'stif' function returns the material tangent modulus and the stress (tensor) in MATSTATE
           'post' function returns data structure MATPOST with post-processing information
  depending on the value of character variable ACTION the function returns information in data structure MATRESP
  for the material with number MAT_NO; data structure MATDATA supplies the material property data
  
### Response
  
  data structure MATRESP stands for one of the following data objects depending on value of ACTION 
  MATRESP = MATDATA   for action = 'chec'
  MATRESP = MATSTATE  for action = 'init'
  MATRESP = MATSTATE  for action = 'stif'
  MATRESP = MATSTATE  for action = 'forc'
  MATRESP = MATPOST   for action = 'post'
  MATRESP is empty    for unsupported keywords
  
### State
  
MATSTATE is a data structure with information about the current material state in fields

- eps    = total strain (tensor for 2d or 3d)
- Deps   = strain increments from last convergence
- DDeps  = strain increments from last iteration
- epsdot = strain rate (tensor for 2d or 3d)
- km     = material stiffness matrix; returned under ACTION = 'stif'
- sig    = stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'
- Past   = material history variables at last converged state
- Pres   = current values of material history variables
  
### Data
  
  MATDATA is a data structure with material property information; it has the fields
        E  = initial modulus
        fy = yield strength
        Eh = post-yield modulus
  
### Post
  
  MATPOST is a data structure with material response information for post-processing in fields
        eps = total strain
        sig = uniaxial stress

## BiLinOrOr1dMat

uniaxial stress-strain relation for bilinear origin-oriented material

MATRESP = BILINOROR1dMAT (ACTION,MATNO,MATDATA,MATSTATE)
Uniaxial stress-strain relation for bilinear origin-oriented material
  
### Action
  
the character variable ACTION should have one of the following values
ACTION = 'chec' function checks material property data for omissions and returns default values in MATDATA

- 'data' function prints material properties in output file IOW
- 'hist' function returns the material history variables in MATSTATE
- 'forc' function returns the material stress (tensor) in MATSTATE
- 'stif' function returns the material tangent modulus and the stress (tensor) in MATSTATE
- 'post' function returns data structure MATPOST with post-processing information

depending on the value of character variable ACTION the function returns information in data structure MATRESP
for the material with number MAT_NO; data structure MATDATA supplies the material property data

### Response
  
  data structure MATRESP stands for one of the following data objects depending on value of ACTION 
  MATRESP = MATDATA   for action = 'chec'
  MATRESP = MATSTATE  for action = 'hist'
  MATRESP = MATSTATE  for action = 'stif'
  MATRESP = MATSTATE  for action = 'forc'
  MATRESP = MATPOST   for action = 'post'
  MATRESP is empty    for action = 'data' and for unsupported keywords
  
### State
  
MATSTATE is a data structure with information about the current material state in fields

- eps    = total strain (tensor for 2d or 3d)
- Deps   = strain increments from last convergence
- DDeps  = strain increments from last iteration
- epsdot = strain rate (tensor for 2d or 3d)
- km     = material stiffness matrix; returned under ACTION = 'stif'
- sig    = stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'
- Past   = material history variables at last converged state
- Pres   = current values of material history variables
  
### Data
  
  MATDATA is a data structure with material property information; it has the fields
        E  = initial modulus
        fy = yield strength
        Eh = post-yield modulus
  
### Post
  
  MATPOST is a data structure with material response information for post-processing in fields
         eps = total strain
         sig = uniaxial stress

## BiLinPKOr1dMat

uniaxial stress-strain relation for bilinear origin-oriented material

MATRESP = BILINPKOR1dMAT (ACTION,MATNO,MATDATA,MATSTATE)
Uniaxial stress-strain relation for bilinear origin-oriented material
  
### Action

  ACTION = 'chec' function checks material property data for omissions and returns default values in MATDATA
           'data' function prints material properties in output file IOW
           'hist' function returns the material history variables in MATSTATE
           'forc' function returns the material stress (tensor) in MATSTATE
           'stif' function returns the material tangent modulus and the stress (tensor) in MATSTATE
           'post' function returns data structure MATPOST with post-processing information
  depending on the value of character variable ACTION the function returns information in data structure MATRESP
  for the material with number MAT_NO; data structure MATDATA supplies the material property data
  
### Response
  
  data structure MATRESP stands for one of the following data objects depending on value of ACTION 
  MATRESP = MATDATA   for action = 'chec'
  MATRESP = MATSTATE  for action = 'hist'
  MATRESP = MATSTATE  for action = 'stif'
  MATRESP = MATSTATE  for action = 'forc'
  MATRESP = MATPOST   for action = 'post'
  MATRESP is empty    for action = 'data' and for unsupported keywords
  
### State

MATSTATE is a data structure with information about the current material state in fields

- eps    = total strain (tensor for 2d or 3d)
- Deps   = strain increments from last convergence
- DDeps  = strain increments from last iteration
- epsdot = strain rate (tensor for 2d or 3d)
- km     = material stiffness matrix; returned under ACTION = 'stif'
- sig    = stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'
- Past   = material history variables at last converged state
- Pres   = current values of material history variables
  
### Data

  MATDATA is a data structure with material property information; it has the fields
         E  = initial modulus
         fy = yield strength
         Eh = post-yield modulus
  
### Post

  MATPOST is a data structure with material response information for post-processing in fields
         eps = total strain
         sig = uniaxial stress

## GMP1DMAT

uniaxial stress-strain relation for Giuffre-Menegotto-Pinto hysteretic material

MATRESP = GMP1DMAT (ACTION,MATNO,MATDATA,MATSTATE)
function determines the uniaxial stress-strain relation for Giuffre-Menegotto-Pinto hysteretic material
  
### Action

  ACTION = 'chec' function checks material property data for omissions and returns default values in MATDATA
           'init' function returns the material history variables in MATSTATE
           'forc' function returns the material stress (tensor) in MATSTATE
           'stif' function returns the material tangent modulus and the stress (tensor) in MATSTATE
           'post' function returns data structure MATPOST with post-processing information
  depending on the value of character variable ACTION the function returns information in data structure MATRESP
  for the material with number MAT_NO; data structure MATDATA supplies the material property data
  
  -------------------------------------------------------------------
  
  data structure MATRESP stands for one of the following data objects depending on value of ACTION 
  MATRESP = MATDATA   for action = 'chec'
  MATRESP = MATSTATE  for action = 'init'
  MATRESP = MATSTATE  for action = 'stif'
  MATRESP = MATSTATE  for action = 'forc'
  MATRESP = MATPOST   for action = 'post'
  MATRESP is empty    for unsupported keywords
  
### State

MATSTATE is a data structure with information about the current material state in fields

- eps    = total strain (tensor for 2d or 3d)
- Deps   = strain increments from last convergence
- DDeps  = strain increments from last iteration
- epsdot = strain rate (tensor for 2d or 3d)
- km     = material tangent modulus; returned under ACTION = 'stif'
- sig    = stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'
- Past   = material history variables at last converged state
- Pres   = current values of material history variables
  
### Data

  MATDATA is a data structure with material property information in fields
         E   = initial modulus
         fy  = yield strength
         b   = strain hardening ratio
         R0  = exp transition elastic-plastic  (default value 20)
         cR1 = coefficient for variation of R0 (default value 0.925)
         cR2 = coefficient for variation of R0 (default value 0.15)
         a1  = isotropic hardening (IH) coefficient in compression (default value 0)
         a2  = trigger strain ductility for IH      in compression (default value 0)
         a3  = isotropic hardening (IH) coefficient in tension     (default value 0)
         a4  = trigger strain ductility for IH      in tension     (default value 0)
  
### Post

  MATPOST is a data structure with material response information for post-processing in fields
         eps = total strain
         sig = uniaxial stress

## InelJ2PwLH3DMat

inelastic 3d material model with J2 plasticity and linear kinematic and isotropic hardening

MATRESP = INELJ2PwLH3DMAT (ACTION,MAT_NO,MATDATA,MATSTATE)
Stress-strain relation for an inelastic 3d material model based on J2 plasticity with isotropic and kinematic hardening
  
### Action

  ACTION = 'chec' function checks material property data for omissions and returns default values in MATDATA
           'init' function returns the material history variables in MATSTATE
           'forc' function returns the material stress (tensor) in MATSTATE
           'stif' function returns the material tangent modulus and the stress (tensor) in MATSTATE
           'post' function returns data structure MATPOST with post-processing information
  depending on the value of character variable ACTION the function returns information in data structure MATRESP
  for the material with number MAT_NO; data structure MATDATA supplies the material property data
  
### Response

  data structure MATRESP stands for one of the following data objects depending on value of ACTION 
  MATRESP = MATDATA   for action = 'chec'
  MATRESP = MATSTATE  for action = 'init'
  MATRESP = MATSTATE  for action = 'stif'
  MATRESP = MATSTATE  for action = 'forc'
  MATRESP = MATPOST   for action = 'post'
  
### State
  
MATSTATE is a data structure with information about the current material state in fields

- eps    = total strain tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23
- Deps   = strain increments from last convergence
- DDeps  = strain increments from last iteration
- epsdot = strain rate tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23
- km     = material stiffness matrix; returned under ACTION = 'stif'
- sig    = stress tensor in 6x1 vector form; returned under ACTION = 'stif' or 'forc'
- Past   = material history variables at last converged state
- Pres   = current values of material history variables
  
### Data
  
  MATDATA is a data structure with material property information; it has the fields
        E  = initial modulus
        fy = yield strength
        nu = Poisson ratio               (default = 0)
        Hk = kinematic hardening modulus (default = 0)
        Hi = isotropic hardening modulus (default = 0)
  
### Post
  
  MATPOST is a data structure with material response information for post-processing in fields
        eps   =         strain tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23
        sig   =         stress tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23
        eps_p = plastic strain tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23

## InelLPwLH1dMAT

inelastic linear-plastic 1d model with linear kinematic and isotropic hardening

MATRESP = INELLPwLH1dMAT (ACTION,MAT_NO,MATDATA,MATSTATE)
Material state under total strain EPSI for an inelastic linear-plastic 1d model with linear kinematic and isotropic hardening with the return map algorithm; the plastic strain EPS_P, the back stress SIG_B and the isotropic hardening variable ALPHA are the history variables of the model

Reference: JC Simo and TJR Hughes, Computational Inelasticity, pp. 43-45
  
### Action

  ACTION = 'chec' function checks material property data for omissions and returns default values in MATDATA
           'init' function returns the material history variables in MATSTATE
           'forc' function returns the material stress (tensor) in MATSTATE
           'stif' function returns the material tangent modulus and the stress (tensor) in MATSTATE
           'post' function returns data structure MATPOST with post-processing information
  depending on the value of character variable ACTION the function returns information in data structure MATRESP
  for the material with number MAT_NO; data structure MATDATA supplies the material property data
  
### Response
  
  data structure MATRESP stands for one of the following data objects depending on value of ACTION
  MATRESP = MATDATA   for action = 'chec'
  MATRESP = MATSTATE  for action = 'hist'
  MATRESP = MATSTATE  for action = 'stif'
  MATRESP = MATSTATE  for action = 'forc'
  MATRESP = MATPOST   for action = 'post'
  MATRESP is empty    for unsupported keywords
  
### State
  
MATSTATE is a data structure with information about the current material state in fields

- eps    = total strain
- Deps   = strain increments from last convergence
- DDeps  = strain increments from last iteration
- epsdot = strain rate
- km     = material stiffness matrix; returned under ACTION = 'stif'
- sig    = stress; returned under ACTION = 'stif' or 'forc'
- Past   = material history variables at last converged state
- Pres   = current values of material history variables
- Past and Pres contain the following history variable(s):
  - eps_p = plastic strain
  - alpha = isotropic hardening variable
  - sig_b = back stress (for kinematic hardening)

### Data

  MATDATA is a data structure with material property information; it has the fields
        E  = initial modulus
        fy = yield strength
        Hi = isotropic plastic   modulus
        Hk = kinematic hardening modulus

### Post
  
  MATPOST is a data structure with material response information for post-processing in fields
        eps   = total strain
        sig   = uniaxial stress
        eps_p = plastic strain

## MANDERCONCR1DMAT

hysteretic concrete stress-strain relation after Mander

MATRESP = MANDERCONCR1DMAT (ACTION,MATNO,MATDATA,MATSTATE)
Uniaxial stress-strain relation for the Mander material model

### Action

  ACTION = 'chec' function checks material property data for omissions and returns default values in MATDATA
           'init' function returns the material history variables in MATSTATE
           'forc' function returns the material stress (tensor) in MATSTATE
           'stif' function returns the material tangent modulus and the stress (tensor) in MATSTATE
           'post' function returns data structure MATPOST with post-processing information
  depending on the value of character variable ACTION the function returns information in data structure MATRESP
  for the material with number MAT_NO; data structure MATDATA supplies the material property data
  
### Response
  
  data structure MATRESP stands for one of the following data objects depending on value of ACTION 
  MATRESP = MATDATA   for action = 'chec'
  MATRESP = MATSTATE  for action = 'init'
  MATRESP = MATSTATE  for action = 'stif'
  MATRESP = MATSTATE  for action = 'forc'
  MATRESP = MATPOST   for action = 'post'
  MATRESP is empty    for unsupported keywords
  
### State
  
MATSTATE is a data structure with information about the current material state in fields

- eps    = total strain (tensor for 2d or 3d)
- Deps   = strain increments from last convergence
- DDeps  = strain increments from last iteration
- epsdot = strain rate (tensor for 2d or 3d)
- km     = material tangent modulus; returned under ACTION = 'stif'
- sig    = stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'
- Past   = material history variables at last converged state
- Pres   = current values of material history variables
  
### Data
  
    MATDATA is a data structure with material property information in fields
         fc    = compressive strength for unconfined concrete
         epc0  = strain at compressive strength for unconfined concrete
         Ec    = initial modulus for unconfined concrete
         Kfc   = ratio of confined to unconfined concrete strength
  
### Post
  
  MATPOST is a data structure with material response information for post-processing in fields
         eps = total strain
         sig = uniaxial stress