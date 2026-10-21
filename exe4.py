import random

def show_winner(user, computer):
    if user == computer:
        return "Tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

class RockPaperScissors:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0
        self.choice = ["rock", "paper", "scissors"]

    def play(self):
        print("Welcome to Rock Paper Scissors")
        while self.user_score < 3 and self.computer_score < 3:
            print(f"\nYour score: {self.user_score} | Computer score: {self.computer_score}")
            
            user_choice = input("Choose (rock, paper, scissors): ").lower()
            
            # اصلاح شد: self.choice به جای self.user_choice
            if user_choice not in self.choice:
                print("Invalid Value")
                continue
                
            computer_choice = random.choice(self.choice)
            print(f"Computer choice: {computer_choice}")
            
            result = show_winner(user_choice, computer_choice)
            
            if result == "user":
                self.user_score += 1
                print("You won this round")
            elif result == "computer":
                self.computer_score += 1
                print("Computer won this round")
            else:
                print("Tie")
                
        # این بخش بعد از حلقه است
        if self.user_score == 3:
            print("You Won this Gameee")
        else:
            print("You lose :( ! Computer Won")

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play()
