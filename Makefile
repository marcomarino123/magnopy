.DEFAULT_GOAL := help

# Sphinx-related variables
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

help:
	@echo "\x1b[31m"
	@echo "Please specify what do you want to do!"
	@echo "\x1b[0m"
	@echo "Available options are:\n"
	@echo "    help - show this message"
	@echo "    html - build the html docs"
	@echo "    clean-html - clean all files from docs and build html docs from scrutch"
	@echo "    doctest - run doctests"
	@echo "    clean - clean all files from docs and pip routines"
	@echo "    install - install the package"
	@echo "    test - execute unit tests"
	@echo "    pictures-for-docs - plot all pictures for the documentation"

html:
	@$(SPHINXBUILD) -M html "docs/$(SOURCEDIR)" "docs/$(BUILDDIR)" $(SPHINXOPTS)

clean-html: clean install html
	@echo "Done"

doctest:
	@$(SPHINXBUILD) -b doctest "docs/$(SOURCEDIR)" "docs/$(BUILDDIR)" $(SPHINXOPTS)

clean:
	-@rm -r docs/build
	-@rm -r docs/source/api/generated
	-@rm -r docs/source/api/crystal/generated
	-@rm -r docs/source/api/exchange/generated
	-@rm -r docs/source/api/spinham/generated
	-@rm -r docs/source/api/magnons/generated
	-@rm -r docs/source/api/_autosummary
	-@rm -r magnopy/magnopy.egg-info
	-@rm -r build
	-@rm -r dist
	-@rm -r .venv/lib/python*/site-packages/magnopy*
	-@rm -r .venv/lib/python*/site-packages/magnopy*
	-@rm -r .venv/bin/magnopy*

install:
	@python3 -m pip install .

test:
	@pytest -s

pictures-for-docs:
	@python3 docs/images/scripts/cs-choice.py -rd .
	@python3 docs/images/scripts/spin-rotations.py -rd .
