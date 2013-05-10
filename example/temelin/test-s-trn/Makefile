proj=$(wildcard SS*.txt)
# local file
coord2gamaObs= ../../../util/coord2gamaObs.py
gizela=gama-data-adj.py
# id testovanych bodu
id_test=117,118
gizela_opt= --local-system-2d \
            --config=temelin.cfg \
            --config-fig=temelin-fig.cfg \
            --fig-scale=1:25000 \
            --displ-scale-xy=25000:2 \
            --title="Primary system JETE" \
            --plot-xy \
            --use-apriori \

all:
	make $(proj:.txt=.gkf)
	make $(proj:.txt=.xml)
	# vykresleni strednich elips chyb
	#$(gizela) $(gizela_opt) --conf-prob=0.39 --show-figure --save-xy=posuny-elipsy.png --subtitle="displacements, error ellipses" $(proj:.txt=.xml) 

	# testovani
	#$(gizela) $(gizela_opt) --conf-prob=0.99 --test-xy --print-test=testy-posunu.txt --show-figure --save-xy=posuny-test.png --subtitle="displacements, tests" $(proj:.txt=.xml)
	#$(gizela) $(gizela_opt) --conf-prob=0.99 --test-id=120 --test-xy --show-figure --save-xy=posuny-test-120.png --subtitle="displacement, test, point 120" $(proj:.txt=.xml)

%.gkf: %.txt
	$(coord2gamaObs) $< > $(<:.txt=.gkf)

%.xml: %.gkf
	gama-local --text $(<:.gkf=.adj) --xml $(<:.gkf=.xml) $<

clean:
	rm -f $(proj:.txt=.gkf)
	rm -f $(proj:.txt=.adj)
	rm -f $(proj:.txt=.xml)
	rm -f posuny-elipsy.png testy.txt obrazek-test.png
