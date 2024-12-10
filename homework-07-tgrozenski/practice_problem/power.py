# 10. Write a Python program to calculate the value of 'a' to the power of 'b' using recursion.
# Test Data :
# (power(3,4) -> 81

def calculate_power(num: int, power: int, total: int = 1):
    if(power == 0):
        return total
    power -= 1
    return calculate_power(num , power, total * num )

print(calculate_power(2,6))
print(calculate_power(3,4))
print(calculate_power(9,3))