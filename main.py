import cv2
from deepface import DeepFace
import os
import time
import sys
import numpy as np

def analyze_live_video(duration):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    start_time = time.time()

    women_scores = []
    men_scores = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        try:
            result = DeepFace.analyze(frame, actions=("gender",), enforce_detection=False)

            if result:
                gender_probabilities = result[0]['gender']
                women_scores.append(gender_probabilities['Woman'])
                men_scores.append(gender_probabilities['Man'])

                dominant_gender = "Man" if gender_probabilities['Man'] > gender_probabilities['Woman'] else "Woman"
                cv2.putText(frame, f"Dominant Gender: {dominant_gender}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            else:
                print("No face detected in the frame.")

        except Exception as e:
            print(f"Error analyzing frame: {e}")
            continue

        cv2.imshow('Webcam', frame)

        if time.time() - start_time > duration:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    if women_scores and men_scores:
        avg_women_score = np.mean(women_scores)
        avg_men_score = np.mean(men_scores)
        final_dominant_gender = "Man" if avg_men_score > avg_women_score else "Woman"

        print(f"Final Gender Analysis over {duration} seconds:")
        print(f"Average Women: {avg_women_score:.2f}%")
        print(f"Average Men: {avg_men_score:.2f}%")
        print(f"Final Dominant Gender: {final_dominant_gender}")
    else:
        print("No face detected during the analysis.")

    sys.exit()

def analyze_video(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video at {video_path}")
        return

    women_scores = []
    men_scores = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        try:
            result = DeepFace.analyze(frame, actions=("gender",), enforce_detection=False)

            if result:
                gender_probabilities = result[0]['gender']
                women_scores.append(gender_probabilities['Woman'])
                men_scores.append(gender_probabilities['Man'])

                dominant_gender = "Man" if gender_probabilities['Man'] > gender_probabilities['Woman'] else "Woman"
                cv2.putText(frame, f"Dominant Gender: {dominant_gender}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            else:
                print("No face detected in the frame.")

        except Exception as e:
            print(f"Error analyzing frame: {e}")
            continue

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    if women_scores and men_scores:
        avg_women_score = np.mean(women_scores)
        avg_men_score = np.mean(men_scores)
        final_dominant_gender = "Man" if avg_men_score > avg_women_score else "Woman"

        print(f"Final Gender Analysis over the video:")
        print(f"Average Women: {avg_women_score:.2f}%")
        print(f"Average Men: {avg_men_score:.2f}%")
        print(f"Final Dominant Gender: {final_dominant_gender}")
    else:
        print("No face detected during the analysis.")

    sys.exit()

def main():
    print("Choose an option:")
    print("1. Analyze live video from webcam")
    print("2. Analyze a video from the 'video' folder")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        duration = int(input("Enter the duration for webcam analysis in seconds: "))
        analyze_live_video(duration)

    elif choice == "2":
        video_folder = "video"
        videos = os.listdir(video_folder)

        if not videos:
            print(f"No videos found in the '{video_folder}' folder.")
            return

        print("Available videos:")
        for i, video in enumerate(videos):
            print(f"{i+1}. {video}")

        video_choice = int(input("Enter the number of the video to analyze: "))
        if 1 <= video_choice <= len(videos):
            video_path = os.path.join(video_folder, videos[video_choice - 1])
            analyze_video(video_path)
        else:
            print("Invalid choice. Exiting.")

    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
