import random

str_input = input()
for i in range(5):
    print(''.join(random.sample(str_input, len(str_input))), end=", ")

