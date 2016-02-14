#!/usr/bin/env python

def applyFuns(L,x):
    for f in L:
        print(f(x))
        
applyFuns([abs, int], -4)
