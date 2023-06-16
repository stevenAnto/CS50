people = [
        {"name":"harrey","houyrse":"Arequipa"},
        {"name":"Esteven","house":"Puno"},
        {"name":"Draco","house":"Juliaca"}
        ]

"""
def f(person):
    return person["name"]
"""
people.sort(key=lambda person: person["name"])
print(people)
