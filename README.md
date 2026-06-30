# 🚀 AI Productivity Companion

## Problem Statement

### The Last-Minute Life Saver

Students, professionals, and entrepreneurs often miss important deadlines, assignments, interviews, meetings, and commitments because traditional productivity tools rely on passive reminders that are easy to ignore.

This project addresses the challenge by building an AI-powered productivity companion that actively helps users plan, prioritize, and complete tasks before deadlines are missed.

---

# Solution Overview
AI Productivity Companion is an agentic productivity assistant powered by Google's Gemini AI.

Instead of acting as a simple reminder application, the system helps users:

- Break large tasks into actionable subtasks
- Prioritize tasks intelligently
- Generate optimized schedules
- Receive personalized productivity guidance
- Track progress through productivity scoring
- Complete tasks before deadlines

The application focuses on proactive assistance rather than passive notifications.

---

# Key Features

## 🧩 AI Task Breakdown

Converts large tasks into manageable actionable steps.

Example:

Task:
Prepare Internship Presentation

AI Output:

- Research company
- Create slide structure
- Add visuals
- Practice presentation
- Final review

---

## 🎯 Intelligent Task Prioritization

Analyzes:

- Task priority
- Deadlines
- Urgency

and generates an optimized order of execution.

---

## 📅 AI Schedule Planner

Generates a realistic daily plan based on available tasks.

Example:

- 6:00 PM - Internship Presentation
- 7:00 PM - Assignment
- 8:00 PM - Interview Preparation

---

## 🧠 AI Productivity Coach

Provides personalized guidance when users feel overwhelmed or unsure where to begin.

---

## ✅ Task Completion Tracking

Users can mark tasks as completed.

---

## 📈 Productivity Score

Tracks performance using:

Productivity Score =

(Completed Tasks / Total Tasks) × 100

This encourages accountability and consistency.

---

# Agentic AI Components

The application demonstrates agentic behavior through:

- Task decomposition
- Intelligent prioritization
- Schedule generation
- Context-aware productivity coaching
- Goal-oriented task completion tracking

Rather than simply reminding users, the AI actively assists in decision-making and planning.

---

# Tech Stack

## Frontend

- Streamlit

## Backend Logic

- Python

## Database

- SQLite

## AI Model

- Google Gemini

---

# Google Technologies Utilized

- Google Gemini API
- Google AI Studio

---

# Project Structure

```text
ai-productivity-companion/

├── app.py
├── main.py
├── ai_agent.py
├── database.py
├── requirements.txt
├── .env
└── README.md
```

# Installation

Clone the repository:

```bash
git clone <repository-url>
cd ai-productivity-companion
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env`

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

# Future Improvements

- Google Calendar Integration
- Voice-Based Task Input
- Overdue Task Detection
- Habit Tracking
- Autonomous Re-planning
- Email and Notification Support

# Impact

Deadline Rescue AI helps users:

- Reduce missed deadlines
- Improve productivity
- Make better decisions
- Stay organized under pressure
- Develop consistent work habits

# Author

Ishika 

Built for the Vibe2Ship Hackathon.