import numpy as np


def perp(a):
    b = np.empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b

# line segment a given by endpoints a1, a2
# line segment b given by endpoints b1, b2
# return
def seg_intersect(a1, a2, b1, b2):
    da = a2 - a1
    db = b2 - b1
    dp = a1 - b1
    dap = perp(da)
    denom = np.dot(dap, db)
    num = np.dot(dap, dp)
    #print(num, denom)
    if denom.astype(float) <1e-10:
        if check_contained(a1,a2,b1) or check_contained(a1,a2,b2):
            return True
        return None
    return (num / denom.astype(float)) * db + b1


def check_contained(a1,a2,b):
    if abs(a2[0] - a1[0]) < 1e-14:
        b_on = abs(b[0] - a2[0]) <1e-14
        b_between = (min(a1[1], a2[1]) <= b[1] <= max(a1[1], a2[1]))
    else:
        slope = (a2[1] - a1[1]) / (a2[0] - a1[0])
        b_on = (b[1] - a1[1]) == slope * (b[0] - a1[0])
        b_between = (min(a1[0], a2[0]) <= b[0] <= max(a1[0], a2[0])) and (min(a1[1], a2[1]) <= b[1] <= max(a1[1], a2[1]))
    return b_on and b_between
