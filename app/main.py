class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        person_data = person
        p = Person.people[person_data["name"]]
        wife = person_data.get("wife")
        if wife:
            p.wife = Person.people[person_data["wife"]]
        husband = person_data.get("husband")
        if husband:
            p.husband = Person.people[person_data["husband"]]
    return person_list
