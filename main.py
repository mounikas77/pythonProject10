# april-18 (iterators for abignacademy)
# definition for iterators
# # examples-1
# nums=[7,8,9,5]
# for i in nums:
#     print(i)
# o/p:7
# 8
# 9
# 5
##########################
from logging import exception


# ways of printing values
# 1.using index numbers
# nums=[7,8,9,5]
# print(nums[0])
# o/p:7
############################
# 2.using for loops
# nums=[7,8,9,5]
# for i in nums:
#     print(i)
# o/p:7
# 8
# 9
# 5
#############################

# how to create an iterator:
# nums=[7,8,9,5]
# it=iter(nums)
# print(it)
# o/p:<list_iterator object at 0x0000028CE5404580>
# note:--iter-- method returns the "iterator object"
####################################
# note:no object we need values or traversal elements so what to use then next method.
#--next--() method helps us traverse the elements in the iterable object.
# example:1
# nums=[7,8,9,5]
# it=iter(nums)
# print(it.__next__())
# o/p:7
##########################
# nums=[7,8,9,5]
# it=iter(nums)
# print(it.__next__())
# print(it.__next__())
# o/p:7
# 8
# note:I said that an iterator refers to an object in Python,so in every example contains list is an inbuilt object.
# qns: How do we create own object?

# for example:
# i print the top ten values:
# so we have how to create a our own iterator here we use the two methods that is,
# iter()-->gives object of iterator
# next()-->gives the next values


# class topten:
#     def __init__(self,num):
#         self.num=num
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num<=10:
#             val=self.num
#             self.num+=1
#             return val
#         else:
#              raise exception("Iteration completed")
# values=topten(5)
# print(next(values))
# for i in values:
#      print(i)

#######################################
# chatgpt example:
# class topten:
#     def __init__(self, num):
#         self.num = num
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.num <= 10:
#             val = self.num
#             self.num += 1
#             return val
#         else:
#             raise StopIteration("Iteration completed")
#
# try:
#     values = topten(5)
#     print(next(values))
#     for i in values:
#         print(i)
# except StopIteration as e:
#     print(e)
# o/p:5
# 6
# 7
# 8
# 9
# 10

#####################

# 1.iterating over list
# my_list = [1, 2, 3, 4, 5]
# for item in my_list:
#     print(item)
# o/p:1
# 2
# 3
# 4
# 5
#####################
# 2.iterating over strings
# my_string = "Hello"
# for char in my_string:
#     print(char)
# o/p:H
# e
# l
# l
# o
##########################
# 3.Iterating Over Dictionaries (Keys):
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# for key in my_dict:
#     print(key)
# o/p:a
# b
# c
#########################
# 4.iterating over dictionaries(values):
# my_dict={'a':1,'b':2,'c':3}
# for value in my_dict.values():
#     print(value)
# o/p:1
# 2
# 3
###################
# 5.iterating over dictionaries(key_value pairs)
# my_dict={'a':1,'b':2,'c':3}
# for key,value in my_dict.items():
#     print(key,value)
# o/p:a 1
# b 2
# c 3
#######################
# 6.using 'iter()' and 'next()':
# my_list = [1, 2, 3, 4, 5]
# my_iterator = iter(my_list)
# print(next(my_iterator))  # Output: 1
# print(next(my_iterator))  # Output: 2
# o/p:1
# 2
##########################3
# 7.using custom iterators:
# class MyIterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.data):
#             value = self.data[self.index]
#             self.index += 1
#             return value
#         else:
#             raise StopIteration

# my_list = [1, 2, 3, 4, 5]
# my_iterator = MyIterator(my_list)
# for item in my_iterator:
#     print(item)
# o/p:1
# 2
# 3
# 4
# 5
#####################












