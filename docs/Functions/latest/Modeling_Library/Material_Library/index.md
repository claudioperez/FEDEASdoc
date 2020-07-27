---
title: Material Collection
...
# Material Library<div class="table-responsive">
<table class="table"><thead> 
         <tr> 
             <th scope="col">#</th> 
             <th scope="col">Element</th> 
             <th scope="col">Description</th> 
         </tr> 
         </thead> 
 <tbody>
	<tr class="accordion-toggle collapsed" data-toggle="collapse" id="accordionBiLinElastic1dMat" data-parent="#accordionBiLinElastic1dMat" href="#collapseBiLinElastic1dMat"><td class="expand-button"></td>
	<td><img src="../matlabicon.gif" alt="" border="">&nbsp;<a href="BiLinElastic1dMat.html">BiLinElastic1dMat</a></td>
	<td>Uniaxial stress-strain relation for a bilinear elastic material </td></tr><tr class="hide-table-padding"> 
 <td></td>                   <td colspan="3">                    <div id="collapseBiLinElastic1dMat" class="collapse in p-3"><div class="row"><div class="col-6">
<b>Parameters</b>
<ul>
<li> <code>E</code>: initial modulus</li>
<li> <code>fy</code>: yield strength</li>
<li> <code>Eh</code>: post-yield modulus</li>
</ul>

<b>State</b>
<ul>
<li> <code>eps</code>: total strain (tensor for 2d or 3d)</li>
<li> <code>Deps</code>: strain increments from last convergence</li>
<li> <code>DDeps</code>: strain increments from last iteration</li>
<li> <code>epsdot</code>: strain rate (tensor for 2d or 3d)</li>
<li> <code>km</code>: material stiffness matrix; returned under ACTION = 'stif'</li>
<li> <code>sig</code>: stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'</li>
<li> <code>Past</code>: material history variables at last converged state</li>
<li> <code>Pres</code>: current values of material history variables</li>
</ul>
</div>
<div class="col-6"><img src="../img/BiLinElastic1dMat.png"></div></div>
</td> 
 </tr>
	<tr class="accordion-toggle collapsed" data-toggle="collapse" id="accordionBiLinHyst1dMat" data-parent="#accordionBiLinHyst1dMat" href="#collapseBiLinHyst1dMat"><td class="expand-button"></td>
	<td><img src="../matlabicon.gif" alt="" border="">&nbsp;<a href="BiLinHyst1dMat.html">BiLinHyst1dMat</a></td>
	<td>Bilinear hysteretic force-deformation relation with pinching </td></tr><tr class="hide-table-padding"> 
 <td></td>                   <td colspan="3">                    <div id="collapseBiLinHyst1dMat" class="collapse in p-3"><div class="row"><div class="col-6">
<b>Parameters</b>
<ul>
<li> <code>sig1p</code>: positive stress at first transition</li>
<li> <code>eps1p</code>: positive strain at first transition</li>
<li> <code>sig2p</code>: ultimate positive stress</li>
<li> <code>eps2p</code>: ultimate positive strain</li>
<li> <code>sig1n</code>: negative stress at first transition</li>
<li> <code>eps1n</code>: negative strain at first transition</li>
<li> <code>sig2n</code>: ultimate negative stress</li>
<li> <code>eps2n</code>: ultimate negative strain</li>
<li> <code>pnchx(+ve ; -ve)</code>: x-pinching parameters under +ve and -ve deformation</li>
<li> <code>pnchy(+ve ; -ve)</code>: y-pinching parameters under +ve and -ve deformation</li>
</ul>

<b>State</b>
<ul>
<li> <code>eps</code>: total strain (tensor for 2d or 3d)</li>
<li> <code>Deps</code>: strain increments from last convergence</li>
<li> <code>DDeps</code>: strain increments from last iteration</li>
<li> <code>epsdot</code>: strain rate (tensor for 2d or 3d)</li>
<li> <code>km</code>: material tangent modulus; returned under ACTION = 'stif'</li>
<li> <code>sig</code>: stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'</li>
<li> <code>Past</code>: material history variables at last converged state</li>
<li> <code>Pres</code>: current values of material history variables</li>
</ul>
</div>
<div class="col-6"><img src="../img/BiLinHyst1dMat.png"></div></div>
</td> 
 </tr>
	<tr class="accordion-toggle collapsed" data-toggle="collapse" id="accordionBiLinInel1dMat" data-parent="#accordionBiLinInel1dMat" href="#collapseBiLinInel1dMat"><td class="expand-button"></td>
	<td><img src="../matlabicon.gif" alt="" border="">&nbsp;<a href="BiLinInel1dMat.html">BiLinInel1dMat</a></td>
	<td>Uniaxial stress-strain relation for bilinear inelastic material </td></tr><tr class="hide-table-padding"> 
 <td></td>                   <td colspan="3">                    <div id="collapseBiLinInel1dMat" class="collapse in p-3"><div class="row"><div class="col-6">
<b>Parameters</b>
<ul>
<li> <code>E</code>: initial modulus</li>
<li> <code>fy</code>: yield strength</li>
<li> <code>Eh</code>: post-yield modulus</li>
</ul>

<b>State</b>
<ul>
<li> <code>eps</code>: total strain (tensor for 2d or 3d)</li>
<li> <code>Deps</code>: strain increments from last convergence</li>
<li> <code>DDeps</code>: strain increments from last iteration</li>
<li> <code>epsdot</code>: strain rate (tensor for 2d or 3d)</li>
<li> <code>km</code>: material stiffness matrix; returned under ACTION = 'stif'</li>
<li> <code>sig</code>: stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'</li>
<li> <code>Past</code>: material history variables at last converged state</li>
<li> <code>Pres</code>: current values of material history variables</li>
</ul>
</div>
<div class="col-6"><img src="../img/BiLinInel1dMat.png"></div></div>
</td> 
 </tr>
	<tr class="accordion-toggle collapsed" data-toggle="collapse" id="accordionBiLinOrOr1dMat" data-parent="#accordionBiLinOrOr1dMat" href="#collapseBiLinOrOr1dMat"><td class="expand-button"></td>
	<td><img src="../matlabicon.gif" alt="" border="">&nbsp;<a href="BiLinOrOr1dMat.html">BiLinOrOr1dMat</a></td>
	<td>Uniaxial stress-strain relation for bilinear origin-oriented material </td></tr><tr class="hide-table-padding"> 
 <td></td>                   <td colspan="3">                    <div id="collapseBiLinOrOr1dMat" class="collapse in p-3"><div class="row"><div class="col-6">
<b>Parameters</b>
<ul>
<li> <code>E</code>: initial modulus</li>
<li> <code>fy</code>: yield strength</li>
<li> <code>Eh</code>: post-yield modulus</li>
</ul>

<b>State</b>
<ul>
<li> <code>eps</code>: total strain (tensor for 2d or 3d)</li>
<li> <code>Deps</code>: strain increments from last convergence</li>
<li> <code>DDeps</code>: strain increments from last iteration</li>
<li> <code>epsdot</code>: strain rate (tensor for 2d or 3d)</li>
<li> <code>km</code>: material stiffness matrix; returned under ACTION = 'stif'</li>
<li> <code>sig</code>: stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'</li>
<li> <code>Past</code>: material history variables at last converged state</li>
<li> <code>Pres</code>: current values of material history variables</li>
</ul>
</div>
<div class="col-6"><img src="../img/BiLinOrOr1dMat.png"></div></div>
</td> 
 </tr>
	<tr class="accordion-toggle collapsed" data-toggle="collapse" id="accordionBiLinPKOr1dMat" data-parent="#accordionBiLinPKOr1dMat" href="#collapseBiLinPKOr1dMat"><td class="expand-button"></td>
	<td><img src="../matlabicon.gif" alt="" border="">&nbsp;<a href="BiLinPKOr1dMat.html">BiLinPKOr1dMat</a></td>
	<td>Uniaxial stress-strain relation for bilinear origin-oriented material </td></tr><tr class="hide-table-padding"> 
 <td></td>                   <td colspan="3">                    <div id="collapseBiLinPKOr1dMat" class="collapse in p-3"><div class="row"><div class="col-6">
<b>Parameters</b>
<ul>
<li> <code>E</code>: initial modulus</li>
<li> <code>fy</code>: yield strength</li>
<li> <code>Eh</code>: post-yield modulus</li>
</ul>

<b>State</b>
<ul>
<li> <code>eps</code>: total strain (tensor for 2d or 3d)</li>
<li> <code>Deps</code>: strain increments from last convergence</li>
<li> <code>DDeps</code>: strain increments from last iteration</li>
<li> <code>epsdot</code>: strain rate (tensor for 2d or 3d)</li>
<li> <code>km</code>: material stiffness matrix; returned under ACTION = 'stif'</li>
<li> <code>sig</code>: stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'</li>
<li> <code>Past</code>: material history variables at last converged state</li>
<li> <code>Pres</code>: current values of material history variables</li>
</ul>
</div>
<div class="col-6"><img src="../img/BiLinPKOr1dMat.png"></div></div>
</td> 
 </tr>
	<tr class="accordion-toggle collapsed" data-toggle="collapse" id="accordionGMP1dMat" data-parent="#accordionGMP1dMat" href="#collapseGMP1dMat"><td class="expand-button"></td>
	<td><img src="../matlabicon.gif" alt="" border="">&nbsp;<a href="GMP1dMat.html">GMP1dMat</a></td>
	<td>Uniaxial stress-strain relation for Giuffre-Menegotto-Pinto hysteretic material </td></tr><tr class="hide-table-padding"> 
 <td></td>                   <td colspan="3">                    <div id="collapseGMP1dMat" class="collapse in p-3"><div class="row"><div class="col-6">
<b>Parameters</b>
<ul>
<li> <code>E</code>: initial modulus</li>
<li> <code>fy</code>: yield strength</li>
<li> <code>b</code>: strain hardening ratio</li>
<li> <code>R0</code>: exp transition elastic-plastic</li>
<li> <code>cR1</code>: coefficient for variation of R0</li>
<li> <code>cR2</code>: coefficient for variation of R0</li>
<li> <code>a1</code>: isotropic hardening (IH) coefficient in compression</li>
<li> <code>a2</code>: trigger strain ductility for IH in compression</li>
<li> <code>a3</code>: isotropic hardening (IH) coefficient in tension</li>
<li> <code>a4</code>: trigger strain ductility for IH in tension</li>
</ul>

<b>State</b>
<ul>
<li> <code>eps</code>: total strain (tensor for 2d or 3d)</li>
<li> <code>Deps</code>: strain increments from last convergence</li>
<li> <code>DDeps</code>: strain increments from last iteration</li>
<li> <code>epsdot</code>: strain rate (tensor for 2d or 3d)</li>
<li> <code>km</code>: material tangent modulus; returned under ACTION = 'stif'</li>
<li> <code>sig</code>: stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'</li>
<li> <code>Past</code>: material history variables at last converged state</li>
<li> <code>Pres</code>: current values of material history variables</li>
</ul>
</div>
<div class="col-6"><img src="../img/GMP1dMat.png"></div></div>
</td> 
 </tr>
	<tr class="accordion-toggle collapsed" data-toggle="collapse" id="accordionInelJ2PwLH3DMat" data-parent="#accordionInelJ2PwLH3DMat" href="#collapseInelJ2PwLH3DMat"><td class="expand-button"></td>
	<td><img src="../matlabicon.gif" alt="" border="">&nbsp;<a href="InelJ2PwLH3DMat.html">InelJ2PwLH3DMat</a></td>
	<td>inelastic 3d material model with J2 plasticity and linear kinematic and isotropic hardening </td></tr><tr class="hide-table-padding"> 
 <td></td>                   <td colspan="3">                    <div id="collapseInelJ2PwLH3DMat" class="collapse in p-3"><div class="row"><div class="col-6">
<b>Parameters</b>
<ul>
<li> <code>E</code>: initial modulus</li>
<li> <code>fy</code>: yield strength</li>
<li> <code>nu</code>: Poisson ratio</li>
<li> <code>Hk</code>: kinematic hardening modulus</li>
<li> <code>Hi</code>: isotropic hardening modulus</li>
</ul>

<b>State</b>
<ul>
<li> <code>eps</code>: total strain tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23</li>
<li> <code>Deps</code>: strain increments from last convergence</li>
<li> <code>DDeps</code>: strain increments from last iteration</li>
<li> <code>epsdot</code>: strain rate tensor in 6x1 vector form in the order 11, 22, 33, 12, 13, 23</li>
<li> <code>km</code>: material stiffness matrix; returned under ACTION = 'stif'</li>
<li> <code>sig</code>: stress tensor in 6x1 vector form; returned under ACTION = 'stif' or 'forc'</li>
<li> <code>Past</code>: material history variables at last converged state</li>
<li> <code>Pres</code>: current values of material history variables</li>
</ul>
</div>
<div class="col-6"><img src="../img/InelJ2PwLH3DMat.png"></div></div>
</td> 
 </tr>
	<tr class="accordion-toggle collapsed" data-toggle="collapse" id="accordionInelLPwLH1dMAT" data-parent="#accordionInelLPwLH1dMAT" href="#collapseInelLPwLH1dMAT"><td class="expand-button"></td>
	<td><img src="../matlabicon.gif" alt="" border="">&nbsp;<a href="InelLPwLH1dMAT.html">InelLPwLH1dMAT</a></td>
	<td>inelastic linear-plastic 1d model with linear kinematic and isotropic hardening. Material state under total strain EPSI for an inelastic linear-plastic 1d model with linear kinematic and isotropic hardening with the return map algorithm; the plastic strain EPS_P, the back stress SIG_B and the isotropic hardening variable ALPHA are the history variables of the model </td></tr><tr class="hide-table-padding"> 
 <td></td>                   <td colspan="3">                    <div id="collapseInelLPwLH1dMAT" class="collapse in p-3"><div class="row"><div class="col-6">
<b>Parameters</b>
<ul>
<li> <code>E</code>: initial modulus</li>
<li> <code>fy</code>: yield strength</li>
<li> <code>Hi</code>: isotropic plastic modulus</li>
<li> <code>Hk</code>: kinematic hardening modulus</li>
</ul>

<b>State</b>
<ul>
<li> <code>eps</code>: total strain</li>
<li> <code>Deps</code>: strain increments from last convergence</li>
<li> <code>DDeps</code>: strain increments from last iteration</li>
<li> <code>epsdot</code>: strain rate</li>
<li> <code>km</code>: material stiffness matrix; returned under ACTION = 'stif'</li>
<li> <code>sig</code>: stress; returned under ACTION = 'stif' or 'forc'</li>
<li> <code>Past</code>: material history variables at last converged state</li>
<li> <code>Pres</code>: current values of material history variables</li>
</ul>
</div>
<div class="col-6"><img src="../img/InelLPwLH1dMAT.png"></div></div>
</td> 
 </tr>
	<tr class="accordion-toggle collapsed" data-toggle="collapse" id="accordionMANDERCONCR1DMAT" data-parent="#accordionMANDERCONCR1DMAT" href="#collapseMANDERCONCR1DMAT"><td class="expand-button"></td>
	<td><img src="../matlabicon.gif" alt="" border="">&nbsp;<a href="MANDERCONCR1DMAT.html">MANDERCONCR1DMAT</a></td>
	<td>hysteretic concrete stress-strain relation after Mander </td></tr><tr class="hide-table-padding"> 
 <td></td>                   <td colspan="3">                    <div id="collapseMANDERCONCR1DMAT" class="collapse in p-3"><div class="row"><div class="col-6">
<b>Parameters</b>
<ul>
<li> <code>fc</code>: compressive strength for unconfined concrete</li>
<li> <code>epc0</code>: strain at compressive strength for unconfined concrete</li>
<li> <code>Ec</code>: initial modulus for unconfined concrete</li>
<li> <code>Kfc</code>: ratio of confined to unconfined concrete strength</li>
</ul>

<b>State</b>
<ul>
<li> <code>eps</code>: total strain (tensor for 2d or 3d)</li>
<li> <code>Deps</code>: strain increments from last convergence</li>
<li> <code>DDeps</code>: strain increments from last iteration</li>
<li> <code>epsdot</code>: strain rate (tensor for 2d or 3d)</li>
<li> <code>km</code>: material tangent modulus; returned under ACTION = 'stif'</li>
<li> <code>sig</code>: stress (tensor for 2d or 3d); returned under ACTION = 'stif' or 'forc'</li>
<li> <code>Past</code>: material history variables at last converged state</li>
<li> <code>Pres</code>: current values of material history variables</li>
</ul>
</div>
<div class="col-6"><img src="../img/MANDERCONCR1DMAT.png"></div></div>
</td> 
 </tr></tbody> 
 </table><script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" 			  integrity="sha256-4+XzXVhsDmqanXGHaHvgh1gMQKX40OUvDEBTu8JcmNs=" 			  crossorigin="anonymous"></script><script>$("a[id^=show_]").click(function(event) {$("#extra_" + $(this).attr('id').substr(5)).slideToggle("fast"); 
 event.preventDefault();})</script>
