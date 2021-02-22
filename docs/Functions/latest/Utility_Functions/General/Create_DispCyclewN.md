---
title: "Create_DispCyclewN"
id: "Create_DispCyclewN"
description: "CREATE_DISPCYCLEwN generate time and value pairs for a single displacement cycle with normal force"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href="#">Utility_Functions</a> &gt; <a href=".autoindex.md">General</a> &gt; 
<!-- Create_DispCyclewN.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../.autoindex.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Utility_Functions\General&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `Create_DispCyclewN`



## <a name="_name"></a>Purpose


CREATE_DISPCYCLEwN generate time and value pairs for a single displacement cycle with normal force

<!-- <div class="box"><strong>CREATE_DISPCYCLEwN generate time and value pairs for a single displacement cycle with normal force</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [DspHst,FrcHst] = Create_DispCyclewN (DspPat,Options)` 

## Description


<pre class="comment">CREATE_DISPCYCLEwN generate time and value pairs for a single displacement cycle with normal force    
  [DSPHST,FRCHST] = CREATE_DISPCYCLEwN (DSPPAT,OPTIONS)
  the function generates the time and value pairs of a single displacement cycle
  for the pattern in DSPPAT under constant or variable normal force N;
  the function returns the displacement history in data structure array DSPHST with fields
  Time and Value and the axial force history in data structure FRCHST with fields Time and Value;
  the displacement history consists of unit values at reversals with zero values in between,
  while the force history consists of unit values for constant axial force +- the variable
  axial force ratio NRat relative to the constant axial force specified in OPTIONS;
  the structure array DSPHST has one entry for uniaxial and 2 entries for biaxial
  displacement patterns; FRCHST has only one entry;
  DSPPAT is a character variable for the displacement path with the following syntax:
  U means uniaxial and B biaxial, with the addition of V indicating a variable axial force;
  the supported patterns are:
  U1(UV1) : uniaxial displacement history in 1-direction
  U2(UV2) : uniaxial displacement history in 2-direction
  U3(UV3) : displacement history at specified ratio of values along axis 1 and 2
  B1(BV1) : circular displacement pattern starting with axis 1
  B2(BV2) : counter-clock wise clover leaf pattern
  B3(BV3) : diamond  displacement pattern
  B4(BV4) : circular displacement pattern starting with axis 2
  OPTIONS is an optional data structure with the following fields:
        .TrmpN = time interval for ramping up         the application of the axial force N
        .TrmpU = time interval for ramping up or down the application of first U
        .Nsub  = time subdivision for description of circular path (default = 100)
        .NRat  = ratio for axial force variation relative to constant value
        .HCyc  = true or false; if true the function returns a half    cycle instead of full
        .QCyc  = true or false; if true the function returns a quarter cycle instead of full</pre>
<!-- <div class="fragment"><pre class="comment">CREATE_DISPCYCLEwN generate time and value pairs for a single displacement cycle with normal force    
  [DSPHST,FRCHST] = CREATE_DISPCYCLEwN (DSPPAT,OPTIONS)
  the function generates the time and value pairs of a single displacement cycle
  for the pattern in DSPPAT under constant or variable normal force N;
  the function returns the displacement history in data structure array DSPHST with fields
  Time and Value and the axial force history in data structure FRCHST with fields Time and Value;
  the displacement history consists of unit values at reversals with zero values in between,
  while the force history consists of unit values for constant axial force +- the variable
  axial force ratio NRat relative to the constant axial force specified in OPTIONS;
  the structure array DSPHST has one entry for uniaxial and 2 entries for biaxial
  displacement patterns; FRCHST has only one entry;
  DSPPAT is a character variable for the displacement path with the following syntax:
  U means uniaxial and B biaxial, with the addition of V indicating a variable axial force;
  the supported patterns are:
  U1(UV1) : uniaxial displacement history in 1-direction
  U2(UV2) : uniaxial displacement history in 2-direction
  U3(UV3) : displacement history at specified ratio of values along axis 1 and 2
  B1(BV1) : circular displacement pattern starting with axis 1
  B2(BV2) : counter-clock wise clover leaf pattern
  B3(BV3) : diamond  displacement pattern
  B4(BV4) : circular displacement pattern starting with axis 2
  OPTIONS is an optional data structure with the following fields:
        .TrmpN = time interval for ramping up         the application of the axial force N
        .TrmpU = time interval for ramping up or down the application of first U
        .Nsub  = time subdivision for description of circular path (default = 100)
        .NRat  = ratio for axial force variation relative to constant value
        .HCyc  = true or false; if true the function returns a half    cycle instead of full
        .QCyc  = true or false; if true the function returns a quarter cycle instead of full</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>

This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="Create_MultDispCycleswN.md" class="code" title="function [DspHst,FrcHst] = Create_MultDispCycleswN (DspPat,Ucyc,Ncyc,TmStr,Options)">Create_MultDispCycleswN</a>	CREATE_MULTDISPCYCLESwN sequence of full, half or quarter displacement cycles with axial force</li></ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->