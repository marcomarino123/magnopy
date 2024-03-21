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
	@echo "    model-input-examples-run - run the model input examples"
	@echo "    requirements - install all requirements"

html:
	@$(SPHINXBUILD) -M html "docs/$(SOURCEDIR)" "docs/$(BUILDDIR)" $(SPHINXOPTS)

clean-html: clean install html
	@echo "Done"

doctest:
	@$(SPHINXBUILD) -b doctest "docs/$(SOURCEDIR)" "docs/$(BUILDDIR)" $(SPHINXOPTS)

clean:
	-@rm -r docs/build
	-@rm -r docs/source/*/generated
	-@rm -r docs/source/*/*/generated
	-@rm -r docs/source/*/*/*/generated
	-@rm -r magnopy/magnopy.egg-info
	-@rm -r build
	-@rm -r dist
	-@rm -r .venv/lib/python*/site-packages/magnopy*
	-@rm -r .venv/lib/python*/site-packages/magnopy*
	-@rm -r .venv/bin/magnopy*

install:
	@python3 -m pip install .

test:
	@pytest -s #-o log_cli=true -o log_cli_level=DEBUG

pictures-for-docs:
	@python3 docs/images/scripts/uvn-rf.py -rd .
	@python3 docs/images/scripts/spin-rotations.py -rd .
	@python3 docs/images/scripts/single-q.py -rd .
	@python3 docs/images/scripts/minimization-exchange.py -rd .
	@python3 docs/images/scripts/plot-repositories.py -rd .

model-input-examples-run:
	@python3 utests/test_io/test_txt/test_verify.py

requirements:
	@pip install -r requirements.txt --no-cache
	@pip install -r requirements-dev.txt --no-cache
	@pip install -r docs/requirements.txt --no-cache
	@pip install -r utests/requirements.txt --no-cache
