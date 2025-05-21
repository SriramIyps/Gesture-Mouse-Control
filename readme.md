# Gesture Controlled Mouse Using OpenCV & MediaPipe

## What I’ve Done

Control your PC mouse using **hand gestures**!
Move cursor with **Right Index Finger**
Click and drag with **Left Hand gestures**

---

## Features

*    Cursor moves with **Right Index Finger**
*    Right Click → **Left Index + Thumb tap**
*    Left Click → **Left Middle + Thumb tap**
*    Drag → **Hold Left Index + Thumb**
*    On-screen gesture status: “Dragging”, “Right Click”, etc.

---

## Libraries Used
pip install opencv-python mediapipe pyautogui numpy

---

##  Installation Guide

1. Make sure you're using **Python 3.10 or 3.11**

2. Install required libraries:

   `in terminal
   pip install opencv-python mediapipe pyautogui numpy


3. Run the project:

   `in terminal
   python gesture_mouse_control.py
   

## 📱 check camera before running
       attached **camtest.py** make it use of it to check your camera
   just copy and paste the code in a new file at your environment
   
---

## 🐞 Common Errors & Fixes

|  Error                      | Solution                                             |
| --------------------------- | ---------------------------------------------------- |
| `No module named cv2`       | Install OpenCV: `pip install opencv-python`          |
| `No module named mediapipe` | Use Python 3.10 or 3.11 and install: `pip install mediapipe` |
| Webcam not showing          | Try changing camera index: `cv2.VideoCapture(1)`     |
| Drag not smooth             | Hold gesture longer, check finger distance           |

---

## Created By

**Sriram iyyappan**
PSGCAS | Always Building Cool Stuff 😎

---
