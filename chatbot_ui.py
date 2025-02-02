import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import random

# Load vocabulary and grammar from JSON files
def load_vocabulary():
    with open('vocabulary.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def load_grammar():
    with open('grammar.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# Load user profiles
def load_user_profiles():
    try:
        with open('user_profiles.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save user profiles
def save_user_profiles(profiles):
    with open('user_profiles.json', 'w', encoding='utf-8') as f:
        json.dump(profiles, f, indent=4)

# Load feedback
def load_feedback():
    try:
        with open('feedback.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save feedback
def save_feedback(feedback):
    with open('feedback.json', 'w', encoding='utf-8') as f:
        json.dump(feedback, f, indent=4)

# Create or load user profile
def create_or_load_profile():
    profiles = load_user_profiles()
    username = simpledialog.askstring("User   Profile", "Enter your name:")
    
    if username:
        if username in profiles:
            messagebox.showinfo("Welcome Back!", f"Welcome back, {username}!")
        else:
            profiles[username] = {"total_score": 0}
            save_user_profiles(profiles)
            messagebox.showinfo("Profile Created", f"Profile created for {username}!")
    
    return username

# Vocabulary Quiz Function
def vocabulary_quiz(username):
    vocabulary = load_vocabulary()
    score = 0
    questions = list(vocabulary.items())
    random.shuffle(questions)
    
    total_questions = len(questions)
    
    for english_word, correct_answer in questions:
        user_answer = simpledialog.askstring("Vocabulary Quiz", f"What is the Spanish word for '{english_word}'?")
        
        if user_answer and user_answer.strip().lower() == correct_answer:
            score += 1
            messagebox.showinfo("Result", "Correct! Well done.")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is '{correct_answer}'.")
    
    messagebox.showinfo("Score", f"Your score: {score}/{total_questions}.")
    
    # Update user profile score
    profiles = load_user_profiles()
    profiles[username]["total_score"] += score
    save_user_profiles(profiles)

# Grammar Explanation Function
def grammar_explanation(username):
    grammar = load_grammar()
    explanation = "Let's learn about verb conjugation in Spanish.\n\n"
    
    for verb, conjugations in grammar.items():
        explanation += f"Conjugation of '{verb}' (to speak):\n"
        for subject, conjugation in conjugations.items():
            explanation += f"{subject} {conjugation}\n"
    
    user_answer = simpledialog.askstring("Grammar Practice", "How do you say 'I eat' in Spanish?")
    
    if user_answer and user_answer.strip().lower() == "yo como":
        messagebox.showinfo("Result", "Correct! 'Yo como' means 'I eat'.")
    else:
        messagebox.showinfo("Result", "Incorrect. The correct answer is 'Yo como'.")
    
    messagebox.showinfo("Grammar Explanation", explanation)

# Feedback Function
def submit_feedback():
    feedback = simpledialog.askstring("Feedback", "Please enter your feedback or suggestions:")
    if feedback:
        existing_feedback = load_feedback()
        existing_feedback.append(feedback)
        save_feedback(existing_feedback)
        messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")

# Main UI Function
def main_ui():
    username = create_or_load_profile()
    
    root = tk.Tk()
    root.title("Language Learning Chatbot")
    root.geometry("500x400")  # Set the window size
    root.configure(bg="#f0f0f0")  # Set background color

    # Title Label
    title_label = tk.Label(root, text="Language Learning Chatbot", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
    title_label.pack(pady=20)

    # Instructions Label
    instructions_label = tk.Label(root, text="Choose an option to start learning:", font=("Helvetica", 12), bg="#f0f0f0")
    instructions_label.pack(pady=10)

    # Buttons with reduced size
    tk.Button(root, text="Take Vocabulary Quiz", command=lambda: vocabulary_quiz(username), bg="#4CAF50", fg="white", font=("Helvetica", 10), width=20).pack(pady=5, padx=20)
    tk.Button(root, text="Learn Grammar", command=lambda: grammar_explanation(username), bg="#2196F3", fg="white", font=("Helvetica", 10), width=20).pack(pady=5, padx=20)
    tk.Button(root, text="Submit Feedback", command=submit_feedback, bg="#FF9800", fg="white", font=("Helvetica", 10), width=20).pack(pady=5, padx=20)

    root.mainloop()

if __name__ == "__main__":
    main_ui()