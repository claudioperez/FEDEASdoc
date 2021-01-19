[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [General](FEDEASLab.html) \>
Add_Damping2State.m

</div>

# Add_Damping2State

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**ADD_DAMPING2STATE setup damping matrix of structural model as field of
data structure STATE**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function State = Add_Damping2State (type,Model,State,zeta,mode)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
ADD_DAMPING2STATE setup damping matrix of structural model as field of data structure STATE
  STATE = ADD_DAMPING2STATE (TYPE,MODEL,STATE,ZETA,MODE)
  function sets up structural damping matrix C according to character variable TYPE
  as field of data structure STATE; the free dof stiffness matrix is field Kf of STATE
  and the free dof lumped mass vector is field Ml of MODEL;
  the damping matrix is calibrated so that the mode numbers in row vector MODE have
  damping ratios as specified in row vector ZETA;
  character variable TYPE should be either 'StifProp' or 'Caughey'
  Note: Caughey with one mode reduces to mass proportional damping matrix and with
        two modes reduces to Rayleigh damping
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

-   [Create_Damping](Create_Damping.html "function C = Create_Damping (type,Kf,Ml,zeta,mode)"){.code}
    CREATE_DAMPING setup damping matrix of structural model

This function is called by:

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
