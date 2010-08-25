
# These make targets aren't really critical, they are more of a cheatsheet to
# remind me of a few commonly-used commands.

# I run these under Ubuntu bash, or on Windows with Cygwin binaries on the PATH


PACKAGE := caughtcube
VERSION := `python -c "from ${PACKAGE}.version import version; print version"`
RUN = run.py


stats:
	@echo "non-blank lines of code:"
	@echo -n 'product: '
	@find ${PACKAGE} -name '*.py' | grep -v "/tests/" | xargs cat | grep -cve "^\W*$$"
	@echo -n 'tests: '
	@find ${PACKAGE} -name '*.py' | grep "/tests/" | xargs cat | grep -cve "^\W*$$"
.PHONY: stats


clean:
	rm -rf build dist tags pip-log.txt
	-find ${PACKAGE} \( -name "*.py[oc]" -o -name "*.orig" \) -exec rm {} \;
.PHONY: clean


tags:
	ctags -R ${PACKAGE}
.PHONY: tags


# runsnake is a GUI profile visualiser, very useful. See README to install.
profile:
	python -O -m cProfile -o profile.out ${RUN}
	runsnake profile.out
.PHONY: profile


tests:
	nosetests ${PACKAGE}
.PHONY: alltests


py2exe:
	rm -rf dist/${PACKAGE}
	python setup.py --quiet py2exe
.PHONY: py2exe


