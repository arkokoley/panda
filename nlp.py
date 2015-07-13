#!/usr/bin/env python
import string
import sys

def getMeaning(Input):
# Looks for words that need to be searched in wiki
    s = "what does is about tell me who".split()
    p = [x for x in Input[1:] if x not in list(set(s).intersection(Input))]
    t = 1

# Looks for words that need to be found in dict
    d = "the of mean meaning".split()
    m = [x for x in p if x not in list(set(d).intersection(p))]
    if(p != m):
        t = 2
        p = m
    return (t," ".join(p))

if __name__ == "__main__":
    print getMeaning(sys.argv)
