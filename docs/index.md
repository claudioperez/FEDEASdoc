# FEDEASLab

## About

The Matlab© toolbox FEDEASLab is a user-friendly, versatile and powerful tool for the
simulation of nonlinear structural response under static and dynamic loads, which has been
used successfully for the development of new elements and material models, as well as for the
simulation of the response of small structural models in research and instruction. Its
development started in 1998 for the support of instruction of the basic graduate courses of linear
and nonlinear structural analysis at the University of California, Berkeley. To date FEDEASLab
has evolved into a powerful framework for research in the nonlinear analysis of structures.
The toolbox consists of several functions that are grouped in categories and are, consequently,
organized in separate directories. These functions operate on five basic data structures which
represent the model, the loading, the element properties, the state of the structural response,
and the parameters of the solution strategy. A sixth data structure is optional and carries postprocessing information that can be used for response interpretation and visualization.
FEDEASLab supports path-dependent static or transient response under multiple force and
displacement patterns. Transient response under multiple force patterns, displacement patterns,
and acceleration patterns with uniform or multi-support excitation is also supported.
The nonlinear response analysis of structural models under static or transient conditions is
decomposed into logical steps. Each step is represented by a separate function with one or
more basic data objects as input and output arguments. In this way the definition of the model,
the specification of element properties, the definition of applied force and displacement patterns
and corresponding load histories, and the analysis of the model under the loading becomes a
sequence of function calls that are organized in script files. With Matlab's scripting language it is
easy to customize the analysis sequence and conduct parameter studies. The modular
architecture of the toolbox and the compact organization of data allow for the easy addition of
new functions for providing new capabilities. It is equally easy to access the data objects and
enhance the information stored in them. A well defined interface for element, section and
material models permits the user to add custom components to the available element, section
and material libraries.
Post-processing is accommodated with a data object that carries all important material, element
and structural information for plotting or printing. Several functions that address basic postprocessing tasks are provided. The user can easily enhance and extend the current capabilities.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

