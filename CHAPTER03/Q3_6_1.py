import random

numbers = [str(i) for i in range(10)]
sample4 = random.sample(numbers, k=4)
num4 = "".join(sample4)

while input() != num4:
    print("NG")

print("OK")
