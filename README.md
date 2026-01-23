# 🚦 AI-Based Traffic Management System

An **AI-powered smart traffic control system** that analyzes traffic density from multiple road videos and intelligently optimizes traffic light timings using **YOLO-based vehicle detection** and a **Genetic Algorithm**.

This project is designed so that **even someone with zero Python background** can run it by following this README step by step.

---

## 📌 Table of Contents
- [🎯 Project Overview](#-project-overview)
- [🧠 How This System Works (Big Picture)](#-how-this-system-works-big-picture)
- [📦 Project Structure](#-project-structure)
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
- NumPy → math operations  
- Pandas → data handling  
- OpenCV → video processing  
- Flask → backend server  
- Flask-CORS → frontend ↔ backend communication  

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
- Modern web browser (Chrome, Firefox, Safari, Edge)

### 🎯 Easiest Way to Start (Recommended)

#### Windows Users
```bash
start_project.bat
```

#### Linux / Mac Users
```bash
chmod +x start_project.sh
./start_project.sh
```

---

## 🔧 Manual Setup

### 1. Backend Setup
```bash
cd backend
pip install -r requirements.txt
python app.py
```

The backend will start on  
`http://localhost:5000`

### 2. Frontend Setup

#### Option A: Using Python's built-in server (Recommended)
```bash
cd frontend
python -m http.server 8000
```

Open in browser:  
`http://localhost:8000`

#### Option B: Direct file opening
Double-click `frontend/index.html`

#### Option C: Using Live Server (VS Code)
1. Install **Live Server**
2. Right-click `frontend/index.html`
3. Open with Live Server

---

### 3. Test Connection (Optional)

```bash
http://localhost:8000/test_connection.html
```

---

### 4. Usage
1. Open `http://localhost:8000/index.html`
2. Select **exactly 4 videos**
3. Click **Run Model**
4. Wait for processing
5. View optimized timings

---

## 🧩 Backend Explained (Deep Dive)

### 🔹 app.py (START HERE)

This is the main entry point.

Responsibilities:
- Accepts 4 lane videos  
- Calls YOLO to detect vehicles  
- Calls Genetic Algorithm to optimize traffic  
- Returns optimized timings to frontend  

---

## 🧠 YOLO Explained (Vehicle Detection)

📄 File: `yolov4.py`

YOLO does:
- Reads video frame-by-frame  
- Detects vehicles  
- Draws bounding boxes  
- Counts vehicles per frame  
- Computes mean vehicle count  

Why mean?  
→ Reduces noise caused by sudden spikes

---

## 🧬 Traffic Optimization Using Genetic Algorithm

📄 File: `algo.py`

### ❓ Why Genetic Algorithm?
Traffic optimization has millions of permutations.  
Traditional methods fail or are too slow.

GA works because:
- Searches large solution spaces efficiently  
- Gives near-optimal results fast  

📘 Detailed explanation:  
https://chatgpt.com/s/t_697392aa717481919e022ac01ff4a9fd

### 🔄 Genetic Algorithm Flow

**1️⃣ Initialize Population**
- Randomly choose 400 solutions  
- Each solution = one traffic signal configuration  

**2️⃣ Fitness Function**
- Measures average delay  

Total Delay =
- 🔴 Red light delay  
- 🟢 Congestion delay  

Typical delay range:  
**390 – 430 seconds (4 lanes combined)**

**3️⃣ New Generation Creation**
- 25 generations  
- Roulette Wheel Selection  
- Crossover, Mutation, Inversion  

**4️⃣ Selection**
- Merge populations  
- Keep best solutions  
- Return optimized timings  

---

## 🌐 Frontend Explained

📄 File: `script.js`

Flow:
- User uploads 4 videos  
- POST API call  
- Backend processes videos  
- Results returned  
- UI displays optimized timings  

No frameworks.  
Works on any modern browser.

---

## 📸 Output Screenshots

📌 Add your screenshots here

![UI Screenshot](screenshots/ui.png)  
![YOLO Detection](screenshots/yolo_output.png)  
![Results](screenshots/results.png)

---

## 🚨 Troubleshooting

**Backend not starting**
- Check Python 3.7+
- Run `pip install -r requirements.txt`
- Ensure port 5000 is free

**Frontend not connecting**
- Backend must be running
- Check CORS errors

**Upload fails**
- Exactly 4 videos
- MP4 / AVI supported

---

## 🧪 Testing

Backend: Postman  
Frontend: Browser DevTools  

---

## 🛠 Customization & Extension

- Change detection → `yolov4.py`
- Modify optimization → `algo.py`
- UI features → `script.js`

---

## 🤝 Contributing

- Fork the repo  
- Create feature branch  
- Commit changes  
- Submit pull request  
