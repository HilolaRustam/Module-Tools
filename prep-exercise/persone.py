class Person:
    def __init__(self, name: str, age: int, address:str, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.address = address 
        self.preferred_operating_system = preferred_operating_system

imran = Person("Imran", 22, "London", "Ubuntu")
print(imran.name)
print(imran.address) # person.py error: "Person" has no attribute "address"  [attr-defined]

eliza = Person("Eliza", 34, "London", "Arch Linux")
print(eliza.name)
print(eliza.address)  # person.py error: "Person" has no attribute "address"  [attr-defined]

def is_adult(person: Person) -> bool:
    return person.age >= 18

print(is_adult(imran)) 


# Because there is no address attribute in the Person class 
# mypy does not accept line 9 and line 13
# so we have to add self.address = address and define the type on def.
# then I add the address to person details. 