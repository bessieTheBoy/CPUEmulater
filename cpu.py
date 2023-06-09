from instructions import *
from memory import MEMORY


class CPU:
	registers = {"a": 0, "x": 0, "y": 0}
	last_instruction = 0
	arg_reg = 0
	mem = MEMORY()
	history = []
	run_inst_reg = None
	pg = 0


	def process_instruction(self, instruction):
		instruction.process(self)

	def __init__(self):
		self.mem.initialize()

	def run_file(self, rom, start_byte=0):
		self.pg = start_byte
		file = open(rom, "rb")
		file = list(file.read())
		history = self.history
		starting_mem_address = False
		starting_int = False
		running = True
		while running:
			try:
				byte = file[self.pg]
			except IndexError:
				print("END OF FILE shutting down (tip: remember to use 'brk 0' at the end of files)")
				exit()
			if byte == 0xf2:
				self.run_inst_reg = LDA(self)
				self.pg += 1
				 
				history.append({"inst": self.run_inst_reg, "arg_reg": self.arg_reg})
			elif byte == 0xf3:
				self.run_inst_reg = JMP(self)
				 
				self.pg += 1
			elif byte == 0x99:
				self.run_inst_reg = STA(self)
				 
				self.pg += 1
				history.append({"inst": self.run_inst_reg, "arg_reg": self.arg_reg})
			elif byte == 0xf9:
				starting_mem_address = True
				self.pg += 1
			elif byte == 0xff:
				starting_int = True
				self.pg += 1
			elif byte == 0xf5:
				self.run_inst_reg = RD(self)
				 
				self.pg += 1
				history.append({"inst": self.run_inst_reg, "arg_reg": self.arg_reg})
			elif byte == 0x83:
				self.run_inst_reg = STX(self)
				 
				self.pg += 1
				history.append({"inst": self.run_inst_reg, "arg_reg": self.arg_reg})
			elif byte == 0x85:
				self.run_inst_reg = STY(self)
				 
				self.pg += 1
				history.append({"inst": self.run_inst_reg, "arg_reg": self.arg_reg})
			elif byte == 0x95:
				self.run_inst_reg = LDX(self)
				 
				self.pg += 1
				history.append({"inst": self.run_inst_reg, "arg_reg": self.arg_reg})
			elif byte == 0x93:
				self.run_inst_reg = LDY(self)
				 
				self.pg += 1
				history.append({"inst": self.run_inst_reg, "arg_reg": self.arg_reg})
			elif byte == 0x92:
				self.run_inst_reg = ADD(self)
				 
				self.pg += 1
				history.append({"inst": self.run_inst_reg, "arg_reg": self.arg_reg})
			elif byte == 0xd2:
				self.run_inst_reg = MUL(self)
				 
				self.pg += 1
				history.append({"inst": self.run_inst_reg, "arg_reg": self.arg_reg})
			elif byte == 0x97:
				self.run_inst_reg = SUB(self)
				 
				self.pg += 1
				history.append({"inst": self.run_inst_reg, "arg_reg": self.arg_reg})
			elif byte == 0xd5:
				self.run_inst_reg = DIV(self)
				 
				self.pg += 1
				history.append({"inst": self.run_inst_reg, "arg_reg": self.arg_reg})
			elif byte == 0xd9:
				self.run_inst_reg = LDXM(self)
				 
				self.pg += 1
				history.append({"inst": self.run_inst_reg, "arg_reg": self.arg_reg})
			elif byte == 0xd8:
				self.run_inst_reg = LDYM(self)
				 
				self.pg += 1
				history.append({"inst": self.run_inst_reg, "arg_reg": self.arg_reg})
			elif byte == 0xd7:
				self.run_inst_reg = IN(self)
				 
				self.pg += 1
				history.append({"inst": self.run_inst_reg, "arg_reg": self.arg_reg})
			elif byte == 0xfc:
				self.run_inst_reg = BRK(self)
				 
				self.pg += 1
				history.append({"inst": self.run_inst_reg, "arg_reg": self.arg_reg})
			else:
				self.arg_reg = byte
				self.run_inst_reg.process(self)
				self.last_instruction = self.run_inst_reg
				self.pg += 1
					
			self.history = history

