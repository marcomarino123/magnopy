==================================================
cell <units> <scale>
a_x a_y a_z
b_x b_y b_z
c_x c_y c_z
==================================================
atoms <units>
atom-1 i j k <spin>
...
atom-n i j k <spin>
==================================================
notation
double-counting  value
spin-normalized  value
exchange-factor  number
on-site-factor   number
==================================================
ground-state <Units>
q1 q2 q3
nx ny nz # or a<number> b<number>
==================================================
exchange <units>
--------------------------------------------------
atom-1 atom-2 i j k
<isotropic Jiso>
<dmi Dx Dy Dz>
<matrix
Jxx Jxy Jxz
Jyx Jyy Jyz
Jzx Jzy Jzz>
<symmetric-anisotropy Sxx Syy Sxy Sxz Syz>
--------------------------------------------------
...
--------------------------------------------------
atom-1 atom-2 i j k
<isotropic Jiso>
<dmi Dx Dy Dz>
<matrix
Jxx Jxy Jxz
Jyx Jyy Jyz
Jzx Jzy Jzz>
<symmetric-anisotropy Sxx Syy Sxy Sxz Syz>
--------------------------------------------------
==================================================
on-site <units>
--------------------------------------------------
atom-1
Axx Ayy Azz Axy Axz Ayz
--------------------------------------------------
...
--------------------------------------------------
atom-n
Axx  Ayy Azz Axy Axz Ayz
--------------------------------------------------
==================================================
