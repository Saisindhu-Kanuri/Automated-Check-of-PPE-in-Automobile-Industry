# 🦺 Automated PPE Compliance Check in the Automobile Industry

This project leverages **computer vision** to automatically detect the presence of **Personal Protective Equipment (PPE)** on individuals in images and video streams. Designed for **automobile industry settings**, it helps ensure compliance with workplace safety standards by identifying essential protective gear.

---

## 🚀 Features

- Detects key PPE items:
  - Helmets  
  - Gloves  
  - Safety vests  
  - Goggles  
  - Masks  
- Supports both **real-time webcam detection** and **pre-recorded video analysis**
- Uses pre-trained deep learning models for accurate detection
- Visualizes detections with bounding boxes and labels
- Logs detection data for further analysis or reporting

---


### 🧠 Tech Stack

- **Python** 
- **OpenCV** 
- **PyTorch** 
- **NumPy** 
- **Deep Learning & Computer Vision** 

---


## 🛠️ Installation

### 🔧 Requirements

Ensure you have Python installed along with the necessary dependencies.

Install all required packages using:

```bash
pip install -r requirements.txt
```

### 📁 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Saisindhu-Kanuri/Automated-Check-of-PPE-in-Automobile-Industry.git
   cd Automated-Check-of-PPE-in-Automobile-Industry
   ```
2. Download the pre-trained model weights (if applicable) and place them in the `models/` directory.

### ▶️ Usage

1. **Video Detection:**
   
   Update the `cap` variable in the `detect.py` script as follows to use a specific video:
   ```python
   cap = cv2.VideoCapture("Videos/ppe-2.mp4")  # Replace with your file path
   ```

2. **Real-time Detection:**
   
   Uncomment and use the following lines in the `detect.py` script for webcam input:
   ```python
   # cap = cv2.VideoCapture(0)  # For Webcam
   # cap.set(3, 1280)
   # cap.set(4, 720)


### 💾 Output

- Detected items will be displayed with bounding boxes and labels.
- Results can be saved in the `output` directory.
