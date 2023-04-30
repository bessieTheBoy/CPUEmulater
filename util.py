

def int_to_text(integer):
	hex_ = chr(integer)
	return bytearray.fromhex(hex_).decode()