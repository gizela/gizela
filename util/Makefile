proj=$(wildcard *.gkf)

all:
	./coord2gamaObs.py --sigma-xy 0.015 ../example/text/epoch0.txt > epoch0.gkf
	./coord2gamaObs.py ../example/text/epoch1.txt > epoch1.gkf
	./coord2gamaObs.py ../example/text/epoch2.txt > epoch2.gkf
	./coord2gamaObs.py ../example/text/epoch3.txt > epoch3.gkf
	make $(proj:.gkf=.xml)

%.xml: %.gkf
	gama-local --text $(<:.gkf=.adj) --xml $(<:.gkf=.xml) $<
