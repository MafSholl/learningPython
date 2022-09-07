# file_obj = open("file.txt", mode="w")
# print("i believe love can only make the world go round", file=file_obj)
# print("My world is not complete without you", file=file_obj)
# print("I only seek two things in life: to love you and to be loved by you", file=file_obj)

# file_obj = open("file.txt", mode="r")
#
# for line in file_obj.


# JSON OBJECT FILE
import json
config_dict = {
    "name": "Adeola",
    "age": 18,
    1: "Birthday",
    "hobby":[1,2,3,4],
    "bool": True
}

with open("config.json", mode='w') as file_obj:
    json.dump(config_dict, file_obj, indent=4, separators=(',', ':'))