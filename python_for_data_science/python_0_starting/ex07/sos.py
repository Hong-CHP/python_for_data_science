import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",

    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. "
}


def main():
    """
        reproduction of built-in filter function
    """

    err_msg = "the arguments are bad\n"
    try:
        if len(sys.argv) != 2:
            raise AssertionError(err_msg)

        if not (sys.argv[1].isalnum() or sys.argv[1].isspace()):
            raise AssertionError(err_msg)

        norm = sys.argv[1]
        code_lst = []
        for x in norm:
            code_lst.append(NESTED_MORSE[x.upper()])

        coded = "".join(code_lst)
        print(coded[:-1])

    except AssertionError as error:
        print(f"AssertionError: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
