# 🤖 SmartRoll AI

### Next-Generation AI-Powered Attendance Management Platform

---

## 🚀 Overview

SmartRoll AI is a multi-tenant attendance management platform designed for educational institutions and organizations. It leverages advanced Artificial Intelligence and biometric verification technologies to automate attendance tracking while preventing fraudulent attendance practices.

Unlike traditional attendance systems that rely on manual entry, RFID cards, or simple QR scans, SmartRoll AI combines facial recognition, voice biometrics, liveness detection, and intelligent attendance validation to ensure authenticity and accuracy.

The platform supports multiple organizations, role-based access control, automated attendance reporting, and real-time analytics through dedicated dashboards for administrators, teachers, and students.

---

## ✨ Key Features

### 🎯 AI-Powered Attendance Verification

* Face Recognition-based attendance
* Voice biometric authentication
* Multi-factor identity verification
* Real-time attendance processing

### 🛡 Advanced Security

* Liveness detection  
* Anti-spoofing protection
* Duplicate face prevention
* Photo attack detection
* Secure role-based access control

### 🏫 Multi-Tenant Architecture

* Multiple organizations support
* Independent institutional management
* Separate teacher and student portals
* Scalable deployment model

### 👨‍🏫 Teacher Portal

* Manage subjects and classes
* Generate attendance sessions
* Monitor attendance records
* Access analytics dashboard
* Generate attendance reports automatically

### 🎓 Student Portal

* Secure registration
* QR-based enrollment
* Attendance tracking
* Subject-wise attendance view
* Personal dashboard access

### 📊 Analytics & Reporting

* Automated attendance reports
* Subject-wise insights
* Attendance statistics
* Real-time monitoring
* Performance tracking

### 📱 Smart QR Enrollment

* Dynamic QR generation
* Quick student onboarding
* Seamless classroom joining
* Secure enrollment workflow

---

## 🔄 System Workflow

### 1️⃣ Landing Platform

Users are introduced to the SmartRoll AI ecosystem through a modern landing page showcasing platform capabilities, features, and attendance workflow.

### 2️⃣ Authentication

Users securely log in through dedicated access portals.

### 3️⃣ Role-Based Dashboard

The platform routes users to their respective dashboards:

* Teacher Dashboard
* Student Dashboard
* Administrative Controls

### 4️⃣ QR-Based Enrollment

Teachers generate QR codes that students scan to join classes and attendance sessions.

### 5️⃣ Biometric Verification

SmartRoll AI validates identity using:

* Facial Recognition
* Voice Authentication

### 6️⃣ Attendance Processing

The system automatically records attendance while preventing:

* Duplicate attendance
* Fake photo submissions
* Identity spoofing attempts

### 7️⃣ Analytics & Reports

Attendance data is processed and visualized through dashboards and automated reporting modules.

---

## 🧠 AI Technologies Used

### Face Biometrics

* Dlib
* Face Recognition

### Voice Biometrics

* Librosa
* Resemblyzer

### Intelligent Validation

* Liveness Detection
* Duplicate Face Prevention
* Identity Verification

---

## 🏗 Architecture

```text
Student / Teacher
        │
        ▼
   Streamlit UI
        │
        ▼
 Authentication Layer
        │
        ▼
 ┌─────────────────────┐
 │  Face Recognition   │
 │  Voice Biometrics   │
 │ Liveness Detection  │
 └─────────────────────┘
        │
        ▼
 Attendance Engine
        │
        ▼
     Supabase
        │
        ▼
 Analytics & Reports
```

---

## 🛠 Tech Stack

### Frontend

* Streamlit

### Programming Language

* Python

### Face Recognition

* Dlib
* Face Recognition

### Voice Authentication

* Librosa
* Resemblyzer

### Database & Backend

* Supabase

### QR Generation

* Segno

### Data Processing

* NumPy
* Pandas

### Visualization

* Plotly
* Matplotlib

---

## 📸 Screenshots

### Landing Page

<p align="center">
  <img src="./static/img/landing-preview.png" width="100%">
</p>

### Teacher Dashboard

<p align="center">
  <img src="./static/img/teacher-dashboard-preview.png" width="100%">
</p>

### Student Dashboard

<p align="center">
  <img src="./static/img/student-dashboard-preview.png" width="100%">
</p>

### Attendance Analytics

<p align="center">
  <img src="./static/img/attendance-analytics-preview.png" width="100%">
</p>

### QR Enrollment System

<p align="center">
  <img src="./static/img/QR-enrollment-preview.png" width="100%">
</p>

---

## 🌐 Live Demo

### Landing Page

https://smart-roll-ai-landing.vercel.app/

### Main Application

https://smartroll-ai-mainapp-cnymqxqmfch249ev6mhkng.streamlit.app

## 🌐 Official Landing Page

Explore the SmartRoll AI website:

➡️ https://github.com/chandansinghbhandari/SmartRoll-AI-Landing

---

## 🎯 Why SmartRoll AI?

✅ Eliminates manual attendance processes

✅ Prevents attendance fraud

✅ Supports large-scale institutions

✅ Combines multiple biometric modalities

✅ Enhances attendance accuracy

✅ Automates reporting and analytics

✅ Provides a modern, scalable attendance solution

---

## 🚀 Future Enhancements

* Mobile Application
* Cloud Deployment
* Facial Emotion Analytics
* Attendance Prediction
* AI-Powered Insights
* Institution Performance Dashboard
* Multi-Campus Management
* Real-Time Notifications

---

## 👨‍💻 Developer

**Chandan Singh Bhandari**

AI Enthusiast • Full Stack Developer • Machine Learning Explorer

Building intelligent systems that solve real-world problems through Artificial Intelligence, Automation, and Modern Web Technologies.

---

### ⭐ If you found this project interesting, consider giving it a star!
