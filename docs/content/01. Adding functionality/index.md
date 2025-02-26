# Adding functionality
If you are running some sort of technical repo, that you'd probably need:

## as MkDocs components

- [x] diagramming:
	- [x] mermaid diagrams
- [x] code blocks
	- code blocks
- [x] user warnings
	- callouts
- [x] switchable content depending on user system
	- various code for different operating systems)
	- a.k.a. tabbed content
- [x] render of math equations:
	- KATEX or MathJax:  [documentation](https://squidfunk.github.io/mkdocs-material/reference/math/)
- [x] some fun / special icons
	- emoji : [documentation](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/#search)
- [ ] Including text-content of sub-files
	- [GitHub](https://github.com/cmacmackin/markdown-include)
	- doesn't work so far
- [ ] For course materials, it might be also good to have the timestamp of the [last update](https://github.com/mkdocs/mkdocs/issues/1408)
	- `mkdocs-git-revision-date-plugin`
	- so far works weirdly
- [x] tasklist render
- [ ] [[WikiLinks]]
	- [ ] supposed to work with either
		- `mkdocs-roamlinks-plugin`
		- `mkdocs-ezlinks-plugin`
	- [ ] doesn't work with `![[  ]]` format
- [ ] add pdf or print button to page with schematics
	- [ ] works with plain text pages, but fails if there is math or diagrams

## As separate from mkdocs

- User scripts for:
	- [ ] batch converting to `svg` illustrations
		- [x] KiCad schematics
			- [x] cropping by content
			- [x] adding white background
		- [ ] Insckape illustrations
			- [ ] all figures to path
			- [ ] same white bakground
			- [ ] padding
			- [ ] incorporate font into svg
		- [ ] fritzing (?)
		- [ ] draw.io diagrams
		- [x] compression of produced svg
- [ ] extra configs for automatic use of those scripts on push to repo?