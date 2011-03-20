GAMA_ALG=envelope
GAMA_OPT=--algorithm $(GAMA_ALG) #--cov-band 2
GKFC=$(wildcard *.gkfc)
PROJS=$(GKFC:.gkfc=.adj.xml)
GAMA=../gama-local

%.adj.xml: %.gkfc
	$(GAMA) $(GAMA_OPT) $< --text $@.txt --xml $@

all:
	make $(PROJS)

clean:
	rm -f $(PROJS)
	rm -f $(PROJS:=.txt)
	rm -f *.out

svd:
	make GAMA_ALG='svd' $(PROJS)

gso:
	make GAMA_ALG='gso' $(PROJS)

cho:
	make GAMA_ALG='cholesky' $(PROJS)

env:
	make GAMA_ALG='envelope' $(PROJS)
