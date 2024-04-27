# Detritus Projection Viewer

This Python code randomly displays the 15585 detritus images in full screen. The viewer displays images in full screen with a time interval between each image and without repeating. Once all images have been displayed, they will reappear randomly.

## Requirements

- Python 3.x
- pygame (pygame)

## Installation of Dependencies

Before running the program, make sure you have the following dependencies installed:

### Python 3.x

If you don't have Python installed, you can download it from the official website: [Python.org](https://www.python.org/).

### pygame

You can install pygame using pip, the Python package manager. Run the following command in your terminal:

pip install pygame

Once these dependencies are installed, you will be able to run the program without any issues

## Usage

1. Clone this repository or download the `detritus.py` file.
2. Make sure you have the images you want to view in a folder.
3. Modify the `images_directory` variable in the code to point to the directory where your images files are located.
4. Run the `detritus.py` script.
5. Images will play randomly across the entire screen
6. Press the 'q' key at any time to exit. IMPORTANT: The program exit may take a couple of seconds. It is not necessary to press the key repeatedly.

## Configuration

- You can adjust the time between changing images by modifying the `seconds_between_images` variable.
The number before the multiplication * 1000 is the number of seconds it will take to make the change. For example, if you want it to take 5 seconds to change the line of code, it should look like this:

seconds_between_images = 5 * 1000