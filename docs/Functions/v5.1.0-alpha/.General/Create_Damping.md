[]{#_top}

<div>

[Home](../FEDEASLab.html) \> [General](FEDEASLab.html) \>
Create_Damping.m

</div>

# Create_Damping

## []{#_name}PURPOSE [![\^](../up.png)](#_top)

::: {.box}
**CREATE_DAMPING setup damping matrix of structural model**
:::

## []{#_synopsis}SYNOPSIS [![\^](../up.png)](#_top)

::: {.box}
**function C = Create_Damping (type,Kf,Ml,zeta,mode)**
:::

## []{#_description}DESCRIPTION [![\^](../up.png)](#_top)

::: {.fragment}
``` {.comment}
CREATE_DAMPING setup damping matrix of structural model
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
        Reference: Chopra, Dynamics of Structures, 2nd edition, pp. 455-463
```
:::

## []{#_cross}CROSS-REFERENCE INFORMATION [![\^](../up.png)](#_top)

This function calls:

This function is called by:

-   [Add_Damping2State](Add_Damping2State.html "function State = Add_Damping2State (type,Model,State,zeta,mode)"){.code}
    ADD_DAMPING2STATE setup damping matrix of structural model as field
    of data structure STATE

------------------------------------------------------------------------

Generated on Wed 22-Jan-2020 08:42:48 by
**[m2html](http://www.artefact.tk/software/matlab/m2html/ "Matlab Documentation in HTML")**
© 2005
