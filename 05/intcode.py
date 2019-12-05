class Instruction:

    def __init__(self, intcode):
        self.intcode = intcode
        self.mem = intcode.memory

        modes = [
            mode == '1'
            for mode
            in f'{intcode.current():05}'[2::-1]]

        pointer = intcode.pointer
        self.og_ops = self.mem[pointer + 1: pointer + self.step]

        self.ops = [
            op if mode else self.mem[op]
            for op, mode
            in zip(self.og_ops, modes)
        ]

    def run(self):
        self._run()
        self.intcode.pointer += self.step


class AddInstruction(Instruction):
    step = 4

    def _run(self):
        self.mem[self.og_ops[2]] = self.ops[0] + self.ops[1]


class MulInstruction(Instruction):
    step = 4

    def _run(self):
        self.mem[self.og_ops[2]] = self.ops[0] * self.ops[1]


class ReadInstruction(Instruction):
    step = 2

    def _run(self):
        self.mem[self.og_ops[0]] = self.intcode.input


class WriteInstruction(Instruction):
    step = 2

    def _run(self):
        print(self.ops[0])


class JumpTrueInstruction(Instruction):
    step = 3

    def _run(self):
        if self.ops[0] != 0:
            self.intcode.pointer = self.ops[1] - self.step


class JumpFalseInstruction(Instruction):
    step = 3

    def _run(self):
        if self.ops[0] == 0:
            self.intcode.pointer = self.ops[1] - self.step


class LessThanInstruction(Instruction):
    step = 4

    def _run(self):
        self.mem[self.og_ops[2]] = int(self.ops[0] < self.ops[1])


class EqualsInstruction(Instruction):
    step = 4

    def _run(self):
        self.mem[self.og_ops[2]] = int(self.ops[0] == self.ops[1])


class HaltInstruction(Instruction):
    step = 0


class IntCode:

    def __init__(self, memory, input):
        self.memory = memory
        self.input = input
        self.pointer = 0

    def run(self):
        while True:
            instruction = self.next_instruction()
            if type(instruction) is HaltInstruction:
                break
            instruction.run()

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
            '99': HaltInstruction,
        }

        in_code = f'{self.current():05}'[-2:]
        return codes[in_code](self)

    def current(self):
        return self.memory[self.pointer]
