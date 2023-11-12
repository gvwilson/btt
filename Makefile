include lib/book/book.mk

## --------------------

## release: make a release
.PHONY: release
ifeq ($(origin BTT_RELEASE),undefined)
release:
	@echo "BTT_RELEASE not defined"
else
release:
	rm -rf docs
	make build
	rm -rf ${BTT_RELEASE}
	mkdir ${BTT_RELEASE}
	(cd docs && tar cf - $$(find . -name '*.css' -o -name '*.html' -o -name '*.ico' -o -name '*.jpg' -o -name '*.js' -o -name '*.png' -o -name '*.svg' -o -name '*.webp')) \
	| (cd ${BTT_RELEASE} && tar xf -)
endif

## settings: show variables
.PHONY: settings
settings: book_settings
