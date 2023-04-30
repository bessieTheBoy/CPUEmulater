
class MEMORY:
	memory = []
	def initialize(self):
		for i in range(127):
			self.memory.append(0)

	def write(self, addr, value):
		self.memory[addr] = value

	def read(self, addr):
		return self.memory[addr]

mem = MEMORY()
mem.initialize()
