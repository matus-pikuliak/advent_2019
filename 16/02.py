signal = [int(char) for line in open('input') for char in line] * 10000
index = int(open('input').read()[:7])

for _ in range(100):
    sum = 0
    for i in range(len(signal), index, -1):
        sum += signal[i-1]
        signal[i-1] = sum % 10

for i in range(8):
    print(signal[i + index], end='')



