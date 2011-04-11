function [corr,zLocalIJ,zGeoIJ] = cs3d_zenith(pointI,pointJ,pointR,R)

%% point - (x y z) coordinates in local system
%%	- i -> point from
%%	- j -> point to
%%	- r -> coordinates of reference point
%% R - radius of reference sphere
%% corr - corection in radians

%% atan2 better then acos? http://www.mathworks.com/matlabcentral/newsreader/view_thread/151925
%% angle = atan2(norm(cross(a,b)),dot(a,b));
%% angle = acos(dot(a,b)/(norm(a)*norm(b)));

ez = [0,0,1];

vectorR = [pointR(1:2) pointR(3)+R];
normal = vectorR+(pointI-pointR);
normal = normal/norm(normal);

vectorIJ = pointJ-pointI;
vectorIJ = vectorIJ/norm(vectorIJ);

% atan2 is not neede because z is not expected near 0 gon
zGeoIJ = acos(dot(normal,vectorIJ));
zLocalIJ = acos(dot(ez,vectorIJ));

corr = zLocalIJ-zGeoIJ;
