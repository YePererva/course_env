from PIL import Image

import os, logging

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

def convert_to_lossless_webp (input_file_path, export_file_path):
    try:
        # Open the original image
        with Image.open(input_file_path) as img:
            img.save(export_file_path, format="WebP", lossless=True, quality=100, method=6)
    except Exception as e:
        logger.info(f"Error converting image {image_name}: {str(e)}")
