# Declare characters used by this game.
define s = Character(_("Sylvie"), color="#c8ffc8")
define m = Character(_("Me"), color="#c8c8ff")

# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default book = False

# The game starts here.
label start:

    # Start by playing some music.
    play music "illurock.opus"

    scene bg lecturehall
    with fade

    "It's been 3 months since Surface Corp. Killed my parents"

    "I've decided i'm going to get revenge by dating them"

    menu : 

        "Which one should i date"
        "The girl":
            jump girl
        "The guy":
            jump later

    scene bg uni
    with fade

label girl:
    show sylvie green smile
    s "I'm the girl ceo."
