---
title: Basic Analysis Functions
...

<h1>Basic Analysis Functions</h1>

**Table of Contents**

- [Introduction](#introduction)
- [Function Organization](#function-organization)
- [Data Organization](#data-organization)
  - [Data Structure `Model`](#data-structure-model)
- [General Utility Functions](#general-utility-functions)
  - [Function `Localize`](#function-localize)
- [Displacement Method of Analysis](#displacement-method-of-analysis)
- [2.10 Direct Stiffness Assembly](#210-direct-stiffness-assembly)

## Introduction

`FEDEASLab` functions implement structural analysis concepts in parallel with their theoretical presentation in the introductory structural analysis course, thus illustrating the generality of the methods and their application to large scale and complex structural models. The intent is not only to reinforce the understanding of the structural response under different types and arrangements of loading, but also to facilitate system and parameter studies.

## Function Organization

The basic structural analysis functions for the introductory course are organized in two folders: `Basic` and `Utilities`. The `Basic` folder contains 14 functions that directly implement the analysis concepts of the course in Matlab. Most functions in this folder are provided in open source form (`.m` file format), so that interested readers can relate the implementation details with the theory presented in the course. They can be classified in the following categories:

1. *Functions for Structural Matrices and Vectors (8)*:  These are listed in Table 2.1.
2. *Analysis Functions and Scripts (4)*: These are listed in Table 2.2.
3. *General Utility Functions (2)*: Namely `Localize` and `ElmLenOr` which are not invoked directly, but are used by the functions in the first category.

The user defines the geometry and properties of the structural model, and then specifies the structural analysis procedure(s) and the graphical post-processing of the results by selecting suitable functions from Table  2.1-Table  2.4  in  a Matlab script  file,  as  described  in  the  following  sections.  Scripting  affords extensive  flexibility  for  the  response  determination  and  the  presentation  of  the  results,  but  puts  the burden  on  the  user  to  assemble  the  whole  by  understanding  its  parts.  This  supports  the  open-ended educational mission of `FEDEASLab`, as opposed to the black-box nature of commercial analysis software. The following sections describe the functions in Table 2.1-Table 2.4 with examples. The notation for function  arguments  and  local  variables  agrees  with  the  notation  of  the  course  reader,  as  summarized in Appendix RB2. The examples in this chapter correspond to examples of the course reader with the Matlab scripts for all examples available in the folder `Examples` of the basic `FEDEASLab` package.

## Data Organization

The initial set of analysis functions for the concepts of an introductory course on structural analysis is built around two data structures: `Model`, for the geometric description of the structural model, and `ElemData` for  the  element  and  material  properties  and  element  loading,  as  is  evident  from  the  input argument list of the functions in Table 2.1-Table 2.4. The organization of structural model information in two data structures serves to emphasize the concept of the introductory structural analysis course that, under linear conditions, the governing static and kinematic relations depend only on the geometry of  the  structural  model  and  not  on  any  element  properties.  Accordingly,  the  functions `Bmatrix` for setting up the linear static matrix $B$ and `Amatrix` for setting up the linear kinematic matrix $A$ of the structure take as single input argument the data structure `Model` with model geometry information.

### Data Structure `Model`

In `FEDEASLab` information about the structural model is collected in the data structure `Model`, which is  set  up  by  the  function `CreateSimpleModel` from  information  supplied  by  the  user.  The  function `CreateSimpleModel` is limited to models consisting of 2-node, 2d or 3d truss and frame elements. The function  numbers  the  degrees  of  freedom  (DOFs)  of  the  structure,  as  discussed  in  the  course  reader, thus  facilitating  their  identification  for  small  structural  models.  With  this  degree  of  freedom  (DOF) numbering the analysis functions set up full matrices that do not take advantage of the small number of non-zero terms in large structural models. The general model creation function `CreateModel` does not have limitations on element type and uses a DOF numbering scheme that minimizes the storage of structure matrices. The use of sparse matrices with minimum storage is essential for the analysis of large structural models with 2d and 3d finite elements.

Fig. 2.1 shows the input data for the structure of Example R4.1 in the form of numerical arrays `XYZ`,`BOUN`, and `CON`. The rows of `XYZ` correspond to the nodes and the *ndm* columns to the node coordinates, where *ndm* is the dimension of the structural model. The rows of `BOUN` also correspond to the nodes and the *ndf* columns to node restraint switches, where *ndf* is the maximum number of DOFs per node for the model. The DOF order for each node is: 1 = force in $X$, 2 = force in $Y$, 3 = moment about $Z$ (for 2d model), or force in $Z$ (for 3d model), 4,5,6 = moment about $X$,$Y$ and $Z$ (for 3d model). The switch value `0` indicates a free and the value 1 a restrained DOF. `CON` can be a numerical array for a structural model with only 2-node elements. For finite element models with elements having a different number of nodes, `CON` needs to be specified as a cell array so that the row contents can vary from element to element. Each row of the numerical `CON` array contains the node numbers to which the corresponding element connects. Finally, `ElemName` is a cell array that accommodates element names with a different number of characters. The names `'Truss'` and `'2dFrm'` suffice for tasks that do not require element and material properties. For tasks requiring element and material properties the element names need to be `'LinTruss'`, `'Lin2dFrm'`, and `'Lin3dFrm'` for the 2d/3d truss, the 2d frame, and the 3d frame element, respectively.

## General Utility Functions

Once the geometry and other relevant information about the structural model is collected in data structure `Model` by the function `CreateSimpleModel`, information about the geometry and the global DOF  correspondence  for  a  particular  element  can  be  extracted  with  the  help  of  two  general  utility functions: `Localize` and `ElmLenOr`. All functions with input arguments `Model` and `ElemData` in Table 2.1 invoke these utility functions for setting up the corresponding structural matrices or vectors.

### Function `Localize`

This function locates the element `el` in the Model and returns its end node coordinates in array `xyz`, and the local-global DOF correspondence in vector `id`. The first column of the two dimensional array `xyz` contains the coordinates of end `i` of the element and the second column those of end `j`.

```{.matlab}
function [xyz,id] = Localize(Model, el)
XYZ = Model.XYZ; % node  coordinates
DOF = Model.DOF; % array with dof numbers for all  nodes

CON = Model.CON{el}; % extract connectivity array for element
ndf = Model.ndf(el); % extract no of dofs /node for element

% extract element  coordinates into array xyz;
% use CON array to extract appropriate rows of global XYZ array
xyz = XYZ(CON(CON>0),:)'; % extract dof numbers into array id

% use CON array to extract appropriate rows of DOF array
id = DOF(CON(CON>0), 1:ndf)'; % reshape id array into vector
id = id(:);
```

Box 2.2: Syntax of function `Localize` with input arguments `Model` and `el` and output arguments `xyz` and `id`.

## Displacement Method of Analysis

The steps of the displacement method of analysis are described in Section $\mathrm{R} 10.3$ and Section $\mathrm{R} 10.4$
A summary of these steps for implementation in `FEDEASLab` is:

1. With the kinematic matrix $\mathbf{A}_{f}$ set up the stiffness matrix $\mathbf{K}_{f}$ and the initial force vector $\boldsymbol{P}_{0}$
$$
\mathbf{K}_{f}=\mathbf{A}_{f}^{T} \mathbf{K}_{s} \mathbf{A}_{f} \quad \boldsymbol{P}_{0}=\mathbf{A}_{J}^{T} \boldsymbol{Q}_{0}+\boldsymbol{P}_{w f}
$$
2. Solve the equilibrium equations for the free DOF displacements $\boldsymbol{U}_{f}$
$$
P_{f}=\mathbf{K}_{f} \boldsymbol{U}_{f}+\boldsymbol{P}_{0}
$$
3. Determine the element deformations $\boldsymbol{V}$ from the kinematic relations
$$
\boldsymbol{V}=\mathbf{A}_{f} \boldsymbol{U}_{f}
$$
4. Determine the basic forces $Q$ from the collection of element force-deformation relations
$$
Q=\mathbf{K}_{s} \boldsymbol{V}+\boldsymbol{Q}_{0}
$$

Box 2.17 shows the implementation of these steps in the Matlab script file `S_DisplMethod`.
As is the case with the script for the force method of analysis, the script `S_DisplMethod` depends on the definition of the structural model geometry in data structure `Model`, and on the specification of the element property and loading information in data structure `ElemData`. The specification of the
nodal forces `Pf` and `Pwf` is optional with default, values equal to zero. The script uses the same auxiliary
functions as the script for the force method to remove the rows of the kinematic matrix $\mathbf{A}$ with release
deformations and pad the vector of basic forces $Q$ from the displacement method of analysis with zero
values at the releases, so that it can determine the element deformations $\boldsymbol{V}_{\varepsilon}$ at the element ends with flexural releases and plot the deformed shape of the corresponding element, if required.


## 2.10 Direct Stiffness Assembly

Section $\mathrm{R} 10.6 .3$ demonstrates the significant advantage of the displacement method over the force
method of analysis: the direct assembly of the structure stiffness matrix $\mathbf{K}_{f}$ and the resisting forces $\boldsymbol{P}_{r}$.
We demonstrate briefly the ease of implementing the direct stiffness assembly in `FEDEASLab` by taking advantage of the array indexing capabilities of Matlab described in Appendix $\mathrm{A}$ and avoiding the
multiplication by the Boolean array in Eq. $\mathrm{R}(10.31) .$ The latter approach is symbolically compact but computationally inefficient, because the Boolean matrix $\mathbf{A}_{b}^{(e l)}$ in Eq. $\mathrm{R}(10.31)$ contains only a few terms of one but mostly zeros.

In the direct assembly process the element $i d$ array serves as index of the element stiffness coefficients into the structure stiffness matrix $\check{\mathrm{K}} .$ `FEDEASLab` function `Kf_matrix.m` assembles the complete stiffness
matrix $\check{\mathrm{K}}$ and then extracts the stiffness $\mathbf{K}$ at the free DOFs (in practice only the free dof stiffness $\mathbf{K}$ is assembled to save storage).

```{.matlab}
K  = zeros(nt, nt);

for el=1:ne % locate element in Model and return end coordinates and id array
    [xyz,id] = Localize(Model, el); % form element stiffness matrix ke in global reference system
    ke = ke_matrix(Model.ElemName{el}, ElemData{el}, xyz); % assemble element stiffness matrix ke into structure matrix K
    K(id,id) = K(id, id) + ke;
end
Kf = K(1:nf, 1:nf); % extract stiffness matrix of free DOFs
```

