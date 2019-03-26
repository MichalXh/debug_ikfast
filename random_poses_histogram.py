#!/usr/bin/env python

from __future__ import print_function, division

from tqdm import tqdm
import numpy as np
from pyquaternion import Quaternion
import matplotlib.pyplot as plt

from ik_solver import get_iks

joint_states = []
failed = 0
for _ in tqdm(range(1000)):
    point = (np.random.random(3) - 0.5)
    iks = get_iks(point, Quaternion.random())
    if not iks:
        failed += 1
    joint_states.extend(iks)

print('failed', failed)
joint_states = np.array(joint_states)

plt.figure(1, clear=True)

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.hist(joint_states[:, i])
    plt.title('joint {}'.format(i))
plt.show()
