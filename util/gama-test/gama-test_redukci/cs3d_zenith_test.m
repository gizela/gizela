R = 6381822.81658;
ro = 200/pi;
pointR = [0,0,0];
pointI = [500,500,20];
hDiff = 20;
scale = 0.1;
pointJCenter = [500,500,0];
pointJ = [
	1000,000,0
	1000,1000,0
	0,1000,0
	-1000,1000,0
	-1000,000,0
	-1000,-1000,0
	0,-1000,0
	1000,-1000,0
	];
pointJ = scale*pointJ;
pointJ = [pointJ(:,1:2) pointJ(:,3)+hDiff];

printf('Test of zenith correction:\n');
printf('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n');
printf('Radius : %10.3f\n',R);
printf('R : %10.3f %10.3f %10.3f\n\n',pointR);
printf('I : %10.3f %10.3f %10.3f\n',pointI);

for (i = 1:1:size(pointJ,1))
	pointJTmp = pointJ(i,:)+pointJCenter;
	[corr,zLocalIJ,zGeoIJ] = cs3d_zenith(pointI,pointJTmp,pointR,R);

	printf('J : %10.3f %10.3f %10.3f\n',pointJTmp);
	printf('Corr : %0.4f g\n',corr*ro);
%	printf('Z geo: %0.10f g\n',zGeoIJ*ro);
%	printf('Z loc: %0.10f g\n\n',zLocalIJ*ro);

%%Computation by L.Hradilek formulas

%Geocentric angle from R->I
gammaRI = cs3d_gamma(pointR,pointI,R);
[dircorr,dirLocalIJ,dirGeoIJ] = cs3d_direction(pointI,pointJTmp,pointR,R);

%L.Hradilek formula
corr2 = cos(dirGeoIJ)*gammaRI;

	printf('Sigma  geo: %0.10f g\n',(dirGeoIJ)*ro);
%	printf('Zenith geo: %0.10f g\n',zGeoIJ*ro);
%	printf('2Gamma : %0.10f g\n',gammaRI*ro);
	printf('Corr2  : %0.4f g\n\n',corr2*ro);	
endfor
