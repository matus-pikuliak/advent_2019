from intcode import intcode

mem = [
    int(num)
    for num
    in open('input').read().split(',')
]

mem[1] = 12
mem[2] = 2

print(intcode(mem)[0])
