# ⚔️ TASK RPG: Gamified Productivity System

![Status](https://img.shields.io/badge/STATUS-OPERATIONAL-green?style=for-the-badge)
![Python](https://img.shields.io/badge/PYTHON-3.14-blue?style=for-the-badge&logo=python&logoColor=white)
![Lib](https://img.shields.io/badge/LIB-COLORAMA-red?style=for-the-badge)
![Data](https://img.shields.io/badge/DATA-JSON_PERSISTENCE-orange?style=for-the-badge)

> *"Gamify your life. Hack your productivity."*

## 📖 ABOUT
**Task RPG** is a persistent Command Line Interface (CLI) application that turns daily tasks into an RPG game. Designed for Netrunners who need to track their productivity, it allows users to earn **XP** for completing tasks, level up, and maintain their stats across sessions using local JSON storage.

It features a **Neon-Cyberpunk Interface** powered by `colorama` for a immersive terminal experience.

## ⚡ FEATURES
- [x] **Persistent Save System:** Automatically saves/loads User Stats (Level, XP, Name) using JSON.
- [x] **XP & Leveling Logic:** Mathematical progression system (Level Up every 100 XP).
- [x] **Neon UI:** Visual feedback with Red/Green/Cyan colors depending on actions.
- [x] **Visual Health Bars:** Dynamic ASCII progress bars for XP tracking.

## 🛠️ THE PROCESS (What I Learned)
Based on the **Python Zero to Hero** roadmap, this project represents the Capstone of Phase 5 & 6.

- **Challenge:** Making data survive after closing the script.
- **Solution:** Learned to use `json` module and Context Managers (`with open...`) to read/write data safely to the hard drive.
- **Evolution:** - *v1.0:* Simple variables (Volatile memory).
    - *v2.0:* OOP Class `Agente` (Better structure).
    - *v3.0:* `colorama` integration for better UX (Current).

## 🚀 HOW TO RUN
1. **Clone the repository:**
   ```bash
   git clone https://github.com/NamelessVamp/python-zero-to-hero.git
   ```
2. **Install dependencies:**
   ```bash
   pip install colorama
   ```
3. **Run the system:**
   ```bash
   python B4T_L4B_ZERO.py
   ```
