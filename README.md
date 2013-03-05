redshift
========

A simple 16-bit processor implemented in MyHDL (Python)

Architecture
------------

* 16-bit instruction set
* Instructions take one operand and operate on the working (w) register
* Harvard architecture with separate program and data memory buses

Registers
---------

    W        - (working) instructions operate on the working register
    PC       - (program counter) address of the next instruction
    PS       - (processor status) stores the status flags
    Z  (R15) - tied to zero
    I  (R9)  - input register, connected to input bus
    O  (R8)  - output register, connected to output bus
    R0-R7    - general purpose registers

Instruction Set
---------------

* No support for load immediate
* Immediate values must come from data memory

### Arithmetic

    ADD - add
    SUB - subtract

### Logic

    AND - bitwise and
    OR  - bitwise or
    NOT - bitwise not
    XOR - bitwise exclusive or

### Program Flow and Moves

    MOV - move register into or out of W
    STR - store W into address
    LDR - load address into W
    B   - unconditional branch
    BNE - branch if not zero
    BEQ - branch if zero
    NOP - no operation (pseudo instruction - ADD Z)
