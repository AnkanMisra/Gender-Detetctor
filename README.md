# Gender Detection Using Deep Learning

## Overview

This repository offers an advanced and comprehensive solution for gender detection, harnessing cutting-edge deep learning methodologies. Developed in Python, the application integrates powerful libraries including DeepFace, TensorFlow, and OpenCV to deliver highly accurate gender predictions from multiple sources, such as static images, pre-recorded videos, and live webcam streams. Designed for versatility, it also features a fully-functional Flask API, enabling seamless integration into web applications and broader deployment scenarios. This robust framework ensures that the application is not only accurate but also easily adaptable to various use cases, making it an ideal tool for developers, researchers, and professionals seeking to implement sophisticated gender detection capabilities within their projects.

## Features
 - **Image Analysis** : Detect gender from images stored in the faces folder.
 - **Live Webcam Analysis** : Perform real-time gender detection using your webcam with a customizable duration.
 - **Video Analysis** : Analyze pre-recorded videos for gender detection.
 - **High Accuracy** : Utilizes state-of-the-art models like MTCNN and RetinaFace for reliable predictions
 - **Flask API** : Integrate gender detection into web applications with ease.
 - **Cross-Platform** : Works on Windows, macOS, and Linux.

 ## Installation
 1. **Clone this Repository**
 ```bash
 git clone https://github.com/AnkanMisra/Gender-Detector.git
cd Gender-Detector
```
2. **Set Up a Virtual Environment (Optional but Recommended)**
```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
3. **Install Dependencies**
Install all necessary packages using the req.txt file:
```bash
pip install -r req.txt
```
## Usage
1. **Run the application**
```bash
python3 main.py
```
2. **Choose an Option**
- 1: Analyze a photo from the faces folder.
- 2: Analyze live video from the webcam with a custom duration.
- 3: Analyze a video from the video folder.

3. **Analyze Images, Videos, or Webcam Feeds**
- For photos, place them in the faces folder.
- For videos, place them in the video folder.
- Follow the on-screen prompts to select the file or set the duration for webcam analysis.

## Flask API
This project includes a **Flask API**, allowing you to integrate gender detection into web applications.

1. **Running Flask**
To start the Flask API:
```bash
export FLASK_APP=app.py
flask run
```
2. **API Endpoints**
- **POST /analyze_photo** : Analyze a photo.
- **POST /analyze_video** : Analyze a video.
- **GET /live_analysis** : Perform live webcam analysis.

## Project Structure
```bash
Gender-Detector/
│
├── faces/                     # Directory containing images for analysis
├── video/                     # Directory containing videos for analysis
├── env/                       # Virtual environment directory (optional)
├── req.txt                    # Requirements file
├── main.py                    # Main script for running the application
├── app.py                     # Flask API script
├── README.md                  # Project documentation
```

## Dependencies
This project relies on several Python packages, including but not limited to:
- **Deepface**: For facial attribute analysis
- **TensorFlow & Keras**: Core deep learning frameworks
- **OpenCV**: For image and video processing
- **Flask**: For the web API
- **MTCNN & RetinaFace**: For face detection and gender prediction.

See ```req.txt``` for the full list of dependencies.

## Acknowledgments
- **Deepface** : A Python library for face recognition and facial attribute analysis.
- **TensorFlow & Keras** :  Powerful frameworks for deep learning.
- **OpenCV** :  A versatile library for computer vision tasks.

## Contribution
Contributions are welcome! 

If you have any suggestions, bug reports, or feature requests, feel free to open an issue or submit a pull request.

