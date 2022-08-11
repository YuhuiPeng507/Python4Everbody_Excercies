# Exercise 4: Add code to the above program to figure out who has the
# # most messages in the file. After all the data has been read and the dic-
# # tionary has been created, look through the dictionary using a maximum
# # loop (see Chapter 5: Maximum and minimum loops) to find who has
# # the most messages and print how many messages the person has.

fhand = open('mbox-short.txt')
counts = {}
for lines in fhand:
    if not lines.startswith('From'):
        continue
    words = lines.split()
    if len(words) > 3:
        counts[words[1]] = counts.get(words[1], 0) + 1

big_key = None
big_value = None
for key, value in counts.items():
    if big_value is None or value > big_value:
        big_value = value
        big_key = key

print(big_key, big_value)
