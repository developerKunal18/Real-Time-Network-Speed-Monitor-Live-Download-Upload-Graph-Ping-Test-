# 🌐 Real-Time Network Speed Monitor 

## 💡 Overview
The **Real-Time Network Speed Monitor** is a Python-based terminal tool that continuously measures your:

- 📡 Download speed (Mbps)  
- 📤 Upload speed (Mbps)  
- 🏓 Ping latency (ms)  
- 📊 Live ASCII graph visualization  
- ⏱ Speed history (last 40 seconds)

This project is practical, visually appealing, and demonstrates multithreading, real-time monitoring, and ASCII UI rendering.

---

## 🚀 Features

### ✔ Real-Time Speed Tests
Updates every second using background threading.

### ✔ Download & Upload Speeds
Displays Mbps values along with visual bar indicators.

### ✔ Ping Tracking
Measures ping to **Google DNS (8.8.8.8)**.

### ✔ Live ASCII Graphs
Dynamic bars showing speed levels in real-time.

### ✔ Speed History
Stores and displays the last 40 measurements for:
- Download  
- Upload  
- Ping  

### ✔ Multithreaded
Speed testing occurs in a separate thread for smooth UI updates.

---

## 🧠 Technologies Used
- **Python**
- **Speedtest API (`speedtest-cli`)**
- **Subprocess (ping)**  
- **Threading**
- **ASCII rendering**
- **Terminal UI**

---
