# By default, show available commands
.DEFAULT: commands

# Tools
ARK := ark
BIBER := biber
PYTHON := python

# Directories.
ARK_BIN := lib/mccole/bin
SRC_DIR := src
HTML_DIR := docs

# Files.
CONFIG := config.py
MARKDOWN := ${SRC_DIR}/index.md $(wildcard src/*/index.md)

# Configuration.
SLUG := $(shell python ${CONFIG} --slug)
BUILD_DATE := $(shell date '+%Y-%m-%d')
STEM := $(strip ${SLUG})-${BUILD_DATE}

# Generated output.
HTML := $(patsubst ${SRC_DIR}/%.md,${HTML_DIR}/%.html,${MARKDOWN})
LATEX := ${HTML_DIR}/${STEM}.tex

# ----------------------------------------------------------------------

## commands: show available commands
.PHONY: commands
commands:
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## build: rebuild the site
.PHONY: build
build:
	@mkdir -p ${HTML_DIR}
	${ARK} build

## serve: rebuild and serve the site
.PHONY: serve
serve:
	@mkdir -p ${HTML_DIR}
	${ARK} serve

## docs: rebuild code documentation
docs: DOCS.md
DOCS.md: ${ARK_BIN}/make_docs.py
	python ${ARK_BIN}/make_docs.py \
		--config ${CONFIG} \
		--src ${SRC_DIR} \
		--title "Documentation" \
		--notdirs conduct docs license \
		--notfiles '*/test_*.py' \
		> $@

## latex: re-create all-in-one LaTeX file
latex:
	@${PYTHON} ${ARK_BIN}/html2tex.py --config ${CONFIG} --outfile ${LATEX}

## --------------------

## style: check code style
.PHONY: style
style:
	@ruff check .

## reformat: reformat unstylish code
.PHONY: reformat
reformat:
	@ruff format .

## lint: check project organization
.PHONY: lint
lint: ${HTML}
	@${PYTHON} ${ARK_BIN}/lint.py --config ${CONFIG} --src src

## bibvalid: run biber to validate bibliography
.PHONY: bibvalid
bibvalid:
	@biber --tool --validate-datamodel info/bibliography.bib

## valid: run html5validator on generated files
.PHONY: valid
valid:
	@html5validator --root ${HTML_DIR} ${HTML} \
	--ignore \
	'Attribute "markdown" not allowed on element'

## --------------------

## clean: tidy up
.PHONY: clean
clean:
	@rm -rf ${HTML_DIR}
	@find . -name '*~' -exec rm {} \;
	@find . -name '*.blg' -exec rm {} \;
	@find . -name __pycache__ -exec rm -r {} +
	@find . -name .pytest_cache -exec rm -r {} +

## sterile: really tidy up
.PHONY: sterile
sterile: clean
	@rm -rf ${OUT_DIR}

## --------------------

## order: show chapter order
.PHONY: order
order:
	@python ${ARK_BIN}/order.py ${CONFIG}

# book_settings: show common settings
.PHONY: book_settings
book_settings:
	@echo "ARK:" ${ARK}
	@echo "ARK_BIN:" ${ARK_BIN}
	@echo "CONFIG:" ${CONFIG}
	@echo "HTML:" ${HTML}
	@echo "HTML_DIR:" ${HTML_DIR}
	@echo "LATEX:" ${LATEX}
	@echo "MARKDOWN:" ${MARKDOWN}
	@echo "SRC_DIR:" ${SRC_DIR}
	@echo "SLUG:" ${SLUG}
	@echo "BUILD_DATE:" ${BUILD_DATE}
	@echo "STEM:" ${STEM}
