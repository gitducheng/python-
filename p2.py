# coding=utf-8

counter = 100 # 整型变量
miles = 100.0 # 浮点型
name = "pydc" # 字符串

print(counter, miles, name)

# 多变量赋值
a = b = c = 1
a, b, c = 1, 2, 'pydc'

print(a, b, c)

# 删除del
del a
# print(a) # 报错

# 字符串截取
s = "abcdefg"
s1 = s[0]
s2 = s[1:3]
print(s1)
print(s2)
print(s2 * 2)

# 字典（对象）
dict = {}
dict['one'] = "this is one"
dict[2] = "this is 2"
tinydict = {"name": "pydc", "code": 123}
print(dict["one"])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
