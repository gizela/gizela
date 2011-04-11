function [corr,dhLocalIJ,dhGeoIJ] = cs3d_height(pointI,pointJ,pointR,R)

%% point - (x y z) coordinates in local system
%%	- i -> point from
%%	- j -> point to
%%	- r -> coordinates of reference point
%% R - radius of reference sphere
%% corr - corection in radians

gammaRI = cs3d_gamma(pointR,pointI,R);
gammaRJ = cs3d_gamma(pointR,pointJ,R);

q1RI = (R+pointR(3))*(1/cos(gammaRI)-1);
q1RJ = (R+pointR(3))*(1/cos(gammaRJ)-1);

q2RI = pointI(3)-pointR(3)-(pointI(3)-pointR(3))/cos(gammaRI);
q2RJ = pointJ(3)-pointR(3)-(pointJ(3)-pointR(3))/cos(gammaRJ);

corr = -q2RJ-q1RJ+q2RI+q1RI;
dhLocalIJ = pointJ(3)-pointI(3);
dhGeoIJ = dhLocalIJ - corr;
