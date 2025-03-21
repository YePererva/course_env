import os
import logging 
from scour import scour

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger('svg_compressor')

kicad_compression_options = scour.generateDefaultOptions()

kicad_compression_options.strip_comments = True
kicad_compression_options.strip_xml_prolog = True
kicad_compression_options.remove_metadata = True
kicad_compression_options.enable_viewboxing = True
kicad_compression_options.indent_type = 'none'
kicad_compression_options.simplify_colors = True
kicad_compression_options.remove_descriptive_elements = True
kicad_compression_options.strip_ids = True
kicad_compression_options.shorten_ids = True
kicad_compression_options.enable_id_stripping = True
kicad_compression_options.newlines = False


def compress_svg(input_file, output_file=None):
  
    with open(input_file, 'r') as f:
        svg_raw_data = f.read()

    compressed_svg = scour.scourString(svg_raw_data, kicad_compression_options)
    
    # Calculate size reduction percentage
    original_size = len(svg_raw_data)
    reduction_delta = (original_size - len(compressed_svg))
    reduction_ratio = reduction_delta / original_size * 100

    logger.info(f"Space saving:\n\t {reduction_delta} bytes, {reduction_ratio:.2f}%")
    
    # Determine output path
    if output_file is None:
        output_file = input_file
        logger.info("No output file specified, will overwrite input file")
    
    # Write the compressed SVG
    with open(output_file, 'w') as f:
        f.write(compressed_svg)
