import pyttsx3
import speech_recognition as sr

# Initialize pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def takeCommand():
    """Take voice command from the user."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
        except Exception as e:
            print("Say that again please...")
            return "None"
    return query.lower()

def speak(audio):
    """Speak the provided audio text."""
    engine.say(audio)
    engine.runAndWait()

def regulate_temp():
    """Demonstrate regulation of body temperature."""
    speak("Enter the body temperature.")
    body_temp = float(input("Enter the body temperature (°C): "))
    print(f"Current Body Temperature: {body_temp:.1f} °C")
    speak(f"Current Body Temperature: {body_temp:.1f} degrees Celsius.")
    
    if body_temp < 36.1:
        message = "Body temperature is low. Mechanism: Shivering and vasoconstriction activated."
    elif body_temp > 37.2:
        message = "Body temperature is high. Mechanism: Sweating and vasodilation activated."
    else:
        message = "Body temperature is normal. No action required."
    
    print(message)
    speak(message)

def regulate_bd():
    """Demonstrate regulation of blood sugar levels."""
    speak("Enter the blood sugar level.")
    blood_sugar = float(input("Enter the blood sugar level (mg/dL): "))
    print(f"Current Blood Sugar Level: {blood_sugar:.1f} mg/dL")
    speak(f"Current Blood Sugar Level: {blood_sugar:.1f} milligrams per deciliter.")
    
    if blood_sugar < 70:
        message = "Blood sugar is low. Mechanism: Release of glucagon to increase sugar levels."
    elif blood_sugar > 140:
        message = "Blood sugar is high. Mechanism: Release of insulin to lower sugar levels."
    else:
        message = "Blood sugar level is normal. No action required."
    
    print(message)
    speak(message)

def regulate_ph():
    """Demonstrate regulation of blood pH levels."""
    speak("Enter the blood pH levels of the body.")
    ph = float(input("Enter the blood pH levels of the body: "))
    print(f"Current Blood pH Level: {ph:.1f}")
    speak(f"Current Blood pH Level: {ph:.1f}.")
    
    if ph < 7.35:
        message = "Blood pH is low (acidic). Mechanism: Increased breathing rate to expel CO2."
    elif ph > 7.45:
        message = "Blood pH is high (alkaline). Mechanism: Decreased breathing rate to retain CO2."
    else:
        message = "Blood pH level is normal. No action required."
    
    print(message)
    speak(message)

def osmoregulation():
    """Demonstrate regulation of water and salt balance."""
    speak("Enter the osmolality of the body fluids.")
    osm = float(input("Enter the osmolality of the body fluids (mOsm/kg): "))
    print(f"Current Osmolality: {osm:.1f} mOsm/kg")
    speak(f"Current Osmolality: {osm:.1f} milliosmoles per kilogram.")
    
    if osm < 280:
        message = "Osmolality is low. Mechanism: Decreased ADH release to promote water excretion."
    elif osm > 300:
        message = "Osmolality is high. Mechanism: Increased ADH release to retain water."
    else:
        message = "Osmolality is normal. No action required."
    
    print(message)
    speak(message)

def main():
    """Main program to demonstrate homeostasis."""
    print("Welcome to Homeostasis Demonstrator")
    speak("Welcome to Homeostasis Demonstrator")
    print("1: Demonstrate regulation of body temperature")
    speak("Press 1 to demonstrate the regulation of body temperature.")
    print("2: Demonstrate regulation of blood sugar levels")
    speak("Press 2 to demonstrate the regulation of blood sugar levels.")
    print("3: Demonstrate regulation of pH in the body")
    speak("Press 3 to demonstrate the regulation of pH in the body.")
    print("4: Demonstrate regulation of water and salts in the body")
    speak("Press 4 to demonstrate the regulation of water and salts in the body.")

    while True:
        speak("Please choose an option.")
        ask = takeCommand()
        if 'one' in ask or '1' in ask:
            regulate_temp()
        elif 'two' in ask or '2' in ask:
            regulate_bd()
        elif 'three' in ask or '3' in ask:
            regulate_ph()
        elif 'four' in ask or '4' in ask:
            osmoregulation()
        else:
            print("Invalid choice. Please try again.")
            speak("Invalid choice. Please try again.")
            continue

        print("Say 1 to continue or 2 to exit:")
        speak("Say 1 to continue or 2 to exit.")
        ask_2 = takeCommand()

        if 'one' in ask_2 or '1' in ask_2:
            continue
        elif 'two' in ask_2 or '2' in ask_2:
            print("Exiting. Goodbye!")
            speak("Exiting. Goodbye!")
            break
        else:
            print("Error: Invalid input. Exiting.")
            speak("Error: Invalid input. Exiting.")
            break

if __name__ == "__main__":
    main()
