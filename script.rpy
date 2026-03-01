# Declare characters used by this game.
define s = Character(_("Assistant"), color="#c8ffc8")
define unknown = Character(_("???"), color="#ffffff")
define c = DynamicCharacter(_('ceo_name'), color="#b46fbc") 

transform custom_default_transform:
    # Your desired transform properties here, e.g.,
    xalign 0.5
    yalign 1.0
    zoom 1.5

default player_name = "Player"

default ceo_name = "idk"
default ceo_gender = "f"
default he = "he"
default him = "him"
default his = "her"

default challenge1_badend = False



# The game starts here.
label start:
    $ config.default_transform = custom_default_transform
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
    unknown "... Did you hear Surface Corp. is cutting health research funding..?"
    unknown "... I know! They are just so greedy..."
    pc "These are the rumours that have been going around."

    scene bg lecturehall
    with fade
    pc "Which is why I have to uncover what's going on!"
    pc "I'm going to go into the company and get close to the CEO..."
    pc "And take down the company for good!"

    pc "Today I'm starting my first day as an intern at Surface Corp. I'd better hurry and not be late."

    scene bg office
    with fade
    show sylvie blue smile
    s "Hello! "
    show sylvie blue normal
    extend "You must be [player_name]."
    menu:
        s "Are you here for your first day?"
        "Yep!":
            show sylvie blue giggle
            s "Well then, "
            show sylvie blue smile
            extend "you better see the CEO to get set up."
            show sylvie blue normal
    pc "Yes ma'am. "
    extend "(Yes! This is my chance!)"
    show sylvie blue giggle
    s "You're lucky, because both the CEO's happen to be free today!"
    show sylvie blue smile
    s "So.."
    menu:
        s "Who do you want to see first?"
        "Camilla Emma O'Leary":
            $ ceo_name = "Camilla"
            $ ceo_gender = "f"
            $ he = "she"
            $ his = "her"
            $ him = "her"
        "Calvin Ezra Osborn":
            $ ceo_name = "Calvin"
            $ ceo_gender = "m"
            $ he = "he"
            $ his = "his"
            $ him = "him"

    show sylvie blue normal
    s "Hmm. Alright!"
    show sylvie blue normal at right with move 
    "The assistant then walks me to an important-looking office."
    s "Here you are."
    show sylvie blue smile
    s ".. Good luck!"

    scene bg blackscreen with fade
    pc "(I knock on the door.)"
    jump challenge_1
label challenge_1:
    "Challenge 1: {nw}" with hpunch
    extend "{cps=5}First impression{/cps}" with hpunch
    unknown "Come in."
    scene bg ceooffice with fade
    show expression "[ceo_gender] normal"
    "You walk in to see the CEO, looking at you like you're walking trash."
    menu:
        c "What do you want?"
        "Hello. I'm here to check in as the new intern.":
            show expression "[ceo_gender] angry"
            c "Oh.{w=0.5} Right. {w=0.5}You must be [player_name]."
            show expression "[ceo_gender] normal"
            c "Well, {w=0.5}you're dismissed."

        "What I want? Only you, babygirl.":
            c "..."
            c "What the hell?"
            c "Get out." with vpunch
            scene bg blackscreen
            "You get instantly fired, and get blacklisted from half the jobs in your city."
            jump bad_ending
    menu: 
        pc "(That was quick!{w=1.0} Maybe [he]'s just playing hard to get..)" with vpunch
        "How do you suggest I can be of value to this company?":
            show expression "[ceo_gender] angry"
            c "I said, {w=0.5}{nw}"
            show expression "[ceo_gender] normal"
            extend "you're dismissed." with hpunch
            pc "(Oops..)"
            jump challenge_1_badend
        "What does this company do?":
            c "You should know that already if you're working here."
            c "But, we fund research."
            pc "(Then why did you {nw}"
            extend "stop {nw}" with hpunch
            extend "funding health research?)"
            pc "I see. Thanks for your time."
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
    extend "{cps=5}Impress the CEO!{/cps}" with hpunch
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
                        show expression "[ceo_gender] normal"
                        c "What?"
                        show expression "[ceo_gender] smirk"
                        "Well, I do stuff far more important than talking to you."
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
                                pc ".. I'm sorry.. It won't happen again. "
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
    show expression "[ceo_gender] angry"
    c "... No. {nw}"
    show expression "[ceo_gender] normal"
    extend "Of course not. What are you asking?"
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
            c "(Huh... {w=0.5}But... They do seem very hardworking... Unlike that arranged partner..){nw}"
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
    extend "{cps=5}Get [his] attention..{/cps}" with hpunch

    scene bg office with fade
    "As soon as you walk into work, there's a crowd of your fellow coworkers huddled up."
    unknown "Hey! [player_name]! Come here. Got any gossip?"
    menu:
        pc "(Ooh! I love some gossip!)"
        "Talk about the company":
            pc "(I want to expose this scummy company. They deserve to know!)"
            pc "You guys heard right? The CEO is going to cut our salaries in half next week!"
            pc "You all work so hard, and he's trying to underpay us.."
            show expression "[ceo_gender] smirk" with dissolve
            c "... *Ahem*..." with vpunch
            show expression "[ceo_gender] angry" 
            c "[player_name]! Come to my office! Now!" with vpunch
            "You've messed up."
            scene ceooffice with fade
            show expression "[ceo_gender] normal" 
            c "Hmph. {w=0.5}{nw}"
            show expression "[ceo_gender] smirk" 
            extend "'Reducing salaries'? Where did you get that from?"
            pc "Ugh.. You can't tell that everyone hates you? Playing dumb huh?" with vpunch
            show expression "[ceo_gender] angry" 
            c "Hey! How dare you speak like this to your boss!" with vpunch
            "You throw all your papers onto the desk and leave." with vpunch
            jump bad_ending
        "Talk about his personal life":
            pc "(I wanna expose this scummy CEO.)"
            pc " Did you guys know the CEO has a wife? I can't believe that a cold-blooded human has a WIFE."
            show expression "[ceo_gender] smirk" with dissolve
            c "... *Ahem*..." with vpunch
            show expression "[ceo_gender] angry" 
            c "[player_name]! Come to my office! Now!" with vpunch
            "You've messed up."
            scene ceooffice with fade
            show expression "[ceo_gender] angry"
            c "Huh, wife? Cold-blooded? Where on EARTH did you get all that from?"
            pc "Well.. You can't tell that everyone hates you? Playing dumb huh?" with vpunch
            show expression "[ceo_gender] angry" 
            "You throw all your papers onto the desk and leave." with vpunch
            jump bad_ending
        "Don't gossip":
            pc "(I don't wanna get on [ceo_name]'s bad side..)"
            show expression "[ceo_gender] normal" with dissolve
            "Perfect timing! [ceo_name] walks up up to you with a serious expression."
            c "You. {w=0.5}Show me the paperwork you've done. And you, {w=0.5}{nw}"
            show sylvie blue normal at right with move
            extend "([ceo_name] turns to [his] assistant), bring me some tea."
            hide sylvie blue normal with dissolve
            "The assistant rushes off while you organize your carefully written papers."
            pc "It's all here, boss!"
            show expression "[ceo_gender] angry"
            c "Good."
            show expression "[ceo_gender] normal" 
            extend "Hmm.."
            show expression "[ceo_gender] smirk"
            c "Not bad. Not what I expected from you."
            menu:
                "Thank you.":
                    "Before you can say anything else, you hear a crash, and a horrible burning sensation on your hands!"
                    show sylvie blue surprised at right with dissolve
                    show expression "[ceo_gender] angry"
                    "You see the assistant, looking panicked, and tea all over the floor."
                    s "Ahh! I'm so sorry!" with vpunch
                    menu: 
                        "Run away and treat the wound immediately!":
                            show expression "[ceo_gender] normal"
                            c "What? Wait! Where are you going? Ugh.."
                            scene bg blackscreen with fade
                            "What did you seriously think would happen!"
                            "You try to repair your relationship with the CEO after, but no matter what, [he] stays distant."
                            jump bad_ending
                        "Tough it out and risk looking stupid":
                            hide sylvie blue surprised with dissolve
                            show expression "[ceo_gender] normal"
                            c "Are you okay?"
                            pc "Yes. I'm okay. Please execuse me."
                            "You feel like your hands are melting off!" with vpunch
                            show expression "[ceo_gender] angry"
                            c "Wait! "
                            show expression "[ceo_gender] normal"
                            extend "Let me take a look."
                            pc "(It hurts so much! But I need to bare this for my mission..)"
                            "You try to act courteous."
                            pc "Noooo.. It's fine.."
                            show expression "[ceo_gender] angry"
                            c "No. Let me take a look." with vpunch
                            show expression "[ceo_gender] normal"
                            "[ceo_name] grabs your hand."
                            "You act shy hoping [he] falls for it."
                            show expression "[ceo_gender] angry"
                            c "Sit down."
                            show expression "[ceo_gender] normal" at left with move
                            "Grabbing your hand, [he] walks to grab the first aid kit and begins to apply ointment."
                            show expression "[ceo_gender] angry"
                            c "Your hand is red. {nw}"
                            show expression "[ceo_gender] normal"
                            extend "Does it hurt?"
                            pc "Yeah.. It hurts. You're pressing too hard."
                            c "..."
                            c ".. I'm sorry.{w=0.5} I'll be more careful."
                            scene bg blackscreen with fade
                            c "{cps=10}(Why do I care so much about how they feel?){/cps}"
            pc "[ceo_name] is acting nice, but... I can't forget what they did.."
            "You feel like you two have grown a lot closer!"
            $renpy.pause(1.0)
            jump challenge_4

label challenge_4:
    "Challenge 4: " with hpunch
    extend "{cps=5}Date!{/cps}" with hpunch

    scene bg office with fade
    "Today, as soon as you walk into the office..."
    show expression "[ceo_gender] normal" with dissolve
    c "See me in my office. "
    show expression "[ceo_gender] angry"
    extend "Now."

    pc "(What? {nw}" with vpunch
    extend "Did I do something? {nw}" with vpunch
    extend "Is [he] onto me?)" with vpunch

    show expression "[ceo_gender] normal"
    c "What are you doing? I said {w=0.5}{nw}"
    show expression "[ceo_gender] angry"
    c "now!" with vpunch

    scene bg blackscreen with fade
    "You walk to his office."
    scene bg ceooffice with fade
    show expression "[ceo_gender] normal"
    $renpy.pause()
    show expression "[ceo_gender] angry"
    c "Are you free tonight?"
    show expression "[ceo_gender] normal"
    pc "What?" with vpunch
    pc "No, I'm not.. "
    extend "(Is [he] asking me to work overtime?)"
    c "No. That's not your decision to make."
    show expression "[ceo_gender] angry"
    menu:
        c "That's an order from me."
        "No. I'm busy.":
            c "Hm."
            scene bg blackscreen with fade
            jump flashback
            scene bg ceooffice with fade
            show expression "[ceo_gender] normal" with dissolve
            c "Okay. I understand.."
            "[ceo_name] leaves your office without another word."
            "You feel as though you've done something wrong.."
            jump bad_ending
        "Okay. It's a date!"
            c "(Phew...)"
            pc "Something wrong?"
            c "No. I'll send you an address. Be there at 6."
            pc "Right..."
    scene bg blackscreen with fade
    "You go on with your day as usual, but receive [his] text message with an address."
    "You click on it, and it's.. A restaurant!"
    pc "(Huh? A restaurant? Do we have a special guest or something?)"
    scene bg street with fade
    "You manage to find your way to the address, walking into the restaurant. It's high end, way out of your pay grade. You hope [he] is paying.."
    "You find [ceo_name], and go over to [him]."
    show expression "[ceo_gender] normal" with dissolve
    pc "Hey. Sorry for the wait."
    c "Don't worry. I wasn't waiting long."
    c "(I came 30 minutes early. " with vpunch
    extend "Spent 20 minutes doing my hair and choosing my clothes. " with vpunch
    extend "I even bought exotic flowers from France with overnight air shipping and a 2000% rush fee..)" with vpunch
    c "(I wonder if it's enough..?)"
    pc "Are we waiting on someone?"
    c "No. It's just me and you."
    pc "(Huh?)"
    pc "(Wait.. This is.. An actual date?)"
    "The waiter comes up and asks for your orders."
    c "We want two Truffle Caviar Wagyu a5 Gold steaks please."
    pc "We? No, it's fine.. {w=0.5}{nw}"
    extend "(Because I don't have that kind of money!)" with vpunch
    c "No. I insist."
    define waiter = Character("Waiter")
    waiter "Alrighty then! Two Truffle Caviar Wagyu a5 Gold steaks coming up."
    c "So.."
    c "What do we talk about?"
    menu:
        pc "(This is my chance!)"
        "Ask about [his] family.":
            c "My family..."
            jump flashback
            pc "Oh.. I see."
            pc "(So that's why [he] asked me out.)"

        "Ask [his] favourite colour.":
            c "My favourite colour?"
            c "I guess I like the colour blue."

        "Ask about why they cut the funding...":
            c "What?"
            c "You're just like all the other people from the media..."
            c "You didn't care about me at all!"
            pc "(I screwed up!)"
            menu:
                "I do care!":
                    c "Fine. Prove it."
            menu:
                c "What is my favourite colour?"
                "Blue": 
                    c "Hm.. So you do know."
                "Purple": 
                    c "You don't even know my favourite colour!"
                    "You messed up..."
                    "Try making some small talk first!"
                    jump bad_ending

                "Green": 
                    c "You don't even know my favourite colour!"
                    "You messed up..."
                    "Try making some small talk first!"
                    jump bad_ending
            menu:
                c "Hmmm.. Fine."
                c "We were investing money into an expiremental treatment instead."
                c "Is that what you wanted to hear? You just came to find what's under the surface and sell out to the media?"
                menu:
                    "Yes":
                        c "I knew it."
                        jump sellout
                    "No":
                        c "What? Really?"
                        jump date


label flashback:
    unknown "[ceo_name]. You need to hurry and get married to continue the family name."
    unknown "We've already arranged someone for you."
    unknown "You know time is running out. If you don't have anyone else in mind, we're going to go through with this."
    c "No... "
    extend "I do have someone in mind."

label sellout:
    scene bg blackscreen with fade
    "You sell the information you found to the highest bidder."
    "Now, you're worth a fortune!"

    scene bg street with fade
    waiter "Good evening. What will it be?"
    pc "One Truffle Caviar Wagyu a5 Gold steak, please."
    waiter "Coming right up."
    scene bg blackscreen with fade
    unknown "Ugh. How can someone get so rich?"
    unknown "I wish I could see under the surface of all these rich people..."

label date:
    scene bg blackscreen with fade
    "You and [ceo_name] talk it out, and you end up getting together."
    "Today, you find yourself in a familiar place."
    scene bg street with fade
    c "Happy five year anniversary."
    pc "Yeah. Happy anniversary."
    waiter "Hello. The usual?"
    c " Yes please."
    scene bg blackscreen with fade

label bad_ending:
    image bg lose:
        "bg lose.jpg"
        xysize (1080, 920) # Target screen resolution
        fit "cover"
    window hide
    show bg lose with fade
    $ renpy.pause()
    $ renpy.full_restart()# Declare characters used by this game.
define s = Character(_("Sylvie"), color="#c8ffc8")
define m = Character(_("Me"), color="#c8c8ff")
define unknown = Character(_("???"), color="#ffffff")
define c = Character(_("CEO"), color="#b46fbc") 

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

    show sylvie green smile
    s "I'm the girl ceo."
