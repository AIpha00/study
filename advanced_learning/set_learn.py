# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
# intersection取交集
print(valid.intersection(input_set))
# difference 取差集
print(valid.difference(input_set))


is_fat = False
state = "fat" if is_fat else "not fat"
print(state)

fat = True
fitness = ("skinny", "fat")[fat]
print("Ali is", fitness)