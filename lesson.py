# def oldest(person1):                  # 1 - misol
#     i = 0
#     while i < len(person1):
#         a = max(person1)
#         i += 1
#         return f"the oldest person is {a}"
# print(oldest({
#   "Emma": 71,
#   "Jack": 45,
#   "Amy": 15,
#   "Ben": 29
# }))
#
# print(oldest({
#   "Max": 9,
#   "Josh": 13,
#   "Sam": 48,
#   "Anne": 33
# }))


"https://edabit.com/challenge/5KqHNS9wS97zN7Xyy"            # 2 - misol



# def top_note(*qwargs):                # 3 - misol
#     i = 0
#     while i < len(qwargs):
#         a = qwargs[i]
#         b = a.get("notes")
#         i += 1
#         return max(b)
#
#
# print(top_note({"name": "John", "notes": [3, 5, 4]}))


# def profit(lst):                  # 4 - misol
#     i = 0
#     while i < len(lst):
#         a = lst.get("cost_price")
#         b = lst.get("sell_price")
#         d = lst.get("inventory")
#
#         cost = b - a
#         total = d * cost
#         i += 1
#         return total
#
#
# print(profit({
#   "cost_price": 32.67,
#   "sell_price": 45.00,
#   "inventory": 1200
# }))


# def mapping(letters):             # 5 - misol
#     result = {}
#     i = 0
#     while i < len(letters):
#         result[letters[i].lower()] = letters[i].upper()
#         i += 1
#     return result
# print(mapping(["p", "s"]))


# ------------------------------------------------------------------------------------


# List

# def total_volume(*t_volume):                   # 1- misol
#    i = 0
#    result = 0
#    while i < len(t_volume):
#        list = t_volume[i]
#        a = list[0] * list[1] * list[2]
#        result += a
#        i += 1
#    return result
#
# print(total_volume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1]))
# print(total_volume([2, 2, 2], [2, 1, 1]))



# def index_multiplier(lst):                # 2 - msiol
#     i = 0
#     result = 0
#     while i < len(lst):
#         a = enumerate(lst[i])
#         i += 1
#         print(a)
#
#
#
# print(index_multiplier([1, 2, 3, 4, 5]))


# def is_subset(lst, lst2):                 # 3 - misol
#     i = 0
#     while i < len(lst):
#         a = set(lst)
#         b = set(lst2)
#         i += 1
#         return a.issubset(b)
#
# print(is_subset([3, 2, 5], [5, 3, 7, 9, 2]))


"https://edabit.com/challenge/ASpHKyuSXZL3MjL92"   # 4-misol


# def unique_sort(lst):                 # 5 - misol
#     i = 0
#     a = []
#     while i < len(lst):
#         b = lst[i]
#         if i not in lst:
#             a.append(b)
#         i += 1
#         return sorted(a)
#
# print(unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]))
