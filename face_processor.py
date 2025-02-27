import sys
import mediapipe as mp
import cv2
import numpy as np
import base64
import io
import json
from PIL import Image
import tensorflow as tf
import os

# Suppress TensorFlow warnings and logs completely by setting environment variables
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppresses TensorFlow logs
# Optionally, redirect TensorFlow logs to a file instead of stderr:
# os.environ['TF_LOG_DIR'] = 'tensorflow_logs'

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.2)

def generate_fingerprint(image_data):
    # Convert byte data to an image
    image = Image.open(io.BytesIO(image_data))
    image = np.array(image.convert('RGB'))
    
    # Process image with MediaPipe
    results = face_detection.process(image)
    
    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = image.shape
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
            face_image = image[y:y+h, x:x+w]  # Crop the face

            # Flatten image as a simple embedding
            fingerprint = np.array(face_image).flatten().tolist()
            return fingerprint
    return None

if __name__ == "__main__":
    try:
        # Read input JSON from Node.js
        input_data = json.loads(sys.stdin.read())
        image_data = base64.b64decode(input_data['image'].split(',')[1])
        
        # Generate fingerprint
        fingerprint = generate_fingerprint(image_data)

        # Output fingerprint as JSON
        if fingerprint:
            print(json.dumps({"success": True, "face_embedding": fingerprint}))
        else:
            print(json.dumps({"success": False, "error": "No face detected"}))
    except Exception as e:
        print(json.dumps({"success": False, "error": str(e)}))
