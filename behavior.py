import numpy as np


def naive_hunter(name, hunters, prey):
    target_range = np.inf
    target_name = None
    for target in prey.values():
        new_target_range = np.linalg.norm(hunters[name].position - target.position)
        if new_target_range < target_range:
            target_range = new_target_range
            target_name = target.name

    if target_name is None:
        return np.array([0,0])

    return prey[target_name].position - hunters[name].position, 1


def naive_prey(name, hunters, prey):
    threat_range = np.inf
    threat_name = None
    for threat in hunters.values():
        new_threat_range = np.linalg.norm(prey[name].position - threat.position)
        if new_threat_range < threat_range:
            threat_range = new_threat_range
            threat_name = threat.name

    if threat_name is None:
        return np.array([0, 0])

    return prey[name].position - hunters[threat_name].position, 1
