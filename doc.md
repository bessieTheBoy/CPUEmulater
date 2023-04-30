lda: loads a int into the a register (hex: f2)\n
ldx: loads a int into the x register (hex: 95)\n
ldy: loads a int into the x register (hex: 93)
ldxm: loads the int in the memory address given into the x register (hex: d9)
ldym: loads the int in the memory address given into the y register (hex: d8)
sta: copy the a register into the memory address given (hex: 99)
stx: copy the x register into the memory address given (hex: 83)
sty: copy the y register into the memory address given (hex: 85)
add: adds the x and y and puts the output into the memory address given (hex: 92)
mul: multiplies the x and y register and puts the output into the memory address given (hex: d2)
sub: subtracts the x and y register and puts the output into the memory address given (hex: 97)
div: divides the x and y register and puts the output into the memory address given (hex: d5)
rd: prints out the value in the memory address given (hex: f5)
in: asks for input then stores it in the memory address given (hex: d7)
brk: stops the cpu and prints out the exit code given (hex: fc)
jmp: jumps to a specific byte (hex: f3)


NOTES:
1. for jump since it jumps to a specific byte you CANNOT input a line number if you want to jump to a specific line each line is 3 bytes
2. THE MAX INT IS 127 because of chr function (accepting fixes i made a issue in github)
3. if your looking at the hex in your rom F9 means starting memory address and FF means starting int
