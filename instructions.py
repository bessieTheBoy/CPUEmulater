import math

class Instruction:
	def __init__(self, cpu):
		self.cpu = cpu
		self.arg_reg = cpu.arg_reg
	def process(self, cpu):
		pass


class LDA(Instruction):
	def __init__(self, cpu):
		super().__init__(cpu)
	def process(self, cpu):
		cpu.registers["a"] = cpu.arg_reg


class LDX(Instruction):
	def __init__(self, cpu):
		super().__init__(cpu)
	def process(self, cpu):
		cpu.registers["x"] = cpu.arg_reg


class LDY(Instruction):
	def __init__(self, cpu):
		super().__init__(cpu)
	def process(self, cpu):
		cpu.registers["y"] = cpu.arg_reg


class STA(Instruction):
	def __init__(self, cpu):
		super().__init__(cpu)
	def process(self, cpu):
		cpu.mem.write(cpu.arg_reg, cpu.registers["a"])


class STX(Instruction):
	def __init__(self, cpu):
		super().__init__(cpu)
	def process(self, cpu):
		cpu.mem.write(cpu.arg_reg, cpu.registers["x"])


class STY(Instruction):
	def __init__(self, cpu):
		super().__init__(cpu)
	def process(self, cpu):
		cpu.mem.write(cpu.arg_reg, cpu.registers["y"])


class RD(Instruction):
	def __init__(self, cpu):
		super().__init__(cpu)
	def process(self, cpu):
		print(cpu.mem.read(cpu.arg_reg))


class ADD(Instruction):
	def __init__(self, cpu):
		super().__init__(cpu)
	def process(self, cpu):
		cpu.mem.write(cpu.arg_reg, cpu.registers["x"] + cpu.registers["y"])


class MUL(Instruction):
	def __init__(self, cpu):
		super().__init__(cpu)
	def process(self, cpu):
		cpu.mem.write(cpu.arg_reg, cpu.registers["x"] * cpu.registers["y"])


class SUB(Instruction):
	def __init__(self, cpu):
		super().__init__(cpu)
	def process(self, cpu):
		cpu.mem.write(cpu.arg_reg, cpu.registers["x"] - cpu.registers["y"])


class DIV(Instruction):
	def __init__(self, cpu):
		super().__init__(cpu)
	def process(self, cpu):
		cpu.mem.write(cpu.arg_reg, cpu.registers["x"] / cpu.registers["y"])


class LDXM(Instruction):
	def __init__(self, cpu):
		super().__init__(cpu)
	def process(self, cpu):
		cpu.registers["x"] = cpu.mem.read(cpu.arg_reg)


class LDYM(Instruction):
	def __init__(self, cpu):
		super().__init__(cpu)
	def process(self, cpu):
		cpu.registers["y"] = cpu.mem.read(cpu.arg_reg)


class IN(Instruction):
	def __init__(self, cpu):
		self.thing = 0
		super().__init__(cpu)
	def process(self, cpu):
		exec(f"self.thing = " + input("INPUT: "))
		cpu.mem.write(cpu.arg_reg, self.thing)


class JMP(Instruction):
	def __init__(self, cpu):
		super().__init__(cpu)
	def process(self, cpu):
		cpu.run_file("test.rom", start_byte=cpu.arg_reg)




class BRK(Instruction):
	def __init__(self, cpu):
		super().__init__(cpu)
	def process(self, cpu):
		print("BRK called shutting down...")
		print(f"EXIT CODE: {cpu.arg_reg}")
		exit()
