This folder is the template of the chapter folder.

This folder should contain subfolders based on structure:
- `/images`
  should contain all images/illustrations per chapter
	- `/images/src`
	  contains all illustrations made in software that must be rendered before use
		- `/images/src/kicad`
		  schematics in kicad. Needs to be rendered to svg before inserting
		- `/images/src/inkscape`
		  theoretically may be used to create `svg` as is, but better to re-render later to plain svg (include fonts, text as vector, etc.)
	- `/images/render`
	  contains rendered images as per `src` scheme above
	- `/images/other`
	  contains pictures / photos and other stuff that might have been taken from the other places of as a photographed
- `/references`
  should contain all the documentation and references for chapter. according to substructure:
	- `/references/datasheets`
		- datasheets for components, devices, ICs, etc.
	- `/references/application_notes`
		- application noted from manufacturers of electronics
	- `/references/publications`
		- articles, other publications
	- `/references/manuals`
		- operational manuals, if illustration is taken from it
		- protocol descriptions
	- `/references/lectures`
		- lecture notes, presentation from online courses, etc.
	- `/references/patents`
		- patents
	- `/references/regulatory`
		- stuff like standards, etc.


Template folder should contain empty `.gitkeep` file per each sub-folder since git by default ignores empty folders.

For each online resource: consider having back-up link, created with [Wayback Machine](https://web.archive.org/)

