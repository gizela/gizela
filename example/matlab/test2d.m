syms sxx syy sxy dx dy
S=[sxx sxy; sxy syy]
D=[dx; dy]
det(S)
t=simplify(D'*inv(S)*D*det(S))