# epl = {
#     "man_city": 98,
#     "villa": 92,
#     "arsenal": 90
# }

# # for c, p in epl.items():
# #     print(c, p)

# print(list(epl.values()))

# dict_1 = {"foo":"bar", "egg":"nog", "2": "tuu"}
# dict_2 = {"foo":"baz", 2:"two"}

# # dict_1.update(dict_2)

# print({**dict_2, **dict_1})

#########################################################################

# count = int(input("How many numbers?\n> "))
# nums = []

# for idx in range(count):
#     nums.append(float(input(f"enter num {idx + 1} of {count}\n> ")))

# def average(*args):
#     print(args)
#     total = 0
#     for arg in args:
#         total += arg
#     return round(total / len(args), 2)

# print(average(*nums))

#########################################################################

def student_score(first, last, *score):
    print(f"{first.capitalize()} {last.capitalize()} scored {score}")

# student_score(input("first\t"), input("last\t"), *[input("score 1\t"),input("score 2\t"),input("score 3\t")])
student_score("Mary")






#########################################################################