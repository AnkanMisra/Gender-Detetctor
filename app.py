from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
from deepface import DeepFace
import os

app = Flask(__name__)
CORS(app)

def analyze_gender(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return {"error": "Could not open image"}
    
    try:
        result = DeepFace.analyze(img, actions=("gender",), enforce_detection=False)
        if result:
            gender_probabilities = result[0]['gender']
            dominant_gender = result[0]['dominant_gender']
            return {
                "dominant_gender": dominant_gender,
                "gender_probabilities": gender_probabilities
            }
        else:
            return {"error": "No face detected in the image"}
    except Exception as e:
        return {"error": str(e)}

@app.route('/analyze_photo', methods=['POST'])
def analyze_photo():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    file_path = os.path.join("temp", file.filename)
    file.save(file_path)
    
    result = analyze_gender(file_path)
    os.remove(file_path)
    
    return jsonify(result)

@app.route('/analyze_video', methods=['POST'])
def analyze_video():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    file_path = os.path.join("temp", file.filename)
    file.save(file_path)
    
    result = {"message": "Video analysis is not yet implemented."}
    
    os.remove(file_path)
    
    return jsonify(result)

@app.route('/live_analysis', methods=['GET'])
def live_analysis():
    return jsonify({"message": "Live analysis is not yet implemented."})

if __name__ == '__main__':
    if not os.path.exists('temp'):
        os.makedirs('temp')
    app.run(debug=True)