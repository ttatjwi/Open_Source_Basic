def is_prime_number(x):
    for num in range(2, x):
        if x <= 1:
            print("Error: The input value should be larger than 1".format(num1=x))
            return
    print("The number {num1} is a prime number.".format(num1=x))
