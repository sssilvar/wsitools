github:
	@cd docsrc && make html
	@ rm -rf docs/
	@cp -r docsrc/_build/html/ ./docs
	@touch docs/.nojekyll