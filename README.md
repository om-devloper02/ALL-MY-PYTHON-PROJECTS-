===================#Connectin Whizttech chatbot=======================


# 🎓 Connectinwhizttech Admission ChatBot


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




===================#Connectinwhizttech Voice Chatbo=======================


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


==============# Python Restaurant Ordering System - Bhakri House================



# 🥘 Python Restaurant Ordering System - Bhakri House

This is a beginner-friendly Python console application that simulates a food ordering system for a Maharashtrian-style restaurant called "Bhakri House".

---

## 📋 Features

- Menu-based item selection
- Order confirmation with pricing
- Supports up to 4 items per order
- Calculates and displays the final bill

---

## 🧾 Menu

Maharashtrian Veg Thali : ₹120
Special Veg Thali : ₹160
Bhakri Thali (2 Bhakris) : ₹130
Pithla Bhakri : ₹100
Zunka Bhakri : ₹90
Chapati Bhaji Plate : ₹80
Varan Bhat + Papad : ₹70
Matki Usal + Bhakri : ₹110

yaml
Copy
Edit

---

## ▶️ How to Run

1. Save the Python code in a file, e.g. bhakri_house.py
2. Open a terminal and run:

```bash
python bhakri_house.py
Follow the on-screen instructions to place your order.

💻 Sample Code
python
Copy
Edit
# Define the menu of restaurant
menu = {
    'Maharashtrian Veg Thali': 120,
    'Special Veg Thali': 160,
    'Bhakri Thali (2 Bhakris)': 130,
    'Pithla Bhakri': 100,
    'Zunka Bhakri': 90,
    'Chapati Bhaji Plate': 80,
    'Varan Bhat + Papad': 70,
    'Matki Usal + Bhakri': 110,
}

print("WELCOME TO PYTHON RESTAURANT //Bhakri House//")
print("\nMaharashtrian Veg Thali:120\nSpecial Veg Thali:160\nBhakri Thali (2 Bhakris):130\nPithla Bhakri:100\nZunka Bhakri:90\nChapati Bhaji Plate:80\nVaran Bhat + Papad:70\nMatki Usal + Bhakri:110")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "Yes":
    item_3 = input("Enter the name of third item = ")
    if item_3 in menu:
        order_total += menu[item_3]
        print(f"Item {item_3} has been added to order")
    else:
        print(f"Ordered item {item_3} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "Yes":
    item_4 = input("Enter the name of fourth item = ")
    if item_4 in menu:
        order_total += menu[item_4]
        print(f"Item {item_4} has been added to order")
    else:
        print(f"Ordered item {item_4} is not available yet!")

print(f"\n🧾 Total Amount to Pay: ₹{order_total}")
🧠 Author
Developed by Omkar as part of a Python learning journey.


