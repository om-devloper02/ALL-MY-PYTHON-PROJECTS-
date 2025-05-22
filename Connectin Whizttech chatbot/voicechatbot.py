import colorama
import speech_recognition as sr
import pyttsx3
from colorama import Fore, Back, Style

colorama.init()

# Text-to-Speech setup
engine = pyttsx3.init()

def speak(text):
    print(Fore.GREEN + text)
    engine.say(text)
    engine.runAndWait()

# Speech-to-Text
def take_voice_input(prompt="Speak now:"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak(prompt)
        audio = recognizer.listen(source)

        try:
            user_input = recognizer.recognize_google(audio)
            print(Fore.CYAN + f"You said: {user_input}")
            return user_input.lower()
        except sr.UnknownValueError:
            speak("Sorry, I could not understand your voice.")
            return ""
        except sr.RequestError:
            speak("Speech Recognition service is unavailable.")
            return ""

def print_course_details():
    speak("Choose a course you want to enroll:")
    print(Fore.BLUE + "\n1. C/C++")
    print(Fore.LIGHTGREEN_EX + "2. Core / Advance Java")
    print(Fore.LIGHTMAGENTA_EX + "3. Python")
    print(Fore.LIGHTRED_EX + "4. Golang")
    print(Fore.BLUE + "5. HTML/CSS/JavaScript")
    print(Fore.LIGHTGREEN_EX + "6. DotNet")
    print(Fore.LIGHTMAGENTA_EX + "7. C#")
    print(Fore.LIGHTRED_EX + "8. Ethical Hacking")
    print(Fore.BLUE + "9. Computer Hacking Forensic Investigator")
    print(Fore.LIGHTGREEN_EX + "10. Networking")
    print(Fore.LIGHTMAGENTA_EX + "11. Cyber Law")
    print(Fore.LIGHTRED_EX + "12. Exit")

def admission_chatbot():
    speak("Welcome to Connectinwhizttech ChatBot")

    speak("Please tell me your name.")
    name = take_voice_input("What is your name?")

    while True:
        speak("Please tell me your contact number.")
        contact_number = take_voice_input("Say your contact number digit by digit.")

        if contact_number.replace(" ", "").isdigit():
            break
        else:
            speak("Please say only digits.")

    speak("Please tell me your email.")
    email = take_voice_input()

    speak("Which city are you from?")
    city = take_voice_input()

    speak("What is your qualification?")
    qualification = take_voice_input()

    speak(f"Hello {name}, thank you for your interest.")

    while True:
        print_course_details()
        speak("Please say the course number.")
        user_input = take_voice_input("Say the number between 1 to 12.")

        course_info = {
            "1": ("C/C++", "C/C++ Developer, Analyst.", "5000"),
            "2": ("Core / Advance Java", "Java Developer, DevOps Engineer, Solutions Architect, Project Manager", "20000"),
            "3": ("Python", "Data Analyst, Cyber Security Expert, Machine Learning Engineer, Database Administrator", "20000"),
            "4": ("Golang", "Golang Developer, Backend Developer, Open Source Contributor, Technical Lead", "20000"),
            "5": ("HTML/CSS/JavaScript", "Web Developer, Front-end Developer, JavaScript Developer, Content Editor, HTML Email Developer, SEO Specialist, UI Designer", "20000"),
            "6": ("DotNet", ".NET Software Developer, .NET Engineer, .NET Architect", "20000"),
            "7": ("C#", "C# Developer, Software Engineer, Application Developer, Web Developer, Systems Analyst, Solution Architect, Backend Developer", "20000"),
            "8": ("Ethical Hacking", "Network Support, Network Engineering, InfoSec roles", "20000"),
            "9": ("CHFI", "Forensic Analyst, Security Consultant, Incident Responder, IT Auditor", "20000"),
            "10": ("Networking", "Network Administrator, Analyst, Help Desk Technician, Network Architect", "20000"),
            "11": ("Cyber Law", "Cyber Lawyer, Cyber Advisor, InfoSec Auditor, Research Assistant", "20000"),
        }

        if user_input in course_info:
            course_name, careers, fees = course_info[user_input]
            speak(f"{course_name}")
            speak(f"Career Options: {careers}")
            speak(f"Admission Fees: {fees}")
            speak("Last Date to Apply: 30th June")
            speak("Online and Offline Classes available from 1st July")
            speak("Projects and Internship available")
        elif user_input == "12":
            speak("Thank you for using Connectinwhizttech ChatBot. Goodbye!")
            break
        else:
            speak("Sorry, I didn't get you. Please choose a number between 1 and 12.")
            continue

        speak("Do you have any other questions? Say yes or no.")
        further_question = take_voice_input()

        if "no" in further_question:
            speak("Thank you for using Connectinwhizttech ChatBot. Goodbye!")
            speak("For more details, contact Ms. Shruti Jain at Connectin Whizttech, Chhatrapati Sambhajinagar. Phone: 9921990176")
            break
        elif "yes" not in further_question:
            speak("Please say yes or no.")

if __name__ == "__main__":
    admission_chatbot()



# # python_learning_tracker.py
# import json
# from datetime import datetime
# from typing import List, Dict

# class PythonLearningTracker:
#     def __init__(self, student_name: str):
#         self.student_name = student_name
#         self.progress_data = {
#             "student_name": student_name,
#             "topics_covered": [],
#             "completed_exercises": [],
#             "skill_level": "beginner",
#             "learning_history": [],
#             "last_updated": datetime.now().isoformat()
#         }
#         self._load_progress()

#     def _load_progress(self):
#         try:
#             with open(f"{self.student_name}_progress.json", "r") as f:
#                 self.progress_data = json.load(f)
#         except FileNotFoundError:
#             self._save_progress()

#     def _save_progress(self):
#         with open(f"{self.student_name}_progress.json", "w") as f:
#             json.dump(self.progress_data, f, indent=4)

#     def update_topic_progress(self, topic: str, proficiency: int):
#         self.progress_data["topics_covered"].append({
#             "topic": topic,
#             "proficiency": proficiency,
#             "date": datetime.now().isoformat()
#         })
#         self._update_skill_level()
#         self._save_progress()

#     def complete_exercise(self, exercise_name: str, difficulty: str):
#         self.progress_data["completed_exercises"].append({
#             "name": exercise_name,
#             "difficulty": difficulty,
#             "date": datetime.now().isoformat()
#         })
#         self._save_progress()

#     def _update_skill_level(self):
#         if len(self.progress_data["topics_covered"]) > 10:
#             self.progress_data["skill_level"] = "advanced"
#         elif len(self.progress_data["topics_covered"]) > 5:
#             self.progress_data["skill_level"] = "intermediate"
#         else:
#             self.progress_data["skill_level"] = "beginner"

#     def get_recommendations(self) -> List[Dict]:
#         recommendations = []
#         skill_level = self.progress_data["skill_level"]
        
#         if skill_level == "beginner":
#             recommendations.extend([
#                 {
#                     "type": "tutorial",
#                     "title": "Python Basics",
#                     "url": "https://docs.python.org/3/tutorial/index.html",
#                     "description": "Official Python tutorial for beginners"
#                 },
#                 {
#                     "type": "exercise",
#                     "title": "Basic Python Exercises",
#                     "url": "https://www.practicepython.org/",
#                     "description": "Practice basic Python concepts"
#                 }
#             ])
#         elif skill_level == "intermediate":
#             recommendations.extend([
#                 {
#                     "type": "tutorial",
#                     "title": "Intermediate Python",
#                     "url": "https://realpython.com/intermediate-python/",
#                     "description": "Advanced Python concepts and patterns"
#                 },
#                 {
#                     "type": "exercise",
#                     "title": "Python Challenges",
#                     "url": "https://www.codewars.com/",
#                     "description": "Practice intermediate Python challenges"
#                 }
#             ])
#         else:
#             recommendations.extend([
#                 {
#                     "type": "tutorial",
#                     "title": "Advanced Python",
#                     "url": "https://realpython.com/advanced-python/",
#                     "description": "Advanced Python programming concepts"
#                 },
#                 {
#                     "type": "exercise",
#                     "title": "Advanced Python Projects",
#                     "url": "https://github.com/topics/python-projects",
#                     "description": "Work on real-world Python projects"
#                 }
#             ])
#         return recommendations

#     def get_progress_summary(self) -> Dict:
#         return {
#             "student_name": self.student_name,
#             "skill_level": self.progress_data["skill_level"],
#             "topics_covered": len(self.progress_data["topics_covered"]),
#             "exercises_completed": len(self.progress_data["completed_exercises"]),
#             "last_updated": self.progress_data["last_updated"]
#         }