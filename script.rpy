# Declare characters used by this game.
define s = Character(_("Sylvie"), color="#c8ffc8")
define m = Character(_("Me"), color="#c8c8ff")
define unknown = Character(_("???"), color="#ffffff")
define c = Character(_("CEO"), color="#b46fbc") 

default screen_width = 1920 
default screen_height = 1080

    # Define a default transform to apply to all images
transform fit:
    xysize (screen_width, screen_height)
    fit "contain" 

default player_name = "Player"

default ceo_name = "idk"
default ceo_gender = "f"
default he = "he"
default him = "him"
default his = "her"

default challenge1_badend = False



# The game starts here.
label start:

    # Start by playing some music.
    play music "illurock.opus"

    $ player_name = renpy.input("What is your name?", default=player_name, length=20)
    # The strip() method removes leading/trailing whitespace
    $ player_name = player_name.strip()

        # Check if the input is empty and prompt again if necessary (optional)
    if not player_name:
        $ player_name = "Player" # Set a fallback name
    
    # Define a character using the entered name
    define pc = Character("[player_name]")

    scene bg blackscreen
    with fade
    unknown "... I heard Surface Corp. is embezzling funds..."
    unknown "... I know right! They are so greedy..."
    pc "These are the rumours that have been going around."

    scene bg lecturehall
    with fade
    pc "Which is why I have to uncover what's going on!"
    pc "I'm going to go into the company and get close to the CEO's..."
    pc "And take down the company for good!"

    pc "Today I'm starting my first day as an intern at Surface Corp. I'd better hurry and not be late."

    scene bg office
    with fade
    show sylvie blue smile
    s "Hello! "
    show sylvie blue normal
    extend "You must be [player_name]."
    s "Are you here for your first day?"
    show sylvie blue giggle
    s "Well then, you better see the CEO to get set up."
    pc "Yes ma'am. "
    extend "(Yes! This is my chance!)"
    show sylvie blue normal
    s "You're lucky, because both the CEO's happen to be free today!"
    show sylvie blue smile
    s "So.."
    menu:
        s "Who do you want to see first?"
        "Girl CEO":
            $ ceo_name = "Girl name"
            $ ceo_gender = "f"
            $ he = "she"
            $ his = "her"
            $ him = "her"
        "Guy CEO":
            $ ceo_name = "Guy name"
            $ ceo_gender = "m"
            $ he = "he"
            $ his = "his"
            $ him = "him"

    show sylvie blue normal
    s "Hmm. Alright!"
    show sylvie blue normal at right with move 
    "Sylvie then walks me to an important-looking office."
    s "Here you are."
    show sylvie blue smile
    s ".. Good luck!"

    scene bg blackscreen with fade
    pc "(I knock on the door.)"
    jump challenge_1
label challenge_1:
    "Challenge 1: {nw}" with hpunch
    extend "First impression" with hpunch
    unknown "Come in."
    scene bg ceooffice with fade
    show expression "[ceo_gender] normal"
    "You walk in to see the CEO, looking at you like you're walking trash."
    menu:
        c "What do you want?"
        "Hello. I'm here to check in as the new intern.":
            c "Oh.{w=0.5} Right. {w=0.5}You must be [player_name]."
            c "Well, {w=0.5}you're dismissed."

        "What I want? Only you, babygirl.":
            c "..."
            c "What the hell?"
            c "Get out."
            scene bg blackscreen
            "You get instantly fired, and get blacklisted from half the jobs in your city."
            jump bad_ending
    menu: 
        pc "(That was quick!{w=1.0} Maybe [he]'s just playing hard to get..)" with vpunch
        "How do you suggest I can be of value to this company?":
            c "I said, {w=0.5}{nw}"
            extend "you're dismissed." with hpunch
            pc "(Oops..)"
            jump challenge_1_badend

        "Leave it be":
            pc "(I should just leave it be.)"
            pc "Thank you. I hope I can be of value to this company."
            c "I hope so too."
            jump challenge_1_goodend

label challenge_1_goodend:
    scene bg office with fade
    "You exit the office."
    pc "(I think that went pretty well.)"
    "You go on with the rest of your day, and go to sleep in hopes of a good day tomorrow!"
    scene bg blackscreen with fade
    jump challenge_2

label challenge_1_badend:
    $ challenge1_badend = True
    "You exit the office."
    scene bg office with fade
    pc "(That could have went better..)"
    "You go on with the rest of your day, and go to sleep hoping you do better tomorrow."
    scene bg blackscreen with fade
    jump challenge_2

    
label challenge_2:
    "Challenge 2: {nw}" with hpunch
    extend "Impress the CEO!" with hpunch
    scene bg office with fade
    "You rush into work with a huge stack of paperwork, after doing them all in one night, all in order to make a good impression."
    pc "(Today, I need to make [ceo_name] fall in love with me!)"
    pc "{fast}(I just need to show how hardworking and attractive I am, find out all the secrets, and.. {nw})"
    show expression "[ceo_gender] normal" with vpunch
    c "Ugh!"
    "You bump into [ceo_name], and papers fly everywhere."
    show expression "[ceo_gender] angry" with vpunch
    c "Hey! Watch where you're going."
    pc "(Oh no.. I've screwed up..)"
    show expression "[ceo_gender] normal"
    "[ceo_name] begins picking up some of the papers from the ground and inspecting them."
    c "Wait.."
    c "Are these all.. Finished?"
    menu: 
        c "You did this all in one night?"
        "Yes, I did.":
            show expression "[ceo_gender] smirk"
            if (challenge1_badend):
                c "Hm."
                c "Well.. That's the least you could do."
                menu: 
                    "Well, then what does someone like you do every day?":
                        c "What? Well, I do stuff far more important than talking to you."
                        show expression "[ceo_gender] normal"
                        c "Hey. "
                        show expression "[ceo_gender] angry"
                        extend "How dare you say that to your boss?" with hpunch
                        show expression "[ceo_gender] normal"
                        menu: 
                            c "Don't you know you can get fired?" 
                            "I would rather get fired than not stand up for myself and stay.":
                                c ".. Hmm."
                                show expression "[ceo_gender] smirk"
                                c "Well said."
                                hide expression "[ceo_gender] smirk" with dissolve
                                "With that, [ceo_name] walks away, and you continue with your day."
                            "I'm sorry boss. It won't happen again.":
                                pc "(Oh no! I got too bold!)"
                                c ".. Ugh."
                                show expression "[ceo_gender] angry"
                                c "What a pushover. After that? You're fired."
                                scene bg blackscreen with fade
                                "You get kicked out, and you leave after only one day at the company..."
                                jump bad_ending
            else:
                c "Hm. Not bad."
                c "Keep it up."
    scene bg blackscreen with fade
    "During lunch break.."
    scene bg office with fade
    show expression "[ceo_gender] normal" with dissolve
    "You stroll up and take a seat across from the CEO."
    pc "Hey! Didn't know I'd meet you here. Today's busy, huh?"
    c "Yeah."
    pc "(Jeez! At least try to make conversation!)" with vpunch
    pc "Do you know who I am?"
    pc "Do you know my name?" with vpunch
    pc "{fast}I'm the worker that submitted all that work this morning, remember? {nw}" with vpunch
    extend "{fast}Are you impressed?" with vpunch
    c "... Mhm. "
    extend "(.. So annoying.. Do you ever shut up?)" with vpunch
    pc "Yeah, I know you must be impressed by my great work!"
    pc "By the way, [ceo_name]... Do you have a girlfriend yet?"
    c "... No. Of course not. what are you asking?"
    menu: 
        pc "Ha! You're finally talking.. So hard to get words out of your mouth.."
        "... What's your type?":
            pc "{fast}What's your type? Anyone you like or have liked before? Do you like guys, or girls?"
            show expression "[ceo_gender] angry"
            c "Eat quickly and go do your work! "
            show expression "[ceo_gender] normal"
            extend "(What the heck?)"
            c "(Huh... {w=0.5}It's not just my grandma urging me to find a partner anymore...)"
            c "(Instead of an arranged marriage... {w=0.5}Maybe I should really consider...{nw}"
            show expression "[ceo_gender] normal" with vpunch
            pc "Did you say something?"
            show expression "[ceo_gender] angry" 
            c "What? No! Ugh.. {nw}" 
            extend "Get back to work, now!!" with vpunch
        "... Since you answered.. What do you think of me?":
            c "..."
            show expression "[ceo_gender] angry"
            c "You're not my type." with vpunch
            pc "What do you think I can do better? Working hard? Helping out?? Different style?"
            show expression "[ceo_gender] normal"
            c "If you really want to do something for me, {nw}"
            show expression "[ceo_gender] angry"
            extend "get out of my sight, now! " with vpunch
            show expression "[ceo_gender] normal"
            extend "(Ugh! Why am I spending time answering this nonsense?)"
            c "(Huh... {w=0.5}But... They do seem very hardworking...){nw}"
            pc "Did you say something?"
            show expression "[ceo_gender] angry" 
            c "What? No! Ugh.. {nw}"
            extend "Break is over! Get back to work!" with vpunch

    scene bg blackscreen with fade
    "With that, you finish your meal and continue on with your duties.."
    "But [ceo_name] seems to be warming up to you!"
    pc "(Now, I just need to get more information...)"
    $renpy.pause(1.0)

label challenge_3:
    "Challenge 3: " with hpunch
    extend "Get [his] attention.." with hpunch

label challenge_4:
    "Challenge 4: DATE!"
label challenge_5:
    "Challenge 5: Lock in "


        

label bad_ending:
    scene lose
    $ renpy.pause()
    $ renpy.full_restart()# Declare characters used by this game.
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
