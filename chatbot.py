import json
import random

def load_vocabulary():
    with open('vocabulary.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def load_grammar():
    with open('grammar.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# Vocabulary Quiz Function
def vocabulary_quiz():
    vocabulary = load_vocabulary()
    score = 0
    total_questions = len(vocabulary)
    
    for _ in range(total_questions):
        english_word = random.choice(list(vocabulary.keys()))
        correct_answer = vocabulary[english_word]
        
        print(f"What is the Spanish word for '{english_word}'?")
        user_answer = input("Your answer: ").strip().lower()
        
        if user_answer == correct_answer:
            print("Correct! Well done.")
            score += 1
        else:
            print(f"Incorrect. The correct answer is '{correct_answer}'.")
    
    print(f"Your score: {score}/{total_questions}.")

# Grammar Explanation Function
def grammar_explanation():
    grammar = load_grammar()
    explanation = "Let's learn about verb conjugation in Spanish.\n\n"
    
    for verb, conjugations in grammar.items():
        explanation += f"Conjugation of '{verb}' (to speak):\n"
        for subject, conjugation in conjugations.items():
            explanation += f"{subject} {conjugation}\n"
    
    print("How do you say 'I eat' in Spanish?")
    user_answer = input("Your answer: ").strip().lower()
    
    if user_answer == "yo como":
        print("Correct! 'Yo como' means 'I eat'.")
    else:
        print("Incorrect. The correct answer is 'Yo como'.")
    
    print(explanation)

if __name__ == "__main__":
    # You can call the vocabulary_quiz or grammar_explanation functions here if needed
    pass