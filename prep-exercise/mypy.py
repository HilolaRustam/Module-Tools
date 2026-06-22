def double(number):
    return number * 3

print(double(10))


# when checked with mypy --strict it pointed to two errors 
# first missing annotation on line 1 
# secondly in line 4 call to untyped function in typed context. 
# but it did not notice that in  we are putting *3
# so mypy is good for helping us to check the types.