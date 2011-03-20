dirs = $(shell ls -d */)
.PHONY: all

run:
	#echo $(dirs)
	make $(dirs:/=.run)
	
%.run: %
	$(MAKE) -C $<


