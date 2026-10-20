import random

class Hangman:
    def __init__(self):
        self.words = ["cat", "dog", "roozbeh", "lag", "jar"]
        self.secret_word = random.choice(self.words)
        self.lives = 6
        self.guessed_letters = []

    def show_word(self):
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.secret_word])

    def guess(self, letter):
        if letter in self.guessed_letters:
            return print("Already guessed!")
        self.guessed_letters.append(letter)
        self.lives -= (letter not in self.secret_word)
        print("Good!" if letter in self.secret_word else f"Wrong! Lives: {self.lives}")

    def run(self):
        print("\nWelcome to Hangman!")
        while self.lives > 0:
            print(f"\nWord: {self.show_word()} | Lives: {self.lives}")
            
            if "_" not in self.show_word():
                print("You won! 🎉")
                break
                
            letter = input("Guess: ").lower()
            if len(letter) == 1 and letter.isalpha():
                self.guess(letter)
            else:
                print("Single letter only.")
        
        if self.lives <= 0:
            print(f"\nGame Over! The word was: {self.secret_word}")
            
        # بخش بازی مجدد
        choice = input("\n1. Play Again | 2. Exit: ")
        if choice == "1":
            Hangman().run()
        else:
            print("Goodbye!")

if __name__ == "__main__":
    Hangman().run()
