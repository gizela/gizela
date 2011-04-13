#!/usr/bin/octave --silent

% vypocet redukci pomoci vektoru

R = 6356752.31425 % polomer nahradni koule

% stanovisko
cb_stn = 222;
x_stn = 2e3; y_stn = 2e3; z_stn = 2e3 + R;

% cilove body
x=[]; y=[]; z=[]; cb=[];
for i=1:3
	for j=1:3
		for k=1:3
			if i==2 & j==2
				continue
			end

			cb(end+1) = i*100 + j*10 + k;
		        x(end+1) = i*1e3;
		        y(end+1) = j*1e3;
			z(end+1) = k*1e3 + R;
		end
	end
end

%[lam, phi, r] = cart2sph(x, y, z)

%plot3(x, y, z, '*r')
%pause

% redukce zenitoveho uhlu
P1 = [x_stn y_stn z_stn]; % vektor stanoviska
nz = [0 0 1]; % vektor z-ove osy
for i=1:length(x)
	P2 = [x(i) y(i) z(i)];
	v12 = P2 - P1;
        zm(i) = acos(v12*P1'/norm(P1)/norm(v12));
	zr(i) = acos(v12*nz'/norm(v12)/norm(nz));
end
dz= zr - zm;

fprintf('Redukce zenitoveho uhlu\n')
fprintf('%5s %8s %8s %9s\n', 'cb.', 'zenit m', 'zenit r', 'redukce cc')
fprintf('%5i %8.4f %8.4f %9.4f\n', [cb; zm*200/pi; zr*200/pi; dz*200/pi*1e4])

% redukce vodorovneho smeru
% normaly rovin
nx = [1 0 0]; 
nr1 = cross(nx,P1);
nr1r = cross(nz,nx);
for i=1:length(x)
	P2 = [x(i) y(i) z(i)];
	v12 = P2 - P1;
	nr2 = cross(P1,v12);
	psim(i) = acos(nr1*nr2'/norm(nr1)/norm(nr2));
	% redukovane smery
	%nr2r = cross(nz,v12);
	%psir(i) = acos(nr1r*nr2r'/norm(nr1r)/norm(nr2r));
	psir(i) = atan2(P2(2) - P1(2), P2(1) - P1(1));
	if psir(i) < 0
		psir(i) = psir(i) + 2*pi;
	end
	dpsi_pom = [psir(i) - psim(i)
	            psir(i) - psim(i) + pi
	            psir(i) - psim(i) + pi/2
	            psir(i) - psim(i) - pi
	            psir(i) - psim(i) - pi/2];
	[absmin, imin] = min(abs(dpsi_pom)); 
	dpsi(i) = dpsi_pom(imin);
end
%dpsi = psir - psim;

fprintf('Redukce vodorovneho smeru\n')
fprintf('%5s %8s %8s %9s\n', 'cb.', 'smer m', 'smer r', 'redukce cc')
fprintf('%5i %8.4f %8.4f %9.4f\n', [cb; psim*200/pi; psir*200/pi; dpsi*200/pi*1e4])

% vytvoreni tabulky latexu
fprintf('\\begin{tabular}{|c|r|r|r|}')

% vytvoreni vstupni davky pro gama
%outf = 'theCube.gkf';
%%fid = fopen(outf,'wt');
%fid = 1;
%fprintf(fid,'<gama-local>\n<network angles="left-handed" axes-xy="en">\n<description>The Cube - from vectors</description>\n<points-observations direction-stdev="10" distance-stdev="10" zenith-angle-stdev="10">\n')
%fprintf(fid, '  <point id="%i" x="%.5f" y="%.5f" z="%.5f" fix="xyz">\n', [cb_stn; x_stn; y_stn; z_stn-R])
%fprintf(fid, '  <point id="%i" x="%.5f" y="%.5f" z="%.5f" adj="xyz">\n', [cb; x; y; z-R])
%
%
%fprintf(fid, '</points-observations>\n</network>\n</gama-local>')
%fclose(fid)
