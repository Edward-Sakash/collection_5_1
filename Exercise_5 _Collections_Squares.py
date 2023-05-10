# Exercise 5 (Collections - Squares):
#Write a program that takes a list of numbers and returns a new list containing the squares of each number.
#use list comprehension
#numbers = [1, 2, 3, 4, 5] ---> [1, 4, 9, 16, 25]

def square_numbers(numbers):
    return [n**2 for n in numbers]

numbers = [1, 2, 3, 4, 5]
print("numbers = [1, 2, 3, 4, 5] --->", square_numbers(numbers))  # Output: [1, 4, 9, 16, 25]
