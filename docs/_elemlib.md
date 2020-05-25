---
elems: [LE2dFrm,Other]
title: othertitle

---


# Nonlinear Element Modeling

## Element Data Structures

When the character variable ACTION has one of the following values,
the function performs the listed operations and returns the results in ELEMRESP:

- `'size'`: report size of element arrays
- `'chec'`: check element property data for omissions and assign default values
- `'init'`: initialize element history variables
- `'forc'`: report element resisting forces
- `'stif'`: report element stiffness matrix and resisting forces
- `'mass'`: report lumped mass vector and consistent mass matrix
- `'post'`: report post-processing information
- `'defo'`: report function handle for deformed shape

This is a test equation:
$$V = A_f U_f$$



The data structure ELEMRESP stands for the following data object(s) for each ACTION:

- ELEMRESP = ARSZ        for `action = 'size'`
- ELEMRESP = ELEMDATA    for `action = 'chec'`
- ELEMRESP = ELEMSTATE   for `action = 'init'`
- ELEMRESP = ELEMSTATE   for `action = 'stif'`
- ELEMRESP = ELEMSTATE   for `action = 'forc'`
- ELEMRESP = ELEMMASS    for `action = 'mass'`
- ELEMRESP = ELEMPOST    for `action = 'post'`
- ELEMRESP = FunHandle   for `action = 'defo'`
- ELEMRESP is empty      for unsupported keywords


ELEMDATA is a data structure with element property information in fields

ELEMSTATE is a data structure with the current element state; it has the fields
- u     = vector of total element displacements in global reference
- Du    = vector of element displacement increments from last convergence
- DDu   = vector of element displacement increments from last iteration
- ke    = element stiffness matrix in global reference; updated under - ACTION = `stif`
- p     = element resisting force vector in global reference; updated - under ACTION = `stif` or `forc`
- Past  = element history variables at last converged state
- Pres  = current element history variables
- lamda = row vector of current load factor(s)


ELEMMASS is a data structure with element mass information in fields
        ml    = lumped mass vector
        mc    = consistent mass matrix

  ARSZ   is an Boolean array of size NDF x NEN,
         where NDF = number of DOFs/node, NEN = number of nodes,
         with unit values corresponding to the active element DOFs

  ELEMDATA is a data structure with element property information in fields

  ELEMSTATE is a data structure with the current element state; it has the fields

  ELEMMASS is a data structure with element mass information in fields

  ELEMPOST is a data structure with element response information for post-processing in fields

## Element Library

{% raw %}
{% for elem in meta.elems %}
### {{elem}} {$ elem $}
  <details>
  <summary> {{ elem }} {$ elem $}</summary>
  other text
  </details>

{% endfor %}
{% endraw %}


{% for elem in meta.elems %}
### {{elem}} {$ elem $}
  <details>
  <summary> {{ elem }} {% title %} {% elem %}</summary>
  other text
  </details>

{% endfor %}

### LE2dFrm

<details>
  <summary>Click here {{page.elems[0]}}</summary>
  
  #### Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets
</details>