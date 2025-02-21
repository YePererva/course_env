import os, sys, subprocess
import logging

content_folder_name = "docs"
images_folder_name = "images"
images_src_folder_name = "src"
images_render_folder_name = "render"
images_software_folder_name = "kicad"

project_root_folder = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
content_folder = os.path.join(project_root_folder, content_folder_name)
src_folder_postfix = os.path.join(images_folder_name, images_src_folder_name, images_software_folder_name)
target_folder_postfix = os.path.join(images_folder_name, images_render_folder_name, images_software_folder_name)


