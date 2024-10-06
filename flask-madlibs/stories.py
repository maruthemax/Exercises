"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

# Story 1: A Fairy Tale
story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

# Story 2: A Day at the Park
story2 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """One sunny day at the {place}, a {adjective} {noun} decided to {verb} 
       with some {plural_noun}."""
)

# Story 3: A Funny Adventure
story3 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """In the strange land of {place}, there was a {adjective} {noun} 
       that loved to {verb} all kinds of {plural_noun}."""
)

# Dictionary to store the stories
stories = {
    "story1": story1,
    "story2": story2,
    "story3": story3
}