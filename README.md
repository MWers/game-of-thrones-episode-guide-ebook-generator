# Game of Thrones Episode Guide eBook Generator

This repo contains code that will generate ebooks from the Game of Thrones episode summaries at the excellent [Game of Thrones Wiki](https://gameofthrones.fandom.com/).

## Requirements

This has the following dependencies:

- [Pandoc](http://pandoc.org/)
- [LaTeX](https://www.latex-project.org/)

Additionally, the Python wiki download script requires [requests](http://docs.python-requests.org/en/master/).

## Usage

### Generate PDF

```bash
make pdf

# => build/pdf/game-of-thrones-episode-guide.pdf
```

### Generate Markdown

```bash
make markdown

# => build/markdown/game-of-thrones-episode-guide.md
```

### Generate EPUB

```bash
make epub

# => build/epub/game-of-thrones-episode-guide.epub
```

### Generate HTML

```bash
make html

# => build/html/game-of-thrones-episode-guide.html
```

### Generate All Document Types

```bash
make all

# =>
# └── build
#     ├── epub
#     │   └── game-of-thrones-episode-guide.epub
#     ├── html
#     │   └── game-of-thrones-episode-guide.html
#     ├── markdown
#     │   └── game-of-thrones-episode-guide.md
#     └── pdf
#         └── game-of-thrones-episode-guide.pdf
```

### Remove Generated Files

```bash
make clean
```

## Acknowledgements

Massive thanks to the awesome [Game of Thrones Wiki](https://gameofthrones.fandom.com/) for their great content. I strongly encourage everyone to give them your support.