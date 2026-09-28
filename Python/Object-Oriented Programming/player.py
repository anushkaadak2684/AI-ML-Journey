class Player:
    player_count = 0
    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1

p1 = Player("Anushka", 'A')
p2 = Player("Mainak", 'L')
p3 = Player("Mayukh", 'C')

print("Total players:", Player.player_count)
print("Player 1:", p1.name, p1.level)
print("Player 2:", p2.name, p2.level)
print("Player 3:", p3.name, p3.level)