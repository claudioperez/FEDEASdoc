V0 = V0_VECTOR (MODEL,ELEMDATA,ROPTION)
the function sets up the initial element deformation vector V0 for the structural model
specified in data structure MODEL with element property information in cell array ELEMDATA
if ROPTION=0, element release information is not accounted for in setting up V0 (default=1)
=========================================================================================
FEDEASLab - Release 5.0, July 2018
Matlab Finite Elements for Design, Evaluation and Analysis of Structures
Professor Filip C. Filippou (filippou@berkeley.edu)
Department of Civil and Environmental Engineering, UC Berkeley
Copyright(c) 1998-2018. The Regents of the University of California. All Rights Reserved.
=========================================================================================
function added                                                                    11-2003
Roption added                                                                     07-2012

+   ----------------------------------------------------------------------------------------
    
