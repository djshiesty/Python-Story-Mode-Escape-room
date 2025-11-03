# Python-Story-Mode-Escape-room

## Project Description
You wake up in a mysterious white room with a dead person and a malnourished companion. You have **10 minutes** to figure out what to do before time runs out. This is a **text-based escape room game in Python**, where you explore objects, solve puzzles, and make decisions that affect your fate. You’ll interact with **safes, notes, and a computer** that requires passing a quiz. Depending on your choices, you might find a **labyrinth, portals, or a village** with secrets about the world 🌎.

---

## Technical Summary 🛠️
- **Language:** Python 3  
- **Libraries:** `os`, `sys`, `time`, `random`  
- **Features:**
  - Countdown timer for each room:
    ```python
    def countdown(seconds):
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            print(f"Time remaining: {mins:02}:{secs:02}", end='\r')
            time.sleep(1)
    ```
  - Multiple-choice quizzes for **Science, Algebra, and English**
  - Functions for each room, safe, note, computer, portal, and labyrinth
  - Input validation and retry for incorrect options

---

## Gameplay Highlights 🎮
- **Check a safe for keys**:
    ```python
    code = "Don't Break"
    guess = input("Enter the code: ")
    if guess == code:
        print("You find a key!")
    ```
- **Read cryptic notes**:
    ```python
    print("The note says: Gjstu xpse jt Epo’u.")
    ```
- **Unlock the computer with a quiz**:
  - One random question from each category: Science, Algebra, English  
  - Multiple-choice format (A/B/C/D)  
  - Score 3/3 to pass
- Navigate a **labyrinth**: correct path is LEFT → RIGHT → FORWARD  
- Reach the **village or portal** depending on your choices

---

## Learning Goals 📚
- Practice Python basics: loops, conditionals, functions, and input/output  
- Implement random question selection for quizzes  
- Combine storytelling with interactive gameplay  
- Work with timers, branching paths, and replayability  
- Strengthen logic and problem-solving skills

---

## Example Quiz Questions

**Science:**  
> Which planet is known as the Red Planet?  
> A. Mars  
> B. Venus  
> C. Jupiter  
> D. Mercury  

**Algebra:**  
> Solve for x: 2x + 6 = 14  
> A. 4  
> B. 5  
> C. 3  
> D. 6  

**English (SAT-style):**  
> Although the author’s tone is generally admiring, his critique suggests the conclusions are _____.  
> A. groundbreaking yet hastily constructed  
> B. meticulous and logically irrefutable  
> C. intellectually rigorous though somewhat inaccessible  
> D. ambitious but ultimately unsound  

Score 3/3 to unlock the password and continue the game! 🏆
