import pyttsx3
import time
import csv
import winsound  # For beep alarms

# Initialize pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Body parameters
body = {
    "temperature": 37.0,
    "blood_sugar": 90,
    "ph": 7.4,
    "osmolality": 290,
    "hydration": 100
}

# Evaluate parameters and give symptoms, emergencies, and interventions
def evaluate_parameters():
    emergency_triggered = False
    interventions = {}

    # Temperature
    if body["temperature"] < 36.1:
        speak("Body temperature is low. Shivering and vasoconstriction activated.")
        print("Symptoms: Shivering, pale skin, fatigue.")
        interventions["temperature"] = ["Keep warm", "Drink warm fluids", "Rest"]
        emergency_triggered = True
    elif body["temperature"] > 37.2:
        speak("Body temperature is high. Sweating and vasodilation activated.")
        print("Symptoms: Sweating, flushed skin, rapid heartbeat.")
        interventions["temperature"] = ["Rest", "Hydrate", "Cool environment"]
        emergency_triggered = True
    else:
        speak("Body temperature is normal.")

    # Blood sugar
    if body["blood_sugar"] < 70:
        speak("Blood sugar is low. Glucagon released.")
        print("Symptoms: Weakness, dizziness, hunger.")
        interventions["blood_sugar"] = ["Consume sugar", "Eat a snack", "Rest"]
        emergency_triggered = True
    elif body["blood_sugar"] > 140:
        speak("Blood sugar is high. Insulin released.")
        print("Symptoms: Thirst, frequent urination, fatigue.")
        interventions["blood_sugar"] = ["Hydrate", "Avoid sugar intake", "Rest"]
        emergency_triggered = True
    else:
        speak("Blood sugar is normal.")

    # pH
    if body["ph"] < 7.35:
        speak("Blood pH is acidic. Breathing rate increases.")
        print("Symptoms: Rapid breathing, confusion, fatigue.")
        interventions["ph"] = ["Check breathing", "Avoid strenuous activity"]
        emergency_triggered = True
    elif body["ph"] > 7.45:
        speak("Blood pH is alkaline. Breathing rate decreases.")
        print("Symptoms: Slow breathing, muscle twitching, irritability.")
        interventions["ph"] = ["Monitor symptoms", "Avoid vomiting or antacids"]
        emergency_triggered = True
    else:
        speak("Blood pH is normal.")

    # Osmolality
    if body["osmolality"] < 280:
        speak("Osmolality is low. Water excretion increased.")
        print("Symptoms: Confusion, weakness, headache.")
        interventions["osmolality"] = ["Hydrate", "Check electrolytes", "Rest"]
        emergency_triggered = True
    elif body["osmolality"] > 300:
        speak("Osmolality is high. Water retained.")
        print("Symptoms: Thirst, dry mouth, reduced urine output.")
        interventions["osmolality"] = ["Drink water", "Monitor hydration", "Avoid salt overload"]
        emergency_triggered = True
    else:
        speak("Osmolality is normal.")

    # Emergency alert
    if emergency_triggered:
        speak("Emergency detected! Immediate attention required!")
        for _ in range(3):
            winsound.Beep(1000, 500)

    return interventions

# Apply interventions
def apply_intervention(interventions):
    for param, actions in interventions.items():
        speak(f"For {param}, recommended actions are:")
        print(f"\nFor {param}, recommended actions:")
        for idx, action in enumerate(actions,1):
            print(f"{idx}: {action}")
            speak(f"{idx}. {action}")

        choice = input("Choose an action number to apply: ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(actions):
                speak(f"Applied action: {actions[choice-1]}")
                # Simulate effect on body parameters
                if param == "temperature":
                    if "Keep warm" in actions[choice-1]:
                        body["temperature"] += 0.5
                    elif "Hydrate" in actions[choice-1]:
                        body["temperature"] -= 0.3
                elif param == "blood_sugar":
                    if "Consume sugar" in actions[choice-1] or "Eat a snack" in actions[choice-1]:
                        body["blood_sugar"] += 20
                    elif "Hydrate" in actions[choice-1]:
                        body["blood_sugar"] -= 5
                elif param == "ph":
                    body["ph"] += 0.01  # small adjustment
                elif param == "osmolality":
                    if "Hydrate" in actions[choice-1]:
                        body["osmolality"] -= 10
        except:
            speak("Invalid choice, skipping intervention.")

# Log session
def log_session():
    with open("homeostasis_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([time.asctime()] + [v for v in body.values()])

# Main loop
def main():
    while True:
        try:
            body["temperature"] = float(input("Enter body temperature (°C): "))
            body["blood_sugar"] = float(input("Enter blood sugar level (mg/dL): "))
            body["ph"] = float(input("Enter blood pH level: "))
            body["osmolality"] = float(input("Enter osmolality of body fluids (mOsm/kg): "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            speak("Invalid input. Try again.")
            continue

        interventions = evaluate_parameters()
        if interventions:
            apply_intervention(interventions)

        log_session()

        cont = input("Press Enter to continue or type 'exit' to quit: ").lower()
        if cont == 'exit':
            speak("Exiting program. Goodbye!")
            break

if __name__ == "__main__":
    main()
