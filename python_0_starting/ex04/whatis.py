import sys

if len(sys.argv) < 2:
    print()
    sys.exit(0)

try:
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided\n")

    try:
        val = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer\n")

    if val == 0 or val % 2 == 0:
        print("I'm Even.\n")
    else:
        print("I'm Odd.\n")

except AssertionError as error:
    print(f"AssertionError: {error}")
    sys.exit(1)
