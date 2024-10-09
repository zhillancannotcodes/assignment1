x = int(input("Enter an integer: "))
prime = []


for numerator in range(2, x):
    boolprime = True
    for denominator in range(2, numerator):
        if numerator % denominator == 0:
            boolprime = False
            break
    if boolprime:
        prime.append(str(numerator))

print(f"All prime numbers less than {x}, is: {", ".join(prime)}")