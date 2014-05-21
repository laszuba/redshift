redshift
========

A simple 16-bit processor implemented in [MyHDL](http://www.myhdl.org/doku.php) (Python)

Architecture
------------

* 16-bit instruction set
* Instructions take one operand and operate on the working (w) register
* Harvard architecture with separate program and data memory buses

## Execution

1. Fetch from program memory. Increment PC
2. Decode instruction, read reg file
3. Compute (ALU)
4. Memory operation (load/store)
5. Place result in register

Registers
---------

    W        - (working) instructions operate on the working register
    PS       - (processor status) stores the status flags
    Z  (R15) - tied to zero
    PC (R14) - (program counter) address of the next instruction
    I  (R9)  - input register, connected to input bus
    O  (R8)  - output register, connected to output bus
    R0-R7    - general purpose registers

Instruction Set
---------------

## Instruction Encoding

    XXXX XXXX XXXX XXXX
    |  | |  | |       |
    |  | |  | +-------+- Immediate low byte
    |  | +--+----------- First operand/Immediate high nibble
    +--+---------------- Instruction type

### Arithmetic

    ADD - add
    0000 XXXX 0000 0000

    SUB - subtract
    0001 XXXX 0000 0000


### Logic

    AND - bitwise and
    0010 XXXX 0000 0000

    OR  - bitwise or
    0011 XXXX 0000 0000

    NOT - bitwise not
    0100 XXXX 0000 0000

    XOR - bitwise exclusive or
    0101 XXXX 0000 0000

    LSL - logical shift left (pad with zeros)
    0110 XXXX 0000 0000

    LSR - logical shift right (pad with zeros)
    0111 XXXX 0000 0000

### Program Flow and Moves

    MOV  - move register into or out of W
    1000 XXXX 0000 0000

    MOVI - move immediate into W
    1001 XXXX XXXX XXXX

    STR  - store W into address
    1010 XXXX 0000 0000

    LDR  - load address into W
    1011 XXXX 0000 0000

    NOP  - no operation
    1100 0000 0000 0000

    B    - unconditional branch (ADD PC, W)
    1101 0000 0000 0000

    BNE  - branch if not zero (ADD PC, W)
    1110 0000 0000 0000

    BEQ  - branch if zero (ADD PC, W)
    1111 0000 0000 0000

