import numpy as np


class Agent:
    def __init__(self, max_velocity, max_acceleration, decision_function, position, name):
        self.max_velocity = max_velocity
        self.max_acceleration = max_acceleration
        self.decision_function = decision_function
        self.hunters = None
        self.prey = None
        self.name = name
        self.position = position
        self.velocity = np.array((0,0))
        self.last_move = [np.array([0,0]),np.array([0,0])]

    def update_situation(self, agents):
        self.hunters, self.prey = agents

    def make_maneuver(self):
        vector, thrust = self.decision_function(self.name, self.hunters, self.prey)
        if np.linalg.norm(vector) < 1e-5:
            self.position = self.position + self.velocity
            return np.array([0,0])
        acceleration = vector/np.linalg.norm(vector)*self.max_acceleration*thrust
        new_velocity = self.velocity + acceleration
        if np.linalg.norm(new_velocity) > self.max_velocity:
            new_velocity = new_velocity/np.linalg.norm(new_velocity)*self.max_velocity
        self.velocity = new_velocity
        self.last_move = self.position
        self.position = self.position + self.velocity
        print(self.name, 'velocity=', self.velocity, 'position = ', self.position)
        return new_velocity


class Prey(Agent):
    def __init__(self, max_velocity, max_acceleration, decision_function, position, evasion_chance, name):
        super().__init__(max_velocity, max_acceleration, decision_function, position, name)
        self.role = 'pray'
        self.evasion_chance = evasion_chance


class Hunter(Agent):
    def __init__(self, max_velocity, max_acceleration, decision_function, position, catch_radius, name):
        super().__init__(max_velocity, max_acceleration, decision_function, position, name)
        self.role = 'hunter'
        self.catch_radius = catch_radius
