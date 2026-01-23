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
- [🚀 Quick Start (Recommended)](#-quick-start-recommended)
- [🔧 Manual Setup (Step-by-Step)](#-manual-setup-step-by-step)
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

## 📦 Project Structure

AI-Based-Traffic-Management-SIH-main/
├── backend/
│ ├── app.py # Flask server (ENTRY POINT)
│ ├── algo.py # Traffic optimization (Genetic Algorithm)
│ ├── yolov4.py # YOLO vehicle detection logic
│ ├── yolov4_Recording.py # Video processing utilities
│ ├── requirements.txt # Python dependencies
│ ├── yolov4-tiny.cfg # YOLO configuration
│ ├── yolov4-tiny.weights # YOLO trained model weights
│ └── classes.txt # Object classes (car, bus, truck)
│
├── frontend/
│ ├── index.html # Main UI
│ ├── styles.css # Styling
│ ├── script.js # API calls & logic
│ └── README-VANILLA.md # Frontend documentation
│
└── README.md # You are reading this file


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

## 🚀 Quick Start (Recommended)

### Windows
```bash
start_project.bat
Linux / macOS
chmod +x start_project.sh
./start_project.sh
This automatically:

installs dependencies

starts backend

runs frontend

🔧 Manual Setup (Step-by-Step)
1️⃣ Backend Setup
cd backend
pip install -r requirements.txt
python app.py
Backend runs at:

http://localhost:5000
2️⃣ Frontend Setup
Option A (Recommended)
cd frontend
python -m http.server 8000
Open:

http://localhost:8000
Option B
Double-click:

frontend/index.html
🧩 Backend Explained (Deep Dive)
🔹 app.py (START HERE)
This is the main entry point.

Responsibilities:

Accepts 4 lane videos

Calls YOLO to detect vehicles

Calls Genetic Algorithm to optimize traffic

Returns optimized timings to frontend

🧠 YOLO Explained (Vehicle Detection)
📄 File: yolov4.py
YOLO does:

Reads video frame-by-frame

Detects vehicles

Draws bounding boxes

Counts vehicles per frame

Computes mean vehicle count across frames

Why mean?
→ reduces noise caused by sudden spikes

🧬 Traffic Optimization Using Genetic Algorithm
📄 File: algo.py

❓ Why Genetic Algorithm?
Traffic optimization has millions of permutations.

Traditional methods fail or are too slow.

GA works because:

It searches large solution spaces efficiently

Gives near-optimal results fast

📘 Detailed explanation here:
👉 https://chatgpt.com/s/t_697392aa717481919e022ac01ff4a9fd

🔄 Genetic Algorithm Flow
1️⃣ Initialize Population
Randomly choose 400 solutions

Each solution = one traffic signal configuration

2️⃣ Fitness Function
Measures average delay

Total Delay =

🔴 Red light delay

🟢 Congestion delay (green but traffic not cleared)

Delay depends on:

Green light effectiveness

Congestion

Red light duration

Typical delay range:

390 – 430 seconds (combined for 4 lanes)
3️⃣ New Generation Creation
Total generations = 25

Roulette Wheel Selection for parents

Apply:

Crossover

Mutation

Inversion (if population size is low)

4️⃣ Selection
Merge old + new population

Keep best solutions (least delay)

Return optimal traffic timings

🌐 Frontend Explained
📄 script.js

Flow:

User uploads 4 videos

Form submits via POST API

Backend processes videos

Results returned

UI displays optimized timings

No frameworks.
Works on any modern browser.

📸 Output Screenshots
📌 Add your screenshots here

🔹 UI Interface
![UI Screenshot](screenshots/ui.png)
🔹 Vehicle Detection
![YOLO Detection](screenshots/yolo_output.png)
🔹 Optimized Traffic Timings
![Results](screenshots/results.png)
(Create a screenshots/ folder and add images)

🚨 Troubleshooting
Backend not starting
Check Python 3.7+

Run pip install -r requirements.txt

Ensure port 5000 is free

Frontend not connecting
Backend must be running

Check CORS errors in console

Upload fails
Exactly 4 videos

Supported formats: MP4, AVI

🧪 Testing
Backend: Postman

Frontend: Browser DevTools

🛠 Customization & Extension
Change detection logic → yolov4.py

Modify optimization → algo.py

Add UI features → script.js

🤝 Contributing
Fork the repo

Create feature branch

Commit changes

Open pull request
