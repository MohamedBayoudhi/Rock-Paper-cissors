from random import choice

CHOICES: tuple = ('R', 'P', 'S')
BEATS: dict = {
    'R': 'S',
    'S': 'P',
    'P': 'R'
}
RPS: dict = {
    'R': "Rock",
    'P': "Paper",
    'S': "Scissors"
}


class Player:
    def __init__(self, name: str):
        self.name: str = name
        self.move: str = ''
        self.score: int = 0
    
    def play(self):
        """Make a move"""
        if self.name == "Computer":
            self.move = choice(CHOICES)
        else:
            while True:
                move = input("What's your choice?: ")
                if move.upper() in CHOICES:
                    self.move = move.upper()
                    break
                else:
                    print("Invalid input")


class Game:
    def __init__(self):
        self.player1: Player = Player("You")
        self.player2: Player = Player("Computer")
        
    def winner(self):
        """Returns the winner Player if there's a winner, None if there's a tie"""
        if BEATS[self.player1.move] == self.player2.move:
            return self.player1
        elif self.player1.move == self.player2.move:
            return None
        else:
            return self.player2
        
    def gameRound(self):
        """One round of Rock Paper Scissors"""
        self.player1.play()
        self.player2.play()
        print(f"{self.player1.name} played {RPS[self.player1.move]}")
        print(f"{self.player2.name} played {RPS[self.player2.move]}")
        if self.winner() != None:
            print(f"{self.winner().name} wins!" if self.winner().name != "You" else "You win!")
            if self.winner() == self.player1:
                self.player1.score += 1
            else:
                self.player2.score += 1
        else:
            print("Tie")
        print(f"{self.player1.name}: {self.player1.score} | {self.player2.name}: {self.player2.score}")
    
    def game(self):
        """The game itself"""
        while True:
            try:
                rounds = int(input("How many rounds?\n> "))
            except:
                print("Enter an integer, please")
            else:
                if rounds > 0:
                    break
                else:
                    print("Enter a number that makes sense, please")
        for i in range(rounds):
            print(f"\nRound {i + 1}:")
            self.gameRound()


if __name__ == "__main__":
    G = Game()
    G.game()
