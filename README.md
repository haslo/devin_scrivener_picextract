# Scrivener Image Extractor

This Python script is designed to extract all images from a Scrivener project and save them to a specified output directory.

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
- Images are copied with their original filenames. If the original filenames are not available, they will be saved with the filenames found in the project.
- The script does not currently restore original filenames if they have been changed within the Scrivener project. This may be a feature added in future updates.

## Contributing

If you would like to contribute to this project or suggest improvements, please feel free to do so via the GitHub repository.

## License

This project is open-source and available under the MIT License.
