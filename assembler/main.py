import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="the path of the jjasm file")
parser.add_argument("output", help="the path of the rom file you want to output")
args = parser.parse_args()


def assemble(file, output):
	file = open(file, "r")
	os.system(f"echo   > {output}")
	jjrom = open(output, "wb")
	for line in file.readlines():
		line = line.split(" ")
		match line[0]:
			case "lda":
				jjrom.write(b"\xf2")
				jjrom.write(b"\xff")
				value = chr(int(line[1]))
				jjrom.write(f"{value}".encode())
			case "ldx":
				jjrom.write(b"\x95")
				jjrom.write(b"\xff")
				value = chr(int(line[1]))
				jjrom.write(f"{value}".encode())
			case "ldy":
				jjrom.write(b"\x93")
				jjrom.write(b"\xff")
				value = chr(int(line[1]))
				jjrom.write(f"{value}".encode())
			case "jmp":
				jjrom.write(b"\xf3")
				jjrom.write(b"\xff")
				value = chr(int(line[1]))
				jjrom.write(f"{value}".encode())
			case "sta":
				jjrom.write(b"\x99")
				jjrom.write(b"\xf9")
				value = chr(int(line[2]))
				jjrom.write(f"{value}".encode())
			case "stx":
				jjrom.write(b"\x83")
				jjrom.write(b"\xf9")
				value = chr(int(line[2]))
				jjrom.write(f"{value}".encode())
			case "sty":
				jjrom.write(b"\x85")
				jjrom.write(b"\xf9")
				value = chr(int(line[2]))
				jjrom.write(f"{value}".encode())
			case "rd":
				jjrom.write(b"\xf5")
				jjrom.write(b"\xf9")
				value = chr(int(line[2]))
				jjrom.write(f"{value}".encode())
			case "ldxm":
				jjrom.write(b"\xd9")
				jjrom.write(b"\xf9")
				value = chr(int(line[2]))
				jjrom.write(f"{value}".encode())
			case "ldym":
				jjrom.write(b"\xd8")
				jjrom.write(b"\xf9")
				value = chr(int(line[2]))
				jjrom.write(f"{value}".encode())
			case "in":
				jjrom.write(b"\xd7")
				jjrom.write(b"\xf9")
				value = chr(int(line[2]))
				jjrom.write(f"{value}".encode())
			case "add":
				jjrom.write(b"\x92")
				jjrom.write(b"\xf9")
				value = chr(int(line[2]))
				jjrom.write(f"{value}".encode())
			case "mul":
				jjrom.write(b"\xd2")
				jjrom.write(b"\xf9")
				value = chr(int(line[2]))
				jjrom.write(f"{value}".encode())
			case "sub":
				jjrom.write(b"\x97")
				jjrom.write(b"\xf9")
				value = chr(int(line[2]))
				jjrom.write(f"{value}".encode())
			case "div":
				jjrom.write(b"\xd5")
				jjrom.write(b"\xf9")
				value = chr(int(line[2]))
				jjrom.write(f"{value}".encode())
			case "brk":
				jjrom.write(b"\xfc")
				jjrom.write(b"\xff")
				value = chr(int(line[1]))
				jjrom.write(f"{value}".encode())
	file.close()
	jjrom.close()


assemble(args.file, args.output)
