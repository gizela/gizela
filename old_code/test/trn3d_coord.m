%%
%% function [xx, yy, zz] = trn3d_coord(key, x, y, z)
%% 
%% fukce pro prostorovou transformaci souradnic
%%
%% key = [ q, alpha, beta, gamma, tx, ty, tz ] 
%%

%% Author: Tomas Kubin
%% License: GPL

function [xx, yy, zz] = trn3d_coord(key, x, y, z)

if nargin ~= 4
	error('trn3d_coord: chybny pocet vstupnich parametru')
end

if length(key) ~= 7
	error('trn3d_coord: transformacni klic musi mit 7 prvku')
end

if length(x) ~= length(y) | length(x) ~= length(z)
	error('trn3d_coord: vektory souradnic nemaji stejne dimenze')
end

x=x(:); y=y(:); z=z(:);

q     = key(1);
alpha = key(2);
beta  = key(3);
gamma = key(4);
tx    = key(5);
ty    = key(6);
tz    = key(7);

R(alpha, beta, gamma)
XX = q*[x y z] * R(alpha, beta, gamma)' + repmat([tx ty tz], length(x), 1);

xx = XX(:,1); yy = XX(:,2); zz = XX(:,3);

end


%% lokalni funkce

function R = Ra(alpha)
R = [ 1      0            0
      0   cos(alpha)   sin(alpha)
      0  -sin(alpha)   cos(alpha) ];
end

function R = Rb(beta)
R = [ cos(beta)   0  -sin(beta)
         0        1      0
      sin(beta)   0   cos(beta) ];
end

function R = Rc(gamma)
R = [  cos(gamma)   sin(gamma)   0
      -sin(gamma)   cos(gamma)   0
          0            0         1 ];
end

function R = R(alpha, beta, gamma)
R = Rb(beta)*Ra(alpha)*Rc(gamma);
end
