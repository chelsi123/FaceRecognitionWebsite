# Real-Time Face Recognition Attendance System

## Overview
Developed a **real-time biometric attendance system** as part of Microsoft Engage 2022. The system automates student identification and attendance logging using **face recognition**, improving accuracy and speed compared to manual methods.

---

## Key Features
- **Real-Time Face Detection & Recognition:** Uses OpenCV and LBPH (Local Binary Pattern Histogram) for robust identification.  
- **Data Management:** Integrated with **MySQL** to securely store and manage student records (ID, Name, Gender).  
- **GUI Front-End:** Built using **Tkinter** for easy interaction and attendance tracking.  
- **Optimized Training Pipeline:** Utilized Haar Cascade for initial face detection, generating a standardized dataset (100 images per student) for model training.  
- **High Accuracy & Speed:** Automated attendance reduces manual effort and ensures data integrity.  

---

## Tech Stack
- **Programming Language:** Python  
- **Libraries & Tools:** OpenCV, Tkinter, MySQL, Haar Cascade, LBPH Classifier  

---

## How It Works
1. Student stands in front of the camera.  
2. Haar Cascade detects the face in real-time.  
3. LBPH classifier recognizes the student using the pre-trained dataset.  
4. Attendance is logged automatically in the MySQL database with timestamp.  
5. GUI displays student information and attendance status.  

---

## Key Skills Demonstrated
- Real-time computer vision and facial recognition  
- GUI development with Tkinter  
- Database integration and management using MySQL  
- Data preprocessing and model training for face recognition  
- Automation and optimization of ML pipelines  

---

## Impact
- Fully automated attendance system reduces human error.  
- Scalable to manage large student datasets securely.  
- Demonstrates integration of ML, database management, and GUI development.  

---

## How to Run
1. Clone the repository:  
```bash
git clone https://github.com/yourusername/Face_Recognition_Attendance.git
2. pip install opencv-python mysql-connector-python
3. python main.py
