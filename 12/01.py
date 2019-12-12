import numpy as np

pos = np.loadtxt('input', dtype=np.int)
vel = np.zeros((4, 3), dtype=np.int)

for _ in range(1000):
    for i in range(4):
        for j in range(3):
            vel[i, j] += sum(pos[i, j] < pos[:, j]) - sum(pos[i, j] > pos[:, j])
    pos += vel


pos = np.sum(np.abs(pos), axis=1)
vel = np.sum(np.abs(vel), axis=1)
print(pos, vel)
print(sum(pos * vel))