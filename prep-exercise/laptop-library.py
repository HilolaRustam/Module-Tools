from dataclasses import dataclass
from enum  import Enum
from typing import List
import sys


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem 


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system:
            possible_laptops.append(laptop)
    return possible_laptops


laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH,),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU,),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU,),
    Laptop(id=4, manufacturer="Apple", model="MacBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS,),
]

name = input("Name: ")
age_input = input("Age: ")
os_input = input("Preferred operating system: ")

try:
    age = int(age_input)
except ValueError:
    print("Age must be a number", file=sys.stderr)
    sys.exit(1)
    
try:
    preferred_os = OperatingSystem(os_input)
except ValueError:
    print(
        "Operating system must be one of: macOS, Arch Linux, Ubuntu",
        file=sys.stderr,
    )
    sys.exit(1)    
    
person = Person(
    name=name,
    age=age,
    preferred_operating_system=preferred_os,
)    

possible_laptops = find_possible_laptops(laptops, person)

print(
    f"we have {len(possible_laptops)} laptop(s) with "
    f"{person.preferred_operating_system.value}."
)

ubuntu_count = 0
arch_count = 0 
macos_count = 0 


for laptop in laptops:
    if laptop.operating_system == OperatingSystem.UBUNTU:
        ubuntu_count += 1
    elif laptop.operating_system == OperatingSystem.ARCH:
        arch_count += 1 
    elif laptop.operating_system == OperatingSystem.MACOS:
        macos_count += 1    
        
        
preferred_count = len(possible_laptops)        
       
best_os = OperatingSystem.UBUNTU
best_count = ubuntu_count

if arch_count > best_count:
    best_os = OperatingSystem.ARCH
    best_count = arch_count
    
if macos_count > best_count:
    best_os = OperatingSystem.MACOS
    best_count = macos_count
    
 
if best_count > preferred_count:
    print(
         f"If you're willing to accept {best_os.value}, "
        f"you're more likely to get a laptop because "
        f"we have {best_count} available."
    )
           
           