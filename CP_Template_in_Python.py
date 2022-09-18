'''
This is a template to speed up Python code in competitive programming
with some added functionalities. This template takes input from
input.txt file and prints results to output.txt file. For more speed
submit this code under PyPy which is a compiled version.

@author: Samir Paul
'''
from __future__ import division, print_function
import os
import io
import re
import sys
import math
import time
import heapq
import runpy
import types
import shlex
import bisect
import pprint
import random
import string
import decimal
import pathlib
import asyncio
import operator
import builtins
import argparse
import fractions
import functools 
import itertools
import statistics
import collections
from sys import stdin, stdout  
from io import BytesIO, IOBase
from math import gcd, floor, sqrt, log, factorial
from bisect import bisect_left, bisect_right
from collections import deque, Counter, defaultdict, OrderedDict, namedtuple, UserDict, UserList, UserString

inp    =lambda: int(input())
strng  =lambda: input().strip()
jn     =lambda x,l: x.join(map(str,l))
strl   =lambda: list(input().strip())
mul    =lambda: map(int,input().strip().split())
mulf   =lambda: map(float,input().strip().split())
seq    =lambda: list(map(int,input().strip().split()))
ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1
flush  =lambda: stdout.flush()
stdstr =lambda: stdin.readline()
stdint =lambda: int(stdin.readline())
stdpr  =lambda x: stdout.write(str(x))
MOD = 1000000007

sys.setrecursionlimit(100000000)
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

# region fastio
BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b: break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()

if sys.version_info[0] < 3: sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else: sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

input = lambda: sys.stdin.readline().rstrip("\r\n")













# ---------------- I/O file handling ----------------------
# sys.stdout = open('output.txt', 'w') # Write to output.txt
# sys.stdin = open('input.txt', 'r') # Read from input.txt

# -------------------- Code From Here ---------------------
class Solution:
    def main():

        # Code Here

        t = int(input()) 
        for case in range(1, t+1):

            n = int(input()) 
            arr = list(map(int, input().split(' ')))
               
            print(f"Case #{case}: {arr}")














# ----------------------- End Code -----------------------

if __name__ == '__main__':
    Solution.main()
