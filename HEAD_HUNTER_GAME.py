import random

class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.guess = None

    def make_guess(self):
        while True:
            guess = input(f"{self.name}, enter your guess (head/tail): ").strip().lower()
            if guess in ["head", "tail"]:
                self.guess = guess
                break
            print("Invalid input. Please enter 'head' or 'tail'.")

class HeadHunterGame:
    def __init__(self):
        self.players = []
        self.rounds = 10

    def add_player(self, name):
        self.players.append(Player(name))

    def toss_coin(self):
        return random.choice(["head", "tail"])

    def play_round(self):
        results = []
        for player in self.players:
            result = self.toss_coin()
            if player.guess == result:
                points = 5 if player.guess == "head" else 2
                player.points += points
                print(f"{player.name} guessed correctly! Earned {points} points.")
            else:
                player.points -= 3
                print(f"{player.name} guessed wrong. Lost 3 points.")
            results.append((player.name, player.guess, result, player.points))
        return results

    def display_ranking(self):
        print("\nCurrent Rankings:")
        for player in sorted(self.players, key=lambda x: x.points, reverse=True):
            print(f"{player.name}: {player.points} points")

    def play_game(self):
        print("Welcome to the Head Hunter Game!")
        num_players = int(input("Enter number of players: "))
        for _ in range(num_players):
            name = input("Enter player name: ").strip()
            self.add_player(name)

        while all(player.points < 50 for player in self.players):
            print("\nStarting a new round...")
            for player in self.players:
                player.make_guess()
            self.play_round()
            self.display_ranking()

        winner = max(self.players, key=lambda x: x.points)
        print(f"\nCongratulations {winner.name}! You won the game with {winner.points} points.")

if __name__ == "__main__":
    game = HeadHunterGame()
    game.play_game()