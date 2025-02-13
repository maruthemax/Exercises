from flask import Flask, render_template, request, jsonify, session
from boggle import Boggle

app = Flask(__name__)
app.secret_key = "your-secret-key"

# Initialize Boggle instance
boggle_game = Boggle()

@app.route("/")
def homepage():
    """Display the Boggle game board."""
    board = boggle_game.make_board()
    session["board"] = board
    session["games_played"] = session.get("games_played", 0)
    session["high_score"] = session.get("high_score", 0)
    return render_template("index.html", board=board)

@app.route("/check-word", methods=["POST"])
def check_word():
    """Check if the submitted word is valid."""
    word = request.json["word"]
    board = session["board"]
    result = boggle_game.check_valid_word(board, word)
    return jsonify({"result": result})

@app.route("/post-score", methods=["POST"])
def post_score():
    """Update the score and statistics."""
    score = request.json["score"]
    session["games_played"] += 1
    session["high_score"] = max(score, session["high_score"])
    return jsonify({"high_score": session["high_score"], "games_played": session["games_played"]})

if __name__ == "__main__":
    app.run(debug=True)
