import random
import numpy as np
import matplotlib.pyplot as plt


class FrozenLake:
    def __init__(self, map_filename, close_reward, slippery_rate):
        self.posx = 0
        self.posy = 0
        self.map = self.parseMap(map_filename)
        self.close_reward = close_reward
        self.slippery_rate = slippery_rate
        self.qtable = np.zeros((64, 4))

    def parseMap(self, filename):
        try:
            with open(filename, 'r') as file:
                map_array = [[char for char in line.strip()] for line in file]
            if len(map_array) != 8 or any(len(row) != 8 for row in map_array):
                raise ValueError("Map must be 8x8.")
            if not map_array.count('S') == 1 and map_array.count('H') == 1:
                raise ValueError("Invalid start or/and finish!")
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

    def print_state(self):
        for i in range(8):
            for j in range(8):
                if not (i == self.posy and j == self.posx):
                    print(f"{self.map[i][j]} ", end="")
                else:
                    print("A ", end="")
            print()
        print()

    def train(self, epochs, learning_rate,
              discount_factor, epsilon, test_name):
        successes = 0
        successes_epochs = []
        for epoch in range(epochs):
            print(f"Epoch: {epoch+1}")
            self.posx, self.posy = 0, 0
            done = False

            while not done:
                state = self.posy * 8 + self.posx
                if random.random() < epsilon:
                    action = random.choice([0, 1, 2, 3])
                else:
                    action = np.argmax(self.qtable[state])

                new_state, reward, done = self.take_action(action)
                max_future_q = np.max(self.qtable[new_state])
                current_q = self.qtable[state][action]

                new_q = (1 - learning_rate) * current_q + learning_rate * (
                    reward + discount_factor * max_future_q)
                self.qtable[state][action] = new_q

            if self.map[self.posy][self.posx] == 'G':
                print("Found!")
                successes += 1
                successes_epochs.append(epoch)

        self.plot_cumulative_successes(successes_epochs, test_name)
        print(f"Wins: {successes}, {(successes * 100 / epochs):.2f}%")
        self.print_qtable(test_name)

    def plot_cumulative_successes(self, epochs_with_success, test_name):
        cumulative_successes = []

        if epochs_with_success != []:
            for epoch in range(1, max(epochs_with_success) + 1):
                print(f"Creating plot: {epoch}")
                cumulative_successes.append(sum(
                    1 for e in epochs_with_success if e <= epoch))

            plt.figure(figsize=(10, 6))
            plt.plot(range(1, max(epochs_with_success) + 1),
                     cumulative_successes, marker='o')
            plt.xlabel('Epoch')
            plt.ylabel('Cumulative Number of Successes')
            plt.title('Cumulative Number of Successes over Epochs')
            plt.grid(True)
            if test_name:
                plt.savefig(f"results/{test_name}_successes.pdf")
            else:
                plt.show()
        else:
            print("No successes!")

    def take_action(self, action):
        prev_pos = (self.posy, self.posx)
        if action == 0:
            self.move_up()
        elif action == 1:
            self.move_down()
        elif action == 2:
            self.move_left()
        elif action == 3:
            self.move_right()

        if random.random() < self.slippery_rate:
            self.slip()

        new_state = self.posy * 8 + self.posx
        reward = self.get_reward(prev_pos)
        done = self.map[self.posy][self.posx] in ['G', 'H']

        return new_state, reward, done

    def slip(self):
        if self.map[self.posy][self.posx] not in ['G', 'H']:
            action = random.choice([0, 1, 2, 3])
            if action == 0:
                self.move_up()
            elif action == 1:
                self.move_down()
            elif action == 2:
                self.move_left()
            elif action == 3:
                self.move_right()

    def get_reward(self, prev_pos):
        if self.map[self.posy][self.posx] == 'G':
            return 100
        if self.map[self.posy][self.posx] == 'H':
            return -100

        if self.close_reward:
            goal_position = self.find_goal_position()
            curr_pos_dist = np.linalg.norm(
                np.array([self.posy, self.posx]) - np.array(goal_position))
            prev_pos_dist = np.linalg.norm(
                np.array(prev_pos) - np.array(goal_position))
            return prev_pos_dist - curr_pos_dist
        else:
            return 0

    def find_goal_position(self):
        for y in range(8):
            for x in range(8):
                if self.map[y][x] == 'G':
                    return (y, x)
        return None

    def move_right(self):
        if not self.posx + 1 > 7:
            self.posx += 1

    def move_left(self):
        if not self.posx - 1 < 0:
            self.posx -= 1

    def move_up(self):
        if not self.posy - 1 < 0:
            self.posy -= 1

    def move_down(self):
        if not self.posy + 1 > 7:
            self.posy += 1

    def print_qtable(self, test_name):
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_xlim(0, 8)
        ax.set_ylim(0, 8)

        colors = {'S': 'lightgreen', 'G': 'lightcoral', 'H': 'lightblue'}

        for x in range(8):
            for y in range(8):
                cell_content = self.map[7-y][x]
                color = colors.get(cell_content, 'white')

                rect = plt.Rectangle((x, 7-y), 1, 1,
                                     fill=True, color=color,
                                     edgecolor='black', zorder=0)
                ax.add_patch(rect)

                state = (7-y) * 8 + x
                q_values = self.qtable[state]
                ax.text(x + 0.5, 7-y + 0.15, f'↑({q_values[0]:.1f})',
                        horizontalalignment='center', fontsize=6,
                        color='blue', zorder=1)
                ax.text(x + 0.5, 7-y + 0.85, f'↓({q_values[1]:.1f})',
                        horizontalalignment='center', fontsize=6,
                        color='blue', zorder=1)
                ax.text(x + 0.25, 7-y + 0.5, f'←({q_values[2]:.1f})',
                        horizontalalignment='center', fontsize=6,
                        color='blue', zorder=1)
                ax.text(x + 0.75, 7-y + 0.5, f'({q_values[3]:.1f})→',
                        horizontalalignment='center', fontsize=6,
                        color='blue', zorder=1)

        ax.set_xticks(np.arange(0, 8, 1))
        ax.set_yticks(np.arange(0, 8, 1))
        ax.grid(False)
        ax.set_aspect('equal', adjustable='box')
        ax.invert_yaxis()
        if test_name:
            plt.savefig(f"results/{test_name}_map.pdf")
        else:
            plt.show()
