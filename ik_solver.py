#!/usr/bin/env python

from __future__ import print_function, division

import os
import subprocess32 as subprocess


def get_iks(position, orientation):
    """
    Args:
        position (iterable): [x, y, z]
        orientation (pyquaternion): tooltip orientaiton
        robot_name (str): robot name to call correct ik solver

    Returns:
       List of robot configuration, where robot configuration is list of joint
       positions [j1, j2, j3, j4, j5, j6]
    """
    args = _transformation_to_ik_arguments(position, orientation)
    ik_executable = '{}/ik'.format(os.path.dirname(os.path.abspath(__file__)))
    args = [ik_executable] + args
    try:
        with open(os.devnull, 'w') as devnull:
            s = subprocess.check_output(args, stderr=devnull)
    except subprocess.CalledProcessError as e:
        if e.returncode == 255:
            return []
        else:
            raise

    configs = _ik_output_to_list_of_configurations(s)
    return configs


def _transformation_to_ik_arguments(position, orientation):
    T = orientation.transformation_matrix
    T[:, -1][:-1] = position
    return [str(element) for element in T[:-1].reshape(-1)]


def _ik_output_to_list_of_configurations(s):
    lines = [l for l in s.split('\n') if l.startswith('sol')]
    configs = []
    for line in lines:
        line = line[line.find(':') + 1:]
        config = [float(pos) for pos in line.split(',') if pos.strip()]
        configs.append(config)

    return configs
