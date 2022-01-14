#!/usr/bin/python3

print("Hello World!")







#
# def uniq(list):
#     """ Returns unique values of a list """
#     u_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     for item in list:
#         if item not in u_list:
#             u_list.append(item)
#     return u_list
#
# # list = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 9, 10, (1, 2, 3), (1, 2, 3)]
# # list = uniq(list)
# list = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
# list = uniq(list)
#
# # import builtins
# # from inspect import getmembers, isclass, isfunction
#
# # for (name, memeber) in getmembers(builtins, isclass):
# #     print(name)
#
#
# # # help(functools.lru_cache)
# # # my_help = dir([])
# # my_help_class = help(["__class__"])
#
# # class User:
# #     """
# #     A Member of Class User storing name, birthday
# #     """
# #     def __init__(self, fullname, birthday) -> None:
#
# #         self.name  = fullname
# #         self.birthday = birthday # yyyymmdd
#
#
# #         name_peices = fullname.split(" ")
# #         self.first_name = name_peices[0]
# #         self.last_name = name_peices[-1]
#
# #     def age(self):
# #         pass
    
    
# print(help(User))


# user0 = User()
# user0.firstname = "Dave"
# user0.lastname = "Bowman"

# user1 = User()
# user1.firstname = "Frank"
# user1.lastname = "Something"

# user2 = User()
# user2.firstname = "Something"
# user2.lastname = "BEale"

# user3 = User()
# user3.firstname = "Random"
# user3.lastname = "Words"

# user4 = User()
# user4.firstname = "Wordz"
# user4.lastname = "Rand0m"


# FIB WITH DEFINED CACHE


# fibonacci_cache = {}

# def fibonacci(n):
#     if n in fibonacci_cache:
#         return fibonacci_cache[n]


#     if n == 1:
#         value = 1
#     elif n == 2:
#         value = 1
#     elif n > 2:
#         value = fibonacci(n-1) + fibonacci(n-2)

#     fibonacci_cache[n] = value
#     return value
    
# for n in range(1, 5):
#     print(n, ":", fibonacci(n))

# FIB WITH LRU CACHE



# @lru_cache
# def fibonacci_lru(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)

# for n in range(1, 5):
#     print(n, ":", fibonacci_lru(n))



# fibonacci_lru.cache_clear()


# cartesian_product

# A = []
# B = []

# for i in range(1, 100, 2):
#     A.append(i)

# for i in range(2, 101, 2):
#     B.append(i)

# cartesian_product = [(a, b) for a in A for b in B]
# print(cartesian_product)


