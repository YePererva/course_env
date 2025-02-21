'''
# Kicad Project Files. Keeping only schematics and custom symbols
Get-ChildItem -Path "$ProjectFolder" -Recurse -File -include *.kicad_pro, *.pro, *.kicad-pcb, *.kicad_prl  | Remove-Item

'''

import os, sys
import logging
import re

from local_repo import project_root_folder, content_folder

purgatory_extensions = ['.kicad_pro', '.pro', '.kicad-pcb', '.kicad_prl']

if __name__ == "__main__":
	logger = logging.getLogger(__name__)
	logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

	logger.info(f"Detected project root folder:\n\t{project_root_folder}")
	logger.info(f"Looking for KiCAD schematics in folder:\n\t{content_folder}")

	for root, dirs, files in os.walk(content_folder):
		for _ in dirs:
			if _.lower().endswith(r"-backups".lower()):
				_ = os.path.join(root, _)
				logger.info(f"Deleting backups folder:\n\t{_}")
				os.remove(_)

		for _ in files:
			if any(_.lower().endswith(extension.lower()) for extension in purgatory_extensions):
				_ = os.path.join(root, _)
				logger.info(f"Deleting KiCAD not-needed files:\n\t{_}")
				print(_)

