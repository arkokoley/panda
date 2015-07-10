#!/usr/bin/env python
import sys
from nlp import *
from pandawiki import *
from proj import *

(t,word) = getMeaning(sys.argv)
if(t == 1):
    print "Looking up wiki entry for",word
    wikisearch(word)
if(t == 2):
    print "Looking up the dictionary entry for",word
    dictionary(word)
