# Compile MarkDown notes into static web-site

I want to keep personal notes on technical topics (microcontroller programming, typical circuit solutions, etc.) and later publish them on GitHub pages for easier access from whereever I would need to.

## General concept

- To use MarkDown notes and appropriate software. For example:
	- Obsidian
	- VSCode with plugins
- For illustrations, use (if necessary) [InkScape](https://inkscape.org/release/), [KiCAD](https://www.kicad.org/download/), etc.
- Save notes to GitHub repository
- Export the Github repository for the site to
	- GitHub pages
	- local server for self-hosting

## Tools used and their versions

Thease instruction were tested on WIndows 11 and Ubuntu 24.04. LTS running on WSL.

- [mkdocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
	- Static web page generator with additional plugins
- [GitHub](https://github.com/) + [Github pages](https://pages.github.com/)
	- Storage and hosting
- [Inkscape](https://inkscape.org/release/) 1.4
	- for additional illustrations
- [KiCad](https://www.kicad.org/download) 9
	- for technical illustrations on circuitry
- [Python](https://www.python.org/downloads/) 3.13.2
	- for local tests and skips for batch processing of files (conversion kicad to svg, etc.)