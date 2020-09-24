import sys
import string

letters = list(string.ascii_letters)
numbers = list(range(10))
allowed = letters + numbers

txt = sys.argv[1]
print(''.join([f':meow_{t}:' if t in allowed else f'{t}   ' for t in txt]))
