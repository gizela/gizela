syms sxx syy szz sxy sxz syz dx dy dz
S=[sxx sxy sxz; sxy syy syz; sxz syz szz]
D=[dx; dy; dz]
det(S)
t=simplify(D'*inv(S)*D*det(S))