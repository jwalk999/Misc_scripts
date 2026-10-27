BINARY_VALUES = [128, 64, 32, 16, 8, 4, 2, 1]

HEX_VALUES = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
}

HEX_DIGITS = "0123456789ABCDEF"

# Errors are wrapped in ! ! for easier parsing.


def convert_decimal_to_8bit_binary(number: str) -> str | None:
    """Manually convert decimal value to 8bit binary"""
    # Error handling: make sure the string is a whole number.
    try:
        x = int(number)
    except ValueError:
        print(f"!'{number}' is not a whole number.!")
        return None
    # 8bit binary can only hold 0 to 255.
    if x < 0 or x > 255:
        print("!can only convert numbers (0 to 255)!")
        return None
    # Use subtraction to assign binary value. Store bits as strings.
    binary = []
    for i in BINARY_VALUES:
        if i <= x:
            x = x - i
            binary.append("1")
        else:
            binary.append("0")

    return "".join(binary)


def convert_8bit_binary_to_decimal(number: str) -> int | None:
    """Manually convert 8bit binary to decimal value"""
    # Make sure string is 8 characters long.
    if len(number) != 8:
        print("!please only enter 8bit binary!")
        return None
    # Make sure there are only 1s and 0s in the string.
    for i in number:
        if i != "1" and i != "0":
            print("!binary must only use 1s and 0s!")
            return None

    # Multiply each digit by its matching place value.
    running_total = 0
    for x, y in zip(number, BINARY_VALUES):
        running_total += int(x) * y

    return running_total


def convert_8bit_binary_to_hex(number: str) -> str | None:
    """Manually convert 8bit binary to hexadecimal value"""
    # Make sure string is 8 characters long.
    if len(number) != 8:
        print("!please only enter 8bit binary!")
        return None
    # Make sure there are only 1s and 0s in the string.
    for i in number:
        if i != "1" and i != "0":
            print("!binary must only use 1s and 0s!")
            return None

    # Turn each bit into its place value, then split into 2 nibbles.
    byte = []
    for x, y in zip(number, BINARY_VALUES):
        byte.append(int(x) * y)
    n = 4
    nibble = [byte[z : z + n] for z in range(0, len(byte), n)]

    # Convert each nibble into its hex character.
    first_character = 0
    second_character = 0
    for bit1, bit2 in zip(nibble[0], nibble[1]):
        first_character += bit1 // 16
        second_character += bit2
    if first_character >= 10:
        first_character = HEX_VALUES[first_character]
    if second_character >= 10:
        second_character = HEX_VALUES[second_character]

    return f"{first_character}{second_character}"


def convert_hex_to_decimal(number: str) -> int | None:
    """Manually convert 2-character hexadecimal to decimal value"""
    # Check hex length.
    if len(number) != 2:
        print("!hex only has 2 characters!")
        return None
    # Compare each character to the valid hex digits.
    for i in number:
        if i not in HEX_DIGITS:
            print("!wrong format!")
            return None
    # A character's position in HEX_DIGITS is its value (0 to 15).
    first_character = HEX_DIGITS.index(number[0])
    second_character = HEX_DIGITS.index(number[1])
    return (first_character * 16) + second_character


def convert_hex_to_8bit_binary(number: str) -> str | None:
    """Convert hexadecimal to 8bit binary by going through decimal"""
    decimal_value = convert_hex_to_decimal(number)
    if decimal_value is None:
        return None
    return convert_decimal_to_8bit_binary(str(decimal_value))


def convert_decimal_to_hex(number: str) -> str | None:
    """Convert decimal to hexadecimal by going through binary"""
    binary_value = convert_decimal_to_8bit_binary(number)
    if binary_value is None:
        return None
    return convert_8bit_binary_to_hex(binary_value)


def show_result(result) -> None:
    """Print a conversion result, unless the converter returned None."""
    if result is not None:
        print(result)


def main() -> None:

    while True:
        choice = (
            input(
                "\nWhat would you like to convert from?\n"
                "(b)inary\n"
                "(d)ecimal\n"
                "(h)exadecimal\n"
                "(q)uit\n"
            )
            .strip()
            .lower()
        )

        if choice == "b":
            which_one = input("\nTo what?\n(d)ecimal\n(h)exadecimal\n").strip().lower()
            if which_one == "d":
                user_input = input("Enter 8bit binary: ").strip()
                show_result(convert_8bit_binary_to_decimal(user_input))
            elif which_one == "h":
                user_input = input("Enter 8bit binary: ").strip()
                show_result(convert_8bit_binary_to_hex(user_input))
            else:
                print("Not a recognized option.")

        elif choice == "d":
            which_one = input("\nTo what?\n(b)inary\n(h)exadecimal\n").strip().lower()
            if which_one == "b":
                user_input = input("Enter decimal number: ").strip()
                show_result(convert_decimal_to_8bit_binary(user_input))
            elif which_one == "h":
                user_input = input("Enter decimal number: ").strip()
                show_result(convert_decimal_to_hex(user_input))
            else:
                print("Not a recognized option.")

        elif choice == "h":
            which_one = input("\nTo what?\n(b)inary\n(d)ecimal\n").strip().lower()
            if which_one == "b":
                user_input = input("Enter hex number: ").strip().upper()
                show_result(convert_hex_to_8bit_binary(user_input))
            elif which_one == "d":
                user_input = input("Enter hex number: ").strip().upper()
                show_result(convert_hex_to_decimal(user_input))
            else:
                print("Not a recognized option.")

        elif choice == "q":
            break

        else:
            print("Not a recognized option.")


if __name__ == "__main__":
    main()
