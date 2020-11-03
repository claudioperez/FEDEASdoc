---
title: FEDEASLab Basic Structural Analysis Functions
hide_toc: true
template: partials/card_index.html
...

<h1>FEDEASLab Basic Structural Analysis Functions</h1>

## Abstract

`FEDEASLab` is  a  collection  of `Matlab` functions  for  instruction  and  research  in  linear  and  nonlinear finite element analysis. These functions take advantage of the widespread use of `Matlab` in engineering curricula around the world, and the extensive set of built-in and customized `Matlab` functions for many branches of science and engineering. In parallel with the introduction of basic concepts in an introductory course on structural analysis,the initial set of functions is rather small. This report is limited to this initial set. As the complexity of structural analysis concepts and procedures grows, the number of functions grows rapidly under the following criteria:

1. Maintain modularity by keeping the extent of each function focused on a specific task realizing that composite tasks can be accomplished by collecting functions into scripts or higher order functions.
2. Maintain modularity by organizing the variables of the analysis process in a small set of data structures serving as input and output arguments of the different functions.

The organization of structural analysis variables in data structures accommodates the subsequent growth in complexity of the structural analysis task with the addition of fields to the existing data structures. For the same reason general utility functions start out with input arguments of simple data types and subsequently expand to accommodate more complex data types while retaining the same interface
