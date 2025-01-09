#Write a Python Program to Check Prime Number

def is_prime(number):
    if number <= 1:
        return False  # 1 and numbers less than or equal to 1 are not prime

    # Check for factors from 2 to the square root of the number
    for i in range(2, number):
        if (number % i) == 0:
            return False  # Number has a factor other than 1 and itself

    return True  # Number is prime

# Example usage:
user_input = int(input("Enter a number to check if it's prime: "))

if is_prime(user_input):
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")




# list of prime number

def prime_list(number):
    primes = []
    
    for num in range(2, number + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        
    return primes
        
print(prime_list(5)) 
