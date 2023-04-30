class Instruction:
	def process(self, cpu):
		pass


class LDA(Instruction):
	def process(self, cpu):
		cpu.registers["a"] = cpu.arg_reg


class LDX(Instruction):
	def process(self, cpu):
		cpu.registers["x"] = cpu.arg_reg


class LDY(Instruction):
	def process(self, cpu):
		cpu.registers["y"] = cpu.arg_reg


class STA(Instruction):
	def process(self, cpu):
		cpu.mem.write(cpu.arg_reg, cpu.registers["a"])


class STX(Instruction):
	def process(self, cpu):
		cpu.mem.write(cpu.arg_reg, cpu.registers["x"])


class STY(Instruction):
	def process(self, cpu):
		cpu.mem.write(cpu.arg_reg, cpu.registers["y"])


class RD(Instruction):
	def process(self, cpu):
		print(cpu.mem.read(cpu.arg_reg))


class ADD(Instruction):
	def process(self, cpu):
		cpu.mem.write(cpu.arg_reg, cpu.registers["x"] + cpu.registers["y"])


class MUL(Instruction):
	def process(self, cpu):
		cpu.mem.write(cpu.arg_reg, cpu.registers["x"] * cpu.registers["y"])


class SUB(Instruction):
	def process(self, cpu):
		cpu.mem.write(cpu.arg_reg, cpu.registers["x"] - cpu.registers["y"])


class DIV(Instruction):
	def process(self, cpu):
		cpu.mem.write(cpu.arg_reg, cpu.registers["x"] / cpu.registers["y"])


class LDXM(Instruction):
	def process(self, cpu):
		cpu.registers["x"] = cpu.mem.read(cpu.arg_reg)


class LDYM(Instruction):
	def process(self, cpu):
		cpu.registers["y"] = cpu.mem.read(cpu.arg_reg)


class IN(Instruction):
	def process(self, cpu):
		cpu.mem.write(cpu.arg_reg, int(input("INPUT: ")))


class JMP(Instruction):
	def process(self, cpu):
		cpu.run_file("test.rom", start_byte=cpu.arg_reg)


class BRK(Instruction):
	def process(self, cpu):
		print("BRK called shutting down...")
		print(f"EXIT CODE: {cpu.arg_reg}")
		exit()