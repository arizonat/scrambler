import sys

max = 0

with open(sys.argv[1]) as f:
    for word in f:
       if len(word) > max:
           max = len(word)

print max
    
