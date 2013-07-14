cfg=epydoc.cfg
cfg-test= epydoc-test.cfg

all:
	epydoc --config $(cfg)

check:
	epydoc --check --config $(cfg)

verb:
	epydoc -v --config $(cfg)

sync:
	make all
	rsync -av html/ slon:/var/www/gizela/html

test:
	epydoc --config $(cfg-test)
	
clean:
	-rm -rf build/*

clean-test:
	-rm -rf build-test/*
