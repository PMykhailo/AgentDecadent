import numpy as np


def perp(a):
    b = np.empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b

# line segment a given by endpoints a1, a2
# line segment b given by endpoints b1, b2
# return
# def seg_intersect(a1, a2, b1, b2):
#     da = a2 - a1
#     db = b2 - b1
#     dp = a1 - b1
#     dap = perp(da)
#     denom = np.dot(dap, db)
#     num = np.dot(dap, dp)
#     #print(num, denom)
#     if abs(denom.astype(float)) <1e-10:
#         if check_contained(a1,a2,b1) or check_contained(a1,a2,b2):
#             return True
#         print(num, denom.astype(float))
#         return None
#     return (num / denom.astype(float)) * db + b1
#
#
# def check_contained(a1,a2,b):
#     if abs(a2[0] - a1[0]) < 1e-14:
#         b_on = abs(b[0] - a2[0]) <1e-14
#         b_between = (min(a1[1], a2[1]) <= b[1] <= max(a1[1], a2[1]))
#     else:
#         slope = (a2[1] - a1[1]) / (a2[0] - a1[0])
#         b_on = (b[1] - a1[1]) == slope * (b[0] - a1[0])
#         b_between = (min(a1[0], a2[0]) <= b[0] <= max(a1[0], a2[0])) and (min(a1[1], a2[1]) <= b[1] <= max(a1[1], a2[1]))
#     return b_on and b_between


def on_segment(p, q, r):
    if r[0] <= max(p[0], q[0]) and r[0] >= min(p[0], q[0]) and r[1] <= max(p[1], q[1]) and r[1] >= min(p[1], q[1]):
        return True
    return False


def orientation(p, q, r):
    val = ((q[1] - p[1]) * (r[0] - q[0])) - ((q[0] - p[0]) * (r[1] - q[1]))
    if val == 0: return 0
    return 1 if val > 0 else -1


def intersects(seg1, seg2):
    p1, q1 = seg1
    p2, q2 = seg2

    o1 = orientation(p1, q1, p2)

    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and on_segment(p1, q1, p2): return True

    if o2 == 0 and on_segment(p1, q1, q2): return True
    if o3 == 0 and on_segment(p2, q2, p1): return True
    if o4 == 0 and on_segment(p2, q2, q1): return True

    return False
