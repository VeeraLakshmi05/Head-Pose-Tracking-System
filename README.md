# Head Pose Tracking System

## Overview

The Head Pose Tracking System is a real-time computer vision application that monitors user attention by detecting head movements and identifying whether a user is looking away from the screen.

The system uses a webcam feed and MediaPipe Face Mesh to detect facial landmarks. These landmarks are processed using OpenCV to estimate head orientation and calculate yaw, pitch, and roll angles. Based on predefined angle and time thresholds, the system determines whether the user is attentive or looking away.

This project can be applied in online examination proctoring, remote interviews, attention monitoring, and human behavior analysis.

---

## Objectives

- Detect suspicious head movements.
- Estimate head pose using yaw, pitch, and roll.
- Identify looking-away behavior.
- Track head deviation over time.
- Generate session statistics.

---

## Features

- Real-time webcam-based tracking.
- Facial landmark detection using MediaPipe Face Mesh.
- Head pose estimation using OpenCV solvePnP().
- Yaw, pitch, and roll angle calculation.
- Threshold-based attention monitoring.
- Duration-based detection to reduce false positives.
- Real-time ATTENTIVE and LOOKING AWAY status.
- Session statistics:
  - Total look-away events.
  - Maximum deviation angle.
  - Longest look-away duration.
  - Away time tracking.

---

## Technologies Used

### Programming Language

- Python

### Libraries

- OpenCV
- MediaPipe Face Mesh
- NumPy

### Tools

- Visual Studio Code
- Git & GitHub
- Python Virtual Environment (venv)

---

## System Workflow

```
Webcam Input
      ↓
Face Landmark Detection
      ↓
Facial Landmark Selection
      ↓
Head Pose Estimation
      ↓
Yaw, Pitch, Roll Calculation
      ↓
Threshold-Based Attention Logic
      ↓
Looking Away Detection
      ↓
Session Statistics Generation
```

---

## Project Structure

```
Head-Pose-Tracking-System/
│
├── main.py
│   └── Main application execution
│
├── pose_estimation.py
│   └── Face landmark detection and pose estimation
│
├── attention_logic.py
│   └── Attention checking and statistics tracking
│
├── test_cases.py
│   └── Test scenarios
│
├── requirements.txt
│   └── Python dependencies
│
└── screenshots/
    ├── attentive.png
    ├── looking_away.png
    └── session_report.png
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Head-Pose-Tracking-System.git
```

### Navigate to Project

```bash
cd Head-Pose-Tracking-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment (Windows)

```powershell
.\venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run:

```bash
python main.py
```

The system displays:

- Yaw angle
- Pitch angle
- Roll angle
- ATTENTIVE / LOOKING AWAY status
- Away time

Press `ESC` to exit the application and view the final session statistics.

---

## Test Cases

| Test Scenario | Expected Result |
|--------------|----------------|
| Looking straight | ATTENTIVE |
| Looking left | LOOKING AWAY |
| Looking right | LOOKING AWAY |
| Looking up/down | LOOKING AWAY |
| Short natural movement | ATTENTIVE |
| Return to center | ATTENTIVE |

---

## Sample Output

### JSON Output

```json
{
  "looking_away": true,
  "angle": 35.2,
  "away_time": 3.4
}
```

### Session Report

```
========== SESSION REPORT ==========

Total Look Away Events : 4
Maximum Angle Reached : 37.82 degrees
Longest Away Duration : 6.43 seconds

====================================
```

---

## Challenges Faced

- MediaPipe compatibility issues with Python versions.
- Threshold tuning for accurate detection.
- Avoiding false detection due to normal movements.
- Handling different lighting and camera positions.

---

## Future Enhancements

- Eye gaze tracking.
- Multi-person head pose tracking.
- Deep learning-based attention analysis.
- Real-time alerts.
- Dashboard monitoring.
- Cloud-based storage and analysis.

---

## References

Python Documentation:
https://docs.python.org/3/

OpenCV Documentation:
https://docs.opencv.org/

MediaPipe Documentation:
https://developers.google.com/mediapipe

MediaPipe Face Mesh:
https://developers.google.com/mediapipe/solutions/vision/face_mesh

NumPy Documentation:
https://numpy.org/doc/

---

## Author

Name: Veera Lakshmi Malladi
Project: Head Pose Tracking System
