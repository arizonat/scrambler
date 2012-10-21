scrambler
=========

Program to list all highest scoring words in Zynga's Scramble game. Code is original and programmed without looking at other solutions (as there have been quite a few versions that I have seen after completing this). Cannot recall where I found the lexicon, I will post soon, it was on another person's Google Code repo that I had to find afterwards, other lexicons do not work well with Scramble's.

General Usage/Algorithm:
To use, simply run:

> ./scrambler.py "<letters separated by spaces, 'qu' is needed for 'Qu'>"

and prints out the first 100 highest scoring words in descending order (so that the bottom of your terminal has the highest scoring words, no need to scroll up)

For example, a game board like:
a b c d
e f g h
i j k l
m n o qu

> ./scrambler.py "a b c d...m n o qu"
ae
on
lo
...
knife
jink

General Code Notes:
There is a lot of refactoring that needs to be done, since most of this is prototyping. There are several features lacking, and code structure can be greatly improved to allow for general game solving, currently it only handles 4x4 games with the precise rules of scramble. Also lacks the ability to handle different point-values of letters. Also a way to help you find the words faster would be nice (printing the entire path, or creating the GUI/image if you want to be super intense)