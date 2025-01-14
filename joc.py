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

# Funcția pentru actualizarea jocului
def update_game():
    global guesses, turns
    display_word = ""
    failed = 0

    # Construim progresul cuvântului
    for char in word:
        if char in guesses:
            display_word += char + " "
        else:
            display_word += "_ "
            failed += 1

    word_label.config(text=display_word.strip())

    # Verificăm dacă jocul s-a terminat
    if failed == 0:
        result_label.config(text="Felicitări, ai câștigat! Cuvântul era: " + word)
        disable_game()
        return

    if turns == 0:
        hangman_label.config(text=hangman_stages[-1])
        result_label.config(text="Ai pierdut! Cuvântul era: " + word)
        chances_label.config(text="Mai ai 0 șanse.")  # Corectăm mesajul pentru șansele rămase
        disable_game()
        return

    # Afișăm starea curentă a spânzurătorii
    hangman_label.config(text=hangman_stages[len(hangman_stages) - 1 - turns])

    # Afișăm șansele rămase
    if turns == 1:
        chances_label.config(text="Mai ai 1 șansă.")
    else:
        chances_label.config(text=f"Mai ai {turns} șanse.")

# Funcția pentru ghicirea unei litere
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

    # Adăugăm litera ghicită
    guesses += guess

    # Dacă litera nu este în cuvânt
    if guess not in word:
        turns -= 1
        result_label.config(text=f"Greșit! Litera '{guess}' nu este în cuvânt.")
    else:
        result_label.config(text=f"Ai ghicit corect! Litera '{guess}' este în cuvânt.")

    # Golește câmpul de text
    guess_entry.delete(0, tk.END)

    # Actualizează jocul
    update_game()

# Dezactivează jocul la final
def disable_game():
    guess_entry.config(state="disabled")
    guess_button.config(state="disabled")

# Fereastra principală
root = tk.Tk()
root.title("Jocul Spânzurătoarea")

# Elemente grafice
word_label = tk.Label(root, text="_ " * len(word), font=("Helvetica", 20))
word_label.pack()

hangman_label = tk.Label(root, text=hangman_stages[0], font=("Courier", 12), justify="left")
hangman_label.pack()

chances_label = tk.Label(root, text=f"Mai ai {turns} șanse.", font=("Helvetica", 14))
chances_label.pack()

guess_entry = tk.Entry(root, font=("Helvetica", 14))
guess_entry.pack()

guess_button = tk.Button(root, text="Ghiceste o literă", font=("Helvetica", 14), command=guess_letter)
guess_button.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack()

# Inițializare joc
update_game()

# Rulează aplicația
root.mainloop()
