Part B: Rectangular Section
---------------------------

This problem was used to study some possible applications of automatic
differentiation to inelastic section analysis. Using a differentiable
programming framework, a return-mapping algorithm was implemented which
accounts for linear or nonlinear isotropic hardening, and basic
kinematic hardening. This algorithm is called to evaluate cross
sectional forces for a given strain distribution, and this procedure is
differentiated with forward-mode automatic differentiation to yield the
tangent stiffness of the cross section.

![Plastic limit surface for various integration
rules.](docs/img/p3/B-1-1-40.pdf)

plastic surface

### Experiment I: O-A-B-O

![](docs/img/p1/limit-quad-4.png){width="60%," height="60%"}

![Section response to load history
O-A-B-O](docs/img/p1/stress-hist-3d-4-4.png){width="60%," height="60%"}

![Figure 1: Strain and stiffness history for load path
O-A-B-O](docs/img/p1/strain-stiffness-1-4.png){#fig:ssh-oabo}

### Experiment II: O-A-B-C-O

![](docs/img/p1/limit-quad4-4.png){width="60%," height="60%"}

![Section response to load history
O-A-B-C-O](docs/img/p1/stress-hist-3d-4-4-4.png){width="60%,"
height="60%"}

![Figure 2: Strain and stiffness history for load path
O-A-B-O](docs/img/p1/strain-stiffness-1-4.png){#fig:ssh-oabo}
