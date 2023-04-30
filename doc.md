lda: loads a int into the a register (hex: f2)<br>
ldx: loads a int into the x register (hex: 95)<br>
ldy: loads a int into the x register (hex: 93)<br>
ldxm: loads the int in the memory address given into the x register (hex: d9)<br>
ldym: loads the int in the memory address given into the y register (hex: d8)<br>
sta: copy the a register into the memory address given (hex: 99)<br>
stx: copy the x register into the memory address given (hex: 83)<br>
sty: copy the y register into the memory address given (hex: 85)<br>
add: adds the x and y and puts the output into the memory address given (hex: 92)<br>
mul: multiplies the x and y register and puts the output into the memory address given (hex: d2)<br>
sub: subtracts the x and y register and puts the output into the memory address given (hex: 97)<br>
div: divides the x and y register and puts the output into the memory address given (hex: d5)<br>
rd: prints out the value in the memory address given (hex: f5)<br>
in: asks for input then stores it in the memory address given (hex: d7)<br>
brk: stops the cpu and prints out the exit code given (hex: fc)<br>
jmp: jumps to a specific byte (hex: f3)<br>
<br>
<br>
NOTES:<br>
1. for jump since it jumps to a specific byte you CANNOT input a line number if you want to jump to a specific line each line is 3 bytes<br>
2. THE MAX INT IS 127 because of chr function (accepting fixes i made a issue in github)<br>
3. if your looking at the hex in your rom F9 means starting memory address and FF means starting int<br>
