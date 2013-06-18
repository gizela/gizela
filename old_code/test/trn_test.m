output_precision(15)

lat = 50.091153311111
lon = 14.401833202777

alpha = 0
beta = (lat - 90) * pi / 180
gamma = (lon - 180) * pi / 180

%% key = [ q, alpha, beta, gamma, tx, ty, tz ] 
key = [1, alpha, beta, gamma, 0, 0, 0]

x =  354.799
y = -465.803
z = -164.077

[xx, yy, zz] = trn3d_coord(key, x, y, z)
