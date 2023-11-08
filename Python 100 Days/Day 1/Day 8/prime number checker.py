def prime_checker(number):
    """This function checks if a number is prime or not
    and prints the answer in a display format"""
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

        if is_prime:
            print("It's a prime number")
        else:
            print("It's not a prime number")


n = int(input("check this number:"))
prime_checker(number=n)

#for n in range(2, 100):
    #prime_checker(number=n)

