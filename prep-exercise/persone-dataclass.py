from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str

imran = Person("Imran", date(2004, 4, 15), "Ubuntu")  # We can call this constructor - @dataclass generated it for us.
print(imran)  

imran2 = Person("Imran", date(2004, 4, 15), "Ubuntu")
print(imran == imran2)  # Prints True