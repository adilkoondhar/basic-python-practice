from itertools import count

for i in count(3):
    print(i)

    if i >= 10:
        break

from itertools import accumulate, takewhile

numbers = list(accumulate(range(5)))
print(numbers)

print(list(takewhile(lambda x: x < 6, numbers)))