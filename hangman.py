import random

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

print("Hai să ne jucăm Spânzurătoarea! Succes!")

# Listă de cuvinte pentru joc
words = ['individ', 'calculator', 'programare', 'paguba',
         'floare', 'muschi', 'drumetie', 'conditie',
         'totul', 'betoniera', 'fazan', 'ochelari']

# Alege un cuvânt aleatoriu
word = random.choice(words)

# Inițializări
guesses = ''
turns = len(hangman_stages) - 1  # 6 șanse (număr total de etape minus 1)

while turns > 0:
    failed = 0

    # Afișează progresul cuvântului
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    print("\n")  # Linie nouă pentru claritate

    # Verificăm dacă toate literele au fost ghicite
    if failed == 0:
        print("Felicitări, ai câștigat! Cuvântul era:", word)
        break

    # Afișăm starea curentă a spânzurătorii
    print(hangman_stages[len(hangman_stages) - 1 - turns])

    guess = input("Ghiceste o literă: ").lower()

    # Validare intrare
    if len(guess) != 1 or not guess.isalpha():
        print("Te rog introdu o singură literă validă!")
        continue

    # Verificare literă deja ghicită
    if guess in guesses:
        print("Ai încercat deja această literă. Încearcă alta!")
        continue

    # Adaugă litera ghicită în lista de ghiciri
    guesses += guess

    # Verificăm dacă litera ghicită nu se află în cuvânt
    if guess not in word:
        turns -= 1
        print("Gresit! Litera nu este în cuvânt.")
        print("Mai ai", turns, "șanse.")
        if turns == 0:
            print(hangman_stages[-1])  # Afișăm ultima etapă (omul complet spânzurat)
            print("Ai pierdut! Cuvântul era:", word)
