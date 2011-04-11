R = 6381822.81658;
ro = 200/pi;
pointR = [0,0,0];
pointI = [1000,1000,0];
hDiff = 1000;
scale = 1;
pointJCenter = [1000,00,0];
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

printf('Test of height correction:\n');
printf('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n');
printf('Radius : %10.3f\n',R);
printf('R : %10.3f %10.3f %10.3f\n\n',pointR);
printf('I : %10.3f %10.3f %10.3f\n',pointI);

for (i = 1:1:size(pointJ,1))
	pointJTmp = pointJ(i,:)+pointJCenter;
	[corr,dhLocalIJ,dhGeoIJ] = cs3d_height(pointI,pointJTmp,pointR,R);

	printf('J : %10.3f %10.3f %10.3f\n',pointJTmp);
	printf('dh geo: %0.4f\n',dhGeoIJ);
	printf('dh loc: %0.4f\n',dhLocalIJ);
	printf('Corr : %0.4f\n',corr);
endfor
