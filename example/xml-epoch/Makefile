GAMA_ALG=envelope
GAMA_OPT=--algorithm $(GAMA_ALG) --cov-band 2
GKFC=$(wildcard epoch*.gkfc)
PROJS=$(GKFC:.gkfc=.adj.xml)
joined=joined.gkfc
PROJS+=$(joined:.gkfc=.adj.xml)
GAMA=../../../gama/gama-local/gama-local

%.adj.xml: %.gkfc
	$(GAMA) $(GAMA_OPT) $< --text $(@:.xml=.txt) --xml $@

all:
	make $(PROJS)

clean:
	rm -f $(PROJS)
	rm -f $(PROJS:.xml=.txt)

svd:
	make GAMA_ALG='svd' $(PROJS)

gso:
	make GAMA_ALG='gso' $(PROJS)

cho:
	make GAMA_ALG='cholesky' $(PROJS)

env:
	make GAMA_ALG='envelope' $(PROJS)

join:
	../../bin/gama-data-obs.py --xml=$(joined) --change-id-prefix="e_%i_" --hold-id="ABC1,ABC2" $(GKFC)
