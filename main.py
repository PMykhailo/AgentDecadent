from behavior import *
from arena import Arena
import numpy as np

arena1 = Arena()
arena1.add_hunter(10,1,naive_hunter, np.array([0,10]), 1, name = 'evil_wolf')
arena1.add_prey(5,2,naive_prey, np.array([0,0]), 0, name = 'poor_rabit')
arena1.simulate(10)