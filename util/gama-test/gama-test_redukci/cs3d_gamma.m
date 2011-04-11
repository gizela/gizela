function [gamma] = cs3d_gamma(pointI,pointR,R)

vectorR = [pointR(1:2) pointR(3)+R];
n = vectorR+(pointI-pointR);
n = n/norm(n);

gamma = atan2(norm(cross(vectorR,n)),dot(vectorR,n));
