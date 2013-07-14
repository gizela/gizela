all:
	@echo "Generate Sphinx"
	@echo
	#$(MAKE) -C sphinx/ html
	cd ./sphinx; make html
	
	@echo
	@echo "Generate Epydoc"
	cd ./epydoc; make

test:
	@echo "Generate Sphinx"
	@echo
	#$(MAKE) -C sphinx/ html
	cd ./sphinx; make html-test
	
	@echo
	@echo "Generate Epydoc"
	cd ./epydoc; make test
