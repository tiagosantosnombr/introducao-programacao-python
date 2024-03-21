num = 6 / 7
outro_num = 10
t1 = "Hello"
t2 = "World"

print('num: {0:f}'.format(num)) # Standard display of floating point with six decimal places.
print('num: {0:.2f}'.format(num)) # Formats with two decimal places.
print('num: {0:8.2f}'.format(num)) #  Formats with two decimal places, limited to eight characters, with left-aligned white space padding.
print('num: {0:8d}'.format(outro_num)) # Formats with a minimum of eight characters (left-aligned), padding with whitespace if necessary.
print('{0:10}{1:10}'.format(t1, t2)) # Formats with at least ten characters, no alignment
print('{0:^10}{1:^10}'.format(t1, t2)) # Formats with at least ten characters, centered
print('{0:>10}{1:>10}'.format(t1, t2)) # Formats with at least ten characters, right-aligned
