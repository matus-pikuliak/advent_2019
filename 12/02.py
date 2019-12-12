import numpy as np

init = np.loadtxt('input', dtype=np.int)
pos = np.loadtxt('input', dtype=np.int)
vel = np.zeros((4, 3), dtype=np.int)
cyc = {}

for step in range(10**10):

    for dim in range(3):
        if (
            step != 0
            and dim not in cyc
            and np.array_equal(pos[:, dim], init[:, dim])
            and np.count_nonzero(vel[:, dim]) == 0
        ):
            cyc[dim] = step

    for i in range(4):
        for j in range(3):
            vel[i, j] += sum(pos[i, j] < pos[:, j]) - sum(pos[i, j] > pos[:, j])
    pos += vel

    if len(cyc) == 3:
        print(cyc)
        break
