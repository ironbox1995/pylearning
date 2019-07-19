# 字典在3.7之后为有序
d = {'name': 'jason', 'age': 20}
d.get('name')
'jason'
d.get('location', 'null')
'null'
# 可防止报错

d.pop('dob')
# 删除键为'dob'的元素对

d = {'b': 1, 'a': 2, 'c': 10}
d_sorted_by_key = sorted(d.items(), key=lambda x: x[0]) # 根据字典键的升序排序
d_sorted_by_value = sorted(d.items(), key=lambda x: x[1]) # 根据字典值的升序排序
# d_sorted_by_key
# [('a', 2), ('b', 1), ('c', 10)]
# d_sorted_by_value
# [('b', 1), ('a', 2), ('c', 10)]

# 字典是一个哈希表，可直接通过键找到值，查找的时间复杂度为O（1）
# 而列表则是O（logn）
# 字典的键必须是不可变类型
