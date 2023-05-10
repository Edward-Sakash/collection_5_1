# Bonus 1 (Collections - Tuples of Fractions):
# Create a list of tuples where each tuple contains a number and its factors using list comprehension.
# numbers = [1, 2, 3, 4, 5] ----> [(1, [1]), (2, [1, 2]), (3, [1, 3]), (4, [1, 2, 4]), (5, [1, 5])]

# Solution 1
def get_factors(num):
    factors = [1]
    for i in range(2, num+1):
        if num % i == 0:
            factors.append(i)
    return factors

numbers = [1, 2, 3, 4, 5]
result = [(n, get_factors(n)) for n in numbers]

print("numbers = [1, 2, 3, 4, 5] ---->", result)  # Output: [(1, [1]), (2, [1, 2]), (3, [1, 3]), (4, [1, 2, 4]), (5, [1, 5])]

print("---------------------------------------------------")

# Solution 2
def factors(num):
    return [i for i in range(1, num+1) if num % i == 0]

numbers = [1, 2, 3, 4, 5]
result = [(num, factors(num)) for num in numbers]
print("numbers = [1, 2, 3, 4, 5] ---->", result)

