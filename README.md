# **GunTracker**

A simple real-time weapon detection system using Python and OpenCV. The project utilizes Haar Cascade for detecting guns in live video streams captured through a webcam.

---

## **Features**
- **Real-Time Detection**: Detects guns in a live video feed.
- **Bounding Box Visualization**: Highlights detected guns with a red bounding box.
- **Lightweight Implementation**: Runs efficiently on most systems using OpenCV.

---

## **Getting Started**

### **Prerequisites**
Ensure you have the following installed:
- Python 3.x
- OpenCV
- NumPy
- Webcam (for live detection)

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/Hesara2003/Gun-tracker.git
   cd Gun-tracker
   ```

2. Install required libraries:
   ```bash
   pip install opencv-python numpy
   ```

3. Add the Haar Cascade file (`cascade.xml`) to the project directory.

---

## **Usage**

1. Run the `GunTracker.py` script to start detection:
   ```bash
   python GunTracker.py
   ```

2. Press the `Esc` key to exit the application.

---

## **Code Overview**

### **GunTracker.py**
- Captures live video from your webcam.
- Converts frames to grayscale for processing.
- Detects guns using the Haar Cascade classifier (`cascade.xml`).
- Highlights detected guns with red bounding boxes in the live video feed.

### **Key Code Snippet:**
```python
guns = gun_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in guns:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
```

---

![Leonardo_Phoenix_A_visually_appealing_representation_of_a_weap_0](https://github.com/user-attachments/assets/2f6e81c0-a8bc-4b0f-94a7-746181c02934)


---

## **Project Structure**
```
Gun-tracker/
│
├── cascade.xml          # Haar Cascade file for gun detection
├── GunTracker.py        # Main script for real-time detection
└── README.md            # Project documentation
```

---

## **Limitations**
- Haar Cascade can produce false positives or miss detections in complex environments.
- Performs best in well-lit scenes with clear visibility of the gun.
- Designed specifically for guns; may require modifications for detecting other weapons.

---

## **Future Improvements**
- Replace Haar Cascade with a deep learning model (e.g., YOLO or SSD) for improved accuracy.
- Add support for multiple weapon types (e.g., knives).
- Integrate notifications or logging for detection events.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**
- OpenCV for its comprehensive computer vision library.
- Haar Cascade for object detection capabilities.
- Inspiration from real-world surveillance applications.

---
