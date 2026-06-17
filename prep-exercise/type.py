def half(value):
    return value / 2 

def double(value):
    return value * 2 

def second(value):
    return value[1]

print(half(22))
print(half("hello"))
print(half("22"))
    
print(double(22))
print(double("hello"))
print(double("22"))
    
print(second(22))
print(second(0x16))
print(second("hello"))
print(second("22"))


# First bug is half("hello"),
# python tries to /2 but division only works on numbers.
# second bug double("hello") again same issue, python tries to double it "hellohello" 
# but it might be unintended behavior.
# third bug second(22) as it expects indexable value(str or list)
# so it is going to crash at runtime.