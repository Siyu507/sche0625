import os
import datetime

# Dictionary mapping symptoms to health advice
SYMPTOM_ADVICE = {
    "fever": "You may have an infection. Stay hydrated and rest. Consider seeing a doctor if it persists.",
    "cough": "Try to rest and drink warm fluids. If the cough is severe or lasts more than a week, consult a doctor.",
    "headache": "Stay hydrated and rest. Over-the-counter pain relief may help. Persistent pain needs medical attention.",
    "sore throat": "Gargle with warm salt water and avoid irritants. If it persists or is severe, consult a doctor.",
    "nausea": "Avoid solid food and drink clear fluids. Seek medical advice if vomiting occurs or persists.",
    "runny nose": "Use tissues, wash hands frequently, and consider antihistamines if allergy-related.",
    "fatigue": "Ensure adequate sleep, nutrition, and hydration. Chronic fatigue may need medical evaluation.",
    "shortness of breath": "Could be serious. Rest and seek medical help if it's sudden or severe.",
    "chest pain": "May indicate a serious issue. Seek emergency help if it's sharp, sudden, or radiating.",
    "diarrhea": "Stay hydrated and avoid greasy foods. If prolonged or severe, see a doctor.",
    "constipation": "Increase fiber and fluid intake. Gentle exercise helps. Consult if it lasts more than a few days.",
    "dizziness": "Sit or lie down, hydrate, and avoid sudden movements. Seek care if frequent or with other symptoms.",
    "rash": "Avoid scratching, use soothing lotions. If it spreads or becomes painful, get medical advice.",
    "vomiting": "Rest the stomach. Drink small sips of water. Seek help if it’s continuous or includes blood.",
    "back pain": "Use good posture and stretch gently. If it persists or worsens, seek professional evaluation."
}

HISTORY_FILE = "user_history.txt"  # File to store user history


def show_welcome():
    """Print welcome message."""
    print("=== Welcome to MediBuddy – A Symptom Checker ===")


def get_user_input_by_questionnaire():
    """
    Ask the user about each symptom using yes/no questions.
    Returns a list of symptoms the user confirms having.
    """
    print("\nPlease answer the following questions with 'yes' or 'no':")
    selected_symptoms = []
    for symptom in SYMPTOM_ADVICE.keys():
        answer = input(f"Do you have {symptom}? ").strip().lower()
        if answer in ["yes", "y"]:
            selected_symptoms.append(symptom)
    return selected_symptoms


def give_advice(symptoms):
    """
    Display advice for each selected symptom.
    Returns a list of (symptom, advice) pairs for saving.
    """
    result = []
    for symptom in symptoms:
        advice = SYMPTOM_ADVICE.get(symptom)
        if advice:
            print(f"\nAdvice for '{symptom}': {advice}")
        else:
            print(f"\nSorry, no advice available for '{symptom}'. Try another common symptom.")
        result.append((symptom, advice))
    return result


def save_to_history(symptom_advice_pairs):
    """
    Append the user's symptom and advice results to a local text file with timestamps.
    """
    with open(HISTORY_FILE, "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for symptom, advice in symptom_advice_pairs:
            f.write(f"{timestamp} | Symptom: {symptom} | Advice: {advice or 'Not found'}\n")


def view_history():
    """Display the contents of the user history file."""
    if not os.path.exists(HISTORY_FILE):
        print("No history found.")
        return
    print("\n--- Symptom Check History ---")
    with open(HISTORY_FILE, "r") as f:
        print(f.read())


def main():
    """Main program loop with menu options."""
    show_welcome()
    while True:
        print("\nOptions:")
        print("1. Start symptom questionnaire")
        print("2. View history")
        print("3. Exit")
        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            symptoms = get_user_input_by_questionnaire()
            if not symptoms:
                print("No symptoms selected.")
            else:
                symptom_advice_pairs = give_advice(symptoms)
                save_to_history(symptom_advice_pairs)
        elif choice == "2":
            view_history()
        elif choice == "3":
            print("Thank you for using MediBuddy. Stay healthy!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

