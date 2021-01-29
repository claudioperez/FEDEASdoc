
<!-- <a name="_top"></a>
<div><a href="../../_index.md">Home</a> &gt;  <a href="#">latest</a> &gt; <a href="_index.md">General_Functions</a> &gt; Create_Damping.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../_index.md"><img alt="<" border="0" src="../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href="_index.md">Index for latest\General_Functions&nbsp;<img alt=">" border="0" src="../../right.png"></a></td></tr></table>-->
# `Create_Damping`
<!-- <h1>Create_Damping
</h1> -->

## <a name="_name"></a>Purpose

<!-- <h2 id="purpose"><a name="_name"></a>Purpose</h2> -->

CREATE_DAMPING setup damping matrix of structural model

<!-- <div class="box"><strong>CREATE_DAMPING setup damping matrix of structural model</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function C = Create_Damping (type,Kf,Ml,zeta,mode)` 
## <a name="_description"></a>Description

<pre class="comment">CREATE_DAMPING setup damping matrix of structural model
  C = CREATE_DAMPING (TYPE,KF,ML,ZETA,MODE)
  function sets up damping matrix C according to character variable TYPE
  for a structure with free dof stiffness matrix KF and free dof lumped mass vector ML;
  the damping matrix is calibrated so that the mode numbers in row vector MODE have
  damping ratios as specified in row vector ZETA;
  character variable TYPE should be either 'StifProp', 'Caughey' or 'Modal'
  Note: Caughey with one mode reduces to mass proportional damping matrix and
        with two modes reduces to Rayleigh damping;
        for more than 2 modes Caughey damping works only if Ml is fully populated;
        Modal damping refers to the method of superposing modal damping matrices
        Reference: Chopra, Dynamics of Structures, 2nd edition, pp. 455-463</pre>
<!-- <div class="fragment"><pre class="comment">CREATE_DAMPING setup damping matrix of structural model
  C = CREATE_DAMPING (TYPE,KF,ML,ZETA,MODE)
  function sets up damping matrix C according to character variable TYPE
  for a structure with free dof stiffness matrix KF and free dof lumped mass vector ML;
  the damping matrix is calibrated so that the mode numbers in row vector MODE have
  damping ratios as specified in row vector ZETA;
  character variable TYPE should be either 'StifProp', 'Caughey' or 'Modal'
  Note: Caughey with one mode reduces to mass proportional damping matrix and
        with two modes reduces to Rayleigh damping;
        for more than 2 modes Caughey damping works only if Ml is fully populated;
        Modal damping refers to the method of superposing modal damping matrices
        Reference: Chopra, Dynamics of Structures, 2nd edition, pp. 455-463</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="../../latest/Analysis_Functions/Dynamic/EigenMode" class="code" title="function [omega,Ueig] = EigenMode (Kf,M,nmod)">EigenMode</a>	EIGENMODE determines eigenfrequencies and eigenmodes of structural model</li></ul>
This function is called by:
<ul style="list-style-image:url(../../matlabicon.gif)">
<li><a href="Add_Damping2State.md" class="code" title="function State = Add_Damping2State (type,Model,State,zeta,mode)">Add_Damping2State</a>	ADD_DAMPING2STATE setup damping matrix of structural model as field of data structure STATE</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Thu 28-Jan-2021 18:22:44 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->