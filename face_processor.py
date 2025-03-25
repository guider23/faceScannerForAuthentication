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

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.2)

def generate_fingerprint(image_data):
    image = Image.open(io.BytesIO(image_data))
    image = np.array(image.convert('RGB'))
    
    results = face_detection.process(image)
    
    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = image.shape
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
            face_image = image[y:y+h, x:x+w]

            fingerprint = np.array(face_image).flatten().tolist()
            return fingerprint
    return None

if __name__ == "__main__":
    try:
        input_data = json.loads(sys.stdin.read())
        image_data = base64.b64decode(input_data['image'].split(',')[1])
        
        fingerprint = generate_fingerprint(image_data)

        if fingerprint:
            print(json.dumps({"success": True, "face_embedding": fingerprint}))
        else:
            print(json.dumps({"success": False, "error": "No face detected"}))
    except Exception as e:
        print(json.dumps({"success": False, "error": str(e)}))
