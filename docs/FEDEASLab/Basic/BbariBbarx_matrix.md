[BBARI,BBARX,IND_X] = BBARIBBARX_MATRIX (BF,IND_R)
the function determines the force influence matrices BBARI and BBARX
of the primary structure from static matrix BF;
the optional argument IND_R specifies the index for the selected redundant basic forces;
BBARI is the force influence matrix for the applied forces at the free dofs,
and BBARX is the force influence matrix for the redundant basic forces;
IND_X is the redundant force index vector into the basic forces of the structure
=========================================================================================
FEDEASLab - Release 5.0, July 2018
Matlab Finite Elements for Design, Evaluation and Analysis of Structures
Professor Filip C. Filippou (filippou@berkeley.edu)
Department of Civil and Environmental Engineering, UC Berkeley
Copyright(c) 1998-2018. The Regents of the University of California. All Rights Reserved.
=========================================================================================
function added                                                                    01-2004
added case for empty ind_r                                                        04-2012
changed function name                                                             11-2012

+   ----------------------------------------------------------------------------------------
    
