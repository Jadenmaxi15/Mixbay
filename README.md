# Mixabay Image Viewer

This is a simple Python application built using the Tkinter library to fetch and display images from Pixabay. It allows the user to enter a keyword, and then it fetches relevant images using the Pixabay API based on that keyword. The user can navigate through the fetched images using "Next" and "Previous" buttons and close the image viewer window when done.

## Requirements

Before running the application, make sure you have the following:

1. Python installed on your system.
2. Tkinter library (usually included with Python installations).
3. Requests library (`pip install requests`)
4. PIL (Python Imaging Library) library (`pip install pillow`)

## Getting Started

1. Clone this repository to your local machine.
2. Replace `'YOUR_PIXABAY_API_KEY'` with your actual Pixabay API key in the code.

## How to Use

1. Run the application by executing the script: `python pixabay_image_viewer.py`
2. The main application window will open with a text entry field and a "Search Images" button.
3. Enter a keyword (e.g., "nature," "animals," etc.) in the text entry field.
4. Click the "Search Images" button to fetch images related to the entered keyword from Pixabay.
5. A new window will pop up displaying the images fetched from Pixabay in a slideshow format.
6. Click the "Next" and "Previous" buttons to navigate through the images.
7. Click the "Close" button to close the image viewer window when done.

## Important Note

Make sure to replace `'YOUR_PIXABAY_API_KEY'` with your actual Pixabay API key before running the application. You can obtain a free API key by signing up on the Pixabay website.

**Disclaimer**: This application is for educational purposes and uses the Pixabay API to fetch images. Make sure to review and comply with the Pixabay API terms and conditions before using this application in any commercial or production environment.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
