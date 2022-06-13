# MemoryGame

import random

# get a sequence length from the user
digits = input("How many digits do you want to guess: ")
digits = int(digits)

# create a random sequence
sequence = []
for i in range(0, digits):
    sequence.append(random.randint(0, 20))
print(sequence)

# show it for 3 seconds
import time
time.sleep(3)

#hide the numbers
for i in range(0, 20):
    print('')


# check user remember

for i in range(0, digits):
    print("Enter number at index "  + str(i))
    rem_num = int(input())
    if rem_num == sequence[i]:
        print('correct')
    else:
        print('wrong')
        break
print(sequence)

    
