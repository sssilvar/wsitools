github:
	@cd docsrc && make html
	@cp -a docsrc/_build/html/. ./docs