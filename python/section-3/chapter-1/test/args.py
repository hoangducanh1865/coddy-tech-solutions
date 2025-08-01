class Calculator:
    def add_numbers(self, *args):
        return sum(args)
    
    def show_numbers(self, *args):
        for i, num in enumerate(args):
            print(f"Number {i+1}: {num}")
            
    
class Logger:
    def log_message(self, level, *messages):
        print(f"[{level}]", end=" ")
        for message in messages:
            print(message, end=" ")
        print()  # New line

class Team:
    def __init__(self, team_name, *players):
        self.team_name = team_name
        self.players = list(players)
    
    def show_team(self):
        print(f"Team: {self.team_name}")
        for player in self.players:
            print(f"- {player}")

team = Team("Warriors", "Alice", "Bob", "Charlie", "Diana")
team.show_team()

calc = Calculator()
result1 = calc.add_numbers(1, 2, 3)
result2 = calc.add_numbers(10, 20, 30, 40, 50)
print(result1)  # 6
print(result2)  # 150

numbers = [1, 2, 3, 4, 5]
result = calc.add_numbers(*numbers)  # Unpacks the list
print(result)  # 15