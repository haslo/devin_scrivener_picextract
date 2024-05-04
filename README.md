# Scrivener Image Extractor

This Python script is designed to extract all images from a [Scrivener](https://www.literatureandlatte.com/scrivener/overview) project and save them to a specified output directory.

## Creation

This script was entirely written by [Devin](https://www.cognition-labs.com/introducing-devin), with prompting by [haslo](https://github.com/haslo).

## Usage

To use the script, you need to have Python installed on your system. The script is compatible with macOS, which is similar to the Linux environment it was developed in.

Run the script from the command line using the following format:

```
python extract_images.py <path_to_scrivener_project> <path_to_output_directory>
```

Replace `<path_to_scrivener_project>` with the full path to the root directory of your Scrivener project (the .scriv folder), and `<path_to_output_directory>` with the path where you want the images to be saved.

## Example

```
python extract_images.py /Users/username/Documents/MyScrivenerProject.scriv /Users/username/Documents/MyScrivenerImages
```

This will extract all images from `MyScrivenerProject.scriv` and place them in the `MyScrivenerImages` directory.

## Script Parameters

- `scrivener_project_root`: The root directory of the Scrivener project from which to extract images.
- `output_directory`: The directory where the extracted images will be saved.

## Notes

- The script currently extracts images with the following extensions: `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`.
- Images are copied with their names as in the Scrivener project.

## License

This project is open-source and available under the MIT License.
