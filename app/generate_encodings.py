# app/generate_encodings.py

import os
import cv2
import face_recognition
import pickle

DATASET_DIR = "../dataset"
ENCODING_FILE = "../encodings/face_encodings.pkl"

def encode_faces():
    known_encodings = []
    known_names = []

    print("[INFO] Starting encoding process...")

    # Loop over each person’s folder
    for person_name in os.listdir(DATASET_DIR):
        person_path = os.path.join(DATASET_DIR, person_name)

        if not os.path.isdir(person_path):
            continue

        print(f"[INFO] Processing {person_name}")

        # Loop over each image for this person
        for img_name in os.listdir(person_path):
            img_path = os.path.join(person_path, img_name)

            # Load image and convert to RGB
            image = cv2.imread(img_path)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Detect faces
            boxes = face_recognition.face_locations(rgb, model='hog')

            # Encode faces
            encodings = face_recognition.face_encodings(rgb, boxes)

            for encoding in encodings:
                known_encodings.append(encoding)
                known_names.append(person_name)

    print(f"[INFO] Total encodings: {len(known_encodings)}")

    # Save encodings to file
    data = {"encodings": known_encodings, "names": known_names}
    os.makedirs(os.path.dirname(ENCODING_FILE), exist_ok=True)

    with open(ENCODING_FILE, "wb") as f:
        pickle.dump(data, f)

    print(f"[INFO] Encodings saved to {ENCODING_FILE}")

if __name__ == "__main__":
    encode_faces()
