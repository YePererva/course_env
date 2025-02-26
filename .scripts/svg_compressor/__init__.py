import os
import logging 
from scour import scour

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def compress_svg(input_file, output_file=None):

    options = scour.generateDefaultOptions()
    
    # High compression settings
    options.strip_comments = True
    options.strip_xml_prolog = True
    options.remove_metadata = True
    options.enable_viewboxing = True
    options.indent_type = 'none'
    #options.digits = 3
    options.simplify_colors = True
    options.remove_descriptive_elements = True
    options.strip_ids = True
    options.shorten_ids = True
    options.enable_id_stripping = True
    options.newlines = False
    
    # Read the input file
    with open(input_file, 'r') as f:
        svg_raw_data = f.read()
    
    # Get original file size
    original_size = len(svg_raw_data)
    
    # Compress the SVG
    compressed_svg = scour.scourString(svg_raw_data, options)
    
    
    # Calculate size reduction percentage
    reduction_delta = (original_size - len(compressed_svg))
    reduction_ratio = reduction_delta / original_size * 100

    logger.info(f"Space saving: {reduction_delta} bytes, {reduction_ratio:.2f}%")
    
    # Determine output path
    if output_file is None:
        output_file = input_file
        logger.info("No output file specified, will overwrite input file")
    
    # Write the compressed SVG
    with open(output_file, 'w') as f:
        f.write(compressed_svg)
    
        logger.info(f"Compressed size: {compressed_size:,} bytes")