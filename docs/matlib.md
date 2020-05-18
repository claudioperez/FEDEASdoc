# Material Library
## `BiLinElastic1dMat`
<details>
<summary>uniaxial stress-strain relation for a bilinear elastic material</summary>

**Parameters**
<ul>
<li> `E`: initial modulus</li>
<li> `fy`: yield strength</li>
<li> `Eh`: post-yield modulus</li>
</ul>

**State**
<ul>
<li> `eps`: total strain (tensor for 2d or 3d)</li>
<li> `Deps`: strain increments from last convergence</li>
<li> `DDeps`: strain increments from last iteration</li>
<li> `epsdot`: strain rate (tensor for 2d or 3d)</li>
<li> `km`: material stiffness matrix; returned under ACTION = 'stif'</li>
<li> `sig`: stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'</li>
<li> `Past`: material history variables at last converged state</li>
<li> `Pres`: current values of material history variables</li>
</ul>
</details>

## `BiLinHyst1dMat`
<details>
<summary>Bilinear hysteretic force-deformation relation with pinching</summary>

**Parameters**
<ul>
<li> `sig1p`: positive stress at first transition</li>
<li> `eps1p`: positive strain at first transition</li>
<li> `sig2p`: ultimate positive stress</li>
<li> `eps2p`: ultimate positive strain</li>
<li> `sig1n`: negative stress at first transition</li>
<li> `eps1n`: negative strain at first transition</li>
<li> `sig2n`: ultimate negative stress</li>
<li> `eps2n`: ultimate negative strain</li>
<li> `pnchx(+ve ; -ve)`: x-pinching parameters under +ve and -ve deformation</li>
<li> `pnchy(+ve ; -ve)`: y-pinching parameters under +ve and -ve deformation</li>
</ul>

**State**
<ul>
<li> `eps`: total strain (tensor for 2d or 3d)</li>
<li> `Deps`: strain increments from last convergence</li>
<li> `DDeps`: strain increments from last iteration</li>
<li> `epsdot`: strain rate (tensor for 2d or 3d)</li>
<li> `km`: material tangent modulus; returned under ACTION = 'stif'</li>
<li> `sig`: stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'</li>
<li> `Past`: material history variables at last converged state</li>
<li> `Pres`: current values of material history variables</li>
</ul>
</details>

## `BiLinInel1dMat`
<details>
<summary>uniaxial stress-strain relation for bilinear inelastic material</summary>

**Parameters**
<ul>
<li> `E`: initial modulus</li>
<li> `fy`: yield strength</li>
<li> `Eh`: post-yield modulus</li>
</ul>

**State**
<ul>
<li> `eps`: total strain (tensor for 2d or 3d)</li>
<li> `Deps`: strain increments from last convergence</li>
<li> `DDeps`: strain increments from last iteration</li>
<li> `epsdot`: strain rate (tensor for 2d or 3d)</li>
<li> `km`: material stiffness matrix; returned under ACTION = 'stif'</li>
<li> `sig`: stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'</li>
<li> `Past`: material history variables at last converged state</li>
<li> `Pres`: current values of material history variables</li>
</ul>
</details>

## `BiLinOrOr1dMat`
<details>
<summary>uniaxial stress-strain relation for bilinear origin-oriented material</summary>

**Parameters**
<ul>
<li> `E`: initial modulus</li>
<li> `fy`: yield strength</li>
<li> `Eh`: post-yield modulus</li>
</ul>

**State**
<ul>
<li> `eps`: total strain (tensor for 2d or 3d)</li>
<li> `Deps`: strain increments from last convergence</li>
<li> `DDeps`: strain increments from last iteration</li>
<li> `epsdot`: strain rate (tensor for 2d or 3d)</li>
<li> `km`: material stiffness matrix; returned under ACTION = 'stif'</li>
<li> `sig`: stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'</li>
<li> `Past`: material history variables at last converged state</li>
<li> `Pres`: current values of material history variables</li>
</ul>
</details>

## `BiLinPKOr1dMat`
<details>
<summary>uniaxial stress-strain relation for bilinear origin-oriented material</summary>

**Parameters**
<ul>
<li> `E`: initial modulus</li>
<li> `fy`: yield strength</li>
<li> `Eh`: post-yield modulus</li>
</ul>

**State**
<ul>
<li> `eps`: total strain (tensor for 2d or 3d)</li>
<li> `Deps`: strain increments from last convergence</li>
<li> `DDeps`: strain increments from last iteration</li>
<li> `epsdot`: strain rate (tensor for 2d or 3d)</li>
<li> `km`: material stiffness matrix; returned under ACTION = 'stif'</li>
<li> `sig`: stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'</li>
<li> `Past`: material history variables at last converged state</li>
<li> `Pres`: current values of material history variables</li>
</ul>
</details>

## `GMP1DMAT`
<details>
<summary>uniaxial stress-strain relation for Giuffre-Menegotto-Pinto hysteretic material</summary>

**Parameters**
<ul>

**State**
<ul>
</details>

## `InelJ2PwLH3DMat`
<details>
<summary>inelastic 3d material model with J2 plasticity and linear kinematic and isotropic hardening</summary>

**Parameters**
<ul>

**State**
<ul>
</details>

## `InelLPwLH1dMAT`
<details>
<summary>inelastic linear-plastic 1d model with linear kinematic and isotropic hardening. Material state under total strain EPSI for an inelastic linear-plastic 1d model with linear kinematic and isotropic hardening with the return map algorithm; the plastic strain EPS_P, the back stress SIG_B and the isotropic hardening variable ALPHA are the history variables of the model</summary>

**Parameters**
<ul>
<li> `E`: initial modulus</li>
<li> `fy`: yield strength</li>
<li> `Hi`: isotropic plastic   modulus</li>
<li> `Hk`: kinematic hardening modulus</li>
</ul>

**State**
<ul>
<li> `eps`: total strain</li>
<li> `Deps`: strain increments from last convergence</li>
<li> `DDeps`: strain increments from last iteration</li>
<li> `epsdot`: strain rate</li>
<li> `km`: material stiffness matrix; returned under ACTION = 'stif'</li>
<li> `sig`: stress; returned under ACTION = 'stif' or 'forc'</li>
<li> `Past`: material history variables at last converged state</li>
<li> `Pres`: current values of material history variables</li>
</ul>
</details>

## `MANDERCONCR1DMAT`
<details>
<summary>hysteretic concrete stress-strain relation after Mander</summary>

**Parameters**
<ul>
<li> `fc`: compressive strength for unconfined concrete</li>
<li> `epc0`: strain at compressive strength for unconfined concrete</li>
<li> `Ec`: initial modulus for unconfined concrete</li>
<li> `Kfc`: ratio of confined to unconfined concrete strength</li>
</ul>

**State**
<ul>
<li> `eps`: total strain (tensor for 2d or 3d)</li>
<li> `Deps`: strain increments from last convergence</li>
<li> `DDeps`: strain increments from last iteration</li>
<li> `epsdot`: strain rate (tensor for 2d or 3d)</li>
<li> `km`: material tangent modulus; returned under ACTION = 'stif'</li>
<li> `sig`: stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'</li>
<li> `Past`: material history variables at last converged state</li>
<li> `Pres`: current values of material history variables</li>
</ul>
</details>

