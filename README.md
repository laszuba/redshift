redshift
========

A simple 16-bit processor implemented in [MyHDL](http://www.myhdl.org/doku.php) (Python)

Architecture
------------

* 16-bit instruction set
* Instructions take one operand and operate on the working (w) register
* Harvard architecture with separate program and data memory busses

Registers
---------

    W     - (working) instructions operate on the working register
    PC    - (program counter) address of the next instruction
    PS    - (processor status) stores the status flags
    R0-R7 - general purpose

Instruction Set
---------------

### Arithmetic

    ADD - add
    SUB - subtract

### Logic

    AND - bitwise and
    OR  - bitwise or
    NOT - bitwise not
    XOR - bitwise exclusive or

### Program Flow and Moves

    MOV  - move register into or out of W, or move lower 8 bits immediate into W
    MOVT - move upper 8 bits immediate into W
    STR  - store W into address
    LDR  - load address into W
    B    - unconditional branch
    BNE  - branch if not zero
    BEQ  - branch if zero
    NOP  - no operation
