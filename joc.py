import random
import tkinter as tk

# Animații pentru spânzurătoare cu 6 etape
hangman_stages = [
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """
]

# Listă de cuvinte pentru joc
words = ['individ', 'calculator', 'programare', 'paguba',
         'floare', 'muschi', 'drumetie', 'conditie',
         'totul', 'betoniera', 'fazan', 'ochelari']

# Alege un cuvânt aleatoriu
word = random.choice(words)

# Inițializări
guesses = ''
turns = len(hangman_stages) - 1  # 6 șanse (număr total de etape minus 1)

def update_game():
    global guesses, turns
    display_word = ""
    failed = 0

    # Afișează progresul cuvântului
    for char in word:
        if char in guesses:
            display_word += char + " "
        else:
            display_word += "_ "
            failed += 1

    word_label.config(text=display_word.strip())

    # Verificăm dacă toate literele au fost ghicite
    if failed == 0:
        result_label.config(text="Felicitări, ai câștigat! Cuvântul era: " + word)
        return

    # Afișăm starea curentă a spânzurătorii
    hangman_label.config(text=hangman_stages[len(hangman_stages) - 1 - turns])

    # Dacă jocul a fost pierdut
    if turns == 0:
        hangman_label.config(text=hangman_stages[-1])
        result_label.config(text="Ai pierdut! Cuvântul era: " + word)
        return

    # Actualizează numărul de șanse
    chances_label.config(text="Mai ai " + str(turns) + " șanse.")

def guess_letter():
    global guesses, turns

    guess = guess_entry.get().lower()

    # Validare intrare
    if len(guess) != 1 or not guess.isalpha():
        result_label.config(text="Te rog introdu o singură literă validă!")
        return

    # Verificare literă deja ghicită
    if guess in guesses:
        result_label.config(text="Ai încercat deja această literă. Încearcă alta!")
        return

    # Adaugă litera ghicită în lista de ghiciri
    guesses += guess

    # Verificăm dacă litera ghicită nu se află în cuvânt
    if guess not in word:
        turns -= 1
        result_label.config(text="Gresit! Litera nu este în cuvânt.")
    
    update_game()

# Fereastra principală
root = tk.Tk()
root.title("Jocul Spânzurătoarea")

# Elemente grafice
word_label = tk.Label(root, text="_ " * len(word), font=("Helvetica", 20))
word_label.pack()

hangman_label = tk.Label(root, text="", font=("Courier", 12), height=6)
hangman_label.pack()

chances_label = tk.Label(root, text="Mai ai " + str(turns) + " șanse.", font=("Helvetica", 14))
chances_label.pack()

guess_entry = tk.Entry(root, font=("Helvetica", 14))
guess_entry.pack()

guess_button = tk.Button(root, text="Ghiceste o literă", font=("Helvetica", 14), command=guess_letter)
guess_button.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack()

# Începe jocul
update_game()

# Rulează aplicația
root.mainloop()
