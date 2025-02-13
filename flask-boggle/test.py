from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def setUp(self):
        """Set up test client and configure app for testing."""
        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'test-secret-key'

    def test_homepage(self):
        """Test that the homepage loads correctly and initializes the board."""
        with self.client as client:
            response = client.get("/")
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<table id="board">', response.data)
            self.assertIn('board', session)
            self.assertEqual(len(session['board']), 5)
            self.assertEqual(len(session['board'][0]), 5)

    def test_check_word_valid(self):
        """Test word checking functionality for valid words."""
        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [
                    ['A', 'P', 'P', 'L', 'E'],
                    ['O', 'R', 'A', 'N', 'G'],
                    ['B', 'A', 'N', 'A', 'N'],
                    ['T', 'E', 'S', 'T', 'S'],
                    ['G', 'A', 'M', 'E', 'S']
                ]
            response = client.post("/check-word", json={"word": "APPLE"})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json["result"], "ok")

    def test_check_word_not_on_board(self):
        """Test word checking functionality for words not on the board."""
        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [
                    ['A', 'P', 'P', 'L', 'E'],
                    ['O', 'R', 'A', 'N', 'G'],
                    ['B', 'A', 'N', 'A', 'N'],
                    ['T', 'E', 'S', 'T', 'S'],
                    ['G', 'A', 'M', 'E', 'S']
                ]
            response = client.post("/check-word", json={"word": "BANANAS"})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json["result"], "not-on-board")

    def test_check_word_not_a_word(self):
        """Test word checking functionality for invalid dictionary words."""
        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [
                    ['A', 'P', 'P', 'L', 'E'],
                    ['O', 'R', 'A', 'N', 'G'],
                    ['B', 'A', 'N', 'A', 'N'],
                    ['T', 'E', 'S', 'T', 'S'],
                    ['G', 'A', 'M', 'E', 'S']
                ]
            response = client.post("/check-word", json={"word": "XYZ"})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json["result"], "not-a-word")

    def test_post_score(self):
        """Test posting a score and updating statistics."""
        with self.client as client:
            with client.session_transaction() as sess:
                sess['games_played'] = 0
                sess['high_score'] = 10

            response = client.post("/post-score", json={"score": 15})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json["high_score"], 15)
            self.assertEqual(response.json["games_played"], 1)

            with client.session_transaction() as sess:
                self.assertEqual(sess['high_score'], 15)
                self.assertEqual(sess['games_played'], 1)

    def test_post_score_lower_than_high_score(self):
        """Test posting a score lower than the current high score."""
        with self.client as client:
            with client.session_transaction() as sess:
                sess['games_played'] = 1
                sess['high_score'] = 20

            response = client.post("/post-score", json={"score": 10})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json["high_score"], 20)
            self.assertEqual(response.json["games_played"], 2)

            with client.session_transaction() as sess:
                self.assertEqual(sess['high_score'], 20)
                self.assertEqual(sess['games_played'], 2)