# 替换字符
s = 'hello'
# s[0] = 'H' 不允许
s = 'H' + s[1:]
s = s.replace('h', 'H')
print(s)

str1 = "ver"
str2 = "sion"
str1 += str2  # 表示 str1 = str1 + str2
print(str1)
# Python首先会检测str1还有没有其他的引用。
# 如果没有的话，就会尝试原地扩充字符串buffer的大小，
# 而不是重新分配一块内存来创建新的字符串并拷贝

id = 123
name = "fdskjafds"
# 字符串格式化
print('no data available for person with id: {}, name: {}'.format(id, name))
