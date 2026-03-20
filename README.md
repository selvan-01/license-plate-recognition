# 🚗 License Plate Recognition using OpenCV & Tesseract (Real-Time)

A real-time License Plate Recognition system built using **Python, OpenCV, and Tesseract OCR**. This project detects vehicle number plates from images or webcam feed and extracts the text automatically.

---

## 🔥 Features

* 🎥 Real-time license plate detection using webcam
* 🖼️ Image-based license plate recognition
* 🔍 Contour-based plate detection
* 🔤 OCR text extraction using Tesseract
* 🖍️ Bounding box and live text overlay
* ⚡ Fast and lightweight implementation

---

## 🛠️ Tech Stack

* Python 🐍
* OpenCV 👁️
* Tesseract OCR 🔤
* NumPy

---

## 📁 Project Structure

```
license-plate-recognition/
│
├── data/
│   └── raw/
│       ├── car1.jpg
│       ├── car2.jpg
│
├── main.py
├── requirements.txt
├── README.md

```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/selvan-01/license-plate-recognition.git
cd license-plate-recognition
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Install Tesseract OCR

Download and install from:
https://github.com/tesseract-ocr/tesseract

After installation, update the path in code:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
```

---

## ▶️ Usage

Run the project:

```bash
python main.py
```

* Press **'q'** to exit webcam
* The system will detect and display license plate text in real-time

---

## 🧠 How It Works

1. Convert image to grayscale
2. Apply edge detection (Canny)
3. Find contours and detect rectangular shapes
4. Extract region of interest (license plate)
5. Apply thresholding and noise removal
6. Use Tesseract OCR to extract text
7. Display results with bounding box

---

## 🚀 Future Improvements

* 🔥 Deep Learning (YOLOv8) for better detection
* 📊 Save detected plates to database
* 🌐 Deploy as web application
* 📱 Mobile app integration
* 🎯 Improve OCR accuracy with preprocessing

---

## 🤝 Contributing

Feel free to fork this repository and contribute!

---

## 📬 Contact

👤 Senthamil Selvan
📧 [senthamils445@gmail.com](mailto:senthamils445@gmail.com)

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
