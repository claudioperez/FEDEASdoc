# LimEqns_2dFrm

Returns a matrix of element limit-surface equations, `LimEqns`, for the frame element specified in data structure `ElemData`.

## Syntax

- `LimEqns = LimEqns_2dFrm (ElemData, lim_coef)`
- `LimEqns = LimEqns_2dFrm (ElemData, lim_coef, xyz)`

### Parameters

--------------------

- `ElemData`: cell array\
  Contains element property data.

  Element plastic capacity information is stored in the fields `Np`, `Mp`, and `Vp`, and may take the following forms: (REWRITE/CLARIFY)
  
  $$\left[\begin{array}{ll}
  \mathrm{Q}_{\mathrm{pi}}^{(+)} & \mathrm{Q}_{\mathrm{pi}}^{  (-)} \\
  \mathrm{Q}_{\mathrm{pj}}^{(+)} & \mathrm{Q}_{\mathrm{pj}}^{  (-)}
  \end{array}\right]$$

  $$\left[\begin{array}{ll}
  \mathrm{Q}_{\mathrm{pi}}^{(+)} & \mathrm{Q}_{\mathrm{pi}}^{(-)}
  \end{array}\right]
  \quad \rightarrow \left[\begin{array}{ll}
  \mathrm{Q}_{\mathrm{pi}}^{(+)} & \mathrm{Q}_{\mathrm{pi}}^{(-)}   \\
  \mathrm{Q}_{\mathrm{pi}}^{(+)} & \mathrm{Q}_{\mathrm{pi}}^{(-)}
  \end{array}\right]$$
  
  $$
  \left[\begin{array}{l}
  \mathrm{Q}_{\mathrm{pi}}^{(+)} \\
  \mathrm{Q}_{\mathrm{pj}}^{(+)}
  \end{array}\right] 
  \quad \rightarrow \left[\begin{array}{ll}
  \mathrm{Q}_{\mathrm{pi}}^{(+)} & \mathrm{Q}_{\mathrm{pi}}^{(+)}   \\
  \mathrm{Q}_{\mathrm{pj}}^{(+)} & \mathrm{Q}_{\mathrm{pj}}^{(+)}
  \end{array}\right]
  $$
  
  $$\mathrm{Q}_{\mathrm{pi}}^{(+)} \rightarrow
  \left[\begin{array}{ll}
  \mathrm{Q}_{\mathrm{pi}}^{(+)} & \mathrm{Q}_{\mathrm{pi}}^{(+)}   \\
  \mathrm{Q}_{\mathrm{pi}}^{(+)} & \mathrm{Q}_{\mathrm{pi}}^{(+)}
  \end{array}\right]$$

- `lim_coef`: float array.

   If an $n \times 1$ array is passed, $n$ piecewise linear equations of the following form will be generated for each element:
   $$a_n \frac{|Q_i|}{Q_{i,pl}}    \leq 1.0$$

   If an $n \times 2$ array is passed, $n$ piecewise linear axial-moment interaction equations of the following form will be generated for each element:
   $$a_n \frac{|N|}{N_{pl}} + b_n\frac{|M_z|}{M_{p,z}}   \leq 1.0$$

   If an $n \times 3$ array is passed, $n$ piecewise linear axial-moment-shear interaction equations of the following form will be applied:
   $$a_n \frac{|N|}{N_{p}} + b_n \frac{|M|}{M_{p}} + c_n \frac{|V|}{V_{p}} \leq 1.0$$

### Case III: NVM interaction
-----------------------------

Interaction between shear, moment, and axial forces is implemented with $n$ piecewise linear equations of the following form:

$$a_n\dfrac{|N|}{N_p} + b_n\dfrac{|M|}{M_p} + c_n\dfrac{|V|}{V_p} \leq1.0$$

$N$, $M$, and $V$ are substituted by $Q_1$, $Q_2$, and $(Q_2 +Q_3)/L$ respectively, and the equations are rearranged and implemented follows:

$$\dfrac{a}{N_p}Q_1 + \dfrac{b}{M_p}Q_2 + \dfrac{ c}{LV_p}(Q_2+Q_3) \leq1.0$$

$$\dfrac{a}{N_p}Q_1 + \left(\dfrac{b}{M_p}+\dfrac{c}{LV_p}\right)Q_2 + \dfrac{c}{LV_p}Q_3 \leq1.0$$

