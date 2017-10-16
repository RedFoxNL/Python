# convert an integer to a hex digit (a character)
def hex_char(value):
    if value <= 9 and value >= 0:
        print(chr(value + ord('0')))

    else:
        print(chr(value - 10 + ord('A')))


# convert a decimal to a hex as a string
def to_hex(decimal):
    decimal = decimal
    hex_char(decimal)
    print(decimal)
    return decimal


def main():
    hex_char(123)


main()

assert to_hex(12345) == '3039', 'Error'
assert to_hex(0) == '0', 'Error'