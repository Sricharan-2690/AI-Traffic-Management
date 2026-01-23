# 🚦 AI-Based Traffic Management System

An **AI-powered smart traffic control system** that analyzes traffic density from multiple road videos and intelligently optimizes traffic light timings using **YOLO-based vehicle detection** and a **Genetic Algorithm**.

This project is designed so that **even someone with zero Python background** can run it by following this README step by step.

---

## 📌 Table of Contents
- [🎯 Project Overview](#-project-overview)
- [🧠 How This System Works (Big Picture)](#-how-this-system-works-big-picture)
- [📁 Project Structure](#-project-structure)
- [🛠 Prerequisites (Explained Intuitively)](#-prerequisites-explained-intuitively)
- [⚙️ Technologies Used](#️-technologies-used)
- [🚀 Quick Start (Recommended)](#-quick-start)
- [🔧 Manual Setup (Step-by-Step)](#-manual-setup)
- [🧩 Backend Explained (Deep Dive)](#-backend-explained-deep-dive)
- [🧠 YOLO Explained (Vehicle Detection)](#-yolo-explained-vehicle-detection)
- [🧬 Traffic Optimization Using Genetic Algorithm](#-traffic-optimization-using-genetic-algorithm)
- [🌐 Frontend Explained](#-frontend-explained)
- [📸 Output Screenshots](#-output-screenshots)
- [🚨 Troubleshooting](#-troubleshooting)
- [🧪 Testing](#-testing)
- [🛠 Customization & Extension](#-customization--extension)
- [🤝 Contributing](#-contributing)

---

## 🎯 Project Overview

Traditional traffic lights follow **fixed timing**, which causes:
- long waiting times
- congestion
- inefficient traffic flow

### ✅ What this project does
- Takes **4 traffic videos** (4 lanes of an intersection)
- Detects **number of vehicles using AI**
- Calculates **traffic density**
- Optimizes **green light duration** for each lane
- Reduces **average waiting time**

---

## 🧠 How This System Works (Big Picture)

Traffic Videos (4 lanes)  
↓  
YOLO Vehicle Detection  
↓  
Traffic Density Calculation  
↓  
Genetic Algorithm Optimization  
↓  
Optimized Traffic Light Timings  
↓  
Results shown on Web UI  

---

## 📁 Project Structure

```
AI-Based-Traffic-Management-SIH-main/
├── backend/
│   ├── app.py              # Flask server
│   ├── algo.py             # Traffic optimization algorithm
│   ├── yolov4.py           # YOLO object detection
│   ├── yolov4_Recording.py # Video processing utilities
│   ├── requirements.txt    # Python dependencies 
│   ├── yolov4-tiny.cfg     # YOLO configuration
│   ├── yolov4-tiny.weights # YOLO model weights
│   └── classes.txt         # Object classes
├── frontend/
│   ├── index.html          # Main HTML file
│   ├── styles.css          # CSS styles
│   ├── script.js           # JavaScript functionality
│   └── README-VANILLA.md   # Frontend documentation
└── README.md               # This file
```

---

## 🛠 Prerequisites (Explained Intuitively)

### 🔹 Programming & Concepts
You **do NOT need to be an expert**, but knowing these helps:

- **Python** → main programming language
- **Basic Machine Learning concepts**
- **Neural Networks (CNN)** → YOLO uses CNN
- **YOLO Algorithm** → detects vehicles in video

### 🔹 Python Libraries (What they do)
- `NumPy` → math operations
- `Pandas` → data handling
- `OpenCV` → video processing
- `Flask` → backend server
- `Flask-CORS` → frontend ↔ backend communication

### 🔹 Frontend Basics
- HTML → structure
- CSS → styling
- JavaScript → user interaction & API calls

---

## ⚙️ Technologies Used

### Backend
- **Flask** – Web framework
- **OpenCV** – Computer vision
- **YOLOv4-Tiny** – Vehicle detection
- **NumPy / SciPy** – Computation
- **Genetic Algorithm** – Optimization

### Frontend
- **HTML5**
- **CSS3**
- **Vanilla JavaScript**
- **Fetch API**

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Modern web browser

### 🎯 Easiest Way to Start (Recommended)

#### Windows Users
```
start_project.bat
```

#### Linux / Mac Users
```
chmod +x start_project.sh
./start_project.sh
```

---

## 🔧 Manual Setup

### 1. Backend Setup
```
cd backend
pip install -r requirements.txt
python app.py
```

Backend runs at: `http://localhost:5000`

### 2. Frontend Setup

#### Option A (Recommended)
```
cd frontend
python -m http.server 8000
```
Open: `http://localhost:8000`

#### Option B
Open `frontend/index.html`

#### Option C
Use VS Code Live Server

---

## 🧩 Backend Explained (Deep Dive)

### 🔹 app.py (START HERE)

Accepts 4 lane videos  
Calls YOLO to detect vehicles  
Calls Genetic Algorithm to optimize traffic  
Returns optimized timings to frontend  

---

## 🧠 YOLO Explained (Vehicle Detection)

📄 File: yolov4.py

Reads video frame-by-frame  
Detects vehicles  
Draws bounding boxes  
Counts vehicles per frame  
Computes mean vehicle count  

---

## 🧬 Traffic Optimization Using Genetic Algorithm

📄 File: algo.py

Why Genetic Algorithm?

Traffic optimization has millions of permutations  
Traditional methods fail or are too slow  

Detailed explanation:  
https://chatgpt.com/s/t_697392aa717481919e022ac01ff4a9fd

---

## 🌐 Frontend Explained

📄 File: script.js

User uploads 4 videos  
POST API call  
Backend processes  
Results returned  
Displayed on UI  

---

## 📸 Output Screenshots

![UI Screenshot](screenshots/ui.png)  
![YOLO Detection](screenshots/yolo_output.png)  
![Results](screenshots/results.png)

(Create a screenshots folder and add images)

---

## 🚨 Troubleshooting

Backend not starting  
Frontend not connecting  
Upload fails  

---

## 🧪 Testing

Backend: Postman  
Frontend: Browser DevTools  

---

## 🛠 Customization & Extension

Change detection → yolov4.py  
Modify optimization → algo.py  
UI changes → script.js  

---

## 🤝 Contributing

Fork the repository  
Create a feature branch  
Commit changes  
Submit a pull request  
