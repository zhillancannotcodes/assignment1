def int_to_hexa(n):
    hex_digits = "0123456789ABCDEF"
    hex_str = ""

    if n == 0:
        return "0x0"

    while n > 0:
        remainder = n % 16
        hex_str = hex_digits[remainder] + hex_str
        n //= 16

    return "0x" + hex_str

num = int(input("Enter an integer: "))
print(f"The hexadecimal of {num}: {int_to_hexa(num)}")