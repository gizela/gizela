gama=../../util/gama/gama-local/gama-local
gama_opt=--ellipsoid wgs84 --latitude 50 --cpoint-x 500 --cpoint-y 500 --cpoint-z 500

gkf=$(wildcard *.gkf)
proj=$(gkf:.gkf=)

all:
	make $(proj:=.adj)

%.adj:%.gkf
	$(gama) $(gama_opt) --xml $@ --text $(<:.gkf=.adj.txt) $<

clean:
	rm -f $(proj:=.adj)
	rm -f $(proj:=.adj.txt)

xml:
	$(gama) --ellipsoid wgs84 --latitude 0 --cpoint-x 0 --cpoint-y 0 --cpoint-z 0 xml-corr.xml --text xml-corr.txt

xml2:
	$(gama) --algorithm gso --ellipsoid wgs84 --latitude 0 --cpoint-x 0 --cpoint-y 0 --cpoint-z 0 xml-corr2.xml --text xml-corr2.txt
	$(gama) --algorithm gso xml-corr2.corrected.xml --text xml-corr2.corrected.txt
