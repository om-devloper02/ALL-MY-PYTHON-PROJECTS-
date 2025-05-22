===================Connectin Whizttech chatbot=======================


🎓 Connectinwhizttech Admission ChatBot

A simple command-line based chatbot built using Python that helps users explore and enroll in various technical and IT courses offered by Connectinwhizttech. It uses colorama for colored terminal output and provides detailed information about each course.

📌 Features
Interactive chatbot with user-friendly prompts

Displays course options and detailed information

Validates user input (contact number)

Personalized greeting

Shows admission fees, deadlines, and career opportunities

Provides contact information at the end

Color-coded output using colorama

🛠️ Requirements
Python 3.x

colorama module

You can install colorama using pip:

bash
Copy
Edit
pip install colorama
🚀 How to Run
Clone this repository or copy the script to your local machine, then run:

bash
Copy
Edit
python admission_chatbot.py
🧾 Example Usage
text
Copy
Edit
Welcome to Connectinwhizttech ChatBot

Enter your name: Omkar

Enter your contact number: 9876543210

Enter your email: omkar@example.com

Enter your city: Pune

Enter your qualification: B.Tech

Hello Omkar

Choose a course you want to enroll:
1. C/C++
2. Core / Advance Java
3. Python
...
12. Exit

Enter the course number: 3

Python:
Career Options:
1. Data Analyst,
2. Cyber Security Expert,
3. Machine Learning Engineer,
4. Database Administrator.

Admission Fees:  20000
Last Date to Apply: 30th June
Online Offline Classes Available From 1st July
Projects and Internship Available
📇 Contact Info
mathematica
Copy
Edit
Ms. Shruti Jain  
Connectin Whizttech  
1st Floor Singapur Complex  
Diwanwadi Road, Chhatrapati Sambhajinagar (Aurangabad)  
📞 9921990176
📁 File Structure
bash
Copy
Edit
admission_chatbot.py     # Main Python script
README.md                # Project documentation
📝 License
This project is for educational/demo purposes.




===================Connectinwhizttech Voice Chatbo=======================


# 🎓 Connectinwhizttech Voice Chatbot + Python Learning Tracker

This repository contains two Python-based projects:

1. 🗣️ A Speech-enabled Admission Chatbot for course inquiries using `speech_recognition`, `pyttsx3`, and `colorama`.
2. 📘 A Python Learning Tracker class to help students monitor their progress and receive recommendations based on skill level.

---

## 📌 Features

### 🗣️ Admission Chatbot

- Accepts voice input via microphone.
- Provides course details (career options, fees, dates).
- Supports interactive Q&A via text-to-speech and speech-to-text.
- Colored CLI output using `colorama`.

### 📘 Python Learning Tracker

- Tracks topics covered and exercises completed.
- Calculates skill level (Beginner, Intermediate, Advanced).
- Generates learning resource recommendations.
- Saves and loads progress via JSON.

---

## 🛠️ Tech Stack

- Python 3.7+
- `speech_recognition`
- `pyttsx3`
- `colorama`
- `json`
- `datetime`

---

## 🧑‍💻 How to Run

### 1. Install dependencies

```bash
pip install speechrecognition pyttsx3 colorama
Ensure you have PyAudio installed:

bash
Copy
Edit
pip install pyaudio
Note: If PyAudio installation fails, refer to platform-specific instructions.

2. Run the Admission Chatbot
bash
Copy
Edit
python chatbot.py
3. Use the Python Learning Tracker
python
Copy
Edit
from python_learning_tracker import PythonLearningTracker

tracker = PythonLearningTracker("Omkar")
tracker.update_topic_progress("OOP", 8)
tracker.complete_exercise("Loops Challenge", "Medium")
print(tracker.get_progress_summary())
print(tracker.get_recommendations())
🧪 Sample Output
Voice-based admission chatbot interaction via terminal

Skill level: Intermediate

Recommendation: Intermediate Python courses and projects

📂 File Structure
bash
Copy
Edit
📁 project_root/
├── chatbot.py                  # Voice-based admission chatbot
├── python_learning_tracker.py # Python skill progress tracker
├── README.md                   # You're reading this!
└── Omkar_progress.json         # Auto-generated progress file
💡 Future Enhancements
GUI interface using Tkinter or PyQt.

Store chatbot conversations to CSV or DB.

Add support for language translation.

Integrate with online course APIs.

📞 Contact
For admissions or inquiries, contact Ms. Shruti Jain at Connectin Whizttech, Chhatrapati Sambhajinagar
📱 Phone: 9921990176

