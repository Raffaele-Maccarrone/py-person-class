class Person:
    people = {}

    def __init__(self, name: str, age: str):
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    Person.people = {}
    for person in people:
        adra = person
        p = Person(adra["name"], adra["age"])
        Person.people[adra["name"]] = p
    for person in people:
        adra = person
        p = Person.people[adra["name"]]
        if "wife" in adra and adra["wife"] is not None:
            p.wife = Person.people[adra["wife"]]
        elif "husband" in adra and adra["husband"] is not None:
            p.husband = Person.people[adra["husband"]]
    return list(Person.people.values())
