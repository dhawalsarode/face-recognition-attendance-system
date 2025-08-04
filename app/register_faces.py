# app/register_faces.py

import cv2
import os

def capture_images(person_name, save_dir='dataset/', max_images=20):
    # Initialize webcam
    cam = cv2.VideoCapture(0)

    # Create user directory if not exists
    user_path = os.path.join(save_dir, person_name)
    os.makedirs(user_path, exist_ok=True)

    print(f"[INFO] Starting capture for: {person_name}")
    count = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("[ERROR] Failed to grab frame")
            break

        cv2.imshow("Press 'c' to capture, 'q' to quit", frame)

        key = cv2.waitKey(1)
        
        if key % 256 == ord('c'):
            # Save frame
            img_name = f"{person_name}_{count + 1}.jpg"
            cv2.imwrite(os.path.join(user_path, img_name), frame)
            print(f"[INFO] Saved: {img_name}")
            count += 1

            if count >= max_images:
                print("[INFO] Maximum images reached.")
                break

        elif key % 256 == ord('q'):
            print("[INFO] Quitting capture.")
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    name = input("Enter the person's name: ").strip()
    capture_images(name)
