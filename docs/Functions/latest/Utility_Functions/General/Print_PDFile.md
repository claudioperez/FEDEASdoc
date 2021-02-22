---
title: "Print_PDFile"
id: "Print_PDFile"
description: "PRINT_PDFILE sends the current figure to file"
...

<!-- <a name="_top"></a> -->
<!-- <div><a href="../../../.autoindex.md">Home</a> &gt;  -->
 <a href="#">latest</a> &gt; <a href="#">Utility_Functions</a> &gt; <a href=".autoindex.md">General</a> &gt; 
<!-- Print_PDFile.m</div> -->

<!--<table width="100%"><tr><td align="left"><a href="../../../.autoindex.md"><img alt="<" border="0" src="../../../left.png">&nbsp;Master index</a></td>
<td align="right"><a href=".autoindex.md">Index for latest\Utility_Functions\General&nbsp;<img alt=">" border="0" src="../../../right.png"></a></td></tr></table>-->
# `Print_PDFile`



## <a name="_name"></a>Purpose


PRINT_PDFILE sends the current figure to file

<!-- <div class="box"><strong>PRINT_PDFILE sends the current figure to file</strong></div> -->

## <a name="_synopsis"></a>Synopsis

`function Print_PDFile (FName,FigOpt,PrOpt)` 

## Description


<pre class="comment">PRINT_PDFILE sends the current figure to file 
  PRINT_PDFILE(FNAME,FIGOPT,PROPT)
  the function generates the FNAME.EXT file from the current figure; if FNAME is missing,
  it is replaced by 'PFile'; the optional arguments FIGOPT and PROPT are data structures
  with the following fields for controlling the display and the output:
  FIGOPT.Pos   : position of figure relative to display (1x4 numeric array) 
        .Ornt  : figure orientation ('landscape' or 'portrait')
   PROPT.Format: file format      (default=-dpdf for PDF file)
        .Reso  : print resolution (default=-r600 for PDF file)</pre>
<!-- <div class="fragment"><pre class="comment">PRINT_PDFILE sends the current figure to file 
  PRINT_PDFILE(FNAME,FIGOPT,PROPT)
  the function generates the FNAME.EXT file from the current figure; if FNAME is missing,
  it is replaced by 'PFile'; the optional arguments FIGOPT and PROPT are data structures
  with the following fields for controlling the display and the output:
  FIGOPT.Pos   : position of figure relative to display (1x4 numeric array) 
        .Ornt  : figure orientation ('landscape' or 'portrait')
   PROPT.Format: file format      (default=-dpdf for PDF file)
        .Reso  : print resolution (default=-r600 for PDF file)</pre></div> -->

<!-- crossreference -->
## <a name="_cross"></a>Cross-Reference Information

This function calls:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>

This function is called by:
<ul style="list-style-image:url(../../../matlabicon.gif)">
</ul>
<!-- crossreference -->




<!-- <hr><address>Generated on Mon 15-Feb-2021 18:38:47 by <strong><a href="http://www.artefact.tk/software/matlab/m2html/" title="Matlab Documentation in HTML">m2html</a></strong> &copy; 2005</address> -->