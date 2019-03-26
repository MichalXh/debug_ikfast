#!/usr/bin/env python

from __future__ import print_function, division

from tqdm import tqdm
import numpy as np
from pyquaternion import Quaternion

from ik_solver import get_iks

for i in tqdm(range(1000)):
    point = (np.random.random(3) - 0.5)
    configurations = get_iks(point, Quaternion())
    # configurations = get_iks(point, Quaternion(axis=(1, 0, 0), degrees=1))
    if configurations:
        print()
        print('got a solution at step', i)
        break
else:
    print("couldn't find a solution!")

for conf in configurations:
    print(conf)
