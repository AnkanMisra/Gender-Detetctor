# Gender Detection Using Deep Learning

## Overview

This repository offers an advanced and comprehensive solution for gender detection, harnessing cutting-edge deep learning methodologies. Developed in Python, the application integrates powerful libraries including DeepFace, TensorFlow, and OpenCV to deliver highly accurate gender predictions from multiple sources, such as static images, pre-recorded videos, and live webcam streams. Designed for versatility, it also features a fully-functional Flask API, enabling seamless integration into web applications and broader deployment scenarios. This robust framework ensures that the application is not only accurate but also easily adaptable to various use cases, making it an ideal tool for developers, researchers, and professionals seeking to implement sophisticated gender detection capabilities within their projects.

## Table of Contents
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [How to Use](#how-to-use)
  - [Image Analysis](#image-analysis)
  - [Webcam Analysis](#webcam-analysis)
  - [Video Analysis](#video-analysis)
  - [Flask API](#flask-api)
  - [Model Accuracy Evaluation](#model-accuracy-evaluation)
- [Project Structure](#project-structure)
- [Detailed Explanation of Scripts](#detailed-explanation-of-scripts)
  - [image.py](#imagepy)
  - [app.py](#apppy)
  - [accuracy.py](#accuracypy)
  - [actual_genders.csv](#actual_genderscsv)
- [Data Handling](#data-handling)
- [Visualization and Analysis](#visualization-and-analysis)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)
- [Acknowledgments](#acknowledgments)


## Features

- **Multi-Source Gender Detection:** 
  - Analyze gender from various sources, including static images, pre-recorded video files, and live webcam streams.
  - Supports batch processing of images stored in a directory.

- **Advanced Deep Learning Models:** 
  - Utilizes the DeepFace library built on top of TensorFlow, offering state-of-the-art accuracy in gender classification.
  - Capable of enforcing detection to ensure faces are correctly identified before classification.

- **Flexible Input Methods:** 
  - Manually input the actual gender for each image during analysis or predefine them in a CSV file for automatic comparison.

- **Flask API:** 
  - Deploy the gender detection model as a RESTful API, enabling integration with web applications, mobile apps, or other services.
  - Supports multiple endpoints for analyzing single images or videos.

- **Performance Evaluation:** 
  - Includes a comprehensive accuracy evaluation script that calculates key metrics such as accuracy, precision, recall, and F1-score.
  - Generates confusion matrices and classification reports to help understand model performance in detail.

- **Data Handling and Storage:** 
  - Automatically logs analysis results in a CSV file, including predicted gender, actual gender, probability scores, and timestamps.
  - Stores visual representations of model accuracy and confusion matrices for easy reference and reporting.

![model_accuracy](https://github.com/user-attachments/assets/0a3fa413-8222-4f6a-930f-99d39574e2ab)
![confusion_matrix](https://github.com/user-attachments/assets/123df021-9431-4e9c-b379-fc3d72532c27)


## System Requirements

Before you begin, ensure your system meets the following requirements:

- **Operating System:** 
  - Linux, macOS, or Windows
- **Python Version:** 
  - Python 3.7 or higher
- **Required Python Packages:** 
  - TensorFlow 2.17.0
  - OpenCV 4.10.0
  - DeepFace 0.0.93
  - Flask 1.1.2
  - Pandas
  - Matplotlib
  - Scikit-learn

- **Hardware Requirements:**
  - **CPU:** 
    - Modern multi-core processor for efficient computation.
  - **Memory:**
    - Minimum 8 GB of RAM (16 GB recommended for large datasets).
  - **GPU:**
    - Optional, but recommended for faster TensorFlow computations, especially with large datasets or real-time video analysis.

- **Software Dependencies:**
  - Ensure all required Python packages are installed via the `req.txt` file provided in this repository.

To install all dependencies, please refer to the [Installation](#installation) section.

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
# How to Use
#### Images Analysis
1. Prepapre the Images:
- Place the images you want to analyze in the images folder
2. Run the Image Analysis Scripts:
```bash
python3 image.py
```
3. Input the Actual Gender
- You will be prompted to enter the actual gender (either “Man” or “Woman”) for each image if it’s not predefined in the ```actual_genders.csv``` file.
4. Review results
- The results of the analysis, including the predicted and actual genders, probability scores, and timestamps, are stored in ```Data/gender_analysis.csv```

#### Web Cam Analysis
1. **Run the application**
```bash
python3 main.py
```
2. **Choose the 1nd Option**
- 2: Analyze live video from the webcam with a custom duration.
- 3: Analyze a video from the video folder.

3. **Set Duration** :
- You can set the duration of the live analysis in seconds.
- The script will use the webcam to detect gender in real-time and store the results in the CSV file.

#### Video analysis
1. **Prepapre Video Files** :
- Place your video files in the video folder.
2. Run the Video Analysis Scripts: 
```bash
python3 main.py
```
2. **Choose the 2nd Option**
- 2: Analyze live video from the webcam with a custom duration.
- 3: Analyze a video from the video folder.
3. Review results
- The script will analyze the video and store gender predictions for each frame in ```Data/gender_analysis.csv```



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

3. **Review Performance Metrics** :
- The script calculates accuracy, precision, recall, and generates a confusion matrix.
- Visual representations are saved in the Conclusion folder.



## Project Structure

The project is organized into the following directories and files:

```bash
Gender-Detector/
│
├── Data/
│   ├── actual_genders.csv         # CSV file storing actual gender for each image
│   ├── gender_analysis.csv        # CSV file storing analysis results
│   └── (Other data files as needed)
│
├── Conclusion/
│   ├── confusion_matrix.png       # Confusion matrix graph saved as an image
│   ├── model_accuracy.png         # Accuracy bar chart saved as an image
│   └── (Other visualizations as needed)
│
├── Images/
│   ├── photo1.jpeg                # Example image files for gender analysis
│   ├── photo2.jpeg
│   └── (Other image files)
│
├── Video/
│   ├── sample_video.mp4           # Example video files for gender analysis
│   └── (Other video files)
│
├── env/                           # Virtual environment directory (not included in the repository)
│   └── (Virtual environment files)
│
├── temp/                          # Temporary folder for Flask API file uploads
│   └── (Files uploaded via the Flask API)
│
├── .gitignore                     # Specifies files and directories to be ignored by Git
├── accuracy.py                    # Script to calculate and visualize model accuracy
├── app.py                         # Flask API script for gender detection
├── image.py                       # Script for analyzing images in the 'Images' folder
├── main.py                        # Script for live video and video file analysis
├── README.md                      # Project README file
├── req.txt                        # Python package dependencies
└── (Other project files as needed)
```

## Detailed Explanation of Scripts

1. **image.py**
   
   This script is responsible for analyzing gender in static images. It reads images from the `images` folder, predicts gender using the DeepFace library, and allows you to either input the actual gender manually or use predefined values from the `actual_genders.csv` file. Results are saved to `Data/gender_analysis.csv`.

2. **app.py**
   
   The Flask API script provides a RESTful interface to the gender detection model. It supports endpoints for analyzing individual images or videos, making it easy to integrate the model into web or mobile applications. The API is designed to be scalable and secure, with support for CORS.

3. **accuracy.py**
   
   This script evaluates the performance of the gender detection model. It calculates accuracy, generates confusion matrices, and produces classification reports. The results are visualized and saved in the `Conclusion` folder, providing valuable insights into the model’s strengths and weaknesses.

4. **actual_genders.csv**
   
   This CSV file stores the actual genders of images in the `images` folder. It is used by the `image.py` script to automatically compare predicted and actual genders, streamlining the analysis process and improving accuracy evaluation.

## Data Handling

- **Gender Analysis Data:**  
  - All analysis results are stored in `Data/gender_analysis.csv`, which includes fields for the source image or video, predicted gender, actual gender, probability scores, and timestamps.

- **Actual Genders:**  
  - The `Data/actual_genders.csv` file allows for predefined actual genders, making it easier to evaluate model accuracy without manual input during runtime.

- **Temporary Storage:**  
  - The `temp` folder (created during Flask API runs) is used for temporarily storing uploaded files before analysis. Files are automatically deleted after processing.

## Visualization and Analysis

- **Confusion Matrix:**
  - A graphical representation of the model’s performance, showing the counts of true positive, true negative, false positive, and false negative predictions.

- **Accuracy Plot:**
  - A simple bar chart that visualizes the overall accuracy of the model as a percentage.

- **Classification Report:**
  - A detailed report that provides metrics such as precision, recall, and F1-score for both “Man” and “Woman” classifications.   


## Dependencies
This project relies on several Python packages, including but not limited to:
- **Deepface**: For facial attribute analysis
- **TensorFlow & Keras**: Core deep learning frameworks
- **OpenCV**: For image and video processing
- **Flask**: For the web API
- **MTCNN & RetinaFace**: For face detection and gender prediction.

See ```req.txt``` for the full list of dependencies.

## Troubleshooting

#### Common Issues and Solutions

1. **Dependency Installation Errors:**
   - If you encounter errors during the installation of dependencies, ensure that you are using a compatible version of Python (3.7 or higher). If issues persist, consider upgrading pip using the following command:
     ```bash
     pip install --upgrade pip
     ```
   - Verify that your virtual environment is activated before running the installation command.

2. **Module Not Found Errors:**
   - Ensure all required packages are installed. If a module is not found, try installing it individually using pip:
     ```bash
     pip install <module-name>
     ```

3. **Webcam or Video File Not Opening:**
   - If the webcam or video file does not open, ensure that your system has the necessary permissions to access the camera and that the video file path is correct.
   - Verify that OpenCV is correctly installed and that your webcam is functioning properly.

4. **Errors in Flask API Requests:**
   - If the Flask API is not responding correctly, ensure that the server is running and that the correct endpoint is being accessed.
   - Use tools like Postman to test your API endpoints and verify that the correct file format and data are being sent.

5. **CSV File Not Updating:**
   - If the `gender_analysis.csv` file is not updating, ensure that the script has write permissions for the `Data` folder.
   - Verify that the script is running without errors and that the correct paths are being used.

6. **Incorrect Predictions:**
   - If the model's predictions are consistently incorrect, consider reviewing the quality of the input images or videos. Poor lighting, occlusions, or low resolution can impact the model's performance.
   - Retrain the model or fine-tune its parameters if necessary.

7. **Confusion Matrix and Accuracy Plot Not Generated:**
   - If these visualizations are not being generated, ensure that the `accuracy.py` script is being run after the analysis, and that the `gender_analysis.csv` file contains the required data.
   - Verify that Matplotlib is correctly installed and functioning.

8. **Issues with Actual Gender Input:**
   - If the script fails to match the actual gender, ensure that the `actual_genders.csv` file is correctly formatted and matches the filenames in the `images` folder.
   - Avoid typos and ensure that gender labels ("Man" and "Woman") are consistently used.

## Future Enhancements

1. **Live Streaming Analysis:**
   - Implement live streaming analysis to provide real-time gender detection from online video sources such as YouTube or RTSP streams.

2. **Multi-Gender Classification:**
   - Extend the model to support non-binary and multiple gender classifications, allowing for a more inclusive analysis.

3. **User Interface:**
   - Develop a graphical user interface (GUI) for easier interaction with the model, enabling drag-and-drop functionality for image and video files.

4. **Model Optimization:**
   - Fine-tune the model for faster inference times, particularly in real-time scenarios, by leveraging optimized versions of TensorFlow or exploring lighter-weight models.

5. **Automated Model Retraining:**
   - Implement automated retraining mechanisms to keep the model up-to-date with new data and improve accuracy over time.

6. **Enhanced Error Handling:**
   - Improve error handling to provide more informative feedback to the user, including detailed logs and suggestions for resolving issues.


## Acknowledgments
- **Deepface** : A Python library for face recognition and facial attribute analysis.
- **TensorFlow & Keras** :  Powerful frameworks for deep learning.
- **OpenCV** :  A versatile library for computer vision tasks.

## Contribution
Contributions are welcome! 

If you have any suggestions, bug reports, or feature requests, feel free to open an issue or submit a pull request.





