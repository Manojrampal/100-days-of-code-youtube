# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1


# factorial(n) = n * factorial(n-1)
def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)


print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1

# Quick Quiz: Write a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(3) = f(2) + f(1)
# f(n) = f(n-1) + f(n-2)

# 0 1 1 2 3 5 8....
#0,1,1,2,3,5,8,13,21,34,55,89....


def fibonacci(n):

	if n <=1:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))

output = 8

To calculate value of Fibonacci(6) means getting value of 6th series.
fibonacci(6)

=f5 +f4
=(f4+f3)+(f3+f2)
=(f3+f2+f3)+(f3+f2)
=3*f3+2*f2
=3*(f1+f0+f1)+2*f1+2*f0 --as {f1=1, f0=0}
=3*2+2*1
=6+2
=8

To get value of first 10 values we have to sent fibonacci(0), Fibonacci(1), Fibonacci(2) and so on... so we use a for loop with range 10 for first 10 numbers.

#print ([fibonacci(i) for i in range(10)])

[Program finished][0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
