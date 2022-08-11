# Exercise 3: Write a program to read through a mail log, build a his-
# togram using a dictionary to count how many messages have come from
# each email address, and print the dictionary.

fhand = open('mbox-short.txt')
counts = dict()
for lines in fhand:
    if lines.startswith('From'):
        words = lines.split()
        if len(words) > 3:
            counts[words[1]] = counts.get(words[1], 0)+1

print(counts)
