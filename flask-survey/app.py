from flask import Flask, render_template, redirect, request, flash, session
from surveys import satisfaction_survey


app = Flask(__name__)
app.config['SECRET_KEY'] = "supersecretkey"

responses = [] # Store answers here


@app.route('/')
def start_survey():
    """Display the survey title, instructions, and a start button."""
    return render_template('start.html', survey=satisfaction_survey)

@app.route('questions/0')
def first_question():
    """Redirects to the first question."""
    return redirect('/question/0')

@app.route('/questions/<int:qid>')
def show_question(qid):
    """Ensure users can’t skip questions or access invalid questions."""
    if qid != len(responses):
        flash("Invalid question access.")
        return redirect(f"/questions/{len(responses)}")

    if qid >= len(satisfaction_survey.questions):
        return redirect('/thank-you')

    question = satisfaction_survey.questions[qid]
    return render_template('question.html', question=question, qid=qid)


@app.route('/answer', methods=["POST"])
def handle_answer():
    """Save answer and redirect to the next question."""
    answer = request.form['answer']
    responses.append(answer)
    
    if len(responses) == len(satisfaction_survey.questions):
        return redirect('/thank-you')
    
    return redirect(f"/questions/{len(responses)}")

@app.route('/thank_you.html')
def thank_you():
     """Thank the user after completing the survey."""
    return render_template('thank_you.html')