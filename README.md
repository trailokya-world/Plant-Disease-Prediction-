# 🌿 Plant Disease Prediction Using Deep Learning (CNN)

A Deep Learning-based image classification system that detects and classifies plant leaf diseases using a Convolutional Neural Network (CNN). The application provides real-time disease prediction through an interactive Streamlit web interface, helping identify plant diseases quickly and accurately from leaf images.

---

## 🚀 Features

- 🌱 Upload plant leaf images for disease detection.
- 🤖 Deep Learning model built using Convolutional Neural Networks (CNN).
- 📷 Automatic image preprocessing and normalization.
- 📊 Real-time disease prediction with confidence scores.
- 🎨 User-friendly Streamlit web interface.
- ⚡ Fast and accurate image classification.
- 🔄 Supports multiple plant disease classes.

---

## 🏗️ System Architecture

```
Leaf Image
     │
     ▼
Image Upload (Streamlit)
     │
     ▼
Image Preprocessing
(Resize → Normalize)
     │
     ▼
CNN Model
     │
     ▼
Softmax Classification
     │
     ▼
Predicted Disease
```

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Deep Learning
- TensorFlow
- Keras

### Frontend
- Streamlit

### Image Processing
- Pillow (PIL)
- NumPy

### Computer Vision
- Convolutional Neural Networks (CNN)

---

## 🧠 Model Architecture

The model consists of multiple CNN blocks designed to extract hierarchical image features for accurate disease classification.

### Architecture

- Image Rescaling Layer
- Data Augmentation
- 4 Convolutional Blocks
    - Conv2D
    - Batch Normalization
    - ReLU Activation
    - MaxPooling
    - Dropout
- Global Average Pooling
- Fully Connected Layers
- Softmax Output Layer

---

## ⚙️ Workflow

1. Upload a plant leaf image.
2. Resize and normalize the image.
3. Perform feature extraction using CNN layers.
4. Classify the disease using the trained model.
5. Display the predicted disease with confidence.

---

## 📊 Training Details

- Framework: TensorFlow / Keras
- Image Size: **200 × 200**
- Optimizer: Adam
- Loss Function: Sparse Categorical Crossentropy
- Output Activation: Softmax
- Epochs: **20**
- Regularization:
  - Batch Normalization
  - Dropout
- Data Augmentation:
  - Random transformations for better generalization

---

## 💡 Key Features

- Deep CNN architecture for image classification.
- Batch Normalization for stable training.
- Dropout layers to reduce overfitting.
- Global Average Pooling for improved generalization.
- Interactive Streamlit application.
- Modular and reusable code structure.

---

## 📁 Project Structure

```
project/
│
├── app.py                 # Streamlit application
├── train.py               # Model training
├── model.keras            # Trained CNN model
├── dataset/
├── images/
├── utils.py
├── requirements.txt
└── README.md
```

---

## 📈 Future Improvements

- Transfer Learning (EfficientNet, ResNet50)
- MobileNet deployment for edge devices
- Disease severity estimation
- Treatment recommendation system
- Multi-language support
- Cloud deployment
- Mobile application

---

## 📚 Technologies Used

- Python
- TensorFlow
- Keras
- Streamlit
- NumPy
- Pillow (PIL)

---

## 🎯 Learning Outcomes

This project helped me gain practical experience in:

- Building Convolutional Neural Networks (CNNs)
- Image Classification using Deep Learning
- Data Augmentation techniques
- Model regularization using Batch Normalization and Dropout
- TensorFlow & Keras model development
- Image preprocessing and normalization
- Developing AI-powered web applications using Streamlit

---

## Screenshots
![Plant Disease Prediction](/screenshots/image.png)

## 👨‍💻 Author

**Trailokya Dhotre**

- GitHub: https://github.com/trailokya-world
- LinkedIn: *(Add your LinkedIn profile)*