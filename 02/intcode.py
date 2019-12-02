def intcode(mem):
    for i in range(0, len(mem), 4):
        if mem[i] == 1:
            mem[mem[i + 3]] = mem[mem[i + 1]] + mem[mem[i + 2]]
        elif mem[i] == 2:
            mem[mem[i + 3]] = mem[mem[i + 1]] * mem[mem[i + 2]]
        else:
            break
    return mem
