function [corr,dirLocalIJ,dirGeoIJ] = cs3d_direction(pointI,pointJ,pointR,R)

%% point - (x y z) coordinates in local system
%%	- i -> point from
%%	- j -> point to
%%	- r -> coordinates of reference point
%% R - radius of reference sphere
%% corr - corection in radians

%ex = [1,0,0];
%ey = [0,1,0];
ez = [0,0,1];

vectorR = [pointR(1:2) pointR(3)+R];
n = vectorR+(pointI-pointR);
n = n/norm(n);

vectorRI = pointI-pointR;
vectorRI = vectorRI/norm(vectorRI);

vectorIJ = pointJ-pointI;
vectorIJ = vectorIJ/norm(vectorIJ);

%vxy_ij = [vectorIJ(1:2) 0];

%dirLocal1 = acos(dot(ex,vxy_ij));
%if (vxy_ij(2) < 0)
%	dirLocal1 = 2*pi-dirLocal1;
%endif
%disp(dirLocal1*200/pi);


%Reference plane nLocalRI
nLocalRI = cross(ez,vectorRI);
nLocalRI = nLocalRI/norm(nLocalRI);

%Plane of sight in local system
nLocalIJ = cross(ez,vectorIJ);
nLocalIJ = nLocalIJ/norm(nLocalIJ);

cVectorLocal = cross(nLocalRI,nLocalIJ);
dirLocalIJ = atan2(norm(cVectorLocal),dot(nLocalRI,nLocalIJ));
if (cVectorLocal(3) < 0)
	dirLocalIJ = 2*pi-dirLocalIJ;
endif

%Plane of sight in geodetic system
nGeoIJ = cross(n,vectorIJ);
nGeoIJ = nGeoIJ/norm(nGeoIJ);

%dirGeoIJ = acos(dot(nGeoX,nGeoIJ)/(norm(nGeoX)*norm(nGeoIJ)))
cVectorGeo = cross(nLocalRI,nGeoIJ);
dirGeoIJ = atan2(norm(cross(nLocalRI,nGeoIJ)),dot(nLocalRI,nGeoIJ));
if (cVectorGeo(3) < 0)
	dirGeoIJ = 2*pi-dirGeoIJ;
endif

corr = dirLocalIJ-dirGeoIJ;
