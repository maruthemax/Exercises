def print_upper_words(words):
    """Print each word on separate line, uppercased.

        #: print_upper_words(["Programming", "is", "hard"])
        PROGRAMMING
        IS
        HARD
    """

    for word in words:
        print(word.upper())


def print_upper_words1(words):
    """Print each word on separate line, uppercased, if starts with E or e.

        #: print_upper_words2(["essence", "Engine"])
        ESSENCE
        ENGINE
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words2(words, must_start_with):
    """Print each word on separate line, uppercased, if starts with one of given

         #: print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                                must_start_with={"h", "y"})
        
        this should print "HELLO", "HEY", "YO", and "YES"
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
