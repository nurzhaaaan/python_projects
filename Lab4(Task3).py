nums = []
for i in range(20, 51):
    if i % 3 == 0 and i % 5 != 0:
        nums.append(i)
print("Numbers divisible by 3 but not by 5:", nums)

