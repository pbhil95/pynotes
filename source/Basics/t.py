
from collections import deque

numbers = deque()
numbers.append(99)
numbers.append(15)
numbers.append(82)
numbers.append(50)
numbers.append(47)
print(numbers)
first_item = numbers.popleft()
print(first_item)
print(numbers)
