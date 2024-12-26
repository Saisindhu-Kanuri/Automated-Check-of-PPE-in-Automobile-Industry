# PPE Kit Detection

This project focuses on detecting Personal Protective Equipment (PPE) in images or videos using computer vision techniques. It is designed to ensure compliance with safety standards in workplaces by identifying whether individuals are wearing the necessary protective gear.

## Features

1. Detects common PPE items like helmets, gloves, safety vests, goggles, and masks.
2. Supports real-time detection on video streams.
3. Outputs results with bounding boxes and labels for detected PPE items.
4. Includes visualization and logging capabilities.

## Installation

### Requirements

Ensure you have the necessary dependencies installed. A `requirements.txt` file is included for easy setup.

```bash
pip install -r requirements.txt
```

### Additional Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ppe-kit-detection.git
   cd ppe-kit-detection
   ```
2. Download the pre-trained model weights (if applicable) and place them in the `models` directory.

## Usage

1. **Video Detection:**
   
   Update the `cap` variable in the `detect.py` script as follows to use a specific video:
   ```python
   cap = cv2.VideoCapture("../Videos/ppe-2.mp4")  # For Video
   ```

2. **Real-time Detection:**
   
   Uncomment and use the following lines in the `detect.py` script for webcam input:
   ```python
   # cap = cv2.VideoCapture(0)  # For Webcam
   # cap.set(3, 1280)
   # cap.set(4, 720)


### Output

- Detected items will be displayed with bounding boxes and labels.
- Results can be saved in the `output` directory.
  
