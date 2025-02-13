from flask import Flask, render_template, request
from stories import stories

app = Flask(__name__)

@app.route('/')
def home():
    """Show the form to ask for words."""
    story_id = request.args.get('story', 'story1')  # Default to story1
    selected_story = stories[story_id]
    prompts = selected_story.prompts
    return render_template('home.html', prompts=prompts)

@app.route('/story')
def show_story():
    """Show the story with user input."""
    story_id = request.args.get('story')
    selected_story = stories[story_id]
    answers = request.args
    generated_story = selected_story.generate(answers)
    return render_template('story.html', story=generated_story)

if __name__ == '__main__':
    app.run(debug=True)
