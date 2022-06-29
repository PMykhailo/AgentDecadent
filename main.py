from behavior import *
from arena import Arena
import numpy as np

arena1 = Arena(limits=[[-20,20], [-20,20]])
arena1.add_hunter(10,1,basic_hunter, np.array([0,6]), 1, name = 'evil_wolf')
arena1.add_prey(5,2,basic_prey, np.array([0,0]), 0, name = 'poor_rabit')
#arena1.add_prey(5,2,naive_prey, np.array([20,0]), 0, name = 'poor_rabit 2')
arena1.simulate(100)