# LeetCode imports #############################################################

# coding: utf-8
from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *

import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import statistics
import itertools
import functools
import operator
import io
import sys
import json
import builtins

# import precompiled.__settings__
# from precompiled.__deserializer__ import __Deserializer__
# from precompiled.__deserializer__ import DeserializeError
# from precompiled.__serializer__ import __Serializer__
# from precompiled.__utils__ import __Utils__
# from precompiled.listnode import ListNode
# from precompiled.nestedinteger import NestedInteger
# from precompiled.treenode import TreeNode

from typing import *

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

################################################################################

import os
import ast
import argparse

def parse_test_cases(file_path, num_args):
    inputs = []
    with open(file_path) as f:
        lines = f.readlines()
    
    test_cases_count = len(lines) // num_args
    
    for i in range(test_cases_count):
        case_inputs = []
        for j in range(num_args):
            case_inputs.append(ast.literal_eval(lines[i * num_args + j].strip()))
        
        inputs.append(tuple(case_inputs))
    
    return inputs

def run_solution(problem_name, method_name, num_args):
    try:
        solution_file = os.path.join(problem_name, "solution.py")
        test_cases_file = os.path.join(problem_name, "testcases.txt")
        
        # Create a local context for exec to run solution.py
        solution_globals = {}
        # Add all global imports to solution_globals
        for name in dir(builtins):
            solution_globals[name] = getattr(builtins, name)
        for name in dir(__builtins__):
            solution_globals[name] = getattr(__builtins__, name)

        # Add all imports from main.py to the globals
        solution_globals.update(globals())  # Update with current globals

        with open(solution_file) as f:
            exec(f.read(), solution_globals)  # Execute solution.py in the context of solution_globals
        
        if 'Solution' not in solution_globals:
            print(f"No Solution class found in {solution_file}")
            return
        
        solution_instance = solution_globals['Solution']()
        
        # Parse the test cases
        inputs = parse_test_cases(test_cases_file, num_args)
        
        # Run the tests and print outputs
        for i, input_case in enumerate(inputs):
            # Call the specified method on the Solution instance
            result = getattr(solution_instance, method_name)(*input_case)
            print(f"Test case {i + 1}: {input_case} -> {result}")
    
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
    except AttributeError as e:
        print(f"Method '{method_name}' not found in Solution class.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run solution with specified test cases.')
    parser.add_argument('problem_name', type=str, nargs='?', default='.', help='Name of the problem folder (default: current directory)')
    parser.add_argument('method_name', type=str, help='Name of the method in the Solution class')
    parser.add_argument('num_args', type=int, help='Number of input arguments the method takes')
    
    args = parser.parse_args()
    run_solution(args.problem_name, args.method_name, args.num_args)