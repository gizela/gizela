clear all

syms dx1 dx2 dy1 dy2 dz1 dz2 a11 a12 a13 a22 a23 a33 b11 b12 b13 b22 b23 b33

l1 = [dx1; dy1; dz1]
l2 = [dx2; dy2; dz2]
s1 = [a11 a12 a13; a12 a22 a23; a13 a23 a33]
s2 = [b11 b12 b13; b12 b22 b23; b13 b23 b33]
is1 = inv(s1)
is2 = inv(s2)
is1_p_is2 = is1 + is2
atpa = inv(s1)*l1 + inv(s2)*l2
sx = inv(is1_p_is2)
x = sx*atpa