# 🧠 CogniFact AI: Neural Truth Engine

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> *An advanced AI Dashboard for detecting misinformation patterns, sensationalism, and linguistic bias using Deep Learning.*

---

## 📖 Table of Contents
- [📍 Overview](#-overview)
- [✨ Key Features](#-key-features)
- [🏗️ System Architecture](#-system-architecture)
- [🛠️ Tech Stack](#-tech-stack)
- [⚡ Local Installation](#-local-installation)
- [📸 Dashboard Preview](#-dashboard-preview)
- [🚀 Future Scope](#-future-scope)

---

## 📍 Overview
**CogniFact AI** (formerly Veritas) is a professional-grade misinformation detection system designed for students, researchers, and academic institutions. 

Unlike simple "True/False" checkers, CogniFact provides a **comprehensive audit** of text. It combines **Transformer-based Deep Learning (RoBERTa)** with heuristic algorithms to calculate a "Sensationalism Score," offering users explainable insights into *why* a piece of content might be misleading.

---

## ✨ Key Features
**CogniFact AI** goes beyond basic classification with a full-stack dashboard:

* **🕵️‍♂️ Neural Misinformation Detection:** Uses the `roberta-fake-news-classification` model to identify fake news patterns with high accuracy.
* **📉 Sensationalism Tracker:** A custom algorithmic score (0-100) that detects "clickbait" language, excessive capitalization, and emotional manipulation.
* **🎛️ Interactive Control Panel:** Sidebar controls to adjust model sensitivity and switch between simulation modes.
* **📊 Real-Time Telemetry:** Live probability distribution bars and confidence metrics.
* **📂 Developer Mode:** A "System Architecture" tab that exposes the raw JSON logs for data transparency.

---

## 🏗️ System Architecture

The application follows a modular pipeline approach:

1.  **Input Layer:** User text is sanitized and passed through the **BPE Tokenizer**.
2.  **Deep Learning Layer:** The **RoBERTa Transformer** (12-layer attention mechanism) analyzes semantic context.
3.  **Heuristic Layer:** Parallel algorithms scan for rule-based anomalies (e.g., Caps Lock abuse, punctuation flooding).
4.  **Presentation Layer:** Results are aggregated and visualized via **Streamlit**.

---

## 🛠️ Tech Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Frontend** | ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) | Dashboard UI, Charts, and State Management. |
| **AI Model** | ![Hugging Face](https://img.shields.io/badge/-Hugging_Face-FFD21E?style=flat&logo=huggingface&logoColor=black) | Pre-trained **RoBERTa** model for NLP tasks. |
| **Backend** | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white) | Core logic, API handling, and scoring algorithms. |
| **Deployment** | ![Cloud](https://img.shields.io/badge/-Streamlit_Cloud-FF4B4B?style=flat&logo=streamlit&logoColor=white) | CI/CD Pipeline and Cloud Hosting. |

---

## ⚡ Local Installation

To run the **CogniFact AI** dashboard on your local machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/MANAV-MISHRA-BYTES/fake-news-detector.git](https://github.com/MANAV-MISHRA-BYTES/fake-news-detector.git)
cd fake-news-detector
