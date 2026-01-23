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


## 🚀 Quick Start:
 
### Prerequisites 
- Python 3.7 or higher 
- Modern web browser (Chrome, Firefox, Safari, Edge)

### 🎯 Easiest Way to Start (Recommended)
 
#### Windows Users:
```bash
# Double-click the start_project.bat file
# OR run from command line:
start_project.bat
```
 
#### Linux/Mac Users:
```bash
# Make the script executable (first time only)
chmod +x start_project.sh

# Run the startup script
./start_project.sh
```
 
### 🔧 Manual Setup

#### 1. Backend Setup

```bash 
# Navigate to backend directory 
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Start the backend server 
python app.py
```

The backend will start on `http://localhost:5000`

#### 2. Frontend Setup

The frontend is now a vanilla HTML/CSS/JS application. You can run it in several ways:
  
##### Option A: Using Python's built-in server (Recommended) 
```bash  
# Navigate to frontend directory 
cd frontend 

# Start the HTTP server
python -m http.server 8000
```
Then open `http://localhost:8000` in your browser 
 
##### Option B: Direct file opening
Simply double-click `frontend/index.html` to open it in your browser

##### Option C: Using Live Server (VS Code)
1. Install "Live Server" extension in VS Code
2. Right-click on `frontend/index.html`
3. Select "Open with Live Server"

### 3. Test Connection (Optional)

To verify everything is working correctly, you can test the connection:  
 
```bash
# Open the connection test page
http://localhost:8000/test_connection.html
```

This will automatically test both backend and frontend connections.

### 4. Usage

1. Open the main application: `http://localhost:8000/index.html`
2. Click "Choose Files" and select exactly 4 video files showing different roads at an intersection
3. Click "Run Model" to process the videos 
4. Wait for the AI analysis (may take a few minutes)
5. View the optimized traffic light timings for each direction

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
