vec1=../example/vec/vec2008j.gkf 
vec2=../example/vec/vec2008p.gkf 
vec3=../example/vec/vec2008j-lgo.gkfc
vec3adj=../example/vec/vec2008j-lgo.adj
pol1=../example/pol/pol2008j-3d.gkf
latlon=50.090833,14.400555
epoch1= ../example/xml-epoch/epoch0.adj.xml
epoch2=../example/xml-epoch/epoch1.adj.xml
joined=../example/xml-epoch/joined.adj.xml
gama=../../gama/gama-local/gama-local

all:
	#./compare_obs.py --vecl --cpoint=$(latlon) $(vec1) $(vec2)
	#./tran_vec.py --cpoint=$(latlon) < $(vec1)
	#./view_gama_adj.py --xy --displScale2D=6000:2 --figScale=1:6000 --cpoint=$(latlon) $(epoch1) $(epoch2)
	#./gama-data-obs.py --fileConXY=coor_xy.txt --fix= --tran-vec-2d --config=example.cfg
	#./gama-data-obs.py --fileFixXY=coor_xy.txt --con=AB,1011
	#./gama-data-obs.py --tran-vec-2d --config=example.cfg $(vec3) $(vec3adj)
	#./gama-data-obs.py --config=example.cfg --fileConXYZ=coor_xyz.txt --proj-point-2d --proj-vec-2d --reduce-s-dist --scale-vec-cov-mat=3 --xml=test.xml $(vec1) 
	#./gama-data-obs.py --config=example.cfg --local-system-2d --proj-vec-2d --sdist-to-dist --dist-scale --scale-vec-cov-mat=3 --xml=test.xml --adj-xy=1003,1005 --fix-xy=1011 --fix-xyz=1012 $(pol1) $(vec3) $(vec3adj) 

	#./gama-data-obs.py --config=example.cfg --xml=test.xml --file-coord=coord.txt --change-id-prefix="e_%i_" --hold-id="501,502" $(pol1) $(vec1) --delete-zenith-angle

	#./gama-data-obs.py --config=example.cfg --xml=test.xml --coord-from-adjustment=$(epoch1) --change-id-prefix="e_%i_" --hold-id="501,502" $(pol1) $(vec1) --delete-zenith-angle

	#./gama-data-adj.py --config=example.cfg --local-system-3d --joined='^e_(\d+)_(.+)$$,0,1' $(joined) --print-displacements=displ.txt

	./gama-data-adj.py --config=example.cfg --local-system-2d --print-displacements=displ.txt --plot-xy --fig-scale=1:4500 --use-apriori --show-figure --displ-scale-xy=5000 $(epoch1)

	./gama-data-adj.py --config=example.cfg --local-system-2d --print-displacements=displ.txt --tran-point-2d=0.8660254,0.5,-0.5,0.8660254,1000,5000 --plot-xy --fig-scale=1:4500 --use-apriori --show-figure --displ-scale-xy=5000 $(epoch1)
