""":return
Assignment from coursera course:  Introduction to Data Science in Python
"""

# ------------------------------- Parte A - Find all names in the string

import re


def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    return re.findall(r'Amy|Mary|Ruth|Peter', simple_string)


# print(names())

# ------------------------------------ Part B - Obtain the grades B in the file grades.txt


def grades():
    with open("grades.txt", "r") as file:
        notas = file.read()
    return re.findall(r"\w+ \w+: B", notas)


# print(grades())

# Part C


def logs():
    # texto = '146.204.224.152 - feest6811 [21/Jun/2019:15:45:24 -0700] "POST /incentivize HTTP/1.1" 302 4622'
    with open("logdata.txt", "r") as file:
        data = file.read()
    return re.findall(r'^[0-9]*', data)


print(logs())

one_item = {
    'host': '146.204.224.152',
    'user_name': 'feest6811',
    'time': '21/Jun/2019:15:45:24 -0700',
    'request': 'POST /incentivize HTTP/1.1'
}

# assert one_item in logs(), "Sorry, this item should be in the log results, check your formating"


pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
    print("Search successful.")
else:
    print("Search unsuccessful.")
