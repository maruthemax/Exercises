from flask import Flask, render_template, redirect, session, request, flash
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/')
def start_page():
    """Display the start page with survey instructions."""
    return render_template('start.html', survey=satisfaction_survey)

@app.route('/begin', methods=["POST"])
def begin_survey():
    """Clear responses and start the survey."""
    session['responses'] = []  # Initialize empty responses list in session
    return redirect('/questions/0')

@app.route('/questions/<int:qid>')
def show_question(qid):
    """Display the current question."""
    responses = session.get('responses')

    # Redirect if accessing an invalid or out-of-order question
    if responses is None or qid != len(responses):
        flash("Invalid question access.")
        return redirect(f"/questions/{len(responses)}")

    question = satisfaction_survey.questions[qid]
    return render_template('question.html', question=question, qid=qid, survey=satisfaction_survey)

@app.route('/answer', methods=["POST"])
def handle_answer():
    """Save the user's answer and move to the next question."""
    answer = request.form['answer']

    # Retrieve and update responses list from the session
    responses = session['responses']
    responses.append(answer)
    session['responses'] = responses  # Save updated list to session

    if len(responses) == len(satisfaction_survey.questions):
        return redirect('/thank-you')

    return redirect(f"/questions/{len(responses)}")

@app.route('/thank-you')
def thank_you():
    """Display the thank-you page."""
    return render_template('thank_you.html', survey=satisfaction_survey)

if __name__ == '__main__':
    app.run(debug=True)
