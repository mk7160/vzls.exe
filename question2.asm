INCLUDE Irvine32.inc

TITLE Question 1
; Name: Michael Khosho
; Date: 9/26/23
; ID: 105 029 603
; This assembly language code will initialize y and x and then will add 4 to y and then multiple by 3 and store into x 

.code
main PROC
    ; Load Y into a register
    movzx eax, byte [Y]

    ; Add 4 to Y
    add eax, 4

    ; Multiply by 3
    shl eax, 1  ; Multiply by 2
    add eax, eax  ; Multiply by 2 again (equivalent to multiplying by 4)
    add eax, eax  ; Multiply by 2 again (equivalent to multiplying by 8)

    ; Store the result (X) in ebx
    mov ebx, eax

    ; Call DumpReg to show the output
    call DumpRegs

    ; Exit the program
    exit
main ENDP
END main