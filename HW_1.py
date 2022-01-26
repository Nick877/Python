str = 'String'
i = 10
fl = 5.7
bt = bytes([35, 36, 37])
ll = [str, i, 'text', False, 50]
tu = ('texts', True, 3.14, fl)
s = {'hi','bye'}
fr = frozenset({'hi',3, 'bye'})
d = {'number':23, 2: True, 'my_list':[1,2,3]}
print((type(str), str), (type(i), i), (type(fl), fl), (type(bt), bt), (type(ll), ll), (type(tu), tu), (type(s), s), (type(fr), fr), (type(d), d))
s_1 = 'first'
s_2 = 'second'
can = s_1 + s_2
print(can)

print(str, i, sep=', ')
print(str, i, sep=' + ')