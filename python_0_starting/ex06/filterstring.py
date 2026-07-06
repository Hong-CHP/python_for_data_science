import sys
from ft_filter import ft_filter


def main():
    """
        reproduction of built-in filter function
    """
    err_msg = "the arguments are bad\n"
    try:
        if len(sys.argv) != 3:
            raise AssertionError(err_msg)
        if not sys.argv[2].isnumeric():
            raise AssertionError(err_msg)
        for x in sys.argv[1]:
            if not (x.isalnum() or x.isspace()):
                raise AssertionError(err_msg)

        strings = sys.argv[1].split()
        n = int(sys.argv[2])

        res = ft_filter(lambda s: len(s) > n, strings)
        print(f"{res}\n")

    except AssertionError as error:
        print(f"AssertionError: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
