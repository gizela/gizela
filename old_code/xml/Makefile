pys=$(wildcard *.py)

.PHONY: run

run:
	make $(pys:.py=.run)

%.run: %.py
	python $<

