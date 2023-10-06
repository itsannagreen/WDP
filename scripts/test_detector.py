import os
import re

files = [f.split(".")[0] for f in os.listdir("tests")]
tests_dict = dict()

for file in files:
    file_number = re.findall(r"\d+", file)[-1]
    file_name = file[:len(file) - len(file_number)]
    if file_name in tests_dict.keys():
        tests_dict[file_name] = max(tests_dict[file_name], int(file_number))
    else:
        tests_dict[file_name] = int(file_number)

for test_name, tests_number in tests_dict.items():
    print(test_name, tests_number)