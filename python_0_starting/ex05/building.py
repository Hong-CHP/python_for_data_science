import sys


def main():
    """
        entrypoint of program
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        up = 0
        low = 0
        punc = 0
        spc = 0
        dig = 0

        user_input = ""
        if len(sys.argv) < 2:
            user_input = input("What is the text to count?\n")
            spc += 1
        else:
            user_input = sys.argv[1]

        for x in user_input:
            if x.isupper():
                up += 1
            elif x.islower():
                low += 1
            elif x.isdigit():
                dig += 1
            elif x.isspace():
                spc += 1
            elif x.isprintable():
                punc += 1

        print(f"The text containes {len(user_input)} characters")
        print(f"{up} upper letters")
        print(f"{low} lower letters")
        print(f"{punc} punctuation marks")
        print(f"{spc} spaces")
        print(f"{dig} digits")
    except AssertionError as error:
        print(f"AssertionError: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
