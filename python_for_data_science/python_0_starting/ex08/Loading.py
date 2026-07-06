import os


def ft_tqdm(lst):
    """
        reproduction of tqdm
        1. get terminal col width
        2. use idx to cal percent of total len of range
        3. get bar filled percent
        4. fill bar by str
        5. yield per ele
    """
    total = len(lst)

    term_size = os.get_terminal_size().columns
    bar_size = term_size - 30

    for i, ele in enumerate(lst):
        percent = (i + 1) / total
        filled = int(bar_size * percent)

        bar = '=' * filled + '>' + '-' * (bar_size - filled - 1)
        print(f"\r{int(percent * 100):3d}%|[{bar}]| {i + 1}/{total}", end="")

        yield ele
