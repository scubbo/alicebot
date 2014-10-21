#!/usr/bin/env python
import os, os.path
import json
import random

base_string = 'is the most fun a girl can have without taking her clothes off, but it\'s better if you do.'

cwd = os.path.dirname(os.path.abspath(__file__))

with file(cwd + os.path.sep + 'verbs','r') as f:
    verbs = json.load(f)

def getVerb():
    return random.choice(verbs)

def makeString():
    verb = getVerb()
    prospective = ' '.join([verb.title(), base_string])
    if len(prospective) <= 140:
        return prospective
    else:
        return makeString()

if __name__ == '__main__':
    import sys
    sys.path.append(cwd + os.path.sep + os.path.pardir + os.path.sep + 'twitterbot')
    import tb
    os.chdir(cwd)
    TB = tb.Twitterbot()
    TB.api.PostUpdate(makeString())
