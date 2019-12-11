class IntCode:

    def __init__(self, memory):
        self.mem = memory + [0] * 1000
        self.pointer = 0
        self.rel = 0

    def run(self):
        while True:
            current = f'{self.mem[self.pointer]:05}'
            instruction = current[-2:]
            if instruction == '99':
                break

            modes = [
                int(mode)
                for mode
                in current[2::-1]]

            ops = []
            for i, op in enumerate(self.mem[self.pointer + 1: self.pointer + 4]):
                if modes[i] == 0:
                    ops.append(op)
                if modes[i] == 1:
                    ops.append(self.pointer + i + 1)
                if modes[i] == 2:
                    ops.append(op + self.rel)

            if instruction == '01':
                self.mem[ops[2]] = self.mem[ops[0]] + self.mem[ops[1]]
                self.pointer += 4

            if instruction == '02':
                self.mem[ops[2]] = self.mem[ops[0]] * self.mem[ops[1]]
                self.pointer += 4

            if instruction == '03':
                self.mem[ops[0]] = yield
                yield
                self.pointer += 2

            if instruction == '04':
                yield self.mem[ops[0]]
                self.pointer += 2

            if instruction == '05':
                if self.mem[ops[0]] != 0:
                    self.pointer = self.mem[ops[1]]
                else:
                    self.pointer += 3

            if instruction == '06':
                if self.mem[ops[0]] == 0:
                    self.pointer = self.mem[ops[1]]
                else:
                    self.pointer += 3

            if instruction == '07':
                self.mem[ops[2]] = int(self.mem[ops[0]] < self.mem[ops[1]])
                self.pointer += 4

            if instruction == '08':
                self.mem[ops[2]] = int(self.mem[ops[0]] == self.mem[ops[1]])
                self.pointer += 4

            if instruction == '09':
                self.rel += self.mem[ops[0]]
                self.pointer += 2
