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
        return np.array([0,0]), 0

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


def basic_prey(name, hunters, prey):
    threat_range = np.inf
    threat_name = None
    for threat in hunters.values():
        new_threat_range = np.linalg.norm(prey[name].position - threat.position)
        if new_threat_range < threat_range:
            threat_range = new_threat_range
            threat_name = threat.name

    if threat_name is None:
        return np.array([0, 0]), 0

    if np.linalg.norm(hunters[threat_name].velocity) < 1:
        return prey[name].position - hunters[threat_name].position, 1

    if (threat_range < 3*hunters[threat_name].max_velocity) and (np.linalg.norm(prey[name].velocity) < prey[name].max_velocity):
        print(name, ' taking evasive actions')
        threat_velocity = hunters[threat_name].velocity
        position = prey[name].position
        torque = threat_velocity[0]*(position[1] - threat_velocity[1]) - threat_velocity[1]*(position[0] - threat_velocity[0])
        if abs(threat_velocity[0]) < 1e-10:
            return np.array([-1, 0]), 1
        elif abs(threat_velocity[1]) < 1e-10:
            return np.array([0, -1]), 1
        else:
            evasion = np.array([np.sign(torque)*1/threat_velocity[0], -np.sign(torque)*1/threat_velocity[1]])
            return evasion/np.linalg.norm(evasion), 1

    return prey[name].position - hunters[threat_name].position, 1


def basic_hunter(name, hunters, prey):
    target_range = np.inf
    target_name = None
    for target in prey.values():
        new_target_range = np.linalg.norm(hunters[name].position - target.position)
        if new_target_range < target_range:
            target_range = new_target_range
            target_name = target.name

    if target_name is None:
        return np.array([0, 0]), 0

    if np.linalg.norm(prey[target_name].velocity) < 1:
        return prey[target_name].position - hunters[name].position, 1

    tx = (hunters[name].position[0] - prey[target_name].position[0]) / (
            hunters[name].velocity[0] - prey[target_name].velocity[0])
    ty = (hunters[name].position[1] - prey[target_name].position[1]) / (
                hunters[name].velocity[1] - prey[target_name].velocity[1])
    t = (tx+ty)/2
    intercept_point = prey[target_name].velocity*t + prey[target_name].position

    return intercept_point - hunters[name].position, 1

