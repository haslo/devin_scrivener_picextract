import os
import shutil
import argparse
import xml.etree.ElementTree as ET
from pathlib import Path

# Supported image extensions
IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')

def extract_images(scrivener_project_root, output_directory):
    scrivener_project_root = Path(scrivener_project_root)
    output_directory = Path(output_directory)
    output_directory.mkdir(parents=True, exist_ok=True)

    # Determine the .scrivx file name from the project root directory name
    project_name = scrivener_project_root.stem  # Assuming the project root directory ends with '.scriv'
    if project_name.endswith('.scriv'):
        project_name = project_name[:-6]  # Remove the '.scriv' part
    scrivx_file = scrivener_project_root / f"{project_name}.scrivx"

    tree = ET.parse(scrivx_file)
    root = tree.getroot()
    uuid_to_filename = {}
    for binder_item in root.iter('BinderItem'):
        uuid = binder_item.get('UUID')
        title_element = binder_item.find('Title')
        file_extension_element = binder_item.find('MetaData').find('FileExtension') if binder_item.find('MetaData') is not None else None
        if title_element is not None and file_extension_element is not None:
            title = title_element.text
            file_extension = file_extension_element.text
            if uuid and title and file_extension:
                uuid_to_filename[uuid] = f"{title}.{file_extension}"

    # Walk through the Scrivener project directory to find and copy image files
    for root, dirs, files in os.walk(scrivener_project_root):
        for file in files:
            if file.lower().endswith(IMAGE_EXTENSIONS):
                source_file = Path(root) / file
                # Extract UUID from the directory name
                uuid = Path(root).name
                # Use the original filename if it's in the mapping
                original_filename = uuid_to_filename.get(uuid, file)
                destination_file = output_directory / original_filename
                # Check for duplicate filenames and append a number if necessary
                counter = 1
                while destination_file.exists():
                    name, ext = os.path.splitext(original_filename)
                    destination_file = output_directory / f"{name}({counter}){ext}"
                    counter += 1
                shutil.copy2(source_file, destination_file)
                print(f"Copied {file} to {destination_file}")

def main():
    parser = argparse.ArgumentParser(description='Extract images from a Scrivener project.')
    parser.add_argument('scrivener_project_root', type=str, help='Root directory of the Scrivener project')
    parser.add_argument('output_directory', type=str, help='Output directory to store the extracted images')

    args = parser.parse_args()
    extract_images(args.scrivener_project_root, args.output_directory)

if __name__ == "__main__":
    main()
