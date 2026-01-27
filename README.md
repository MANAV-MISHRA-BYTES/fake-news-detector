# 🕵️‍♂️ Veritas AI: Fake News Detector for Students

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![Status](https://img.shields.io/badge/Status-Live-success?style=for-the-badge)

> *Combating misinformation in the academic world using Deep Learning and NLP.*

---

## 📖 Table of Contents
- [📍 Overview](#-overview)
- [📉 The Problem](#-the-problem)
- [💡 The Solution](#-the-solution)
- [🛠️ Tech Stack](#-tech-stack)
- [⚡ How to Run](#-how-to-run)
- [📸 Screenshots](#-screenshots)
- [🚀 Future Scope](#-future-scope)

---

## 📍 Overview
**Veritas AI** is a web-based application designed to help students and researchers instantly assess the credibility of news articles. Powered by a **RoBERTa Transformer model** fine-tuned on fake news datasets, this tool analyzes linguistic patterns to distinguish between reliable reporting and potential misinformation.

---

## 📉 The Problem
[cite_start]In the digital age, **misinformation spreads quickly** through online news and social media[cite: 8]. [cite_start]Students often struggle to differentiate between reliable facts and fake narratives, which affects academic integrity and general awareness[cite: 8]. There is a critical need for a tool that can:
* Analyze articles instantly.
* Assess credibility.
* [cite_start]Provide trustworthy summaries[cite: 9].

## 💡 The Solution
We developed an **AI-driven Fake News Detector** that:
* **Input:** Takes news headlines or article excerpts as text input.
* **Process:** Uses Natural Language Processing (NLP) to scan for sensationalism and known fake news patterns.
* **Output:** Returns a **"Real"** or **"Fake"** classification along with a **Confidence Score** (%).

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) | For the interactive web interface. |
| **Model** | ![Hugging Face](https://img.shields.io/badge/-Hugging_Face-FFD21E?style=flat&logo=huggingface&logoColor=black) | **RoBERTa** (Transformer) for text classification. |
| **Language** | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white) | Core logic and scripting. |
| **Hosting** | ![Cloud](https://img.shields.io/badge/-Streamlit_Cloud-FF4B4B?style=flat&logo=streamlit&logoColor=white) | Deployed for public access. |

---

## ⚡ How to Run Locally

If you want to run this project on your own machine, follow these steps:

### 1. Clone the Repository
```bash
git clone [https://github.com/MANAV-MISHRA-BYTES/fake-news-detector.git](https://github.com/MANAV-MISHRA-BYTES/fake-news-detector.git)
cd fake-news-detector
