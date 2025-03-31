# Extracting Text from Images Using PyTesseract

This project demonstrates how to extract text from images using PyTesseract, a Python wrapper for Google's Tesseract-OCR Engine.

## 📂 Project Overview

The main goal of this project is to use PyTesseract to recognize and extract text from images and process the output. It's ideal for applications like scanning documents, extracting information from images, or processing images for text-based analysis.

## 🛠 Installation

To run this project, you need to install the necessary dependencies.

### Prerequisites

- Python 3.x
- Tesseract-OCR

### Installing Tesseract-OCR

Follow the instructions to install Tesseract on your machine:

- **Windows**: Download the installer from [here](https://github.com/UB-Mannheim/tesseract/wiki) and follow the installation instructions.
- **macOS**: Install using Homebrew:
  ```bash
  brew install tesseract

## 📸 How to Use

Prepare an Image: Ensure you have an image file containing text that you want to extract.

Run the Script: Execute the script extract_text.py to extract text from the image:
python extract_text.py --image_path path_to_your_image
View the Output: The extracted text will be printed to the console and saved in a text file (output.txt).

## 📝 Example Output

Extracted Text:
This is an example text extracted from the image.

## 🔧 Project Structure

├── extract_text.py        # Python script to extract text from images
├── requirements.txt       # List of Python dependencies
├── output.txt             # File containing extracted text (generated after running the script)
└── README.md              # Project documentation

