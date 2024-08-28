import cv2
from deepface import DeepFace
import os
import time
import csv
import pandas as pd

def load_actual_genders(filename="Data/actual_genders.csv"):
    # Load the actual genders from the CSV file into a dictionary
    df = pd.read_csv(filename)
    actual_genders = dict(zip(df['Filename'], df['Actual Gender']))
    return actual_genders

def save_to_csv(data, filename="gender_analysis.csv"):
    folder = "Data"
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path = os.path.join(folder, filename)
    file_exists = os.path.isfile(file_path)

    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Source", "Dominant Gender", "Actual Gender", "Woman Probability", "Man Probability", "Timestamp"])
        writer.writerow(data)

def analyze_photo(photo_path, actual_gender):
    img = cv2.imread(photo_path)
    if img is None:
        print(f"Error: Could not open image at {photo_path}")
        return

    try:
        # Analyze gender using DeepFace
        result = DeepFace.analyze(img, actions=("gender",), enforce_detection=False)
        if result:
            gender_probabilities = result[0]['gender']
            dominant_gender = result[0]['dominant_gender']
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

            print(f"Photo Gender Analysis for {photo_path}:")
            print(f"Women: {gender_probabilities['Woman']:.2f}%")
            print(f"Men: {gender_probabilities['Man']:.2f}%")
            print(f"Dominant gender: {dominant_gender}")
            print(f"Actual gender: {actual_gender}")

            # Save the results to the CSV file
            save_to_csv([photo_path, dominant_gender, actual_gender, gender_probabilities['Woman'], gender_probabilities['Man'], timestamp])

        else:
            print("No face detected in the photo.")

    except Exception as e:
        print(f"Error analyzing photo: {e}")

def analyze_images_in_folder(folder_path, actual_genders):
    images = os.listdir(folder_path)
    if not images:
        print(f"No images found in the '{folder_path}' folder.")
        return

    for image in images:
        image_path = os.path.join(folder_path, image)
        actual_gender = actual_genders.get(image, "Unknown")
        if actual_gender == "Unknown":
            print(f"Actual gender for {image} not found. Skipping.")
            continue
        analyze_photo(image_path, actual_gender)

def main():
    actual_genders = load_actual_genders("Data/actual_genders.csv")
    folder_path = "images"
    analyze_images_in_folder(folder_path, actual_genders)

if __name__ == "__main__":
    main()