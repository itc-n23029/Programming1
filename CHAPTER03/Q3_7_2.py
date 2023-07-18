with open("number.txt", "r") as f:
    total_sum = sum(int(data) for data in f)
    print(total_sum)
