# Exercise 2: Write a program that categorizes each mail message by
# which day of the week the commit was done. To do this look for lines
# that start with “From”, then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print
# out the contents of your dictionary (order does not matter).

fhand = open('mbox-short.txt')
counts = {}
for lines in fhand:
    if lines.startswith('From'):
        words = lines.split()
        if len(words) > 3:
            counts[words[2]] = counts.get(words[2], 0) + 1
        else:
            continue
    else:
        continue

print(counts)
