.PHONY: pdf
pdf:
	pandoc \
		--toc \
		--toc-depth=2 \
		--template=template.tex \
		--variable mainfont="Palatino" \
		--variable sansfont="Helvetica" \
		--variable monofont="Menlo" \
		--variable fontsize=12pt \
		-s game-of-thrones-episode-guide.md \
		-o output/game-of-thrones-episode-guide.pdf

.PHONY: epub
epub:
	pandoc \
		--toc \
		--toc-depth=2 \
		-s game-of-thrones-episode-guide.md \
		-o output/game-of-thrones-episode-guide.epub
