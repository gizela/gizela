tex=$(wildcard *.tex)
proj=$(tex:.tex=)

all:
	make $(proj:=.pdf)

%.pdf: %.tex
	pdflatex $<

clean:
	rm -f *.pdf
	rm -f *.aux
	rm -f *.log
	rm -f *.toc


