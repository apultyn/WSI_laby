class FrozenLake:
    def __init__(self, map):
        self.posx = 0
        self.posy = 0
        self.map = map

    def print_state(self):
        for i in range(8):
            for j in range(8):
                if not (i == self.posy and j == self.posx):
                    print(f"{self.map[i][j]} ", end="")
                else:
                    print("A ", end="")
            print()
        print()

    def check_hole(self):
        if self.map[self.posy][self.posx] == 'H':
            self.posx = 0
            self.posy = 0

    def move_right(self):
        if not self.posx + 1 > 7:
            self.posx += 1
        self.check_hole()

    def move_left(self):
        if not self.posx - 1 < 0:
            self.posx -= 1
        self.check_hole()

    def move_up(self):
        if not self.posy - 1 < 0:
            self.posy -= 1
        self.check_hole()

    def move_down(self):
        if not self.posy + 1 > 7:
            self.posy += 1
        self.check_hole()


def parseMap(filename):
    try:
        with open(filename, 'r') as file:
            map_array = [[char for char in line.strip()] for line in file]
        if len(map_array) != 8 or any(len(row) != 8 for row in map_array):
            raise ValueError("Map must be 8x8.")
        if map_array[0][0] != 'S':
            raise ValueError("Start in wrong spot!")
        if map_array[7][7] != 'G':
            raise ValueError("End in wrong spot!")
        return map_array
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return None
    except ValueError as ve:
        print(ve)
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    frozenLake = FrozenLake(parseMap("map.txt"))


if __name__ == "__main__":
    main()
