n = int(input())
def fizzbuzz(n):
    for j in range(1, n + 1):
        if j % 15 == 0:
            print("FizzBuzz")
        elif j % 3 == 0:
            print("Fizz")
        elif j % 5 == 0:
            print("Buzz")
        else:
            print(str(i))
fizzbuzz(n)
