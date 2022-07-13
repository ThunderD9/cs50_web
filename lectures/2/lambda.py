people = [
    {"name":"Harry", "house": "Fag"},
    {"name":"White", "house": "Racist"},
    {"name":"Black", "house": "Nigga"}
]



people.sort(key = lambda person: person["name"])
print(people)