def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


print(factorial(5))
number = 5
result = factorial(number)
print(f" the factorial of {number} is {result}")
