#!/usr/bin/python2.6

import sys
from copy import deepcopy

## This program is used to play the game "Scramble with Friends"
## TODO: Add DL, DW, TL, TW Bonuses to the tiles
## TODO: Print graphics/paths

thedict = {}
theprefixes = {}
thepoints = {}
thegame = {}
pointsmap = {}
foundWords = {}

# Read in the dictionary, ensure all lowercase
def loadDictionary(filename, prefix=True):
    with open(filename) as f:
        for word in f:
            word = word.strip().lower()
            thedict[word] = True
            
            if prefix:
                for i in xrange(len(word)):
                    theprefixes[word[0:i]] = True

# Load points map from a file
# Formatting should resemble:
# a\t10
def loadPoints(filename):
    with open(filename) as f:
        for line in f:
            line = line.split("\t")
            pointsmap[line[0]] = int(line[1])

# Save the prefixes only
def savePrefixes(filename):
    with open(filename,'w') as f:
        for prefix in theprefixes:
            f.write(prefix + "\n")

# Save the dictionary only
def saveDictionary(filename):
    with open(filename,'w') as f:
        for word in thedict:
            f.write(word + "\n")

# Loads a game using the provided game array
# which is a list of letters (or "Qu")
def loadGame(game_array):
    for j in range(4):
        for i in range(4):
            thegame[(i,j)] = game_array[i+4*j]

# Generate successors
def successors(pos):
    x,y = pos

    # Only the middle squares
    if x in range(1,3) and y in range(1,3):
        return ranger(x,y,-1,2,-1,2)
    
    # vertical sides
    elif x == 0 and y in range(1,3):
        return ranger(x,y,0,2,-1,2)

    elif x == 3 and y in range(1,3):
        return ranger(x,y,-1,1,-1,2)

    # horizontal sides
    elif x in range(1,3) and y == 3:
        return ranger(x,y,-1,2,-1,1)

    elif x in range(1,3) and y == 0:
        return ranger(x,y,-1,2,0,2)

    # corners
    elif (x,y) == (0,0):
        return ranger(x,y,0,2,0,2)

    elif (x,y) == (3,0):
        return ranger(x,y,-1,1,0,2)

    elif (x,y) == (3,3):
        return ranger(x,y,-1,1,-1,1)

    elif (x,y) == (0,3):
        return ranger(x,y,0,2,-1,1)

# Convenience function    
def ranger(x,y,xi,xj,yi,yj):
    return [(x+i,y+j) for i,j in
            [(i,j) for i in range(xi,xj)
                   for j in range(yi,yj)]]

def getWord(trail):
    word = "".join([thegame[pos] for pos in trail])
    return word

def getPoints(pos):
    return pointsmap[thegame[pos]]

def getLengthBonus(word):
    s = len(word)
    if s > 7:
        return 15
    elif s == 7:
        return 10
    elif s > 5:
        return 6
    elif s > 4:
        return 3
    else:
        return 0
    
def findWords(trail=[], points=0):
    # No words in the dictionary have length
    # greater than 24
    if len(trail) > 24:
        return

    if points == 0:
        points += getPoints(trail[-1])

    succs = successors(trail[-1])

    # Remove the trail from the successors to prevent collisions
    succs = list(set(succs).difference(set(trail)))

    for succ in succs:
        # Add successor to the trail
        newtrail = deepcopy(trail)
        newtrail.append(succ)

        # Check if word
        word = getWord(newtrail)
        if word in thedict:
            # Remember it
            foundWords[word] = points + getLengthBonus(word) + getPoints(succ)

            # Recursive call
            findWords(newtrail, points + getPoints(succ))
            
        # Check if prefix
        elif word in theprefixes:
            # Recursive call
            findWords(newtrail, points + getPoints(succ))

    # Nowhere left to turn
    return

def solve44():
    for x in range(4):
        for y in range(4):
            findWords([(x,y)])

def loadDefault():
    loadPoints("resources/points.txt")
    loadDictionary("resources/enable1.txt")    

# Main function
if __name__ == "__main__":
    loadPoints("resources/points.txt")
    loadDictionary("resources/enable1.txt")
    raw_game = sys.argv[1].split(" ")
    loadGame(raw_game)
    
    solve44()

    #l = sorted(foundWords, key=operator.itemgetter(1), reverse=True)
    l = sorted(foundWords, key=foundWords.get, reverse=True)
    print "Words found: " + str(len(l))

    newl = l[:100]
    newl.reverse()

    for word in newl:
        print word



