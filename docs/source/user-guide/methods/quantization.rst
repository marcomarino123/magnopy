.. _user-guide_methods_quantization:

************
Quantization
************

.. dropdown:: Notation used on this page

  * .. include:: page-notations/bra-ket.inc
  * .. include:: page-notations/uvn-or-spherical.inc
  * .. include:: page-notations/quantum-operators.inc

======================================
Classical to quantum spin fluctuations
======================================

We have seen in :ref:`section <user-guide_methods_spin-fluctuations>`
that small transverse spin fluctuations modify the minimum-energy spin vector
from :math:`\ket{S_i^0}=S_i\,\ket{f_i}` to
:math:`\ket{S_{mi}}=\ket{S_i^0}+\ket{\delta S_{mi}}`, with coordinates
in the spherical local basis

.. math::
  &^{sf}\boldsymbol{S_{mi}}\,=\,S_i\,\,\,^{sf}\boldsymbol{\hat{f}_i}\,+\,
    ^{sf}\boldsymbol{\delta S_{mi}}\\\\
  &\begin{pmatrix}
        \frac{1}{\sqrt{2}}\,S^{pt,-}_{mi}\\
        \frac{1}{\sqrt{2}}\,S^{pt,+}_{mi}\\
        S^{f}_{mi}
    \end{pmatrix}\,=\,
    \begin{pmatrix}
        0\\0\\S_i
    \end{pmatrix}+
    \begin{pmatrix}
        \frac{1}{\sqrt{2}}\,\delta S^{pt,-}_{mi}\\
        \frac{1}{\sqrt{2}}\,\delta S^{pt,+}_{mi}\\
        -\delta S_{mi}^f
    \end{pmatrix}

where the :math:`pt`-superindex will be dropped from now on.
The transition from classical to quantum fluctuations is achieved by replacing those
small classical fluctuations by quantum operators representing quantum fluctuations
as follows:

.. math::
  ^{sf}\boldsymbol{S_{mi}} \,\longrightarrow \,\boldsymbol{\cal{S}_{mi}}

These operators are requested to satisfy the conventional spin algebra
where the quantization axis is chosen to be :math:`\boldsymbol{\hat{f}}`,

.. math::
  [{\cal S}_{mi}^f,\, {\cal S}_{m' j}^{\pm}]\,
  &=\, \pm
  \delta_{m m'}\, \delta_{ij}\, {\cal S}_{mi}^{\pm}
  \\
  [{\cal S}_{mi}^+,\, {\cal S}_{m' j}^{-}]\,
  &=\,
  2\, \delta_{m m'}\, \delta_{ij}\, {\cal S}_{mi}^f
  \\
  [\boldsymbol{\cal S}_{mi}^2,\, {\cal S}_{m' j}^{\alpha}]\,
  &=
  0

They are also requested to act on the Hilbert space of a spin with
total angular momentum :math:`S_i`, meaning  that
:math:`\delta {\cal S}_{mi}^n\leq 2\,S_i`.

==============================================================
Decomposition of spin operators into Holstein-Primakoff bosons
==============================================================
Quantum spin waves are bosonic particles carrying spin 1.
A convenient representation of the quantum spin operators into bosonic
fields is achieved through the Holstein-Primakoff decomposition [1]_

.. math::
  \boldsymbol{\cal S_{mi}}
  =
  \begin{pmatrix}
    \frac{1}{\sqrt{2}}\,{\cal S}^-_{mi}
    \\ \frac{1}{\sqrt{2}}\,{\cal S}^+_{mi}
    \\ {\cal S}^f_{mi}\end{pmatrix}
  =
   \begin{pmatrix}\frac{1}{\sqrt{2}}\,\delta  {\cal S}_{mi}^-\\
  \frac{1}{\sqrt{2}}\,\delta {\cal S}_{mi}^+\\S_{i}-\delta {\cal S}_{mi}^f
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
:math:`\cal S_{mi}^f` with bosons decreases
the spin by one quantum unit per boson.


.. note::
  Note that the definition above departs slightly from convention, because
  :math:`{\cal S}^\pm` are divided by :math:`\sqrt{2}`. The rationale behind this
  departure lies in the connection to the spherical basis.

================
Spin wave theory
================
Expansion of the square roots above leads to an infinite series in :math:`1/S_i`.
Specifically, expanding it to first order one obtains the first four orders
as follows:

.. math::
  \boldsymbol{\cal S}_{mi}
  \approx
  \begin{pmatrix}
    0 \\ 0 \\
    S_i
  \end{pmatrix}
   +
  S_i^{1/2}\,
  \begin{pmatrix}
    a^\dagger_{mi}  \\a_{mi} \\ 0
  \end{pmatrix}
  +
  S_i\,
  \begin{pmatrix}
    0 \\ 0 \\ - n_{mi}
  \end{pmatrix}
  +\frac{1}{4\,S_i^{1/2}}\,
  \begin{pmatrix}
   -a^\dagger_{mi} \,n_{mi} \\
    -n_{mi}\,a_{mi} \\
    0
  \end{pmatrix}

Interestingly, further corrections appear only in the transverse spin components.
This :math:`1/S_i` expansion, that translates directly into the quantum
Hamiltonian is called Spin Wave Theory.

Spin Wave Theory assumes a magnetically ordered ground state
upon which bosonic spin excitations are built.
Therefore, the theory is supposed to work whenever :math:`n_{mi}\ll S_i` or, in
physical terms, when the spin fluctuations are sufficiently small. In practice, the
:math:`1/S_i` expansion of the square roots is truncated either at :math:`1/S_i` or at
:math:`1/S_i^2` orders in the Hamiltonian. The :math:`1/S_i` truncation leads to a
bilinear bosonic Hamiltonian whose handling is termed
:ref:`Linear Spin Wave Theory <user-guide_methods_lswt>`. Truncation at :math:`1/S_i^2`
leads to a biquadratic bosonic Hamiltonian whose handling is called Renormalized Spin
Wave Theory.

==========
References
==========

.. [1] Holstein, T., & Primakoff, H. (1940).
       Field dependence of the intrinsic domain magnetization of a ferromagnet.
       Physical Review, 58(12), 1098.
       |HP-ref|_
