#!/usr/bin/env python
import json
import random

base_string = 'is the most fun a girl can have without taking her clothes off, but it\'s better if you do.'

with file('verbs','r') as f:
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
    sys.path.append('../twitterbot')
    import tb
    TB = tb.Twitterbot()
    TB.api.PostUpdate(makeString())
