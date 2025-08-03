# 📷 Face Recognition Attendance System

An automated real-time attendance system that uses face recognition via webcam or mobile camera. This project allows students or employees to mark their attendance simply by showing their face — using any available camera device.

---

## 🔍 Key Features

- ✅ Real-time face detection and recognition
- ✅ Works with **any camera**: laptop webcam, external webcam, or phone camera (IP camera stream)
- ✅ Automatically logs attendance to `.csv` with name and timestamp
- ✅ Simple face registration: capture and encode new faces
- ✅ Built with Python and OpenCV

---

## 🧠 How It Works

1. **Face Registration**  
   Users register their faces via webcam → encodings are saved for future recognition

2. **Face Recognition & Matching**  
   Live camera feed is scanned → faces are matched against known encodings

3. **Attendance Logging**  
   Recognized users are marked “Present” with timestamp → logged in `attendance.csv`

---

## 🛠️ Tech Stack & Libraries

- Python
- OpenCV
- `face_recognition` (dlib-based)
- NumPy
- Pandas
- `imutils` (optional for resizing)

---

## 📂 Folder Structure
face-recognition-attendance/
├── app/
│ ├── register_faces.py # Face capture & encoding
│ ├── recognize_faces.py # Live recognition & logging
│ └── utils.py # Helper functions
├── dataset/
│ └── (face images per person)
├── encodings/
│ └── face_encodings.pkl
├── attendance/
│ └── attendance.csv
├── requirements.txt
└── README.md

---

## 🧪 Dataset

- No external dataset required
- Face images are captured in real-time and stored in `dataset/`

---

## ⚙️ Installation & Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/face-recognition-attendance-system
   cd face-recognition-attendance-system

2.Install dependencies:
   ```bash
  pip install -r requirements.txt
   ```

3.Run face registration:
```bash
  python app/register_faces.py
   ```

4.Start recognition and logging:
```bash
  python app/recognize_faces.py
```

## 🧠 Project Use Cases

-Classroom attendance systems
-Office/workplace access logging
-Event check-ins

## ✍️ Author
Dhawal Sarode
B.Tech CSE, Amity University (2021–2025)

## 📌 Acknowledgements
Built based on concepts from Udemy Face Recognition course
Utilizes face_recognition by @ageitgey

