import random
words = ["python", "apple", "school", "computer", "coding"]
word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts = 6
guessed_letters = []
print("🎮 Welcome to Hangman Game")
while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Attempts left:", attempts)
    guess = input("Enter a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("✅ Correct Guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong Guess!")
        attempts -= 1
if "_" not in guessed_word:
    print("\n You Won! The word was:", word)
else:
    print("\n💀 You Lost! The word was:", word)
