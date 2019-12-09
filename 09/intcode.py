class Instruction:

    def __init__(self, intcode):
        self.intcode = intcode
        self.mem = intcode.memory

        modes = [
            int(mode)
            for mode
            in f'{intcode.current():05}'[2::-1]]

        pointer = intcode.pointer
        ops = self.mem[pointer + 1: pointer + self.step]
        self.wr_ops = []
        self.re_ops = []
        for i, op in enumerate(ops):
            if modes[i] == 0:
                self.wr_ops.append(op)
                self.re_ops.append(self.mem[op])
            if modes[i] == 1:
                self.wr_ops.append(None)
                self.re_ops.append(op)
            if modes[i] == 2:
                self.wr_ops.append(op + self.intcode.rel)
                self.re_ops.append(self.mem[op + self.intcode.rel])


    def run(self):
        self._run()
        self.intcode.pointer += self.step


class AddInstruction(Instruction):
    step = 4

    def _run(self):
        self.mem[self.wr_ops[2]] = self.re_ops[0] + self.re_ops[1]


class MulInstruction(Instruction):
    step = 4

    def _run(self):
        self.mem[self.wr_ops[2]] = self.re_ops[0] * self.re_ops[1]


class ReadInstruction(Instruction):
    step = 2

    def _run(self):
        self.mem[self.wr_ops[0]] = self.intcode.input.pop()


class WriteInstruction(Instruction):
    step = 2

    def _run(self):
        self.intcode.output.append(self.re_ops[0])
        # print(self.ops[0])


class JumpTrueInstruction(Instruction):
    step = 3

    def _run(self):
        if self.re_ops[0] != 0:
            self.intcode.pointer = self.re_ops[1] - self.step


class JumpFalseInstruction(Instruction):
    step = 3

    def _run(self):
        if self.re_ops[0] == 0:
            self.intcode.pointer = self.re_ops[1] - self.step


class LessThanInstruction(Instruction):
    step = 4

    def _run(self):
        self.mem[self.wr_ops[2]] = int(self.re_ops[0] < self.re_ops[1])


class EqualsInstruction(Instruction):
    step = 4

    def _run(self):
        self.mem[self.wr_ops[2]] = int(self.re_ops[0] == self.re_ops[1])


class RelBaseInstruction(Instruction):
    step = 2

    def _run(self):
        self.intcode.rel += self.re_ops[0]


class HaltInstruction(Instruction):
    step = 0


class IntCode:

    def __init__(self, memory, input):
        self.memory = memory + [0] * 1000
        self.input = list(reversed(input))
        self.output = []
        self.pointer = 0
        self.rel = 0

    def run(self):
        while True:
            instruction = self.next_instruction()
            if type(instruction) is HaltInstruction:
                break
            instruction.run()
            if type(instruction) is WriteInstruction:
                input = yield self.output[-1]
                self.input.append(input)

    def next_instruction(self):

        codes = {
            '01': AddInstruction,
            '02': MulInstruction,
            '03': ReadInstruction,
            '04': WriteInstruction,
            '05': JumpTrueInstruction,
            '06': JumpFalseInstruction,
            '07': LessThanInstruction,
            '08': EqualsInstruction,
            '09': RelBaseInstruction,
            '99': HaltInstruction,
        }

        in_code = f'{self.current():05}'[-2:]
        return codes[in_code](self)

    def current(self):
        return self.memory[self.pointer]
