BUILD = build
MAKEFILE = Makefile
OUTPUT_FILENAME = game-of-thrones-episode-guide
WIKI_DOWNLOAD_SCRIPT = scripts/game-of-thrones-episode-guide-downloader.py
MARKDOWN_OUTPUT = $(BUILD)/markdown/$(OUTPUT_FILENAME).md
PDF_OUTPUT = $(BUILD)/pdf/$(OUTPUT_FILENAME).pdf
HTML_OUTPUT = $(BUILD)/html/$(OUTPUT_FILENAME).html
EPUB_OUTPUT = $(BUILD)/epub/$(OUTPUT_FILENAME).epub
TOC = --toc --toc-depth=2
LATEX_TPL = templates/template.tex
ARGS = $(TOC)

all: book

book: epub html pdf

clean:
	rm -r $(BUILD)

markdown: $(MARKDOWN_OUTPUT)

epub: $(EPUB_OUTPUT)

html: $(HTML_OUTPUT)

pdf: $(PDF_OUTPUT)

$(MARKDOWN_OUTPUT): $(MAKEFILE) $(MARKDOWN_GEN_SCRIPT)
	mkdir -p $(BUILD)/markdown
	python $(WIKI_DOWNLOAD_SCRIPT) $@

$(EPUB_OUTPUT): markdown $(MAKEFILE)
	mkdir -p $(BUILD)/epub
	pandoc $(ARGS) -o $@ -s $(MARKDOWN_OUTPUT)

$(HTML_OUTPUT): markdown $(MAKEFILE)
	mkdir -p $(BUILD)/html
	pandoc $(ARGS) --standalone --to=html5 -o $@ $(MARKDOWN_OUTPUT)

$(PDF_OUTPUT): markdown $(MAKEFILE) $(LATEX_TPL)
	mkdir -p $(BUILD)/pdf
	pandoc $(ARGS) \
		--template=$(LATEX_TPL)  \
		--variable mainfont="Palatino" \
		--variable sansfont="Helvetica" \
		--variable monofont="Menlo" \
		--variable fontsize=12pt \
		-s $(MARKDOWN_OUTPUT) \
		-o $@
