.. _user-guide_methods_quantum-spin-fluctuations:

*************************
Quantum spin fluctuations
*************************

.. dropdown:: Notation used on this page

  * .. include:: page-notations/vector.inc
  * .. include:: page-notations/matrix.inc
  * .. include:: page-notations/parentheses.inc
  * .. include:: page-notations/operators.inc
  * .. include:: page-notations/bra-ket.inc
  * .. include:: page-notations/uvn-or-spherical.inc

======================================
Classical to quantum spin fluctuations
======================================

We have seen in the :ref:`previous section <user-guide_methods_classical-spin-fluctuations>`
that small transverse spin fluctuations modify the spin vector
from :math:`\boldsymbol{S^{F,s}_i}=S_i\,\boldsymbol{\hat{n}}` to

.. math::
  \boldsymbol{\tilde{S}^{F,s}}_{mi}
  =
  S_i\, \boldsymbol{\hat{n}}
  +
  \frac{\delta S_{mi}^-}{\sqrt{2}}\, \boldsymbol{\hat{u}^+}
  +
  \frac{\delta S_{mi}^+}{\sqrt{2}}\, \boldsymbol{\hat{u}^-}
  -
  \delta S_{mi}^n\, \boldsymbol{\hat{n}}
  =
  \begin{pmatrix}
    \frac{1}{\sqrt{2}}\, \delta S_{mi}^- \\
    \frac{1}{\sqrt{2}}\, \delta S_{mi}^+ \\
    S_{i} - \delta S_{mi}^n
  \end{pmatrix}

The transition from classical to quantum fluctuations is achieved by replacing the small
classical fluctuations by quantum operators representing quantum fluctuations

.. math::
  &\delta S_{mi}^{\pm,n} \longrightarrow \delta \cal{S}_{mi}^{\pm,n}
  \\\\
  &\boldsymbol{\tilde{S}^{F,s}}_{mi} \longrightarrow \boldsymbol{\cal{S}^{F,s}}_{mi}

where

.. math::
  \boldsymbol{\cal{S}^{F,s}}_{mi}
  &=
  S_i\, \boldsymbol{\hat{n}}
  +
  \frac{\delta {\cal S}_{mi}^-}{\sqrt{2}}\, \boldsymbol{\hat{u}}^+
  +
  \frac{\delta {\cal S}_{mi}^+}{\sqrt{2}}\, \boldsymbol{\hat{u}}^-
  -
  \delta {\cal S}_{mi}^n\,\boldsymbol{\hat{n}}
  =\\\\&=
  \begin{pmatrix}
    \frac{1}{\sqrt{2}}\,{\cal S}_{mi}^- \\
    \frac{1}{\sqrt{2}}\,{\cal S}_{mi}^+ \\
    {\cal S}_{mi}^n
  \end{pmatrix}
  =
  \begin{pmatrix}
    \frac{1}{\sqrt{2}}\, \delta {\cal S}_{mi}^- \\
    \frac{1}{\sqrt{2}}\, \delta {\cal S}_{mi}^+ \\
    S_{i}-\delta {\cal S}_{mi}^n
  \end{pmatrix}

These operators are requested to satisfy the conventional spin algebra
where the quantization axis is chosen to be :math:`\boldsymbol{\hat{n}}`,

.. math::
  [{\cal S}_{mi}^n,\, {\cal S}_{m' j}^{\pm}]\,
  &=\, \pm
  \delta_{m m'}\, \delta_{ij}\, {\cal S}_{mi}^{\pm}
  \\
  [{\cal S}_{mi}^+,\, {\cal S}_{m' j}^{-}]\,
  &=\,
  2\, \delta_{m m'}\, \delta_{ij}\, {\cal S}_{mi}^{n}
  \\
  [\boldsymbol{\cal S}_{mi}^2,\, {\cal S}_{m' j}^{\alpha}]\,
  &=
  0

They are also requested to act on the Hilbert space of a spin with
total angular momentum :math:`S_i`, meaning  that
:math:`\delta {\cal S}_{mi}^n\leq 2\,S_i`.

Furthermore, application of intracell rotations leads to

.. math::
  \boldsymbol{R}^s_i\, \boldsymbol{\cal{S}^{F,s}}_{mi}
  =
  \frac{\delta {\cal S}_{mi}^-}{\sqrt{2}}\, \boldsymbol{\hat{p}}^s_i
  +
  \frac{\delta {\cal S}_{mi}^+}{\sqrt{2}}\, \boldsymbol{\hat{t}}^s_i
  +
  (S_i - \delta {\cal S}_{mi}^n)\, \boldsymbol{\hat{f}}^s_i

==============================================================
Decomposition of spin operators into Holstein-Primakoff bosons
==============================================================
Quantum spin waves are bosonic particles carrying spin 1.
A convenient representation of the quantum spin operators into bosonic
fields is achieved through the Holstein-Primakoff decomposition [1]_

.. math::
  \boldsymbol{\cal S}^{F,s}_{mi}
  =
  \begin{pmatrix}
    \frac{1}{\sqrt{2}}\,{\cal S}^-_{mi}
    \\ \frac{1}{\sqrt{2}}\,{\cal S}^+_{mi}
    \\ {\cal S}^n_{mi}\end{pmatrix}
  =
   \begin{pmatrix}\frac{1}{\sqrt{2}}\,\delta  {\cal S}_{mi}^-\\
  \frac{1}{\sqrt{2}}\,\delta {\cal S}_{mi}^+\\S_{i}-\delta {\cal S}_{mi}^n
    \end{pmatrix}
    =
  \begin{pmatrix}
    \sqrt{S_i} \,\, a^{\dagger}_{mi} \,\,\sqrt{1 - \dfrac{n_{mi}}{2S_i}} \\
    \sqrt{S_i}\,\,\sqrt{1 - \dfrac{n_{mi}}{2S_i}}\,\,a_{mi} \\
    (S_i - n_{mi})
  \end{pmatrix}

where :math:`a_{mi}^\dagger\,/\,a_{mi}` creates/destroys bosons
at site :math:`(m,\,i)`, and :math:`n_{mi}=a^\dagger_{mi}\,a_{mi}`
is the boson number operator. Hilbert space preservation then requires
that :math:`n_{mi}\leq 2\,S_i`. Notice how populating
:math:`\boldsymbol{\cal S}^{F,s}_{mi}` with bosons decreases
:math:`{\cal S}_z`, by one quantum unit per boson.


.. note::
  Note that the definition above departs slightly from convention, because
  :math:`{\cal S}^\pm` are divided by :math:`\sqrt{2}`. The rationale behind this
  departure lies in the connection to the spherical basis.

================
Spin wave theory
================
Expansion of the square roots above leads to an infinite series in :math:`1/S_i`.
If one expand the square root up to the first order in :math:`1/S_i`, one obtains the
first four orders as follows:

.. math::
  \boldsymbol{\cal S}^{F,s}_{mi}
  \approx
  S_i\, \boldsymbol{\hat{n}}
  +
  S_i^{1/2}\, (
    a_{mi}^\dagger\, \boldsymbol{\hat u}^+
    +
    a_{mi}\, \boldsymbol{\hat u}^-
  )
  -
  n_{mi}\, \boldsymbol{\hat{n}}
  -
  \frac{1}{4\, S_i^{1/2}}\, (
    a_{mi}^\dagger\, n_{mi}\, \boldsymbol{\hat u}^+
    +
    a_{mi}\, n_{mi}\, \boldsymbol{\hat u}^-
  )

These become upon intracell rotation (for definition of vectors
:math:`\boldsymbol{\hat{p}}_i^s`, :math:`\boldsymbol{\hat{t}}_i^s` and
:math:`\boldsymbol{\hat{f}}_i^s` see
:ref:`here <user-guide_methods_spherical-rf_ptf-definition>`)

.. math::
  \boldsymbol{\cal S}^s_{mi}
  \approx
  S_i\, \boldsymbol{\hat{f}}^s_i
  +
  S_i^{1/2}\, (
    a_{mi}^\dagger\, \boldsymbol{\hat p}^s_i
    +
    a_{mi}\, \boldsymbol{\hat t}^s_i
  )
  -
  n_{mi}\, \boldsymbol{\hat{f}}^s_i
  -
  \frac{1}{4\, S_i^{1/2}}\, (
    a_{mi}^\dagger\, n_{mi}\, \boldsymbol{\hat p}^s_i
    +
    a_{mi}\,n_{mi}\, \boldsymbol{\hat t}^s_i
  )

Interestingly, further corrections appear only in the transverse spin components (i.e.
along :math:`\boldsymbol{\hat{u}}^{\pm}`). This :math:`1/S_i` expansion, that
translates directly into the quantum Hamiltonian is called Spin Wave Theory.

Spin Wave Theory assumes a magnetically ordered ground state
:math:`\boldsymbol{S}_{mi}^{F,s}` upon which bosonic spin excitations are built.
Therefore, the theory is supposed to work whenever :math:`n_{mi}\ll S_i` or, in
physical terms, when the spin fluctuations are sufficiently small. In practice, the
:math:`1/S_i` expansion of the square roots is truncated either at :math:`1/S_i` or at
:math:`1/S_i^2` orders in the Hamiltonian. The :math:`1/S_i` truncation leads to a
bilinear bosonic Hamiltonian whose handling is termed
:ref:`Linear Spin Wave Theory <user-guide_methods_lswt>`. Truncation at :math:`1/S_i^2`
leads to a biquadratic bosonic Hamiltonian whose handling is called Renormalized Spin
Wave Theory.

.. dropdown:: Details

  Truncation of the square root expansion at :math:`1/S_i` is given by

  .. math::
    \sqrt{1 - \dfrac{n_{mi}}{2S_i}}
    =
    1 + \mathcal{O}\left(\dfrac{1}{S_i}\right)

  which leads to the expression of the spin operators

  .. math::
    \boldsymbol{\cal S}^s_{mi}
    \approx
    S_i\, \boldsymbol{\hat{f}}^s_i
    +
    S_i^{1/2}\, (
      a_{mi}^\dagger\, \boldsymbol{\hat p}^s_i
      +
      a_{mi}\, \boldsymbol{\hat t}^s_i
    )

  When inserted in the Hamiltonian this truncation leads to the Linear Spin Wave Theory.

  Truncation of the square root expansion at :math:`1/S_i^2` is given by

  .. math::
    \sqrt{1 - \dfrac{n_{mi}}{2S_i}}
    =
    1 - \dfrac{n_{mi}}{4S_i} + \mathcal{O}\left(\dfrac{1}{S_i^2}\right)

  which leads to the expression of the spin operators

  .. math::
    \boldsymbol{\cal S}^s_{mi}
    \approx
    S_i\, \boldsymbol{\hat{f}}^s_i
    +
    S_i^{1/2}\, (
      a_{mi}^\dagger\, \boldsymbol{\hat p}^s_i
      +
      a_{mi}\, \boldsymbol{\hat t}^s_i
    )
    -
    n_{mi}\, \boldsymbol{\hat{f}}^s_i
    -
    \frac{1}{4\, S_i^{1/2}}\, (
      a_{mi}^\dagger\, n_{mi}\, \boldsymbol{\hat p}^s_i
      +
      a_{mi}\,n_{mi}\, \boldsymbol{\hat t}^s_i
    )

  when inserted in the spin Hamiltonian, this truncation leads to the Renormalized
  Spin Wave Theory.



==========
References
==========

.. [1] Holstein, T., & Primakoff, H. (1940).
       Field dependence of the intrinsic domain magnetization of a ferromagnet.
       Physical Review, 58(12), 1098.
       |HP-ref|_
