# 🚦 Autonomous Speed Limit Detection and Alert System
This project implements an edge-deployable real-time speed limit detection and alert system using Convolutional Neural Networks (CNN) and a Raspberry Pi Zero 2W. The system processes live video input from a Pi Camera to detect traffic speed limit signs using a trained deep learning model. Detected speed limits are then displayed on an LCD and communicated via an audio buzzer alert.
## 🧠 Key Features
* 📷 Real-time speed limit sign detection using Pi Camera

* 🧠 Image classification with CNN-based deep learning model

* 📺 LCD output to display speed limits

* 🔊 Buzzer alerts driver on detection

* 🧠 Edge deployment on Raspberry Pi Zero 2W

* 📦 Supports .tflite model for TensorFlow Lite (Edge TPU compatible)

## 🧱 Hardware Used
  Component | Description
  :---|:---
Raspberry Pi Zero 2W | Central processing unit
Pi Camera Module | Captures real-time road sign images
LCD 16x2 | Displays detected speed limit
Buzzer | Audio alert when speed sign is detected
GPIO Interface | Controls LCD and buzzer
## 🧠 Model Architecture (CNN)

```
Input: Preprocessed 100×100 grayscale image
          ↓
Conv2D (60 filters, 5x5) + ReLU
          ↓
Conv2D (60 filters, 5x5) + ReLU
          ↓
MaxPooling (2x2)
          ↓
Conv2D (30 filters, 3x3) + ReLU
          ↓
Conv2D (30 filters, 3x3) + ReLU
          ↓
MaxPooling (2x2)
          ↓
Dropout (0.5)
          ↓
Flatten → Dense(500) + ReLU
          ↓
Dropout (0.5)
          ↓
Dense(9) → Softmax
```

## 🧪 Dataset & Training
* 📚 Dataset: Kaggle — speed limit signs (~4,200 images)

* 📐 Preprocessing:

  * Resized to 100x100

  * Grayscale conversion

  * Histogram Equalization for contrast enhancement

* 🔧 Loss Function: Categorical Cross Entropy

* 🔧 Optimizer: Adam

* 🧠 Model Format: Keras ```.h5``` → converted to ```.tflite``` for deployment

## 🧰 Software Stack

Component | Description
:---|:---
Python | Core scripting language
OpenCV | Image processing
TensorFlow/Keras | Model training and .tflite conversion
RPi.GPIO | Interfacing LCD and buzzer
Picamera | Capturing image frames
TFLite Runtime | Inference on Raspberry Pi

## 🚀 Deployment Flow
* Capture image using Pi Camera

* Preprocess and feed image to CNN model (.tflite)

* Predict speed limit class

* Show result on LCD

* Trigger buzzer alert for driver awareness

## 🎯 Results
|Metric | Value|
|:---:|:---:|
|Accuracy | ~94%|
|Precision | ~93%|
|Recall | ~92%|
|F1-Score | ~92.5%|

These are the images illustrating the final working model

<p align="center">
  <img src="https://github.com/user-attachments/assets/907ee393-75e1-490e-a4bf-01fc153460ce" width="22.5%" alt="Image 1"/>
  <img src="https://github.com/user-attachments/assets/d6caaa02-5871-4792-9943-42d7ab809e9c" width="45%" alt="Image 2"/>
</p>

## 📈 Future Improvements
* Real-time video stream processing (vs frame-by-frame)

* Integrate with GPS to dynamically adjust alerts

* Extend dataset to global sign boards

* Voice alert via speaker module
 
* Vehicle speed integration for overspeed warning
