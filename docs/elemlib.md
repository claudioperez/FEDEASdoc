# Element Library<div class="table-responsive">
<table class="table"><thead> 
         <tr> 
             <th scope="col">#</th> 
             <th scope="col">Element</th> 
             <th scope="col">Description</th> 
         </tr> 
         </thead> 
 <tbody>
	<tr class="accordion-toggle collapsed" data-toggle="collapse" id="accordionDinel2dFrm_EBwDF" data-parent="#accordionDinel2dFrm_EBwDF" href="#collapseDinel2dFrm_EBwDF"><td class="expand-button"></td>
	<td><img src="../matlabicon.gif" alt="" border="">&nbsp;<a href="Dinel2dFrm_EBwDF.html">Dinel2dFrm_EBwDF</a></td>
	<td>2d-frame element with distributed inelasticity (displacement formulation) </td></tr><tr class="hide-table-padding"> 
 <td></td>                   <td colspan="3">                    <div id="collapseDinel2dFrm_EBwDF" class="collapse in p-3">
<b>Parameters</b>
<ul>
<li> <code>w</code>: uniform element load ( w(1) = longitudinal, w(2) = transverse )</li>
<li> <code>jntoff</code>: rigid joint offsets in global X and Y at element ends column 1 for node i, column 2 for node j</li>
</ul>

<b>State</b>
<ul>
<li> <code>u</code>: vector of total element displacements in global reference</li>
<li> <code>Du</code>: vector of element displacement increments from last convergence</li>
<li> <code>DDu</code>: vector of element displacement increments from last iteration</li>
<li> <code>ke</code>: element stiffness matrix in global reference; updated under ACTION = 'stif'</li>
<li> <code>p</code>: element resisting force vector in global reference; updated under ACTION = 'stif' or 'forc'</li>
<li> <code>Past</code>: element history variables at last converged state</li>
<li> <code>Pres</code>: current element history variables</li>
<li> <code>lamda</code>: row vector of current load factor(s)</li>
</ul>
<div class="col-6"><img src="../img/Dinel2dFrm_EBwDF.png"></div></td> 
 </tr>
	<tr class="accordion-toggle collapsed" data-toggle="collapse" id="accordionDinel2dFrm_EBwFF" data-parent="#accordionDinel2dFrm_EBwFF" href="#collapseDinel2dFrm_EBwFF"><td class="expand-button"></td>
	<td><img src="../matlabicon.gif" alt="" border="">&nbsp;<a href="Dinel2dFrm_EBwFF.html">Dinel2dFrm_EBwFF</a></td>
	<td>2d-frame element with distributed inelasticity (force formulation) </td></tr><tr class="hide-table-padding"> 
 <td></td>                   <td colspan="3">                    <div id="collapseDinel2dFrm_EBwFF" class="collapse in p-3">
<b>Parameters</b>
<ul>
<li> <code>w</code>: uniform element load ( w(1) = longitudinal, w(2) = transverse )</li>
</ul>

<b>State</b>
<ul>
<li> <code>u</code>: vector of total element displacements in global reference</li>
<li> <code>Du</code>: vector of element displacement increments from last convergence</li>
<li> <code>DDu</code>: vector of element displacement increments from last iteration</li>
<li> <code>ke</code>: element stiffness matrix in global reference; updated under ACTION = 'stif'</li>
<li> <code>p</code>: element resisting force vector in global reference; updated under ACTION = 'stif' or 'forc'</li>
<li> <code>Past</code>: element history variables at last converged state</li>
<li> <code>Pres</code>: current element history variables</li>
<li> <code>lamda</code>: row vector of current load factor(s)</li>
</ul>
<div class="col-6"><img src="../img/Dinel2dFrm_EBwFF.png"></div></td> 
 </tr>
	<tr class="accordion-toggle collapsed" data-toggle="collapse" id="accordionInel2dFrm_wLHNMYS" data-parent="#accordionInel2dFrm_wLHNMYS" href="#collapseInel2dFrm_wLHNMYS"><td class="expand-button"></td>
	<td><img src="../matlabicon.gif" alt="" border="">&nbsp;<a href="Inel2dFrm_wLHNMYS.html">Inel2dFrm_wLHNMYS</a></td>
	<td>2d linear elastic frame element with linear plastic hardening axial-flexure hinges </td></tr><tr class="hide-table-padding"> 
 <td></td>                   <td colspan="3">                    <div id="collapseInel2dFrm_wLHNMYS" class="collapse in p-3">
<b>Parameters</b>
<ul>
<li> <code>rho</code>: mass density</li>
<li> <code>A</code>: cross sectional area</li>
<li> <code>I</code>: moment of inertia</li>
<li> <code>E</code>: modulus of elasticity</li>
<li> <code>Np</code>: plastic axial capacity of element</li>
<li> <code>Mp</code>: plastic moment capacity of element</li>
<li> <code>GPYSC</code>: polynomial exponents for plastic surface (see help for function GPYS)</li>
<li> <code>Hir</code>: isotropic hardening ratio for flexural end i and j</li>
<li> <code>Hkr</code>: kinematic hardening ratio for axial, flexural end i and end j</li>
<li> <code>w</code>: uniform element load ( w(1) = longitudinal, w(2) = transverse )</li>
<li> <code>jntoff</code>: rigid joint offsets in global X and Y at element ends;</li>
<li> <code>LdIdx</code>: load history no for element loading in x-direction</li>
<li> <code>LdIdy</code>: load history no for element loading in y-direction</li>
<li> <code>Wtol</code>: incremental work tolerance for state convergence</li>
<li> <code>MaxIter</code>: maximum number of iterations for state convergence</li>
<li> <code>SubDivNo</code>: number of element deformation subdivisions</li>
</ul>

<b>State</b>
<ul>
<div class="col-6"><img src="../img/Inel2dFrm_wLHNMYS.png"></div></td> 
 </tr>
	<tr class="accordion-toggle collapsed" data-toggle="collapse" id="accordionInel2dFrm_wLPPM" data-parent="#accordionInel2dFrm_wLPPM" href="#collapseInel2dFrm_wLPPM"><td class="expand-button"></td>
	<td><img src="../matlabicon.gif" alt="" border="">&nbsp;<a href="Inel2dFrm_wLPPM.html">Inel2dFrm_wLPPM</a></td>
	<td>2d frame linear elastic element perfectly plastic flexural response </td></tr><tr class="hide-table-padding"> 
 <td></td>                   <td colspan="3">                    <div id="collapseInel2dFrm_wLPPM" class="collapse in p-3">
<b>Parameters</b>
<ul>

<b>State</b>
<ul>
<div class="col-6"><img src="../img/Inel2dFrm_wLPPM.png"></div></td> 
 </tr>
	<tr class="accordion-toggle collapsed" data-toggle="collapse" id="accordionInel2dFrm_wOneComp" data-parent="#accordionInel2dFrm_wOneComp" href="#collapseInel2dFrm_wOneComp"><td class="expand-button"></td>
	<td><img src="../matlabicon.gif" alt="" border="">&nbsp;<a href="Inel2dFrm_wOneComp.html">Inel2dFrm_wOneComp</a></td>
	<td>one component 2d frame element with rigid-linear hardening end hinges </td></tr><tr class="hide-table-padding"> 
 <td></td>                   <td colspan="3">                    <div id="collapseInel2dFrm_wOneComp" class="collapse in p-3">
<b>Parameters</b>
<ul>
<li> <code>rho</code>: mass density</li>
<li> <code>E</code>: Young's modulus</li>
<li> <code>A</code>: cross-sectional area</li>
<li> <code>I</code>: moment of inertia</li>
<li> <code>Mp</code>: plastic moment capacity at end nodes i & j ( Mp = [Mpi, Mpj] )</li>
<li> <code>Hi</code>: isotropic plastic modulus</li>
<li> <code>Hk</code>: kinematic modulus</li>
<li> <code>w</code>: uniform element load ( w(1) = longitudinal, w(2) = transverse )</li>
<li> <code>jntoff</code>: rigid joint offsets in global X and Y at element ends; column 1 for node i, column 2 for node j</li>
</ul>

<b>State</b>
<ul>
<div class="col-6"><img src="../img/Inel2dFrm_wOneComp.png"></div></td> 
 </tr>
	<tr class="accordion-toggle collapsed" data-toggle="collapse" id="accordionInel2dFrm_wTwoComp" data-parent="#accordionInel2dFrm_wTwoComp" href="#collapseInel2dFrm_wTwoComp"><td class="expand-button"></td>
	<td><img src="../matlabicon.gif" alt="" border="">&nbsp;<a href="Inel2dFrm_wTwoComp.html">Inel2dFrm_wTwoComp</a></td>
	<td>two component 2d frame element (linear + linear-perfectly plastic) </td></tr><tr class="hide-table-padding"> 
 <td></td>                   <td colspan="3">                    <div id="collapseInel2dFrm_wTwoComp" class="collapse in p-3">
<b>Parameters</b>
<ul>

<b>State</b>
<ul>
<div class="col-6"><img src="../img/Inel2dFrm_wTwoComp.png"></div></td> 
 </tr>
	<tr class="accordion-toggle collapsed" data-toggle="collapse" id="accordionLE2dFrm" data-parent="#accordionLE2dFrm" href="#collapseLE2dFrm"><td class="expand-button"></td>
	<td><img src="../matlabicon.gif" alt="" border="">&nbsp;<a href="LE2dFrm.html">LE2dFrm</a></td>
	<td>2d LE frame element under linear or nonlinear geometry </td></tr><tr class="hide-table-padding"> 
 <td></td>                   <td colspan="3">                    <div id="collapseLE2dFrm" class="collapse in p-3">
<b>Parameters</b>
<ul>
<li> <code>A</code>: cross sectional area</li>
<li> <code>E</code>: modulus of elasticity</li>
<li> <code>I</code>: moment of inertia</li>
<li> <code>Mp</code>: plastic moment capacity</li>
<li> <code>rho</code>: mass density</li>
<li> <code>jntoff</code>: rigid joint offsets in global X and Y at element ends; column 1 for node i, column 2 for node j</li>
</ul>

<b>State</b>
<ul>
<li> <code>u</code>: vector of total element displacements in global reference</li>
<li> <code>Du</code>: vector of element displacement increments from last convergence</li>
<li> <code>DDu</code>: vector of element displacement increments from last iteration</li>
<li> <code>ke</code>: element stiffness matrix in global reference; updated under ACTION = 'stif'</li>
<li> <code>p</code>: element resisting force vector in global reference; updated under ACTION = 'stif' or 'forc'</li>
<li> <code>Past</code>: element history variables at last converged state</li>
<li> <code>Pres</code>: current element history variables</li>
<li> <code>lamda</code>: row vector of current load factor(s)</li>
</ul>
<div class="col-6"><img src="../img/LE2dFrm.png"></div></td> 
 </tr>
	<tr class="accordion-toggle collapsed" data-toggle="collapse" id="accordionLE2dFrm_wPdelta" data-parent="#accordionLE2dFrm_wPdelta" href="#collapseLE2dFrm_wPdelta"><td class="expand-button"></td>
	<td><img src="../matlabicon.gif" alt="" border="">&nbsp;<a href="LE2dFrm_wPdelta.html">LE2dFrm_wPdelta</a></td>
	<td>2d linear elastic frame element with P-delta effect under linear or nonlinear geometry </td></tr><tr class="hide-table-padding"> 
 <td></td>                   <td colspan="3">                    <div id="collapseLE2dFrm_wPdelta" class="collapse in p-3">
<b>Parameters</b>
<ul>

<b>State</b>
<ul>
<div class="col-6"><img src="../img/LE2dFrm_wPdelta.png"></div></td> 
 </tr>
	<tr class="accordion-toggle collapsed" data-toggle="collapse" id="accordionHomoCircSecw1dMat" data-parent="#accordionHomoCircSecw1dMat" href="#collapseHomoCircSecw1dMat"><td class="expand-button"></td>
	<td><img src="../matlabicon.gif" alt="" border="">&nbsp;<a href="HomoCircSecw1dMat.html">HomoCircSecw1dMat</a></td>
	<td>None </td></tr><tr class="hide-table-padding"> 
 <td></td>                   <td colspan="3">                    <div id="collapseHomoCircSecw1dMat" class="collapse in p-3">
<b>Parameters</b>
<ul>
<li> <code>R(1:2)</code>: outer radius and inner radius of section (default = R(1) only)</li>
<li> <code>nr</code>: no of integration points (fibers) over radius (default=5)(thus 2 x nr across diameter)</li>
<li> <code>nth</code>: no of integration points (fibers) in circumferential direction (used for 3d only),(default=10)</li>
<li> <code>Rdrat</code>: ratio of inner to outer radius for switching to uniform dicretization</li>
<li> <code>IntTyp</code>: function name for section integration ('Midpoint' or 'Cubature')</li>
<li> <code>MatName</code>: function name for material uniaxial stress-strain relation</li>
<li> <code>MatData</code>: data structure with material property data</li>
</ul>

<b>State</b>
<ul>
<div class="col-6"><img src="../img/HomoCircSecw1dMat.png"></div></td> 
 </tr>
	<tr class="accordion-toggle collapsed" data-toggle="collapse" id="accordionHomoRectSecw1dMat" data-parent="#accordionHomoRectSecw1dMat" href="#collapseHomoRectSecw1dMat"><td class="expand-button"></td>
	<td><img src="../matlabicon.gif" alt="" border="">&nbsp;<a href="HomoRectSecw1dMat.html">HomoRectSecw1dMat</a></td>
	<td>None </td></tr><tr class="hide-table-padding"> 
 <td></td>                   <td colspan="3">                    <div id="collapseHomoRectSecw1dMat" class="collapse in p-3">
<b>Parameters</b>
<ul>
<li> <code>d</code>: section depth</li>
<li> <code>b</code>: section width</li>
<li> <code>ny</code>: no of integration points (fibers) in y (default = 10)</li>
<li> <code>nz</code>: no of integration points (fibers) in z (default = 1 for 2d and 10 for 3d)</li>
<li> <code>IntTyp</code>: function name for section integration</li>
<li> <code>MatName</code>: function name for material uniaxial stress-strain relation</li>
<li> <code>MatData</code>: data structure with material property data</li>
</ul>

<b>State</b>
<ul>
<li> <code>e</code>: vector of total section deformations</li>
<li> <code>De</code>: vector of section deformation increments from last convergence</li>
<li> <code>DDe</code>: vector of section deformation increments from last iteration</li>
<li> <code>edot</code>: vector of section deformation rates</li>
<li> <code>ks</code>: section stiffness matrix; returned under ACTION = 'stif'</li>
<li> <code>s</code>: section resisting force vector; returned under ACTION = 'stif' or 'forc'</li>
<li> <code>Past</code>: section history variables at last converged state</li>
<li> <code>Pres</code>: current section history variables</li>
</ul>
<div class="col-6"><img src="../img/HomoRectSecw1dMat.png"></div></td> 
 </tr>
	<tr class="accordion-toggle collapsed" data-toggle="collapse" id="accordionHomoWFSecw1dMat" data-parent="#accordionHomoWFSecw1dMat" href="#collapseHomoWFSecw1dMat"><td class="expand-button"></td>
	<td><img src="../matlabicon.gif" alt="" border="">&nbsp;<a href="HomoWFSecw1dMat.html">HomoWFSecw1dMat</a></td>
	<td>None </td></tr><tr class="hide-table-padding"> 
 <td></td>                   <td colspan="3">                    <div id="collapseHomoWFSecw1dMat" class="collapse in p-3">
<b>Parameters</b>
<ul>

<b>State</b>
<ul>
<div class="col-6"><img src="../img/HomoWFSecw1dMat.png"></div></td> 
 </tr></tbody> 
 </table><script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" 			  integrity="sha256-4+XzXVhsDmqanXGHaHvgh1gMQKX40OUvDEBTu8JcmNs=" 			  crossorigin="anonymous"></script><script>$("a[id^=show_]").click(function(event) {$("#extra_" + $(this).attr('id').substr(5)).slideToggle("fast"); 
 event.preventDefault();})</script>