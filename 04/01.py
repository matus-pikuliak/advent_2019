total = 0
for i in range(402328, 864247 + 1):
    num = str(i)
    if sorted(num) != list(num):
        continue
    if any(num[j] == num[j+1] for j in range(5)):
        total += 1
print(total)

