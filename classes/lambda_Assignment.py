user_infos = [
    {"username": "Josoon", "age": 23, "tweets": ["I wanna eat", "i love sugar", "Baby pana, I get big cassave"],
     "verification": True},
    {"username": "Awodele", "age": 53, "tweets": ["I dey go", "This Nigeria", "This life is beautiful"],
     "verification": False},
    {"username": "Pasuma", "age": 18, "tweets": ["Awon awo ruggedy", "Tinapa eyan osapa", "Tigalaga shina  tipa",
                                                 "Oya je ka lepo"],
     "verification": True},
    {"username": "KissDaniel", "age": 44, "tweets": ["Let's tata", "i love you baby"], "verification": True},
    {"username": "Kosewe", "age": 29, "tweets": [], "verification": False},
    {"username": "Johanna", "age": 33,
     "tweets": ["Jerusalema", "Burna for life", "Proudly Machala", "Froggy sucks.Lol"],
     "verification": True},
    {"username": "Maryanne", "age": 60, "tweets": ["I belong to Jesus"], "verification": True},
    {"username": "LittleSnake", "age": 20, "tweets": ["Badda than bad", "i hate the truth", "Fuck y'all!!",
                                                      "Y'all sucks"],
     "verification": True},
    {"username": "Ozo", "age": 31, "tweets": ["Thank Jah for the gift of life", "Jah"], "verification": False},
    {"username": "Hennessy", "age": 36, "tweets": ["I love drinking", "Make we go party now", "Trophy", "Budweiser"],
     "verification": True}
]

print([user_info['username'] for user_info in user_infos if user_info["tweets"] != []])
print(list(map(lambda x: x['username'] if x["tweets"] != [] else False, user_infos)))
print([user_info['username'] for user_info in user_infos if user_info["age"] < 25 and user_info["verification"]])
print(list(map(lambda x: x['username'], filter(lambda x: x['username'] if x["age"] < 25 and x["verification"] else False, user_infos))))

# average_calc =
print()

