---
title: "Create_MultDispCycleswN"
id: "Create_MultDispCycleswN"
description: "CREATE_MULTDISPCYCLESwN sequence of full, half or quarter displacement cycles with axial force"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href="#">Utility_Functions</a> &gt; <a href=".autoindex.md">General</a> &gt; 
<!-- Create_MultDispCycleswN.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../.autoindex.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Utility_Functions\General&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `Create_MultDispCycleswN`



## <a name="_name"></a>Purpose


CREATE_MULTDISPCYCLESwN sequence of full, half or quarter displacement cycles with axial force

<!-- <div class="box"><strong>CREATE_MULTDISPCYCLESwN sequence of full, half or quarter displacement cycles with axial force</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function [DspHst,FrcHst] = Create_MultDispCycleswN (DspPat,Ucyc,Ncyc,TmStr,Options)` 

## Description


<pre class="comment">CREATE_MULTDISPCYCLESwN sequence of full, half or quarter displacement cycles with axial force 
  [DSPHST,FRCHST] = CREATE_MULTDISPCYCLESwN (DSPPAT,UCYC,NCYC,TMSTR,OPTIONS)
  the function generates a sequence of full, half or quarter displacement cycles
  after factoring each with the corresponding factor in array UCYC;
  the axial force factor of the correponding cycle is specified in the optional array NCYC;
  UCYC is an ND x NCYC array and NCYC is a 1 x NCYC row vector, where ND is the number
  of imposed displacements/forces (1=uniaxial, 2=biaxial) and NCYC is the number of cycles;
  if NCYC is not specified, it is assumed equal to ONES(1,NCYC);
  the function returns the displacement history in the data structure array DSPHST
  with the fields Time and Value and the axial force history in the data structure FRCHST
  with the fields Time and Value; the data structure array DSPHST has one entry for uniaxial and 2 entries for biaxial
  and 2 entries for biaxial displacement patterns; FRCHST has only one entry.
  DSPPAT is a character variable if the displacement pattern is the same for all cycles and
  a character cell array, if the displacement pattern varies from cycle to cycle;
  the character variable identifies the path of the displacement pattern with the syntax:
  U means uniaxial and B biaxial, with the addition of V indicating a variable axial force;
  the supported patterns are:
  U1(UV1) : uniaxial displacement history in 1-direction
  U2(UV2) : uniaxial displacement history in 2-direction
  U3(UV3) : displacement history at specified ratio of values along axis 1 and 2
  B1(BV1) : circular displacement pattern starting with axis 1
  B2(BV2) : counter-clock wise clover leaf pattern
  B3(BV3) : diamond  displacement pattern
  B4(BV4) : circular displacement pattern starting with axis 2
  the optional argument TMSTR is a logical variable (true or false) to indicate whether the
  the pseudo-time needs stretching/shortening to maintain equal displacement increment
  for each displacement reversal (default = true).
  OPTIONS(NCYC) is an optional structure array with the following fields:
        .TrmpN = time interval for ramping up         the application of the axial force N
        .TrmpU = time interval for ramping up or down the application of the first displacement
        .Nsub  = time subdivision for description of the circular path
        .NRat  = ratio of axial force variation relative to constant value
        .HCyc  = true or false; true for half    cycle instead of full displacement cycle
        .QCyc  = true or false; true for quarter cycle instead of full displacement cycle</pre>
<!-- <div class="fragment"><pre class="comment">CREATE_MULTDISPCYCLESwN sequence of full, half or quarter displacement cycles with axial force 
  [DSPHST,FRCHST] = CREATE_MULTDISPCYCLESwN (DSPPAT,UCYC,NCYC,TMSTR,OPTIONS)
  the function generates a sequence of full, half or quarter displacement cycles
  after factoring each with the corresponding factor in array UCYC;
  the axial force factor of the correponding cycle is specified in the optional array NCYC;
  UCYC is an ND x NCYC array and NCYC is a 1 x NCYC row vector, where ND is the number
  of imposed displacements/forces (1=uniaxial, 2=biaxial) and NCYC is the number of cycles;
  if NCYC is not specified, it is assumed equal to ONES(1,NCYC);
  the function returns the displacement history in the data structure array DSPHST
  with the fields Time and Value and the axial force history in the data structure FRCHST
  with the fields Time and Value; the data structure array DSPHST has one entry for uniaxial and 2 entries for biaxial
  and 2 entries for biaxial displacement patterns; FRCHST has only one entry.
  DSPPAT is a character variable if the displacement pattern is the same for all cycles and
  a character cell array, if the displacement pattern varies from cycle to cycle;
  the character variable identifies the path of the displacement pattern with the syntax:
  U means uniaxial and B biaxial, with the addition of V indicating a variable axial force;
  the supported patterns are:
  U1(UV1) : uniaxial displacement history in 1-direction
  U2(UV2) : uniaxial displacement history in 2-direction
  U3(UV3) : displacement history at specified ratio of values along axis 1 and 2
  B1(BV1) : circular displacement pattern starting with axis 1
  B2(BV2) : counter-clock wise clover leaf pattern
  B3(BV3) : diamond  displacement pattern
  B4(BV4) : circular displacement pattern starting with axis 2
  the optional argument TMSTR is a logical variable (true or false) to indicate whether the
  the pseudo-time needs stretching/shortening to maintain equal displacement increment
  for each displacement reversal (default = true).
  OPTIONS(NCYC) is an optional structure array with the following fields:
        .TrmpN = time interval for ramping up         the application of the axial force N
        .TrmpU = time interval for ramping up or down the application of the first displacement
        .Nsub  = time subdivision for description of the circular path
        .NRat  = ratio of axial force variation relative to constant value
        .HCyc  = true or false; true for half    cycle instead of full displacement cycle
        .QCyc  = true or false; true for quarter cycle instead of full displacement cycle</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
<li><a href="/Functions/Create_DispCyclewN" class="code" title="function [DspHst,FrcHst] = Create_DispCyclewN (DspPat,Options)">Create_DispCyclewN</a>	CREATE_DISPCYCLEwN generate time and value pairs for a single displacement cycle with normal force</li></ul>

This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->