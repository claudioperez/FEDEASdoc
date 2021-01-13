[]{#_top}

<div>

[Home](../../FEDEASLab.html) \> [Utilities](../FEDEASLab.html) \>
[Plotting](FEDEASLab.html) \> Get_ModelScale.m

</div>

# Get_ModelScale

## []{#_name}PURPOSE [![\^](../../up.png)](#_top)

::: {.box}
**GET_MODELSCALE determines maximum and minimum element length in
Model**
:::

## []{#_synopsis}SYNOPSIS [![\^](../../up.png)](#_top)

::: {.box}
**function \[ModSc,maxL,minL\] = Get_ModelScale (Model,Ratio)**
:::

## []{#_description}DESCRIPTION [![\^](../../up.png)](#_top)

::: {.fragment}
``` {.comment}
GET_MODELSCALE determines maximum and minimum element length in Model
  [MODSC,MAXL,MINL] = GET_MODELSCALE(MODEL,RATIO)
  the function determines a critical scale for the structural model
  in data structure MODEL from the maximum distance MAXL and
  the minimum distance MINL between nodes i and j of line elements;
  the maximum distance MAXL is divided by RATIO (default = 1.5-0.5*MINL/MAXL);
  depending on the value of RATIO the model scale is equal
  to the largest (RATIO<MAXL/MINL) or smallest distance (RATIO>MAXL/MINL)
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../../up.png)](#_top)

This function calls:

This function is called by:

-   [Label_Model](Label_Model.html "function Label_Model (Model,LblOpt)"){.code}
    LABEL_MODEL displays element and node numbers and global axes in the
    current window
-   [Plot_2dCurvDistr](Plot_2dCurvDistr.html "function Plot_2dCurvDistr (Model,ElemData,Post,ElemList,UserScale)"){.code}
    PLOT_2dCURVDISTR plot curvature distribution of 2d linear elastic
    frame elements
-   [Plot_2dMomntDistr](Plot_2dMomntDistr.html "function Plot_2dMomntDistr (Model,ElemData,Post,ElemList,UserScale)"){.code}
    PLOT_2dMOMNTDISTR plots moment distribution for 2d frame elements in
    current window
-   [Plot_AxialForces](Plot_AxialForces.html "function Plot_AxialForces (Model,Post,ElemList,UserScale)"){.code}
    PLOT_AXIALFORCES plot axial forces in current window
-   [Plot_DeformedStructure](Plot_DeformedStructure.html "function Plot_DeformedStructure (Model,ElemData,U,Post,PlotOpt)"){.code}
    PLOT_DEFORMEDSTRUCTURE plot deformed shape of the structure
-   [Plot_ElemLoading](Plot_ElemLoading.html "function Plot_ElemLoading (Model,ElemData,PlotOpt)"){.code}
    PLOT_ELEMLOADING display element loading in current window
-   [Plot_IPVarDistr](Plot_IPVarDistr.html "function Plot_IPVarDistr (Model,ElemData,Post,Component,ElemList,UserScale)"){.code}
    PLOT_IPVARDISTR plots distribution of integration point variables of
    elements with sections
-   [Plot_Model](Plot_Model.html "function Plot_Model (Model,U,MPlOpt)"){.code}
    PLOT_MODEL plots the original or deformed geometry of the structural
    model
-   [Plot_NodalForces](Plot_NodalForces.html "function Plot_NodalForces (Model,Loading,PlotOpt)"){.code}
    PLOT_NODALFORCES display nodal forces in current window
-   [Plot_OpenPlasticHinges](Plot_OpenPlasticHinges.html "function Plot_OpenPlasticHinges (Model,ElemData,Post,PlotOpt)"){.code}
    PLOT_OPENPLASTICHINGES display plastic hinge locations in original
    or deformed configuration
-   [Plot_PlasticHinges](Plot_PlasticHinges.html "function Plot_PlasticHinges (Model,ElemData,U,Post,PlotOpt)"){.code}
    PLOT_PLASTICHINGES display plastic hinge locations in current window
-   [Plot_Releases](Plot_Releases.html "function Plot_Releases (Model,ElemData,U,PlotOpt)"){.code}
    PLOT_RELEASES display element releases in current window

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
