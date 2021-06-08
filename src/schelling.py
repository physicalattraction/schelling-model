"""
Schelling model of segragation, based on https://www.binpress.com/simulating-segregation-with-python/
"""

import copy
import os.path
import random
from collections import namedtuple
from typing import Dict, List

import matplotlib.pyplot as plt

Point = namedtuple('Point', ['x', 'y'])
Race = int


class Schelling:
    def __init__(self, width: int, height: int, empty_ratio: float, similarity_threshold: float,
                 nr_iterations: int, nr_races: int = 2):
        self.width = width
        self.height = height
        self.nr_races = nr_races
        self.empty_ratio = empty_ratio
        # If there are less than this percentage of similar people, an agent is unhappy
        self.similarity_threshold = similarity_threshold
        self.nr_iterations = nr_iterations
        self.empty_houses: List[Point] = []
        # Dictionary from point to race, e.g. {(26, 16): 1, (47, 15): 2, ...}
        self.agents: Dict[Point, Race] = {}

    def populate(self):
        all_houses = [
            (x, y)
            for x in range(self.width)
            for y in range(self.height)
        ]
        random.shuffle(all_houses)

        nr_empty = int(self.empty_ratio * len(all_houses))
        self.empty_houses = all_houses[:nr_empty]

        remaining_houses = all_houses[nr_empty:]
        houses_by_race = [remaining_houses[i::self.nr_races] for i in range(self.nr_races)]
        self.agents = {
            house: i + 1
            for i in range(self.nr_races)
            for house in houses_by_race[i]
        }

    def is_satisfied(self, agent: Point) -> bool:
        x, y = agent
        race = self.agents[(x, y)]
        count_similar = 0
        count_different = 0

        # Check top left neighbor
        if x > 0 and y > 0 and (x - 1, y - 1) not in self.empty_houses:
            if self.agents[(x - 1, y - 1)] == race:
                count_similar += 1
            else:
                count_different += 1

        # Check top neighbor
        if y > 0 and (x, y - 1) not in self.empty_houses:
            if self.agents[(x, y - 1)] == race:
                count_similar += 1
            else:
                count_different += 1

        # Check top right neighbor
        if x < (self.width - 1) and y > 0 and (x + 1, y - 1) not in self.empty_houses:

            if self.agents[(x + 1, y - 1)] == race:
                count_similar += 1
            else:
                count_different += 1

        # Check left neighbor
        if x > 0 and (x - 1, y) not in self.empty_houses:
            if self.agents[(x - 1, y)] == race:
                count_similar += 1
            else:
                count_different += 1

        # Check right neighbor
        if x < (self.width - 1) and (x + 1, y) not in self.empty_houses:
            if self.agents[(x + 1, y)] == race:
                count_similar += 1
            else:
                count_different += 1

        # Check bottom left neighbor
        if x > 0 and y < (self.height - 1) and (x - 1, y + 1) not in self.empty_houses:
            if self.agents[(x - 1, y + 1)] == race:
                count_similar += 1
            else:
                count_different += 1

        # Check bottom neighbor
        if x > 0 and y < (self.height - 1) and (x, y + 1) not in self.empty_houses:
            if self.agents[(x, y + 1)] == race:
                count_similar += 1
            else:
                count_different += 1

        # Check bottom right neighbor
        if x < (self.width - 1) and y < (self.height - 1) and (x + 1, y + 1) not in self.empty_houses:
            if self.agents[(x + 1, y + 1)] == race:
                count_similar += 1
            else:
                count_different += 1

        if (count_similar + count_different) == 0:
            # Somebody with no neighbors at all is satisfied
            return True
        else:
            return float(count_similar) / (count_similar + count_different) >= self.similarity_threshold

    def update(self):
        for i in range(1, self.nr_iterations + 1):
            old_agents = copy.deepcopy(self.agents)
            nr_changes = 0
            for agent in old_agents:
                if not self.is_satisfied(agent):
                    agent_race = self.agents[agent]
                    empty_house = random.choice(self.empty_houses)
                    self.agents[empty_house] = agent_race
                    del self.agents[agent]
                    self.empty_houses.remove(empty_house)
                    self.empty_houses.append(agent)
                    nr_changes += 1
            print(f'Iteration {i}/{self.nr_iterations}: {nr_changes} changes')
            if nr_changes == 0:
                break

    def plot(self, title: str, file_name: str):
        fig, ax = plt.subplots()
        # If you want to run the simulation with more than 7 colors, you should set agent_colors accordingly
        agent_colors = {1: 'b', 2: 'r', 3: 'g', 4: 'c', 5: 'm', 6: 'y', 7: 'k'}
        for agent in self.agents:
            ax.scatter(agent[0] + 0.5, agent[1] + 0.5, color=agent_colors[self.agents[agent]])

        ax.set_title(title, fontsize=10, fontweight='bold')
        ax.set_xlim([0, self.width])
        ax.set_ylim([0, self.height])
        ax.set_xticks([])
        ax.set_yticks([])
        root_dir = os.path.dirname(os.path.dirname(__file__))
        file_name = os.path.join(root_dir, 'tmp', file_name)
        plt.savefig(file_name)


if __name__ == '__main__':
    schelling_30 = Schelling(20, 20, 0.3, 0.3, 100, 2)
    schelling_30.populate()
    schelling_30.plot('Schelling Model with 7 colors: Initial State',
                      'schelling_7_30_09_initial.png')
    schelling_30.update()
    schelling_30.plot('Schelling Model with 7 colors: Final State with Similarity Threshold 30%',
                      'schelling_7_30_10_final.png')
    #
    # schelling_50 = Schelling(50, 50, 0.3, 0.5, 100, 2)
    # schelling_50.populate()
    # schelling_50.plot('Schelling Model with 2 colors: Initial State',
    #                   'schelling_50_01_initial.png')
    # schelling_50.update()
    # schelling_50.plot('Schelling Model with 2 colors: Final State with Similarity Threshold 50%',
    #                   'schelling_50_02_final.png')

    # schelling_80 = Schelling(50, 50, 0.3, 0.8, 500, 2)
    # schelling_80.populate()
    # schelling_80.plot('Schelling Model with 2 colors: Initial State',
    #                   'schelling_80_01_initial.png')
    # schelling_80.update()
    # schelling_80.plot('Schelling Model with 2 colors: Final State with Similarity Threshold 80%',
    #                   'schelling_80_02_final.png')
