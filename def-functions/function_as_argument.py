def power():
    return 200

def double(function):
    return function() * 2

result = double(power)

print(result)