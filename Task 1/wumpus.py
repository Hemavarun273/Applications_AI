
import random

class WumpusWorld:
    def __init__(self, size):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.agent_location = (0, 0)
        self.wumpus_location = self.random_location()
        self.pit_locations = [self.random_location() for _ in range(3)]
        self.gold_location = self.random_location()

    def random_location(self):
        return random.randint(0, self.size - 1), random.randint(0, self.size - 1)

    def print_world(self):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) == self.agent_location:
                    print('A', end=' ')
                else:
                    print(self.grid[i][j], end=' ')
            print()
        print()

    def initialize_world(self):
        self.grid[self.wumpus_location[0]][self.wumpus_location[1]] = 'W'
        self.grid[self.gold_location[0]][self.gold_location[1]] = 'G'
        for pit_location in self.pit_locations:
            self.grid[pit_location[0]][pit_location[1]] = 'P'

    def move_agent(self, direction):
        x, y = self.agent_location
        if direction == 'UP' and x > 0:
            x -= 1
        elif direction == 'DOWN' and x < self.size - 1:
            x += 1
        elif direction == 'LEFT' and y > 0:
            y -= 1
        elif direction == 'RIGHT' and y < self.size - 1:
            y += 1

        self.agent_location = (x, y)
        self.grid[x][y] = 'A'

    def check_perceptions(self):
        x, y = self.agent_location

        # Check for Wumpus
        if self.wumpus_location == (x, y):
            return "You smell a terrible odor!"

        # Check for pits
        for pit_location in self.pit_locations:
            if pit_location == (x, y):
                return "You feel a breeze!"

        # Check for gold
        if self.gold_location == (x, y):
            return "You see a glimmer of gold!"

        return "Nothing unusual."

# Example usage
size_of_world = 4
wumpus_world = WumpusWorld(size_of_world)
wumpus_world.initialize_world()

while True:
    wumpus_world.print_world()

    action = input("Enter your action (UP/DOWN/LEFT/RIGHT): ").upper()
    wumpus_world.move_agent(action)

    perception = wumpus_world.check_perceptions()
    print(perception)

    if wumpus_world.agent_location == wumpus_world.wumpus_location:
        print("You were eaten by the Wumpus! Game over.")
        break

    if wumpus_world.agent_location == wumpus_world.gold_location:
        print("Congratulations! You found the gold and won!")
        break
