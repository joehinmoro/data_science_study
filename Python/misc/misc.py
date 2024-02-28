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

# def student_score(first, last, *score):
#     print(f"{first.capitalize()} {last.capitalize()} scored {score}")

# # student_score(input("first\t"), input("last\t"), *[input("score 1\t"),input("score 2\t"),input("score 3\t")])
# student_score("Mary")

#########################################################################

def age(num, **callee):
    
    print(f"{num} age records:")
    for person, age in callee:
        print(f"{person} is {age} years old")

age =  input()


#########################################################################

ocean_temperatures = {
    'Pacific': [25, 25.3, 25.6, 25.2, 25.5, 25.6],
    'Atlantic': [23.4, 23.8, 23.7, 29.9, 24.0, 29.1],  # Exclude > 29
    'Indian': [26.5, 26.7, 27.0, -29, -55, -99, -99]    # Exclude < 0
}

{key: (min([temp for temp in val if 0 < temp < 29]), max([temp for temp in val if 0 < temp < 29])) for key, val in ocean_temperatures.items() }

[num ** 2 for num in [num for num in range(21) if not num & 1] if not num % 4 if num]


[l.upper() for l in "hello"]

[i for i in range(10) if not i & 1 if i]

