from flask import Flask, render_template, request, redirect, url_for
import json
import random

app = Flask(__name__)

# Load vocabulary and grammar from JSON files
def load_vocabulary():
    with open('vocabulary.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz', methods=['POST'])
def quiz():
    vocabulary = load_vocabulary()
    questions = list(vocabulary.items())
    random.shuffle(questions)
    
    # Get the first question for demonstration
    question = questions[0]
    return render_template('quiz.html', question=question[0], correct_answer=question[1])

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    user_answer = request.form['answer']
    correct_answer = request.form['correct_answer']
    
    if user_answer.strip().lower() == correct_answer.lower():
        result = "Correct! Well done."
    else:
        result = f"Incorrect. The correct answer is '{correct_answer}'."
    
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)