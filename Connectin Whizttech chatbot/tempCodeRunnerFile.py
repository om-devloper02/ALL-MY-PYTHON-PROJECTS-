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
