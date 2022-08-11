# Exercise 5: This program records the domain name (instead of the
# address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.

fhand = open('mbox-short.txt')
counts = {}
for lines in fhand:
    if not lines.startswith('From'):
        continue
    words = lines.split()
    if len(words) > 3:
        domains = words[1].split('@')
        counts[domains[1]] = counts.get(domains[1], 0) + 1

# big_key = None
# big_value = None
# for key, value in counts.items():
#     if big_value is None or value > big_value:
#         big_value = value
#         big_key = key
#
# print(big_key, big_value)
print(counts)
