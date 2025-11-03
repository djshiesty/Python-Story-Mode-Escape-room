import os
import sys
import time
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def try_again():
    clear()
    print("Invalid choice. Please try again.")
    input("Press Enter to continue...")
    clear()

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        print(f"Time remaining: {timer}", end='\r')
        time.sleep(1)
        seconds -= 1
    clear()
    print("Time’s up! You failed to escape.")
    sys.exit()

def Escape_restart():
    clear()
    print("Do you want to restart the game? (Y/N)")
    Option_1 = input(": ")
    if Option_1.upper() == 'N':
        print("Thanks for playing!")
        sys.exit()
    elif Option_1.upper() == 'Y':
        Escape_room_beginning()
    else:
        try_again()
        Escape_restart()

def Escape_room_beginning():
    clear()
    print("6 AM. You wake up in a white room. There are two other people in the room with you. One of them is dead. The other is alive, but malnourished. The clock ticks away. You have 10 minutes to figure out what to do.")
    print("Do you want to begin the game? (Y/N)")
    Option_1 = input(": ")
    if Option_1.upper() == 'N':
        Escape_restart()
    elif Option_1.upper() == 'Y':
        print("The timer starts now.")
        time.sleep(1)
        countdown(60)
        Escape_room_1()
    else:
        try_again()
        Escape_room_beginning()

def Escape_room_1():
    clear()
    print("You look around the room. There is a safe, a note, and a computer. What do you want to do?")
    print("A. Check the safe")
    print("B. Read the note")
    print("C. Check the computer")
    Option_1 = input(": ")
    if Option_1.upper() == 'A':
        Escape_room_1_safe()
    elif Option_1.upper() == 'B':
        Escape_room_1_note()
    elif Option_1.upper() == 'C':
        Escape_room_1_computer()
    else:
        try_again()
        Escape_room_1()

def Escape_room_1_safe():
    clear()
    print("The safe is locked. You need a code to open it.")
    code = "Don't Break"
    guess = input("Enter the code: ")
    if guess == code:
        print("The safe opens. You find a key.")
        input("Press Enter to continue...")
        clear()
        print("The timer stops. You have escaped Room 1.")
        input("Press Enter to continue...")
        escape_room_2()
    else:
        print("Incorrect code.")
        input("Press Enter to continue...")
        Escape_room_1()

def Escape_room_1_note():
    clear()
    print("The note says: Gjstu xpse jt Epo’u. You need to figure out what it means.")
    input("Press Enter to continue...")
    Escape_room_1()

def computer_quiz():
    clear()
    print("To unlock the computer, you must pass a short quiz.\n")

    #Multiple choice Science Questions
    science_questions = [
        {
            "question": "Which planet is known as the Red Planet?",
            "choices": ["A. Mars", "B. Venus", "C. Jupiter", "D. Mercury"],
            "answer": "A"
        },
        {
            "question": "What gas do plants absorb from the atmosphere?",
            "choices": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Helium"],
            "answer": "B"
        },
        {
            "question": "Which organ in the human body filters blood?",
            "choices": ["A. Heart", "B. Liver", "C. Kidney", "D. Lungs"],
            "answer": "C"
        },
        {
            "question": "What is the chemical formula of table salt?",
            "choices": ["A. H2O", "B. CO2", "C. NaCl", "D. C6H12O6"],
            "answer": "C"
        },
        {
            "question": "Which of the following is NOT a noble gas?",
            "choices": ["A. Argon", "B. Neon", "C. Oxygen", "D. Helium"],
            "answer": "C"
        }
    ]

    #Multiple choice Algebra Questions
    algebra_questions = [
        {
            "question": "Solve for x: 2x + 6 = 14",
            "choices": ["A. 4", "B. 5", "C. 3", "D. 6"],
            "answer": "A"
        },
        {
            "question": "Simplify: (x^2 + 2x + 1)",
            "choices": ["A. x^2+1", "B. (x+1)^2", "C. (x+2)^2", "D. x(x+2)"],
            "answer": "B"
        },
        {
            "question": "If f(x) = 3x + 2, what is f(4)?",
            "choices": ["A. 12", "B. 14", "C. 10", "D. 16"],
            "answer": "B"
        },
        {
            "question": "Factor: x^2 + 5x + 6",
            "choices": ["A. (x+2)(x+3)", "B. (x+1)(x+6)", "C. (x+3)(x+4)", "D. (x+1)(x+5)"],
            "answer": "A"
        },
        {
            "question": "Solve: x^2 - 9 = 0",
            "choices": ["A. ±3", "B. 3", "C. -3", "D. 0"],
            "answer": "A"
        }
    ]

    #Multiple choice English Questions
    english_questions = [
        {
            "question": (
                "Although the author’s tone throughout the passage is generally one of restrained admiration, "
                "his subtle critique of the subject’s methodology suggests that he regards her conclusions as _____."
            ),
            "choices": [
                "A. groundbreaking yet hastily constructed",
                "B. meticulous and logically irrefutable",
                "C. intellectually rigorous though somewhat inaccessible",
                "D. ambitious but ultimately unsound"
            ],
            "answer": "D"
        },
        {
            "question": (
                "In the context of the passage, the phrase 'an illusion of certainty' (line 47) most nearly serves to "
                "underscore the author’s view that scientific progress is often accompanied by _____."
            ),
            "choices": [
                "A. an overestimation of empirical precision",
                "B. a justified sense of intellectual triumph",
                "C. the decline of philosophical reasoning",
                "D. skepticism toward quantitative analysis"
            ],
            "answer": "A"
        },
        {
            "question": (
                "The narrator’s reflection that 'truth, when spoken too soon, is but a whisper lost in a storm' primarily "
                "emphasizes his belief that _____."
            ),
            "choices": [
                "A. society often fails to recognize insight until it is convenient",
                "B. honesty is a virtue best reserved for private contemplation",
                "C. wisdom can only emerge through the passage of time",
                "D. the nature of truth is inherently unknowable"
            ],
            "answer": "A"
        },
        {
            "question": (
                "By contrasting 'the thunder of rhetoric' with 'the whisper of reason,' the author most likely intends to _____."
            ),
            "choices": [
                "A. expose the futility of emotional argument",
                "B. criticize the use of persuasive appeals in politics",
                "C. highlight the quiet power of rational discourse",
                "D. question the legitimacy of intellectual debate"
            ],
            "answer": "C"
        }
    ]

    #Select 1 question from each category
    chosen_questions = [
        random.choice(science_questions),
        random.choice(algebra_questions),
        random.choice(english_questions)
    ]

    score = 0
    for q in chosen_questions:
        clear()
        print(q["question"])
        for choice in q["choices"]:
            print(choice)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['answer']}")
        time.sleep(1.5)

    clear()
    if score == 3:
        print("Excellent! You passed the quiz! The second word is: Break.")
        input("Press Enter to continue...")
        return True
    else:
        print("You failed the quiz. Try again.")
        input("Press Enter to retry...")
        return computer_quiz()



def Escape_room_1_computer():
    clear()
    print("The computer is locked. You need a password to open it. To get the password, you need to solve the following quiz:")
    computer_quiz()
    Escape_room_1()

def escape_room_2():
    clear()
    print("You take the key, unlocking the door to reveal a hallway. You see two doors at the end of the hallway. One red and one blue. One leads to a forest, the other to a desert. Which door do you want to open?")
    print("A. Open the Red door")
    print("B. Open the Blue door")
    Option_1 = input(": ")
    if Option_1.upper() == 'A':
        print("You open the red door and find yourself in a forest. You see a path leading to a cave. Do you want to go to the cave? (Y/N)")
        Option_1 = input(": ")
        if Option_1.upper() == 'Y':
            print("You go to the cave and find a Labyrinth.")
            input("Press Enter to continue...")
            Labyrinth()
        elif Option_1.upper() == 'N':
            print("You decide not to go to the cave and go back to the hallway. You see a note on the floor. It says: You have made the wrong choice. You die.")
            input("Press Enter to continue...")
            Escape_room_1()
        else:
            try_again()
            escape_room_2()

    elif Option_1.upper() == 'B':
        print("You open the blue door and find yourself in a desert. You see a path leading to an oasis, the other to a village. Do you want to go to the oasis or the village?")
        Option_1 = input(": ")
        if Option_1.upper() == 'OASIS':
            print("You go to the oasis and find a treasure chest. You open it and find a map. The map leads to a Portal.")
            input("Press Enter to continue...")
            fake_portal()
        elif Option_1.upper() == 'VILLAGE':
            Village_sequence()
        else:
            try_again()
            escape_room_2()
    else:
        try_again()
        escape_room_2()

def Labyrinth_computer_quiz():
    clear()
    print("To unlock the computer, you must pass a short quiz.\n")

    #Multiple choice Science Questions
    science_questions = [
        {
            "question": "Which planet is known as the Red Planet?",
            "choices": ["A. Mars", "B. Venus", "C. Jupiter", "D. Mercury"],
            "answer": "A"
        },
        {
            "question": "What gas do plants absorb from the atmosphere?",
            "choices": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Helium"],
            "answer": "B"
        },
        {
            "question": "Which organ in the human body filters blood?",
            "choices": ["A. Heart", "B. Liver", "C. Kidney", "D. Lungs"],
            "answer": "C"
        },
        {
            "question": "What is the chemical formula of table salt?",
            "choices": ["A. H2O", "B. CO2", "C. NaCl", "D. C6H12O6"],
            "answer": "C"
        },
        {
            "question": "Which of the following is NOT a noble gas?",
            "choices": ["A. Argon", "B. Neon", "C. Oxygen", "D. Helium"],
            "answer": "C"
        }
    ]

    #Multiple choice Algebra Questions
    algebra_questions = [
        {
            "question": "Solve for x: 2x + 6 = 14",
            "choices": ["A. 4", "B. 5", "C. 3", "D. 6"],
            "answer": "A"
        },
        {
            "question": "Simplify: (x^2 + 2x + 1)",
            "choices": ["A. x^2+1", "B. (x+1)^2", "C. (x+2)^2", "D. x(x+2)"],
            "answer": "B"
        },
        {
            "question": "If f(x) = 3x + 2, what is f(4)?",
            "choices": ["A. 12", "B. 14", "C. 10", "D. 16"],
            "answer": "B"
        },
        {
            "question": "Factor: x^2 + 5x + 6",
            "choices": ["A. (x+2)(x+3)", "B. (x+1)(x+6)", "C. (x+3)(x+4)", "D. (x+1)(x+5)"],
            "answer": "A"
        },
        {
            "question": "Solve: x^2 - 9 = 0",
            "choices": ["A. ±3", "B. 3", "C. -3", "D. 0"],
            "answer": "A"
        }
    ]

    #Multiple choice English Questions
    english_questions = [
        {
            "question": (
                "Although the author’s tone throughout the passage is generally one of restrained admiration, "
                "his subtle critique of the subject’s methodology suggests that he regards her conclusions as _____."
            ),
            "choices": [
                "A. groundbreaking yet hastily constructed",
                "B. meticulous and logically irrefutable",
                "C. intellectually rigorous though somewhat inaccessible",
                "D. ambitious but ultimately unsound"
            ],
            "answer": "D"
        },
        {
            "question": (
                "In the context of the passage, the phrase 'an illusion of certainty' (line 47) most nearly serves to "
                "underscore the author’s view that scientific progress is often accompanied by _____."
            ),
            "choices": [
                "A. an overestimation of empirical precision",
                "B. a justified sense of intellectual triumph",
                "C. the decline of philosophical reasoning",
                "D. skepticism toward quantitative analysis"
            ],
            "answer": "A"
        },
        {
            "question": (
                "The narrator’s reflection that 'truth, when spoken too soon, is but a whisper lost in a storm' primarily "
                "emphasizes his belief that _____."
            ),
            "choices": [
                "A. society often fails to recognize insight until it is convenient",
                "B. honesty is a virtue best reserved for private contemplation",
                "C. wisdom can only emerge through the passage of time",
                "D. the nature of truth is inherently unknowable"
            ],
            "answer": "A"
        },
        {
            "question": (
                "By contrasting 'the thunder of rhetoric' with 'the whisper of reason,' the author most likely intends to _____."
            ),
            "choices": [
                "A. expose the futility of emotional argument",
                "B. criticize the use of persuasive appeals in politics",
                "C. highlight the quiet power of rational discourse",
                "D. question the legitimacy of intellectual debate"
            ],
            "answer": "C"
        }
    ]

    #Select 1 question from each category
    chosen_questions = [
        random.choice(science_questions),
        random.choice(algebra_questions),
        random.choice(english_questions)
    ]

    score = 0
    for q in chosen_questions:
        clear()
        print(q["question"])
        for choice in q["choices"]:
            print(choice)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['answer']}")
        time.sleep(1.5)

    clear()
    if score == 3:
        print("Excellent! You passed the quiz! You may continue to the village.")
        input("Press Enter to continue...")
        return True
    else:
        print("You failed the quiz. Try again.")
        input("Press Enter to retry...")
        return Labyrinth_computer_quiz()


def Labyrinth():
    clear()
    print("You enter a dark labyrinth. Choose your path carefully.")
    correct_order = ['LEFT', 'RIGHT', 'FORWARD']
    steps = []

    for i in range(3):
        print("Paths: LEFT, RIGHT, FORWARD")
        choice = input(f"Step {i+1}: ")
        steps.append(choice.upper())

    if steps == correct_order:
        print("You find a hidden passage at the end of the labyrinth!")
        input("Press Enter to continue...")
        if Labyrinth_computer_quiz():
            print("A door opens ahead, leading to a bright light...")
            input("Press Enter to continue...")
            Village_sequence()
        else:
            print("You failed the labyrinth quiz. The walls close in.")
            sys.exit()
    else:
        print("You took the wrong path and got lost in the labyrinth. Game over.")
        sys.exit()

def fake_portal():
    clear()
    print("You find yourself in a portal. You see a light at the end of the tunnel. Do you want to go through the portal? (Y/N)")
    Option_1 = input(": ")
    if Option_1.upper() == 'Y':
        print("The portal leads to an abyss. Death is inevitable. You die.")
        sys.exit()
    elif Option_1.upper() == 'N':
        print("You decide not to go through the portal, returning to the outside world.")
        input("Press Enter to continue...")
        escape_room_2()
    else:
        try_again()
        fake_portal()

def portal():
    clear()
    print("You find yourself in a portal. You see a light at the end of the tunnel. Do you want to go through the portal? (Y/N)")
    Option_1 = input(": ")
    if Option_1.upper() == 'Y':
        print("You go through the portal.")
        input("Press Enter to continue...")
        real_world_beginning()
    elif Option_1.upper() == 'N':
        print("You decide not to go through the portal, returning to the outside world.")
        input("Press Enter to continue...")
        escape_room_2()
    else:
        try_again()
        portal()

def Village_sequence():
    clear()
    print("The village is home to a tribe of escapees. These men are the ones who have escaped from the room previously. They tell you the story of the origin of the escape room. It began with the dissolution of the world. Being in a coma, you were unaware of this. 50 Years prior, in geopolitical tensions, The west and the east were at war. After sanctions imposed by the west, the eastern economy was on the verge of collapse. The aristocrats of the east, to save their wealth, issued a nuclear attack upon New York City. The U.S. government, in a secret attempt to preserve the last remnants of the world, created a portal that would lead to a new development in an alternate Earth. The process was successful, but it came at the cost of one's memory and severe neurological impacts, including coma inducement. Being the last men of humanity, you were sent to the escape room, after being revived from the coma, to discern your capabilities mentally and physically to see if you were fit to be sent to the new world. You now have an impending option to choose your fate. The first, to go to the portal to be sent to the new world, or the second, to stay in the new world and live out your days. What do you want to do?")
    print("A. Go to the portal")
    print("B. Stay in the New world")
    Option_1 = input(": ")
    if Option_1.upper() == 'A':
        portal()
    elif Option_1.upper() == 'B':
        print("You decide to stay in the New world. You live out your days in peace. You die peacefully in your sleep. The end.")
        sys.exit()
    else:
        try_again()
        Village_sequence()

def real_world_beginning():
    clear()
    print("You wake up in a new world, alongside the other escapees. You are the last men of humanity (who have escaped from the depths of the new ruler). You see a dying man in the distance. As you approach him, he tells you the condition of the world. Here is what he is to say: \n\n 'After the nuclear attack, not much of the east, nor west survived. A man by the name of Urban claimed that this famine and remnant was a result of humanity's hubris, claiming to know the future. At first, he performed miracles, from feeding the starving to healing the sick. But as time went on, his so-called miracles were more and more grandiose. He began to walk on water, fly, heal the blind, and even resurrect the dead. The people in their desperation flocked to him, and as the king of the world, declared him the son of god, as the second coming of the messiah. And in the end, he revealed himself to be the devil in disguise. He was the one who had orchestrated the nuclear attack, the death, the famine, and all destruction. For the past 50 years, humanity has been crumbling into near extinction. The prophecy states that you are the one who must save the world, you must wage destruction on the devil's kingdom and restore order to humanity!'\n\n He dies shortly after. You now have an impending option to choose your fate. The first, to attack the devil's kingdom, or the second, to give up this mission and submit to the devil's rule. What do you want to do?'")
    print("A. Attack the devil's kingdom")
    print("B. Submit to the devil's rule")
    Option_1 = input(": ")
    if Option_1.upper() == 'A':
        print("You march forward to fulfill the prophecy. The future of humanity is now in your hands.")
        print("To be continued...")
        sys.exit()
    elif Option_1.upper() == 'B':
        print("You decide to submit to the devil's rule. You made the wrong choice. The world is doomed, but before you pass away, you see a white light. You wake up once more in the escape room, seeing it is a dream.")
        input("Press Enter to continue...")
        Escape_room_beginning()
    else:
        try_again()
        real_world_beginning()

Escape_room_beginning()
